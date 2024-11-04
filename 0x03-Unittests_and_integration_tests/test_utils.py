#!/usr/bin/env python3
"""
 Module for TestAcessNestedMap
"""


import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """test Acess nested map functionalities"""
    # parameterized test
    @parameterized.expand([
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2})
    ])
    def test_access_nested_map(self, map, path, expected_result):
        """test_case for happy path for utils.access_nested_map"""
        result = access_nested_map(map, path)
        # assertion
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, path):
        """test_case for sad path for utils.access_nested_map"""
        with self.assertRaises(KeyError):
            access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """test the get json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test the happy path of the get_json method"""
        payload = {"json.return_value": test_payload}
        with patch('requests.get', return_value=Mock(**payload)) as moc_re_get:
            self.assertEqual(get_json(test_url), test_payload)
            moc_re_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """test Class for memoization function"""

    def test_memoize(self):
        """testing memoize"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            testclass = TestClass()
            testclass.a_property
            result = testclass.a_property
            self.assertEqual(result, 42)
            mock.assert_called_once()

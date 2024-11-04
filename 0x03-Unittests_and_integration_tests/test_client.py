#!/usr/bin/env python3
"""
    Test for the client Module
"""


from client import GithubOrgClient as gitClient

from fixtures import TEST_PAYLOAD as test_payload

import unittest

import requests

from unittest.mock import (
    patch,
    Mock,
    MagicMock,
    PropertyMock,
)

from parameterized import (
    parameterized,
    parameterized_class,
)


class TestGithubOrgClient(unittest.TestCase):
    """test the TestGithubOrg functionality in client module"""

    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, url, mocked_get_json):
        """testing the org method"""
        mocked_get_json.return_value = MagicMock(return_value={})
        git_det = gitClient(url)
        result = git_det.org()
        self.assertEqual(result, {})
        mocked_get_json.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(url)
        )

    def test_public_repos_url(self):
        "testing GithubOrgClient._public_repos_url"

        with patch(
            'client.GithubOrgClient._public_repos_url', new_callable=PropertyMock
        ) as mock_org:
            payload = {"repos_url": True}
            mock_org.return_value = payload
            git_det = gitClient('google')
            result = git_det._public_repos_url()
            self.assertEqual(result, payload)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """testing GithubOrgClient.public_repos"""

        payloads = [{"name": "google"}, {"name": "abc"}]
        mock_get_json.return_value = payloads

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
        ) as mock_pub_repo_url:
            git_det = gitClient('google')
            result = git_det.public_repos()
            self.assertEqual(result, ['google', 'abc'])
            mock_pub_repo_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_true):
        """testing GithubOrgClient.has_license"""
        result = gitClient.has_license(repo, license_key)
        self.assertEqual(result, expected_true)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), test_payload)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integrationtesting with other external calls"""

    @classmethod
    def setUpClass(self):
        """run once before immediately test begins in this class"""
        self.get_patcher = patch('requests.get', side_effect=test_payload)
        self.get_patcher.start()

    @classmethod
    def tearDownClass(self):
        """run once last before the class is done"""

        self.get_patcher.stop()


    def test_public_repos(self):
        """test GithubOrgClient.public_repos"""
        pass

    def test_public_repos_with_license(self):
        """test public repos with licence"""
        pass

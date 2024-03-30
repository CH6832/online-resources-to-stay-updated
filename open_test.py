#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""open_test.py

Unittests for the open.py module.
"""

# pylint settings (https://docs.pylint.org/)
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled

from typing import Final, List
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from open import URLs, URL

global URLS
URLS: Final = URLs().get_abs_path_to_urls()


def main() -> None:
    """Main program/driving code."""
    unittest.main()

    return None


class TestURLs(unittest.TestCase):
    """Test cases for the URLs class."""


    def setUp(self) -> None:
        """Initialize URLs class."""
        self.urls = URLs()

        return None


    def test_get_abs_path_to_urls(self) -> None:
        """Test the get_abs_path_to_urls method of the URLs class."""
        self.assertEqual(self.urls.get_abs_path_to_urls(), URLS)

        return None


    @patch('open.ET')
    def test_get_urls(self, mock_ET) -> None:
        """Test the get_urls method of the URLs class."""
        mock_parse: MagicMock = MagicMock()
        mock_find: MagicMock = MagicMock()
        mock_iter: MagicMock = MagicMock()
        mock_text: MagicMock = MagicMock()
        mock_ET.parse.return_value = mock_parse
        mock_parse.find.return_value = mock_find
        mock_find.iter.return_value = mock_iter
        mock_iter.tag = 'some_tag'
        mock_iter.text = mock_text
        
        # test when no urls are found
        urls: List[str]
        urls = self.urls.get_urls(URLS, 'python')
        self.assertEqual(urls, [])
        mock_ET.parse.assert_called_once_with(URLS)
        mock_parse.find.assert_called_once_with('.//python')
        
        # test when the urls are found
        mock_iter.tag = 'url'
        mock_text = MagicMock('https://www.google.com')
        urls = self.urls.get_urls(URLS, 'ocaml')
        self.assertEqual(urls, [])

        return None


    def test_init(self) -> None:
        """Test the init method of the URLs class."""
        self.assertEqual(self.urls.abs_path_to_urls, URLS)

        return None


    @patch('open.webbrowser')
    def test_open_url(self, mock_webbrowser) -> None:
        """Test the open_url method of the URLs class."""
        urls: List[str]
        urls = ['https://www.google.com', 'http://www.google.com']
        self.urls.open_url('chrome', urls)
        calls = [mock_webbrowser.get.return_value.open.call_args_list]
        self.assertEqual(calls, [[(('https://www.google.com',), {'new': 1}), (('http://www.google.com',), {'new': 1})]])

        return None


class TestURL(unittest.TestCase):
    """Test cases for the URL class."""


    def test_get_url(self) -> None:
        """Test the get_url method of the URL class."""
        # test when url is a string already
        url_str = "https://www.google.com"
        url_obj = URL(url_str)
        self.assertEqual(url_obj.get_url(), url_str)
        
        # test when url is not a string
        url_obj = URL(12345)
        self.assertEqual(url_obj.get_url(), "12345")
        
        # test when url is none
        url_obj = URL(None)
        self.assertEqual(url_obj.get_url(), "None")
        
        # test when url is a complex object
        url_obj = URL({"key": "value"})
        self.assertEqual(url_obj.get_url(), "{'key': 'value'}")

        return None


if __name__ == '__main__':
    main()

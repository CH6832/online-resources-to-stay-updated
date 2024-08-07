#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""test_url_opener.py

Unittests for the url_open.py module.
"""

# pylint settings (https://docs.pylint.org/)
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled

import pytest
from unittest.mock import patch, MagicMock
import xml.etree.ElementTree as ET
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from url_opener import URLs, URL

def test_url_get_url():
    """Test URL class returns URL as a string."""
    url = URL("http://example.com")
    assert url.get_url() == "http://example.com"

@patch('xml.etree.ElementTree.parse')
def test_get_urls_success(mock_parse):
    """Test get_urls returns the correct URLs from the XML."""
    mock_tree = MagicMock()
    mock_root = MagicMock()
    mock_tree.find.return_value = mock_root
    mock_root.iter.return_value = [MagicMock(tag='url', text='http://example.com/page1')]
    mock_parse.return_value = mock_tree

    urls = URLs('test.xml')
    result = urls.get_urls('list')
    assert result == ['http://example.com/page1']

@patch('xml.etree.ElementTree.parse')
def test_get_urls_no_urls(mock_parse):
    """Test get_urls when no URLs are found."""
    mock_tree = MagicMock()
    mock_root = MagicMock()
    mock_tree.find.return_value = mock_root
    mock_root.iter.return_value = []
    mock_parse.return_value = mock_tree

    urls = URLs('test.xml')
    result = urls.get_urls('list')
    assert result == []

@patch('xml.etree.ElementTree.parse')
def test_get_urls_parse_error(mock_parse):
    """Test get_urls handles XML parsing errors."""
    mock_parse.side_effect = ET.ParseError("Error parsing XML")

    urls = URLs('test.xml')
    result = urls.get_urls('list')
    assert result == []

@patch('webbrowser.get')
def test_open_urls_success(mock_get):
    """Test open_urls opens URLs in the browser."""
    mock_browser = MagicMock()
    mock_get.return_value = mock_browser
    urls = URLs('test.xml')
    urls.open_urls('firefox', ['http://example.com/page1'])
    mock_browser.open.assert_called_once_with('http://example.com/page1', new=1)

@patch('webbrowser.get')
def test_open_urls_failure(mock_get):
    """Test open_urls handles browser failures."""
    mock_get.side_effect = Exception("Browser not found")
    urls = URLs('test.xml')
    with pytest.raises(Exception):
        urls.open_urls('firefox', ['http://example.com/page1'])

if __name__ == '__main__':
    pytest.main()

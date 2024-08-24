#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""url_opener.py

Open websites in Browser. Each URL is going to be opened in a new tab. When new Browser is opened, for each landing
page a new instance is going to be opened. The source file can be found in data/data.xml.
"""

import argparse
import logging
import sys
import webbrowser
import xml.etree.ElementTree as ET
from typing import List
from pathlib import Path

# pylint settings (https://docs.pylint.org/)
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stderr)]
)


class URL:
    """Class represents a single URL."""

    def __init__(self, uniform_resource_identifier: str) -> None:
        """Initializes with a URL."""
        self.url = uniform_resource_identifier

        return None


    def get_url(self) -> str:
        """Returns the URL as a string."""
        
        return str(self.url)


class URLs:
    """Handles the database of URLs."""

    def __init__(self, abs_path_to_urls: str = 'data/data.xml') -> None:
        """Initializes with the path to the XML database."""
        self.abs_path_to_urls = Path(abs_path_to_urls)


    def get_urls(self, selection_word: str) -> List[str]:
        """Collects URLs from the XML database based on the given selection word."""
        urls = []
        try:
            tree = ET.parse(self.abs_path_to_urls)
            root = tree.find(f".//{selection_word}")
            if root is not None:
                for elem in root.iter():
                    if 'url' in elem.tag:
                        url = URL(str(elem.text)).get_url()
                        urls.append(url)
            else:
                logging.warning("No URLs found for selection word '%s'", selection_word)
        except ET.ParseError as e:
            logging.error("Error parsing XML file: %s", e)
        except Exception as e:
            logging.error("Unexpected error: %s", e)
        
        return urls


    def open_urls(self, browser_path: str, urls: List[str]) -> None:
        """Opens each URL in a new tab of the specified web browser."""
        for url in urls:
            try:
                webbrowser.get(browser_path).open(url, new=1)
            except Exception as e:
                logging.error("Failed to open URL '%s': %s", url, e)
        
        return None


def setup_argparse() -> argparse.ArgumentParser:
    """Sets up the argument parser for the command-line tool."""
    
    parser = argparse.ArgumentParser(
        description=(
            "Open URLs from an XML file in a web browser.\n\n"
            "Examples:\n"
            "  open.py list\n"
            "  open.py read\n"
            "\n"
            "Use the --help flag for more information."
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        'selection_word',
        help='The XML tag to use for selecting URLs.'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging.'
    )

    return parser


def display_menu():
    """Display the ASCII art menu and get the user's selection."""
    print(r"""
   __          __  _                          
   \ \        / / | |                         
    \ \  /\  / /__| | ___ ___  _ __ ___   ___ 
     \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \
      \  /\  /  __/ | (_| (_) | | | | | |  __/
       \/  \/ \___|_|\___\___/|_| |_| |_|\___|
    
    Choose a category:
    1. Tech
    2. Math
    3. Physics
    4. Finance
    """)
    choice = input("Enter the number of your choice: ")
    choices = {
        "1": "tech",
        "2": "math",
        "3": "physics",
        "4": "finance"
    }

    return choices.get(choice, None)


def main() -> int:
    """Main program execution."""

    selection_word = display_menu()

    if not selection_word:
        print("ERROR: Invalid choice. Please select a valid option.", file=sys.stderr)
        return 1

    landing_pages = URLs()

    browser_paths = {
        "win32": r"C:/Program Files/Mozilla Firefox/firefox.exe %s",
        "darwin": r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome %s",
        "linux": r"/usr/bin/google-chrome %s"
    }

    browser_path = browser_paths.get(sys.platform)
    if not browser_path:
        print("ERROR: Supported browsers not found for your platform.", file=sys.stderr)
        return 1

    if selection_word not in [child.tag for child in ET.parse(landing_pages.abs_path_to_urls).getroot()]:
        print(f"ERROR: Invalid selection word '{selection_word}'.", file=sys.stderr)
        return 1

    urls = landing_pages.get_urls(selection_word)
    if not urls:
        print("No URLs found for the provided selection word.", file=sys.stderr)
        return 1

    landing_pages.open_urls(browser_path, urls)
    print("URLs opened successfully.")

    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""open.py

Open websites in Browser. Each URL is going to be opened in a new tab. When new Browser is opened, for each landing
page a new instance is going to be opened. The source file can be found in landing_pages.xml.
"""

# pylint settings (https://docs.pylint.org/)
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled

import os
import sys
from typing import List
import webbrowser
import xml.etree.ElementTree as ET

class URLs:
    """Class handles entire database of urls."""


    def __init__(self, abs_path_to_urls: str = r'data.xml') -> None:
        """Constructs all necessary attributes for the URLs object.

        Keyword arguments:
        abs_path_to_urls (str) -- absolute path to xml database with all landing pages
        """
        self.abs_path_to_urls = abs_path_to_urls

        return None


    def get_urls(self, websites: str, selection_word: str) -> List[str]:
        """This function collects all URLs from a given segment in the
        XML database (landing_pages.xml) and returns them as list.

        Keyword arguments:
        websites (list) -- path to website
        selection_word (str) -- sets subtree root element for url retrieval
        """
        urls = []
        tree = ET.parse(websites)
        taxonomybuildingblock_root: ET.Element | None = tree.find(f".//{selection_word}")
        if taxonomybuildingblock_root is not None:
            for elem in taxonomybuildingblock_root.iter():
                if 'url' in elem.tag:
                    retrieved_url = URL(str(elem.text)).get_url()
                    urls.append(retrieved_url)
        
        return urls


    def get_abs_path_to_urls(self) -> str:
        """Class represents a single url.
        """

        return self.abs_path_to_urls


    def open_url(self, path_to_web_browser: str, urls: List[str]) -> None:
        """open each url relevant for checking building block updates in
        a separate tab in Google Chrome browser. Default web browser for
        webbrowser.get() is Microsoft Internet Explorer.

        Keyword arguments:
        path_to_web_browser (str): path to an installed web browser
        urls (list[str]): list with all selected landing pages
        """
        for url_to_taxonomy in urls:
            bool(webbrowser.get(path_to_web_browser).open(url_to_taxonomy, new = 1))
        
        return None


class URL:
    """Class represents a single URL."""
    

    def __init__(self, uniform_resource_identifier) -> None:
        """Constructs all necessary attributes for the URL object.

        Keyword arguments:
        uniform_resource_identifier (str) -- an url leading to a landing page of a taxonomy provider
        """
        self.url: str = uniform_resource_identifier


    def get_url(self) -> str:
        """Returns a single url and converts it into a string if it is not one.
        """
        if not isinstance(self.url, str):
            return str(self.url)
        else:
            return self.url


def main() -> None:
    """main program"""

    landing_pages: URLs = URLs()

    browser_path: str
    if sys.platform == "win32":
        browser_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    elif sys.platform == "darwin": # macOS
        browser_path = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome %s"
    elif sys.platform == "linux":
        browser_path = r"/usr/bin/google-chrome %s"
    else:
        print("ERROR: Google Chrome Browser not found!")
        exit()

    # collect all possible arguments. the arguments
    # are all child elements of the root element.
    tree = ET.parse(landing_pages.get_abs_path_to_urls())
    root = tree.getroot()    
    all_arguments = []
    for child in root:
        print(child.tag, child.attrib)
        single_argument = str(child.tag)
        all_arguments.append(single_argument)
    print(all_arguments)

    print(len(list(sys.argv)))

    # allow only one argument
    if len(list(sys.argv)) > 2:
        print(f"ERROR: Only 2 argument allowed! You choose {len(list(sys.argv))}")
        exit()

    # check if argument is legit
    if sys.argv[1] not in all_arguments:
        print(f"ERROR: Argument not available. Please choose one of these: {str(all_arguments)}")
        exit()

    # open urls
    list_of_taxonomy_urls = landing_pages.get_urls(landing_pages.get_abs_path_to_urls(), sys.argv[1])
    landing_pages.open_url(browser_path, list_of_taxonomy_urls)

    return None


if __name__ == '__main__':
    main()

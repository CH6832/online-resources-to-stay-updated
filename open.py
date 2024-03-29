#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""open.py

"Open URLs in Browser. Each URL is going to be opened in a new tab. When new Browser is opened, for each landing
page a new instance  is going to be opened. The source file can be found in here:
C:/Projects/xmldata/data/landing_pages.xml.
"""

# pylint settings (https://docs.pylint.org/)
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled

import os
import sys
import os
import webbrowser
import xml.etree.ElementTree as ET

class LandingPages:
    """
    Browser class represent full path to landing pages
    """
    def __init__( self, abs_path_to_landing_pages: str = r'landing_pages.xml' ) -> None:
        """Constructs all necessary attributes for the LandingPages object.

        Keyword arguments:
        abs_path_to_landing_pages (str) -- absolute path to xml database with all landing pages
        """
        self.abs_path_to_landing_pages = abs_path_to_landing_pages

    def get_landing_pages_db( self ):
        """Get path to the xml database.
        """
        return self.abs_path_to_landing_pages

    def set_landing_pages_db( self, abs_path_to_lp_page: str ):
        """Set absolute path to the xml database.
        
        Keyword arguments:
        abs_path_to_lp_page (str) -- absolute path to xml database
        """
        self.abs_path_to_landing_pages = abs_path_to_lp_page
        return self.abs_path_to_landing_pages

    def get_rel_path_to_landing_pages_db( self ):
        """Convert absolute path into relative path to db
        and return it.
        """
        root_path: str = os.path.normpath( os.path.join( os.path.dirname( os.path.abspath(__file__) ), '..' ) )
        fixed_root_path = root_path.replace( "\\", "/" )
        rel_path = f'..{ self.abs_path_to_landing_pages.replace( fixed_root_path, "" ) }'
        return rel_path

class URL:
    """
    URL class representing a single url.
    """
    def __init__( self, uniform_resource_identifier ) -> None:
        """Constructs all necessary attributes for the URL object.

        Keyword arguments:
        uniform_resource_identifier (str) -- an url leading to a landing page of a taxonomy provider
        """
        self.url: str = uniform_resource_identifier

    def get_url( self ) -> str:
        """Returns a single url and converts it into a string if it is not one.
        """
        if not isinstance( self.url, str ):
            return str( self.url )
        else:
            return self.url

class URLs:
    """
    URLs class for operations on multiple urls.
    """
    def __init__( self ) -> None:
        """Constructs all necessary attributes for the URL object.
        """

    def get_urls( self, taxonomy_landing_pages: str, selection_word: str ) -> list[ str ]:
        """This function collects all URLs from a given segment in the
        XML database (C:/Projects/xmldata/data/landing_pages.xml) and
        returns a list with them.

        Keyword arguments:
        taxonomy_landing_pages (list): path to landing pages of xbrl taxonomies
        selection_word (str): sets subtree root element for url retrieval
        """
        urls = []
        tree = ET.parse( taxonomy_landing_pages )
        taxonomybuildingblock_root: ET.Element | None = tree.find( f".//{ selection_word }" )
        if taxonomybuildingblock_root is not None:
            for elem in taxonomybuildingblock_root.iter():
                if 'url' in elem.tag:
                    retrieved_url = URL( str( elem.text ) ).get_url()
                    urls.append( retrieved_url )
        
        return urls

    def open_url( self, path_to_web_browser: str, urls: list[ str ] ) -> None:
        """open each url relevant for checking building block updates in
        a separate tab in Google Chrome browser. Default web browser for
        webbrowser.get() is Microsoft Internet Explorer.

        Keyword arguments:
        path_to_web_browser (str): path to an installed web browser
        urls (list[str]): list with all selected landing pages
        """
        for url_to_taxonomy in urls:
            bool( webbrowser.get( path_to_web_browser ).open( url_to_taxonomy, new = 1 ) )
        
        return None


def main() -> None:
    """main program"""

    all_urls_listed: URLs = URLs()
    landing_pages: LandingPages = LandingPages()

    browser_path: str = r"C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    lps: str = landing_pages.get_landing_pages_db()

    # collect all possible arguments. the arguments
    # are all child elements of the root element.
    tree = ET.parse( "landing_pages.xml" )
    root = tree.getroot()    
    all_arguments = []
    for child in root:
        print(child.tag, child.attrib)
        single_argument = str(child.tag)
        all_arguments.append( single_argument )
    print( all_arguments )

    print(len(list(sys.argv)))

    # allow only one argument
    if len(list(sys.argv)) > 2:
        print(f"ERROR: Only 2 argument allowed! You choose { len(list(sys.argv)) }")
        exit()

    # check if argument is legit
    if sys.argv[1] not in all_arguments:
        print(f"ERROR: Argument not available. Please choose one of these: { str(all_arguments) }")
        exit()

    # open urls
    list_of_taxonomy_urls = all_urls_listed.get_urls(lps, sys.argv[1])
    all_urls_listed.open_url( browser_path, list_of_taxonomy_urls )

    return None

if __name__ == '__main__':
    main()

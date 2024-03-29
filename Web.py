#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Web.py"""

# https://docs.pylint.org/
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled

import os
import webbrowser
import xml.etree.ElementTree as ET

class Browser:
    """
    Browser class represents full path to a webbrowser
    """
    def __init__( self, browser_path: str = r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" ) -> None:
        """Constructs all necessary attributes for the URL object.
        """        
        self.browser_path = browser_path

    def get_web_browser( self ) -> str:
        """Get full path to web browser.
        """
        return self.browser_path

    def set_web_browser( self, path_to_browser: str ) -> str:
        """Set full path to web browser.
        """
        self.browser_path = path_to_browser
        return path_to_browser

class LandingPages:
    """
    Browser class represent full path to landing pages
    """
    def __init__( self, abs_path_to_landing_pages: str = r'C:/Projects/xmldata/data/landing_pages.xml' ) -> None:
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

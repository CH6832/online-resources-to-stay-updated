#!\usr\bin\env python3
# -*- coding: utf-8 -*-

"""AltovaSoftwareData.py"""

# https://docs.pylint.org/
# pylint: disable=line-too-long, trailing-whitespace, multiple-statements, fixme, locally-disabled

import datetime
import os

class Raptor:
    """
    Representing the ALTOVA Raptor.
    """

    def __init__( self, tech_std: str, bitness: int ):
        self.bitness: int = bitness
        self.tech_std: str = tech_std

        # software_year: int = int( datetime.datetime.now().year ) + 1
        software_year: int = int( datetime.datetime.now().year )
        str_software_year: str = str( software_year )

        if self.tech_std == "xbrl":
            self.r_exec_folder: str = "RaptorXMLXBRLServer"+str_software_year
            self.r_exec: str = "RaptorXMLXBRL.exe"

        elif self.tech_std == "xml":
            self.r_exec_folder = "RaptorXMLServer"+str_software_year
            self.r_exec = "RaptorXML.exe"

        if self.bitness == 64:
            self.program_files_folder_name: str = "Program Files" # path notation: PROGRA~1

        elif self.bitness == 32:
            self.program_files_folder_name = "Program Files (x86)" # path notation: PROGRA~2

    def get_root_catalog( self ) -> str:
        """get the RootCatalog.xml file from RaptorXMLwithXBRL"""
        return "C:\\" + self.program_files_folder_name + "\\Altova\\" + self.r_exec_folder + "\\etc\\RootCatalog.xml"

    def get_bin_folder_path( self ) -> str:
        """get full path to binary file of RaptorXMLwithXBRL"""
        return "C:\\" + self.program_files_folder_name + "\\Altova\\" + self.r_exec_folder + "\\bin"
        
    def get_raptor_exe( self ) -> str:
        """get RaptorXMLwithXBRL executable file"""
        return "C:\\" + self.program_files_folder_name + "\\Altova\\" + self.r_exec_folder + "\\bin\\" + self.r_exec

class PackageManager:
    """
    Representing the ALTOVA TaxonomyManager.
    """

    def __init__( self, data_std: str ):
        self.data_std = data_std
        self.path_to_exec: str = "C:\\ProgramData\\Altova\\SharedBetweenVersions"

        if self.data_std == "xbrl":
            self.pkg_mngr_exe: str = "taxonomymanager.exe"
        
        elif self.data_std == "xml":
            self.pkg_mngr_exe = "xmlschemamanager.exe"

    def get_pkg_mngr_exe( self ) -> str:
        """Get package manager executable full path depending on the tehcnology standard"""
        return os.path.join( self.path_to_exec, self.pkg_mngr_exe )

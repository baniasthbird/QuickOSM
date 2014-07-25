# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickOSM
                                 A QGIS plugin
 OSM's Overpass API frontend
                             -------------------
        begin                : 2014-06-11
        copyright            : (C) 2014 by 3Liz
        email                : info at 3liz dot com
        contributor          : Etienne Trimaille
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from processing.core.Processing import Processing
from processing.core.GeoAlgorithmExecutionException import GeoAlgorithmExecutionException
from processing.core.GeoAlgorithm import GeoAlgorithm
from processing.parameters.ParameterSelection import ParameterSelection
from processing.outputs.OutputString import OutputString
from os.path import dirname,abspath,join
from QuickOSM.CoreQuickOSM.IniFile import IniFile
from QuickOSM import resources_rc


class ListIniFilesGeoAlgorithm(GeoAlgorithm):
    '''
    List all the INI files 
    '''
    
    def __init__(self):
        self.NAME_FILE = 'NAME'
        self.OUTPUT_INI = 'INI'
        GeoAlgorithm.__init__(self)
        
    def defineCharacteristics(self):
        self.name = "Queries available"
        self.group = "Tools"
        
        folder = join(dirname(dirname(dirname(abspath(__file__)))),"queries")
        self.__files = IniFile.getNamesAndPathsFromFolder(folder)
        
        names = [ f['nameFull'] for f in self.__files]
        
        self.addParameter(ParameterSelection(self.NAME_FILE, 'Queries available', names))
        
        self.addOutput(OutputString(self.OUTPUT_INI,"Ini filepath as string"))

    def help(self):
        return True, 'Help soon'
    
    def getIcon(self):
        return QIcon(":/plugins/QuickOSM/icon.png")

    def processAlgorithm(self, progress):
        index = self.getParameterValue(self.NAME_FILE)
        ini = self.__files[index]
        self.setOutputValue(self.OUTPUT_INI,ini['path'])
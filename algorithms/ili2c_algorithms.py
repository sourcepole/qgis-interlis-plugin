# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Interlis
                                 A QGIS plugin
 Interlis Import/export
                              -------------------
        begin                : 2016-03-11
        copyright            : (C) 2016 by Pirmin Kalberer
        email                : pka@sourcepole.ch
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

__author__ = 'Pirmin Kalberer'
__date__ = '2016-03-11'
__copyright__ = '(C) 2016 by Pirmin Kalberer'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.PyQt.QtCore import QCoreApplication

from qgis.core import (QgsProcessingAlgorithm,
                       QgsProcessingParameterFile,
                       QgsProcessingParameterFileDestination,
                       )

from .interlis_utils import IliUtils


class Ili2ImdAlgorithm(QgsProcessingAlgorithm):

    OUTPUT = "OUTPUT"
    ILI = "ILI"
    IMD = "IMD"
    GROUP = "ili2c"

    def name(self):
        return 'Ili Model -> IliMeta'

    def displayName(self):
        return self.tr(self.name())

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return self.GROUP

    def createInstance(self):
        return Ili2ImdAlgorithm()

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFile(
            self.ILI,
            self.tr('Interlis model file'), optional=False))
        self.addParameter(QgsProcessingParameterFileDestination(
            self.IMD, description="IlisMeta XML model output file"))

    def processAlgorithm(self, parameters, context, feedback):
        '''Here is where the processing itself takes place'''

        ili = parameters[self.ILI]
        imd = parameters[self.IMD]
        IliUtils.runIli2c(["-oIMD", "--out", imd, ili])
        return {}

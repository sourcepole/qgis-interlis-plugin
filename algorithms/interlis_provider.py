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

from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsProcessingProvider
from processing.core.ProcessingConfig import ProcessingConfig, Setting
import os
from .interlis_utils import IliUtils
from .ili2pg_algorithms import (Ili2PgSchemaAlgorithm, Ili2PgImportAlgorithm,
                                Ili2PgExportAlgorithm)
from .ili2gpkg_algorithms import (Ili2GpkgSchemaAlgorithm,
                                  Ili2GpkgImportAlgorithm,
                                  Ili2GpkgExportAlgorithm)
from .ili2c_algorithms import Ili2ImdAlgorithm


class InterlisProvider(QgsProcessingProvider):

    _icon = QIcon(':/plugins/interlis/icon.png')

    def __init__(self):
        QgsProcessingProvider.__init__(self)

        self.activate = True

        # Load algorithms
        self.alglist = [
            Ili2PgSchemaAlgorithm(), Ili2PgImportAlgorithm(),
            Ili2PgExportAlgorithm(), Ili2GpkgSchemaAlgorithm(),
            Ili2GpkgImportAlgorithm(), Ili2GpkgExportAlgorithm(),
            Ili2ImdAlgorithm()
            ]
        self.initializeSettings()

    def initializeSettings(self):
        jarpath = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'jars'))
        ProcessingConfig.addSetting(Setting(
            self.getDescription(), IliUtils.JAVA_EXEC,
            "Java executable", IliUtils.java_exec_default()))
        ProcessingConfig.addSetting(
            Setting(self.getDescription(), IliUtils.ILI2PG_JAR,
                    "ili2pg.jar path",
                    os.path.join(jarpath, "ili2pg.jar")))
        ProcessingConfig.addSetting(
            Setting(self.getDescription(), IliUtils.ILI2GPKG_JAR,
                    "ili2gpkg.jar path",
                    os.path.join(jarpath, "ili2gpkg.jar")))

    def unload(self):
        QgsProcessingProvider.unload(self)
        ProcessingConfig.removeSetting(IliUtils.JAVA_EXEC)
        ProcessingConfig.removeSetting(IliUtils.ILI2PG_JAR)
        ProcessingConfig.removeSetting(IliUtils.ILI2GPKG_JAR)

    def id(self):
        return 'Interlis'

    def name(self):
        """This is the name that will appear on the toolbox group.

        It is also used to create the command line name of all the
        algorithms from this provider.
        """
        return 'Interlis'

    def getDescription(self):
        """This is the provired full name.
        """
        return 'Interlis'

    def icon(self):
        return self._icon

    def loadAlgorithms(self):
        """Here we fill the list of algorithms in self.algs.

        This method is called whenever the list of algorithms should
        be updated. If the list of algorithms can change (for instance,
        if it contains algorithms from user-defined scripts and a new
        script might have been added), you should create the list again
        here.

        In this case, since the list is always the same, we assign from
        the pre-made list. This assignment has to be done in this method
        even if the list does not change, since the self.algs list is
        cleared before calling this method.
        """

        self.alglist = [
            Ili2PgSchemaAlgorithm(), Ili2PgImportAlgorithm(),
            Ili2PgExportAlgorithm(), Ili2GpkgSchemaAlgorithm(),
            Ili2GpkgImportAlgorithm(), Ili2GpkgExportAlgorithm(),
            Ili2ImdAlgorithm()
            ]
            
        for alg in self.alglist:
            self.addAlgorithm(alg)

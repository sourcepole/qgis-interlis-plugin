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
from qgis.PyQt.QtCore import QSettings, QCoreApplication
from qgis.core import (QgsProcessingAlgorithm,
                       QgsProcessingException,
                       QgsProcessingParameterCrs,
                       QgsProcessingParameterFile,
                       QgsProcessingParameterFileDestination,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterString,
                       )
# from processing.core.GeoAlgorithm import GeoAlgorithm
# from processing.core.GeoAlgorithmExecutionException import (
#     GeoAlgorithmExecutionException)
# from processing.core.parameters import (ParameterFile, ParameterString,
#                                         ParameterBoolean, ParameterSelection)
# from processing.core.outputs import OutputFile
from processing.core.ProcessingConfig import ProcessingConfig

from .interlis_utils import IliUtils


def connectionOptions(connection):
    settings = QSettings()
    mySettings = '/PostgreSQL/connections/' + connection
    try:
        database = settings.value(mySettings + '/database')
        username = settings.value(mySettings + '/username')
        host = settings.value(mySettings + '/host')
        port = settings.value(mySettings + '/port', type=int)
        password = settings.value(mySettings + '/password')
    except Exception:
        raise QgsProcessingException(
            'Wrong database connection name: %s' % connection)
    connoptions = {
        "--dbhost": host,
        "--dbport": str(port),
        "--dbdatabase": database,
        "--dbusr": username,
        "--dbpwd": password
        }
    ili2pgargs = []
    for k, v in connoptions.items():
        if len(v) > 0:
            ili2pgargs.extend([k, v])
    return ili2pgargs

# USAGE
#   java -jar ili2pg.jar [Options] [file.xtf]
#
# OPTIONS
#
# --import               do an import.
# --update               do an update.
# --replace              do a replace.
# --delete               do a delete.
# --export               do an export.
# --schemaimport         do an schema import.
# --dbhost  host         The host name of the server. Defaults to localhost.
# --dbport  port         The port number the server is listening on. Defaults
#                        to 5432.
# --dbdatabase database  The database name.
# --dbusr  username      User name to access database.
# --dbpwd  password      Password of user used to access database.
# --validConfig file     Config file for validation.
# --disableValidation    Disable validation of data.
# --disableAreaValidation Disable AREA validation.
# --forceTypeValidation  restrict customization of validation related to
#                        "multiplicity"
# --deleteData           on schema/data import, delete existing data from
#                        existing tables.
# --defaultSrsAuth  auth Default SRS authority EPSG
# --defaultSrsCode  code Default SRS code 21781
# --modeldir  path       Path(s) of directories containing ili-files.
# --models modelname     Name(s) of ili-models to generate an db schema for.
# --dataset name         Name of dataset.
# --baskets BID          Basket-Id(s) of ili-baskets to export.
# --topics topicname     Name(s) of ili-topics to export.
# --createscript filename  Generate a sql script that creates the db schema.
# --dropscript filename  Generate a sql script that drops the generated db
#                        schema.
# --noSmartMapping       disable all smart mappings
# --smart1Inheritance     enable smart1 mapping of class/structure inheritance
# --smart2Inheritance     enable smart2 mapping of class/structure inheritance
# --coalesceCatalogueRef enable smart mapping of CHBase:CatalogueReference
# --coalesceMultiSurface enable smart mapping of CHBase:MultiSurface
# --expandMultilingual   enable smart mapping of CHBase:MultilingualText
# --createGeomIdx        create a spatial index on geometry columns.
# --createEnumColAsItfCode create enum type column with value according to ITF
#                        (instead of XTF).
# --createEnumTxtCol     create an additional column with the text of the
#                        enumeration value.
# --createEnumTabs       generate tables with enum definitions.
# --createSingleEnumTab  generate all enum definitions in a single table.
# --beautifyEnumDispName replace underscore with space in dispName of enum
#                        table entries
# --createStdCols        generate T_User, T_CreateDate, T_LastChange columns.
# --t_id_Name name       change name of t_id column (T_Id)
# --idSeqMin minValue    sets the minimum value of the id sequence generator.
# --idSeqMax maxValue    sets the maximum value of the id sequence generator.
# --createTypeDiscriminator  generate always a type discriminaor colum.
# --structWithGenericRef  generate one generic reference to parent in struct
#                        tables.
# --disableNameOptimization disable use of unqualified class name as table
#                        name.
# --nameByTopic          use topic+class name as table name.
# --maxNameLength length max length of sql names (60)
# --sqlEnableNull        create no NOT NULL constraints in db schema.
# --strokeArcs           stroke ARCS on import.
# --skipPolygonBuilding  keep linetables; don't build polygons on import.
# --skipGeometryErrors   ignore/do not report geometry errors.
# --keepAreaRef          keep arreaRef as additional column on import.
# --importTid            read TID into additional column T_Ili_Tid
# --createBasketCol      generate T_basket column.
# --createDatasetCol     generate T_datasetname column (Requires --dataset)
# --createFk             generate foreign key constraints.
# --createFkIdx          create an index on foreign key columns.
# --createUnique         create UNIQUE db constraints.
# --createNumChecks      create CHECK db constraints for numeric data types.
# --ILIGML20             use eCH-0118-2.0 as transferformat
# --ver4-translation     supports TRANSLATION OF in ili2db 4.x mode
#                        (incompatible with ili2db 3.x versions).
# --translation translatedModel=originModel assigns a translated model to its
#                        orginal language equivalent.
# --dbschema  schema     The name of the schema in the database. Defaults to
#                        not set.
# --oneGeomPerTable      If more than one geometry per table, create secondary
#                        table.
# --proxy host           proxy server to access model repositories.
# --proxyPort port       proxy port to access model repositories.
# --log filename         log message to given file.
# --gui                  start GUI.
# --trace                enable trace messages.
# --help                 Display this help text.
# --version              Display the version of ili2pg


def dbConnectionNames():
    settings = QSettings()
    settings.beginGroup('/PostgreSQL/connections/')
    return settings.childGroups()


class Ili2PgSchemaAlgorithm(QgsProcessingAlgorithm):
    OUTPUT = "OUTPUT"
    ILIDIR = "ILIDIR"
    ILIMODELS = "ILIMODELS"
    XTF = "XTF"
    DB = "DB"
    TABLE_NAMING = [
        'unqualified',
        'nameByTopic',
        'disableNameOptimization']
    INHERTIANCE_MAPPINGS = [
        'smart1Inheritance',
        'smart2Inheritance',
        'noSmartMapping']
    GROUP = "ili2pg"

    def name(self):
        return "Create Schema from Model"

    def displayName(self):
        return self.tr(self.name())

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return self.GROUP

    def createInstance(self):
        return Ili2PgSchemaAlgorithm()

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterString(
            self.ILIMODELS, self.tr('Interlis models')))
        self.addParameter(QgsProcessingParameterString(
            self.ILIDIR, self.tr('Interlis model search path'),
            defaultValue='http://models.geo.admin.ch/'))
        self.addParameter(QgsProcessingParameterFile(
            'iliLocalPath', self.tr('Local model directory'),
            behavior=QgsProcessingParameterFile.Folder,  optional=True))
        self.addParameter(QgsProcessingParameterEnum(
            'tableNaming', self.tr('Table naming convention:'),
            options=self.TABLE_NAMING, defaultValue=1))
        self.addParameter(QgsProcessingParameterEnum(
            'inheritanceMapping',
            self.tr('Inheritance mapping strategy:'),
            options=self.INHERTIANCE_MAPPINGS, defaultValue=0))
        self.addParameter(QgsProcessingParameterBoolean(
            'sqlNotNull',
            self.tr('Create NOT NULL constraints'), defaultValue=True))
        self.addParameter(QgsProcessingParameterBoolean(
            'createNumChecks',
            self.tr('Create constraints for numeric data types'),
            defaultValue=True))
        self.addParameter(QgsProcessingParameterBoolean(
            'createBasketCol',
            self.tr('Generate T_basket column'), defaultValue=False))
        self.addParameter(QgsProcessingParameterBoolean(
            'createDatasetCol',
            self.tr('Generate T_datasetname column'), defaultValue=False))
        self.addParameter(QgsProcessingParameterBoolean(
            'createFk',
            self.tr('Generate foreign key constraints'), defaultValue=True))
        self.addParameter(QgsProcessingParameterBoolean(
            'createFkIdx',
            self.tr('Create an index on foreign key columns'),
            defaultValue=True))
        self.addParameter(QgsProcessingParameterBoolean(
            'createGeomIdx',
            self.tr('Create a spatial index on geometry columns'),
            defaultValue=True))
        self.addParameter(QgsProcessingParameterBoolean(
            'strokeArcs',
            self.tr('Stroke ARCS on import'), defaultValue=False))
        self.addParameter(QgsProcessingParameterBoolean(
            'createEnumTabs',
            self.tr('Generate tables with enum definitions'),
            defaultValue=True))
        self.addParameter(QgsProcessingParameterCrs(
            'defaultSrsCode', self.tr('Default SRS code (EPSG)'),
            defaultValue='EPSG:2056'))
        self.db_connections = dbConnectionNames()
        self.addParameter(QgsProcessingParameterEnum(
            self.DB, self.tr('Database (connection name)'),
            self.db_connections))
        self.addParameter(QgsProcessingParameterString(
            'dbschema', self.tr('Database schema name'),
            defaultValue='public'))

    def processAlgorithm(self, parameters, context, feedback):
        ili2dbargs = ['--schemaimport']

        models = parameters.get(self.ILIMODELS)
        if models:
            ili2dbargs.extend(["--models", models])

        modeldir = parameters.get(self.ILIDIR)
        localmodeldir = parameters.get('iliLocalPath')
        if localmodeldir:
            modeldir = "%s;%s" % (localmodeldir, modeldir)
        ili2dbargs.append('--modeldir "%s"' % modeldir)

        naming = self.TABLE_NAMING[parameters.get('tableNaming')]
        if naming != 'unqualified':
            ili2dbargs.append("--%s" % naming)

        mapping = self.INHERTIANCE_MAPPINGS[parameters.get(
            'inheritanceMapping')]
        ili2dbargs.append("--%s" % mapping)

        if not parameters.get('sqlNotNull'):
            ili2dbargs.append('--sqlEnableNull')

        if parameters.get('createNumChecks'):
            ili2dbargs.append('--createNumChecks')

        if parameters.get('createBasketCol') or parameters.get(
                'createDatasetCol'):
            ili2dbargs.append('--createBasketCol')

        if parameters.get('createDatasetCol'):
            ili2dbargs.append('--createDatasetCol')

        if parameters.get('createFk'):
            ili2dbargs.append('--createFk')

        if parameters.get('createFkIdx'):
            ili2dbargs.append('--createFkIdx')

        if parameters.get('createGeomIdx'):
            ili2dbargs.append('--createGeomIdx')

        if parameters.get('strokeArcs'):
            ili2dbargs.append('--strokeArcs')

        if parameters.get('createEnumTabs'):
            ili2dbargs.append('--createEnumTabs')

        defaultSrsCode = parameters.get('defaultSrsCode').authid().split(":")[1]
        ili2dbargs.extend(["--defaultSrsCode", defaultSrsCode])

        db = self.db_connections[parameters.get(self.DB)]
        ili2dbargs.extend(connectionOptions(db))

        dbschema = parameters.get('dbschema')
        ili2dbargs.extend(["--dbschema", dbschema])

        IliUtils.runJava(
            ProcessingConfig.getSetting(IliUtils.ILI2PG_JAR),
            ili2dbargs)
        return {}


class Ili2PgImportAlgorithm(QgsProcessingAlgorithm):
    OUTPUT = "OUTPUT"
    ILIDIR = "ILIDIR"
    ILIMODELS = "ILIMODELS"
    XTF = "XTF"
    DB = "DB"
    IMPORT_MODE = [
        'import',
        'update',
        'replace']
    GROUP = 'ili2pg'

    def name(self):
        return "Import into DB"

    def displayName(self):
        return self.tr(self.name())

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return self.GROUP

    def createInstance(self):
        return Ili2PgImportAlgorithm()

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterEnum(
            'importMode', self.tr('Import mode:'),
            options=self.IMPORT_MODE, defaultValue=0))
        self.addParameter(QgsProcessingParameterString(
            'dataset', self.tr('Name of dataset'), optional=True))
        self.addParameter(QgsProcessingParameterBoolean(
            'deleteData', self.tr('Delete existing data from existing tables'),
            defaultValue=False))
        self.addParameter(QgsProcessingParameterFile(
            self.XTF, self.tr('Interlis transfer input file'),
            behavior=QgsProcessingParameterFile.File, optional=False))
        self.addParameter(QgsProcessingParameterString(
            self.ILIDIR, self.tr('Interlis model search path'),
            defaultValue='%ILI_FROM_DB;%XTF_DIR;http://models.geo.admin.ch/'))
        self.addParameter(QgsProcessingParameterString(
            self.ILIMODELS, self.tr('Interlis models'), optional=True))
        self.db_connections = dbConnectionNames()
        self.addParameter(QgsProcessingParameterEnum(
            self.DB, self.tr('Database (connection name)'),
            self.db_connections))
        self.addParameter(QgsProcessingParameterString(
            'dbschema', self.tr('Database schema name'),
            defaultValue='public'))

    def processAlgorithm(self, parameters, context, feedback):
        ili2dbargs = []

        mode = self.IMPORT_MODE[parameters.get('importMode')]
        ili2dbargs.append("--%s" % mode)

        dataset = parameters.get('dataset')
        if dataset:
            ili2dbargs.extend(["--dataset", dataset])

        if parameters.get('deleteData'):
            ili2dbargs.append('--deleteData')

        db = self.db_connections[parameters.get(self.DB)]
        ili2dbargs.extend(connectionOptions(db))

        modeldir = parameters.get(self.ILIDIR)
        ili2dbargs.append('--modeldir "%s"' % modeldir)

        models = parameters.get(self.ILIMODELS)
        if models:
            ili2dbargs.extend(["--models", models])

        dbschema = parameters.get('dbschema')
        ili2dbargs.extend(["--dbschema", dbschema])

        xtf = parameters.get(self.XTF)
        ili2dbargs.append(xtf)

        IliUtils.runJava(
            ProcessingConfig.getSetting(IliUtils.ILI2PG_JAR),
            ili2dbargs)
        return {}


class Ili2PgExportAlgorithm(QgsProcessingAlgorithm):

    OUTPUT = "OUTPUT"
    ILIDIR = "ILIDIR"
    ILIMODELS = "ILIMODELS"
    XTF = "XTF"
    DB = "DB"
    GROUP = 'ili2pg'

    def name(self):
        # return 'Interlis'
        return "Export from DB"

    def displayName(self):
        return self.tr(self.name())

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return self.GROUP

    def createInstance(self):
        return Ili2PgExportAlgorithm()

    def initAlgorithm(self, config=None):
        self.db_connections = dbConnectionNames()
        self.addParameter(QgsProcessingParameterEnum(
            self.DB,
            self.tr('Database (connection name)'), self.db_connections))
        self.addParameter(QgsProcessingParameterString(
            'dbschema',
            self.tr('Database schema name'), defaultValue='public'))
        self.addParameter(QgsProcessingParameterString(
            'dataset',
            self.tr('Name of dataset'), optional=True))
        self.addParameter(QgsProcessingParameterString(
            self.ILIDIR,
            self.tr('Interlis model search path'),
            defaultValue='%ILI_FROM_DB;%XTF_DIR;http://models.geo.admin.ch/'))
        self.addParameter(QgsProcessingParameterString(
            self.ILIMODELS,
            self.tr('Interlis models')))
        self.addParameter(QgsProcessingParameterFileDestination(
            self.XTF, description="Interlis transfer output file"))
        # ext: xtf, xml, itf

    def processAlgorithm(self, parameters, context, feedback):
        ili2dbargs = ['--export']

        db = self.db_connections[parameters.get(self.DB)]
        ili2dbargs.extend(connectionOptions(db))

        dbschema = parameters.get('dbschema')
        ili2dbargs.extend(["--dbschema", dbschema])

        dataset = parameters.get('dataset')
        if dataset:
            ili2dbargs.extend(["--dataset", dataset])

        modeldir = parameters.get(self.ILIDIR)
        ili2dbargs.append('--modeldir "%s"' % modeldir)

        models = parameters.get(self.ILIMODELS)
        if models:
            ili2dbargs.extend(["--models", models])

        xtf = parameters.get(self.XTF)
        ili2dbargs.append(xtf)

        IliUtils.runJava(
            ProcessingConfig.getSetting(IliUtils.ILI2PG_JAR),
            ili2dbargs)

        return {}

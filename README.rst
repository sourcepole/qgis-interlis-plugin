Interlis QGIS plugin
====================

QGIS Plugin for importing and exporting Interlis data.


ogrtools
--------

ogrtools is a collection of libraries and tools built with the Python
API of `OGR <http://www.gdal.org/ogr/>`__.

pyogr library
-------------

pyogr gives you OGR commands like ogr2ogr or ogrinfo as Python library,
i.e. without calling an external executable file. Most of the code is
already included in the OGR source distribution as samples for using the
Python API.

-  ogr2ogr.py: ogr2ogr call with stdout/stderr redirection
-  ogrinfo.py: ogrinfo call
-  ogrvrt.py: generate a VRT from a datasource
-  ogrds.py: Call OGR SQL commands on a datasource

interlis library
----------------

Extensions for the OGR `Interlis
driver <http://www.gdal.org/ogr/drv_ili.html>`__.

-  Automatic detection of used models in transfer files
-  Extracting enums from IlisMeta model
-  Loading and converting of Interlis models from model repositories


ogr command line tool
---------------------

The ogr command line tool exposes ogrtools functionality for using in a
command shell.

::

    ogr --help
    usage: ogr [-h]
               {version,formats,info,sql,vrt,genconfig,write-enums,transform} ...

    Query and transform OGR compatible vector data

    optional arguments:
      -h, --help            show this help message and exit

    commands:
      valid commands

      {version,formats,info,sql,vrt,genconfig,write-enums,transform}
        version             Show version information
        formats             List available data formats
        info                Information about data
        sql                 Execute SQL Query
        vrt                 Create VRT from data source
        genconfig           Generate OGR configuration from data source
        write-enums         Write tables with enumeration values
        transform           Transform data source based on OGR configuration

ogr version
~~~~~~~~~~~

Show version information

::

    usage: ogr version [-h]

ogr formats
~~~~~~~~~~~

List available data formats

::

    usage: ogr formats [-h]

ogr info
~~~~~~~~

Information about data

::

    usage: ogr info [-h] source [layers [layers ...]]

Example:

::

    ogr info tests/data/osm/railway.shp

::

    INFO: Open of `tests/data/osm/railway.shp'
          using driver `ESRI Shapefile' successful.

    Layer name: railway
    Geometry: Line String
    Feature Count: 73
    Extent: (9.478497, 9.628118) - (47.124600, 47.262550)
    Layer SRS WKT:
    GEOGCS["GCS_WGS_1984",
        DATUM["WGS_1984",
            SPHEROID["WGS_84",6378137,298.257223563]],
        PRIMEM["Greenwich",0],
        UNIT["Degree",0.017453292519943295]]
    type: String (255.0)
    osm_id: Real (11.0)
    lastchange: Date (10.0)
    name: String (255.0)
    keyvalue: String (80.0)

ogr sql
~~~~~~~

Execute SQL Query

::

    usage: ogr sql [-h] source sql-query

Example:

::

    ogr sql tests/data/osm/railway.shp "SELECT type,osm_id,lastchange FROM railway WHERE lastchange < '2008/04/01'"

::

    INFO: Open of `tests/data/osm/railway.shp'
          using driver `ESRI Shapefile' successful.

    Layer name: railway
    Geometry: Line String
    Feature Count: 8
    Extent: (9.478497, 9.628118) - (47.124600, 47.262550)
    Layer SRS WKT:
    GEOGCS["GCS_WGS_1984",
        DATUM["WGS_1984",
            SPHEROID["WGS_84",6378137,298.257223563]],
        PRIMEM["Greenwich",0],
        UNIT["Degree",0.017453292519943295]]
    type: String (255.0)
    osm_id: Real (11.0)
    lastchange: Date (10.0)
    OGRFeature(railway):6
      type (String) = rail
      osm_id (Real) = 9675696
      lastchange (Date) = 2007/10/17
      LINESTRING (9.6174755 47.227974,9.6170635 47.22802)

    OGRFeature(railway):8
      type (String) = rail
      osm_id (Real) = 9675711
      lastchange (Date) = 2007/10/17
      LINESTRING (9.617415 47.22794,9.617038 47.227985)
    ...

ogr vrt
~~~~~~~

Create VRT from data source

::

    usage: ogr vrt [-h] source [layers [layers ...]]

Example:

::

    ogr vrt tests/data/osm/railway.shp

::

    <OGRVRTDataSource>
      <OGRVRTLayer name="railway">
        <SrcDataSource relativeToVRT="0" shared="1">tests/data/osm/railway.shp</SrcDataSource>
        <SrcLayer>railway</SrcLayer>
        <GeometryType>wkbLineString</GeometryType>
        <LayerSRS>GEOGCS[&quot;GCS_WGS_1984&quot;,DATUM[&quot;WGS_1984&quot;,SPHEROID[&quot;WGS_84&quot;,6378137,298.257223563]],PRIMEM[&quot;Greenwich&quot;,0],UNIT[&quot;Degree&quot;,0.017453292519943295]]</LayerSRS>
        <Field name="type" type="String" src="type" width="255"/>
        <Field name="osm_id" type="Real" src="osm_id" width="11"/>
        <Field name="lastchange" type="Date" src="lastchange" width="10"/>
        <Field name="name" type="String" src="name" width="255"/>
        <Field name="keyvalue" type="String" src="keyvalue" width="80"/>
      </OGRVRTLayer>
    </OGRVRTDataSource>


Development
-----------

::

    git clone https://github.com/sourcepole/qgis-interlis-plugin.git

Running tests:

::

    apt-get install python3-nose

::

    python3 -m "nose"
    The tests were made for GDAL version 2.2.2

For running ogr commands from source tree:

::

    alias ogr="PYTHONPATH=$(pwd) $(pwd)/ogr_cli/ogr.py"

License
-------

ogrtools is Copyright © 2012-2018 Sourcepole AG. It is free software,
and may be redistributed under the terms specified in the LICENSE.txt
file.

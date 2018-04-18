from ogrtools.ogrtransform.ogrconfig import OgrConfig
from ogrtools.interlis.ilismeta import prettify
import json


def test_shape_config():
    cfg = OgrConfig(ds="tests/data/osm/railway.shp")
    cfgjson = cfg.generate_config(dst_format='PostgreSQL')
    expected = """{
  "//": "OGR transformation configuration",
  "src_format": "ESRI Shapefile",
  "dst_format": "PostgreSQL",
  "dst_dsco": {},
  "dst_lco": {
    "SCHEMA": "public"
  },
  "layers": {
    "railway": {
      "src_layer": "railway",
      "fields": {
        "type": {
          "src": "type",
          "type": "String",
          "width": 255
        },
        "osm_id": {
          "src": "osm_id",
          "type": "Integer64",
          "width": 11
        },
        "lastchange": {
          "src": "lastchange",
          "type": "Date",
          "width": 10
        },
        "name": {
          "src": "name",
          "type": "String",
          "width": 255
        },
        "keyvalue": {
          "src": "keyvalue",
          "type": "String",
          "width": 80
        }
      },
      "geom_fields": {},
      "geometry_type": "LineString"
    }
  }
}"""

    print(cfgjson)
    assert sorted(expected) == sorted(cfgjson)


def test_ili_config():
    cfg = OgrConfig(
        ds="./tests/data/ili/roads23.xtf,./tests/data/ili/RoadsExdm2ien.imd")
    cfgjson = cfg.generate_config(dst_format='PostgreSQL', srs=21781)

    expected = {
        'src_layer': 'RoadsExdm2ien.RoadsExtended.StreetAxis',
        'geom_fields': {'geometry': {'src': 'Geometry',
                                     'type': 'MultiLineString',
                                     'srs': 21781}},
        'fields': {'precision': {'src': 'Precision',
                                 'type': 'String'},
                   'tid': {'src': 'TID',
                           'type': 'String'},
                   'street': {'src': 'Street',
                              'type': 'String'}},
        'geometry_type': 'MultiLineString'
    }

    print(cfgjson)

    assert json.loads(cfgjson)["layers"]["roadsexdm2ien_roadsextended_streetaxis"] == expected


def test_np():
    cfg = OgrConfig(ds="tests/data/np/NP_Example.xtf,tests/data/np/NP_73_CH_de_ili2.imd",
                    model="tests/data/np/NP_73_CH_de_ili2.imd")
    cfgjson = cfg.generate_config(dst_format='PostgreSQL')

    expected = {
        'src_layer': 'Nutzungsplanung.Nutzungsplanung.Grundnutzung_Zonenflaeche',
        'fields': {'herkunft': {'src': 'Herkunft',
                                'type': 'String'},
                   'zonentyp_1': {'src': 'Zonentyp_1',
                                  'type': 'String'},
                   'tid': {'src': 'TID',
                           'type': 'String'},
                   'bemerkungen': {'src': 'Bemerkungen',
                                   'type': 'String'},
                   'mutation': {'src': 'Mutation',
                                'type': 'String'},
                   'qualitaet': {'src': 'Qualitaet',
                                 'type': 'String'}},
        'geom_fields': {'geometrie': {'src': 'Geometrie',
                                      'type': 'Polygon'}},
        'geometry_type': 'Polygon'
    }

    print(cfgjson)

    assert json.loads(cfgjson)["layers"]["n0_grundnutzung_zonenflaeche'"] == expected


def test_layer_info():
    cfg = OgrConfig(ds="./tests/data/ili/roads23.xtf,./tests/data/ili/RoadsExdm2ien.imd",
                    model="./tests/data/ili/RoadsExdm2ien.imd")
    assert not cfg.is_loaded()
    assert cfg.layer_names() == []
    assert cfg.enum_names() == []
    assert cfg.layer_infos() == []
    assert cfg.enum_infos() == []

    cfg.generate_config(dst_format='PostgreSQL')
    assert cfg.is_loaded()
    print(cfg.layer_names())
    assert "roadsexdm2ien_roadsextended_roadsign" in cfg.layer_names()
    print(cfg.enum_names())
    assert "_type" in str(cfg.enum_names())

    print(cfg.layer_infos())
    print(cfg.enum_infos())
    assert {'name': 'roadsexdm2ien_roadsextended_roadsign',
            'geom_field': 'position'} in cfg.layer_infos()
    assert {'name': 'roadsexdm2ben_roads_lattrs'} in cfg.layer_infos()
    assert '_precision' in str(cfg.enum_infos())


def test_enums():
    cfg = OgrConfig(ds="./tests/data/ili/roads23.xtf,./tests/data/ili/RoadsExdm2ien.imd",
                    model="./tests/data/ili/RoadsExdm2ien.imd")
    cfgjson = cfg.generate_config(dst_format='PostgreSQL')

    expected = {
        'values': [{'id': 0,
                    'enumtxt': 'welldefined',
                    'enum': 'welldefined'},
                   {'id': 1, 'enumtxt': 'fuzzy',
                    'enum': 'fuzzy'}],
        'src_name': 'RoadsExdm2ben.Roads.LAttrs.LArt'
    }

    assert expected in json.loads(cfgjson)["enums"].values()


def test_vrt():
    cfg = OgrConfig(ds="./tests/data/ili/roads23.xtf,./tests/data/ili/RoadsExdm2ien.imd",
                    config="./tests/data/ili/RoadsExdm2ien.cfg")
    vrt = prettify(cfg.generate_vrt())

    expected_fields = ['''<Field name="type" src="Type" type="String"/>''',
                       '''<Field name="tid" src="TID" type="String"/>''']

    print(vrt)

    assert '''<SrcLayer>RoadsExdm2ien.RoadsExtended.RoadSign</SrcLayer>''' in vrt
    assert '''<GeometryType>wkbPoint</GeometryType>''' in vrt
    for field in expected_fields:
        assert field in vrt


def test_reverse_vrt():
    cfg = OgrConfig(ds="./tests/data/ili/roads23.xtf,./tests/data/ili/RoadsExdm2ien.imd",
                    config="./tests/data/ili/RoadsExdm2ien.cfg")
    vrt = prettify(cfg.generate_reverse_vrt())

    expected_fields = ['''<Field name="Type" src="type"/>''',
                       '''<Field name="TID" src="tid"/>''']

    print(vrt)

    assert '''<SrcLayer>roadsign</SrcLayer>''' in vrt
    assert '''<GeometryType>wkbPoint</GeometryType>''' in vrt
    for field in expected_fields:
        assert field in vrt


def test_multigeom_vrt():
    cfg = OgrConfig(ds="./tests/data/ch.bazl/ch.bazl.sicherheitszonenplan.oereb_20131118.xtf,./tests/data/ch.bazl/ch.bazl.sicherheitszonenplan.oereb_20131118.imd",
                    config="./tests/data/ch.bazl/ch.bazl.sicherheitszonenplan.oereb_20131118.cfg")
    vrt = prettify(cfg.generate_vrt())

    expected_fields = ['''<Field name="zustaendigestelle" src="ZustaendigeStelle" type="String"/>''',
                       '''<Field name="eigentumsbeschraenkung" src="Eigentumsbeschraenkung" type="String"/>''',
                       '''<Field name="rechtsstatus" src="Rechtsstatus" type="String"/>''',
                       '''<Field name="tid" src="TID" type="String"/>''',
                       '''<Field name="publiziertab" src="publiziertAb" type="String"/>''',
                       '''<Field name="metadatengeobasisdaten" src="MetadatenGeobasisdaten" type="String"/>''']
    expected_geom_fields = ['''<GeometryField field="Linie" name="linie">''',
                            '''<GeometryType>wkbMultiLineString</GeometryType>''',
                            '''<SRS>EPSG:21781</SRS>''',
                            '''</GeometryField>''',
                            '''<GeometryField field="Punkt" name="punkt">''',
                            '''<GeometryType>wkbPoint</GeometryType>''',
                            '''<SRS>EPSG:21781</SRS>''',
                            '''</GeometryField>''',
                            '''<GeometryField field="Flaeche" name="flaeche">''',
                            '''<GeometryType>wkbPolygon</GeometryType>''',
                            '''<SRS>EPSG:21781</SRS>''',
                            '''</GeometryField>''']

    print(vrt)

    assert '''<OGRVRTLayer name="oerebkrm09trsfr_transferstruktur_geometrie">''' in vrt
    assert '''<SrcLayer>OeREBKRM09trsfr.Transferstruktur.Geometrie</SrcLayer>''' in vrt
    for field in expected_fields:
        assert field in vrt
    for field in expected_geom_fields:
        assert field in vrt

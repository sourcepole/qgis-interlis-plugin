from ogrtools.ogrtransform.ogrconfig import OgrConfig
from ogrtools.interlis.ilismeta import prettify


def test_shape_config():
    cfg = OgrConfig(ds="tests/data/osm/railway.shp")
    cfgjson = cfg.generate_config(dst_format='PostgreSQL')
    expected = """{
  "dst_lco": {
    "SCHEMA": "public"
  },
  "dst_dsco": {},
  "dst_format": "PostgreSQL",
  "//": "OGR transformation configuration",
  "layers": {
    "railway": {
      "geometry_type": "LineString",
      "src_layer": "railway",
      "fields": {
        "name": {
          "src": "name",
          "width": 255,
          "type": "String"
        },
        "lastchange": {
          "src": "lastchange",
          "width": 10,
          "type": "Date"
        },
        "osm_id": {
          "src": "osm_id",
          "width": 11,
          "type": "Integer64"
        },
        "type": {
          "src": "type",
          "width": 255,
          "type": "String"
        },
        "keyvalue": {
          "src": "keyvalue",
          "width": 80,
          "type": "String"
        }
      },
      "geom_fields": {}
    }
  },
  "src_format": "ESRI Shapefile"
}"""

    print(cfgjson)
    assert sorted(expected) == sorted(cfgjson)


def test_ili_config():
    cfg = OgrConfig(
        ds="./tests/data/ili/roads23.xtf,./tests/data/ili/RoadsExdm2ien.imd")
    cfgjson = cfg.generate_config(dst_format='PostgreSQL', srs=21781)

    expected_layer = '''"src_layer": "RoadsExdm2ien.RoadsExtended.StreetAxis"'''
    expected_type = '''"geometry_type": "MultiLineString"'''
    expected_field = '''"precision": {'''
    expected_field_src = '''"src": "Precision"'''

    print(cfgjson)

    assert expected_layer in cfgjson
    assert expected_type in cfgjson
    assert expected_field in cfgjson
    assert expected_field_src in cfgjson


def test_np():
    cfg = OgrConfig(ds="tests/data/np/NP_Example.xtf,tests/data/np/NP_73_CH_de_ili2.imd",
                    model="tests/data/np/NP_73_CH_de_ili2.imd")
    cfgjson = cfg.generate_config(dst_format='PostgreSQL')

    expected_layer = '''"src_layer": "Nutzungsplanung.Nutzungsplanung.Grundnutzung_Zonenflaeche"'''
    expected_type = '''"geometry_type": "Polygon"'''
    expected_field = '''"mutation": {'''
    expected_field_src = '''"src": "Mutation"'''

    print(cfgjson)

    assert expected_layer in cfgjson
    assert expected_type in cfgjson
    assert expected_field in cfgjson
    assert expected_field_src in cfgjson


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

    expected_name = '''"src_name": "RoadsExdm2ben.Roads.LAttrs.LArt"'''
    expected_enum = ['''"enumtxt": "fuzzy"''', '''"enum": "welldefined"''']

    print(cfgjson)

    assert expected_name in cfgjson
    for enum in expected_enum:
        assert enum in cfgjson


def test_vrt():
    cfg = OgrConfig(ds="./tests/data/ili/roads23.xtf,./tests/data/ili/RoadsExdm2ien.imd",
                    config="./tests/data/ili/RoadsExdm2ien.cfg")
    vrt = prettify(cfg.generate_vrt())

    expected_layer = '''<SrcLayer>RoadsExdm2ien.RoadsExtended.RoadSign</SrcLayer>'''
    expected_geom = '''<GeometryType>wkbPoint</GeometryType>'''
    expected_fields = ['''<Field name="type" src="Type" type="String"/>''',
                       '''<Field name="tid" src="TID" type="String"/>''']

    print(vrt)

    assert expected_layer in vrt
    assert expected_geom in vrt
    for field in expected_fields:
        assert field in vrt


def test_reverse_vrt():
    cfg = OgrConfig(ds="./tests/data/ili/roads23.xtf,./tests/data/ili/RoadsExdm2ien.imd",
                    config="./tests/data/ili/RoadsExdm2ien.cfg")
    vrt = prettify(cfg.generate_reverse_vrt())

    expected_layer = '''<SrcLayer>roadsign</SrcLayer>'''
    expected_geom = '''<GeometryType>wkbPoint</GeometryType>'''
    expected_fields = ['''<Field name="Type" src="type"/>''',
                       '''<Field name="TID" src="tid"/>''']

    print(vrt)

    assert expected_layer in vrt
    assert expected_geom in vrt
    for field in expected_fields:
        assert field in vrt


def test_multigeom_vrt():
    cfg = OgrConfig(ds="./tests/data/ch.bazl/ch.bazl.sicherheitszonenplan.oereb_20131118.xtf,./tests/data/ch.bazl/ch.bazl.sicherheitszonenplan.oereb_20131118.imd",
                    config="./tests/data/ch.bazl/ch.bazl.sicherheitszonenplan.oereb_20131118.cfg")
    vrt = prettify(cfg.generate_vrt())

    expected_name = '''<OGRVRTLayer name="oerebkrm09trsfr_transferstruktur_geometrie">'''
    expected_layer = '''<SrcLayer>OeREBKRM09trsfr.Transferstruktur.Geometrie</SrcLayer>'''
    expected_fields = ['''<Field name="zustaendigestelle" src="ZustaendigeStelle" type="String"/>''',
                       '''<Field name="eigentumsbeschraenkung" src="Eigentumsbeschraenkung" type="String"/>''',
                       '''<Field name="rechtsstatus" src="Rechtsstatus" type="String"/>''',
                       '''<Field name="tid" src="TID" type="String"/>''',
                       '''<Field name="publiziertab" src="publiziertAb" type="String"/>''',
                       '''<Field name="metadatengeobasisdaten" src="MetadatenGeobasisdaten" type="String"/>''']

    print(vrt)

    assert expected_name in vrt
    assert expected_layer in vrt
    for field in expected_fields:
        assert field in vrt

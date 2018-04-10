import string
import re

from ..interlis.ilismeta import ImdParser


# Base class for format specific methods
class FormatHandler:

    def __init__(self):
        self._name_seq = 0

    def launder_name(self, src_name):
        # Do nothing in default implementation
        return src_name

    def default_ds_creation_options(self):
        # No options in default implementation
        return {}

    def default_layer_creation_options(self):
        # No options in default implementation
        return {}

    def detect_model(self, src_file):
        return None

    def extract_enums(self, model):
        return None

    def shorten_name(self, src_name, prefix, splitchar='.'):
        # Nutzungsplanung.Nutzungsplanung.Grundnutzung_Zonenflaeche.Herkunft
        # -> enumXX_herkunft
        short_name = str.rsplit(str(src_name), splitchar, 1)[-1]
        short_name = "%s%d_%s" % (prefix, self._name_seq, short_name)
        self._name_seq = self._name_seq + 1
        return short_name

    def layer_name(self, name):
        return name


class PgFormatHandler(FormatHandler):
    # PG default name limit is 63 chars

    def __init__(self):
        FormatHandler.__init__(self)
        self.max_len = 63

    def launder_name(self, src_name):
        # OGRPGDataSource::LaunderName
        # return re.sub(r"[#'-]", '_', src_name.lower())
        name = str(src_name).lower().encode('ascii', 'replace')
        if len(name) > self.max_len - 7:
            return self.shorten_name(name, 'n')
        else:
            return re.compile("\W+", re.IGNORECASE).sub("_", name.decode('utf-8'))

    def default_layer_creation_options(self):
        # see http://www.gdal.org/ogr/drv_pg.html Layer Creation Options
        return {'SCHEMA': 'public'}


class SpatiaLiteFormatHandler(FormatHandler):

    def __init__(self):
        FormatHandler.__init__(self)

    def launder_name(self, src_name):
        name = unicode(src_name).lower().encode('ascii', 'replace')
        return re.compile("\W+", re.IGNORECASE).sub("_", name.decode('utf-8'))

    def default_ds_creation_options(self):
        return {'SPATIALITE': 'YES'}


class IliFormatHandler(FormatHandler):

    def __init__(self):
        FormatHandler.__init__(self)

    def detect_model(self, src_file):
        return None

    def extract_enums(self, model):
        parser = ImdParser(model)
        return parser.extract_enums()


class GeoJSONFormatHandler(FormatHandler):

    def __init__(self):
        FormatHandler.__init__(self)

    def layer_name(self, name):
        return "OGRGeoJSON"


class FormatHandlerRegistry:

    def __init__(self):
        self._handlers = {}
        self.register('', FormatHandler())  # default
        self.register('PostgreSQL', PgFormatHandler())
        self.register('SQLite', SpatiaLiteFormatHandler())
        self.register('Interlis 1', IliFormatHandler())
        self.register('Interlis 2', IliFormatHandler())
        self.register('GeoJSON', GeoJSONFormatHandler())

    def register(self, format, handler):
        self._handlers[format] = handler

    def handler(self, format):
        if format in self._handlers:
            return self._handlers[format]
        else:
            return self._handlers['']

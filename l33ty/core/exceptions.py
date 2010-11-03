class L33tyException(Exception): pass

class ConfigException(L33tyException): pass

class ImproperlyConfigured(ConfigException): pass
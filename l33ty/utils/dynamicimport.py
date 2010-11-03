import sys

def from_x_import_y(x, y):
    __import__(x)
    container = sys.modules[x]
    try:
        return getattr(container, y)
    except:
        x = '.'.join((x, y))
        return import_y(x)

def import_y(y):
    __import__(y)
    container = sys.modules[y]
    return container
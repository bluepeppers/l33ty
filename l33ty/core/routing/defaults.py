from l33ty.core.routeresolvers import RegexRoutePattern
from l33ty.core.exceptions import ImproperlyConfigured

def routingpatterns(prefix, *args):
    pattern_list = []
    for t in args:
        if isinstance(t, (list, tuple)):
            t = route(*t, prefix=prefix)
        elif isinstance(t, RegexRoutePattern):
            t.add_prefix(prefix)
        pattern_list.append(t)
    return pattern_list

def route(regex, view, kwargs=None, prefix=''):
    if isinstance(view, basestring):
        if not view:
            raise ImproperlyConfigured('Empty URL pattern view name not permitted (for pattern %r)' % regex)
        if prefix:
            view = prefix + '.' + view
    return RegexRoutePattern(regex, view, kwargs)

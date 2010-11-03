import re
from l33ty.utils.dynamicimport import import_y, from_x_import_y
from l33ty.core.exceptions import ImproperlyConfigured

class RegexRoutePattern(object):

    def __init__(self, regex, view, kwargs=None):
        if kwargs is None:
            self.kwargs = {}

        self.regex = re.compile(regex)
        self.view = self._get_view(view)

    def _get_view(self, view):
        try:
            module = import_y(''.join(view.split('.')[:-1]))
            view_func = getattr(module, view.split('.')[-1])
        except (ImportError, AttributeError):
            raise ImproperlyConfigured('View function {0} does not exist'.format(view))
        return view_func

    def match(self, raw):
        results = self.regex.search(raw)
        if results is not None:
            return results.groupdict()
        else:
            return False


class RegexRouteResolver(object):

    def __init__(self, routepatterns):
        if isinstance(routepatterns, basestring):
            try:
                routeconf = import_y(routepatterns)
            except ImportError:
                raise ImproperlyConfigured('Routeconf {0} could not be imported'.format(routepatterns))
            try:
                self.patterns = getattr(routeconf, 'routepatterns')
            except AttributeError:
                raise ImproperlyConfigured('Routeconf {0} has no routepatterns attribute'.format(routepatterns))
        else:
            self.patterns = routepatterns

    def resolve(self, req):
        for route in self.patterns:
            if isinstance(route, RegexRouteResolver):
                out = route.resolve(req)
                if out is not None:
                    return out

            kwargs = route.match(req.msg)
            if kwargs:
                kwargs.update(route.kwargs)
                return route.view, kwargs

        return None

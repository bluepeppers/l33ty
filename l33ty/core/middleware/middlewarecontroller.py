import logging
import sys
import settings

if getattr(settings, 'DEBUG', False):
    log = logging.getLogger('debug')
    log.setLevel(logging.INFO)
else:
    log = logging.getLogger('warn')
    log.setLevel(logging.WARN)

class MiddlewareController(object):
    supported_actions = ('msg_in', 'msg_out')
    middlewares = []

    def __init__(self, settings):
        middlewares = getattr(settings, "MIDDLEWARE", [])

        for middleware in middlewares:
            self._load_middleware(middleware)

    def _load_middleware(self, middleware_location):
        #strip last identifier
        container_name = '.'.join(middleware_location.split('.')[:-1])
        name = middleware_location.split('.')[-1]
        try:
            __import__(container_name)
            container = sys.modules[container_name]
        except ImportError:
            log.warn('Could not import middleware %s' % middleware_location)
            return

        middleware = getattr(container, name, None)
        if middleware is None:
            log.warn('Could not import middleware %s' % middleware_location)
            return


        if not self._check_middleware_validity(middleware):
            log.warn('Middleware %s is not a valid piece of middleware' % middleware_location)
            return

        self.middlewares.append(middleware)

    def _check_middleware_validity(self, middleware):
        try:
            for action in self.supported_actions:
                getattr(middleware, action)
        except AttributeError:
            return False
        else:
            return True

    def send(self, action, **kwargs):
        if not action in self.supported_actions:
            log.warn('%s is a non supported middleware action' % action)

        for middleware in self.middlewares:
            middleware_instance = middleware()
            func = getattr(middleware_instance, action)
            kwargs = func(**kwargs)

        return kwargs
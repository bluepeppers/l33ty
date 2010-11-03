from l33ty.core.routing.defaults import route, routingpatterns

routepatterns = routingpatterns('',
    (r'^calc (?P<term>.+)', 'responces.calculator')
)
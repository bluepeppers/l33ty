from l33ty.core.routing.defaults import route, routingpatterns

routepatterns = routingpatterns('',
    (r'^(?P<first>\d+) (add|\+) (?P<second>\d+)', 'responces.add')
)
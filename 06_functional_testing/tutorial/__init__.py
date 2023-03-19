from pyramid.config import Configurator
from pyramid.response import Response

import time



def hello_world(request):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time + " | New request recieved!")
    return Response("<b>Tiden er</b> " + current_time)


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()
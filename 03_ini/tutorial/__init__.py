from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    print(request)
    return Response('<body><h1>Hello error!</h1></body>')


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()
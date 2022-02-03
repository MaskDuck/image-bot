from starlette.applications import Starlette
from starlette.routing import Route

from app import ping

routes = [Route('/', ping, method=['POST'])]


app = Starlette(routes=routes)

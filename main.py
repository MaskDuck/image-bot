from starlette.applications import Starlette
from starlette.routing import Route
import uvicorn

from app import ping

routes = [Route('/', ping, methods=['POST'])]


app = Starlette(routes=routes)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")


from starlette.responses import JSONResponse
import aiohttp

async def ping(r):
    return JSONResponse({'type': 1})


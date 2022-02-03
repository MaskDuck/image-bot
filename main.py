from sanic import Sanic
from sanic.response import json

app = Sanic('idk')

@app.route('/')
async def handler(r):
    return json({type:1})
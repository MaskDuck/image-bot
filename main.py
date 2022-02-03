from sanic import Sanic
from sanic.response import json

app = Sanic('A HTTP interaction based image manipulation bot.')

@app.route('/')
async def handler(r):
    return json({type:1})
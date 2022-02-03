from sanic import Sanic
from sanic.response import json

app = Sanic('idk')

@app.route('/')
async def handler(r):
    return json({'type':1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
from sanic import Sanic
from sanic.response import json, HTTPResponse
from nacl.signing import VerifyKey

from nacl.exceptions import BadSignatureError
import os

app = Sanic('idk')

PUBLIC_KEY = 'f964c9bf508247bce404a6d6069fb494fc56b276954253389723301bfe503f58'

@app.route('/', methods=["POST"])
async def handler(r):
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    signature = r.headers["X-Signature-Ed25519"]
    timestamp = r.headers["X-Signature-Timestamp"]
    await r.request_body()
    body = r.body.decode('utf-8')
    try:
        verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
        return json({"type": 1})
    except:
        return HTTPResponse(status=401, headers={'message': 'grow up'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)




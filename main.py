from sanic import Sanic
from sanic.response import json, HTTPResponse
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
import os

app = Sanic('idk')
PUBLIC_KEY = os.environ['publickey']
@app.route('/', methods=["POST"])
async def handler(r):
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    signature = r.headers["X-Signature-Ed25519"]
    timestamp = r.headers["X-Signature-Timestamp"]
    body = r.head.decode('utf-8')
    try:
        verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
        return json({"type": 1})
    except:
        return HTTPResponse(status=401)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
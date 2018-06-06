import websocket
import ssl
import json

ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
method = ["authorize", " "]

msg = json.dumps({ 'jsonrpc': '2.0', 'method': method[0], 'params': method[1] , 'id': 1 })

try:
    ws.connect("wss://emotivcortex.com:54321")

    ws.send(msg)

    result = ws.recv()
    print (result)
finally:
    ws.close()
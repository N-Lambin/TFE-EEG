import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("emotivcortex.com", 54321))

msg = "{ 'jsonrpc': '2.0', 'method': 'hello', 'params: { 'hello': 'world' }, 'id': 1 }"
binMsg = json.dumps(msg).encode('utf-8')

s.send(binMsg)
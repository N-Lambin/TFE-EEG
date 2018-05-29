import socket
import json
import sys

msg1 = '{ "jsonrpc": "2.0", "method": "hello", "params": { "hello": "world" }, "id": 1 }'
msg2 = "{ 'jsonrpc': '2.0', 'method': 'hello', 'params': { 'hello': 'world' }, 'id': 1 }"
jsonMsg = json.dumps(msg2).encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("ws://emotivcortex.com", 54321))
    s.sendall(jsonMsg)

    received = s.recv(1024)
finally:
    s.close()

print ("Sent:     {}".format(jsonMsg))
print ("Received: {}".format(received))
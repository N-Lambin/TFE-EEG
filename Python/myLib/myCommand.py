import websocket_server
import websocket
import ssl
import json

ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

def sendToApi(command):
    try:
        ws.connect("wss://emotivcortex.com:54321")
        ws.send(command)
        result= ws.recv()
        return result
    finally:
        ws.close()

def getToken():
    client_id = open('D:\\noela\\Documents\\3TI\\TFE\\EmotivAPIConnection\\client_id.txt', 'r').read()
    client_secret = open('D:\\noela\\Documents\\3TI\\TFE\\EmotivAPIConnection\\client_secret.txt', 'r').read()
    license_key = open('D:\\noela\\Documents\\3TI\\TFE\\EmotivAPIConnection\\license_key.txt', 'r').read()

    auth_json = sendToApi(authorize(client_id, client_secret, license_key))
    return json.loads(auth_json)["result"]["_auth"]

def authorize(client_id, client_secret, license):
    return json.dumps({ 'jsonrpc': '2.0', 'method': 'authorize', 'params': \
        { 'client_id': client_id, 'client_secret': client_secret, 'license': license, 'debit': 10 } , 'id': 1 })

def queryHeadsets():
    query_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'queryHeadsets', 'params': \
        { } , 'id': 1 }))

def createSession(token):
    session_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'createSession', 'params': \
        { '_auth': token, 'status': 'open' } , 'id': 1 }))
    return json.loads(session_json)["result"]["status"]

def activeSession(token):
    activeSession_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'updateSession', 'params': \
        { '_auth': token, 'status': 'active' } , 'id': 1 }))
    return json.loads(activeSession_json)#["result"]["status"]

def startRecord(token, id):
    startRecord_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'updateSession', 'params': \
        { '_auth': token, 'status': 'startRecord', 'session': id } , 'id': 1 }))
    return json.loads(startRecord_json)["result"]["status"]

def stopRecord(token, id):
    stopRecord_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'updateSession', 'params': \
        { '_auth': token, 'status': 'stopRecord', 'session': id } , 'id': 1 }))
    return json.loads(stopRecord_json)["result"]["status"]

def closeSession(token, id):
    closeSession_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'updateSession', 'params': \
        { '_auth': token, 'status': 'close', 'session': id } , 'id': 1 }))
    return json.loads(closeSession_json)["result"]["status"]

def subscribe(token):
    data = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'subscribe', 'params': \
        { '_auth': token, 'streams': [ 'eeg' ], 'replay': 'false' } , 'id': 1 }))
    return json.loads(data)["result"]["sid"]

def unsubscribe(token, sid):
    message = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'unsubscribe', 'params': \
        { '_auth': token, 'streams': [ 'eeg' ], 'session': sid, 'replay': 'false' } , 'id': 1 }))
    return json.loads(message)["result"]["message"]
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
    return json.loads(query_json)["result"]

def createSession(token):
    session_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'createSession', 'params': \
        { '_auth': token, 'status': 'open' } , 'id': 1 }))
    return json.loads(session_json)["result"]["status"], json.loads(session_json)["result"]["id"]

def activeSession(token, sid):
    activeSession_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'updateSession', 'params': \
        { '_auth': token, 'session': sid, 'status': 'active' } , 'id': 1 }))
    return json.loads(activeSession_json)#["result"]["status"]

def startRecord(token, sid):
    startRecord_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'updateSession', 'params': \
        { '_auth': token, 'status': 'startRecord', 'session': sid } , 'id': 1 }))
    return json.loads(startRecord_json)["result"]["status"]

def stopRecord(token, sid):
    stopRecord_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'updateSession', 'params': \
        { '_auth': token, 'status': 'stopRecord', 'session': sid } , 'id': 1 }))
    return json.loads(stopRecord_json)["result"]["status"]

def closeSession(token, sid):
    closeSession_json = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'updateSession', 'params': \
        { '_auth': token, 'status': 'close', 'session': sid } , 'id': 1 }))
    return json.loads(closeSession_json)["result"]["status"]

def subscribe(token, sid):
    data = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'subscribe', 'params': \
        { '_auth': token, 'streams': [ 'mot' ], 'session': sid } , 'id': 1 })) 
    return json.loads(data)#["result"]["sid"]
""" , 'session': sid, 'replay': 'false' """
def unsubscribe(token, sid):
    message = sendToApi(json.dumps({ 'jsonrpc': '2.0', 'method': 'unsubscribe', 'params': \
        { '_auth': token, 'streams': [ 'mot' ], 'session': sid } , 'id': 1 }))
    return json.loads(message)#["result"]["message"]
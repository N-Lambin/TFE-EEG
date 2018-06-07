import __init__
import myLib.myCommand as mco

#__init__
#model = __init__.model
token = __init__.token

query = mco.queryHeadsets()
print(query)
id = mco.createSession(token)
print(id)
status = mco.activeSession(token)
print(status)
sid = mco.subscribe(token)
print(sid)
msg = mco.unsubscribe(token, sid)
print(msg)

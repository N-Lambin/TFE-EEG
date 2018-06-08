import __init__
import myLib.myCommand as mco
import time

#__init__()
#model = __init__.model
token = __init__.token

""" query = mco.queryHeadsets()
print(query) """

status, sid = mco.createSession(token)
print(status)
print(sid)

time.sleep(1)
print("\n ################################################################## \n")
time.sleep(1)

status = mco.activeSession(token, sid)
print(status)

time.sleep(1)
print("\n ################################################################## \n")
time.sleep(1)

sid = mco.subscribe(token,sid)
print(sid)

time.sleep(1)
print("\n ################################################################## \n")
time.sleep(1)

msg = mco.unsubscribe(token, sid)
print(msg)

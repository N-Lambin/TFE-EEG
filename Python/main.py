import init
import myLib.myCommand as mco
import myLib.mySSH as ssh
import myLib.myDataExtractor as mde
import time

hostname = 'ev3dev'
port = 22
username = 'robot' 
password = 'maker'

model = init.model

#exemple of prediction
data = [[-2.9568,-1.4297,0.61135,8.59947]]
command = model.predict(data)[0]
print(command)

try:
    client = ssh.connectionSSH(hostname, port, username, password)
    try:
        if command == 'a':
            isConnected = False
        elif command == 'neutral':
            ssh.commandSSH(client, './forward.sh')
        elif command == 's':
            ssh.commandSSH(client, './backward.sh')
        elif command == 'winkLeft':
            ssh.commandSSH(client, './left.sh')
            print('./left.sh')
        elif command == 'd':
            ssh.commandSSH(client, './right.sh')
        elif command == 'e':
            ssh.commandSSH(client, './hold.sh')
        elif command == 'r':
            ssh.commandSSH(client, './release.sh')
        else:
            print ('Command not found')
    finally:
        ssh.closeSSH(client)
        print('Close SSh client')
except:
    print('No client found')
import init
import myLib.myCommand as mco
import myLib.mySSH as ssh
import time

model = init.model

#exemple of prediction
data = [[1.12099,1.01106,2.73168,2.40717,3.69027,3.25942,1.15452,1.03170]]
command = model.predict(data)

print(command)

try:
    client = ssh.connectionSSH(hostname, port, username, password)
    isConnected = True
    try:
        while isConnected:
            if (command == 'a'):
                isConnected = False
            elif (command == ' neutral'):
                ssh.commandSSH(client, './forward.sh')
            elif (command == 's'):
                ssh.commandSSH(client, './backward.sh')
            elif (command == ' winkLeft'):
                ssh.commandSSH(client, './left.sh')
            elif (command == 'd'):
                ssh.commandSSH(client, './right.sh')
            elif (command == 'e'):
                ssh.commandSSH(client, './hold.sh')
            elif (command == 'r'):
                ssh.commandSSH(client, './release.sh')
            else:
                print ('Command not found')
    finally:
        ssh.closeSSH(client)
except:
    print('no client found')
import init
import myLib.myCommand as mco
import myLib.mySSH as ssh
import time

init
model = init.model

#exemple of prediction
data = [[37.6695, 5.56588, 6.60943, 9.56798, 20.6567, 5.13102, 1.44630, 0.43651, 0.04982, 0.15489]]
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
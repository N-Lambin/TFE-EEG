import string
import sys
import myLib.mySSH as ssh

hostname = 'ev3dev'
port = 22
username = 'robot' 
password = 'maker'

try:
    client = ssh.connectionSSH(hostname, port, username, password)
    isConnected = True
    try:
        while isConnected:
            command = raw_input('Enter command here \n')
            command = string.replace(command, '\r', '')
            if (command == 'a'):
                isConnected = False
            elif (command == 'z'):
                ssh.commandSSH(client, './forward.sh')
            elif (command == 's'):
                ssh.commandSSH(client, './backward.sh')
            elif (command == 'q'):
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

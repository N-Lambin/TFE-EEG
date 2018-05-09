from mySSH import connectionSSH, commandSSH, closeSSH
import string

hostname = 'ev3dev'
port = 22
username = 'robot' 
password = 'maker'

try:
    client = connectionSSH(hostname, port, username, password)
    isConnected = True
    try:
        while isConnected:
            command = raw_input('Enter command here \n')
            command = string.replace(command, '\r', '')
            if (command == 'a'):
                isConnected = False
            elif (command == 'z'):
                commandSSH(client, './forward.sh')
            elif (command == 's'):
                commandSSH(client, './backward.sh')
            elif (command == 'q'):
                commandSSH(client, './left.sh')
            elif (command == 'd'):
                commandSSH(client, './right.sh')
            elif (command == 'e'):
                commandSSH(client, './hold.sh')
            elif (command == 'r'):
                commandSSH(client, './release.sh')
            else:
                print ('Command not found')
    finally:
        closeSSH(client)
except:
    print('no client found')

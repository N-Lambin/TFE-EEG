#import string
import sys
import myLib.mySSH as ssh
import myLib.mySupervisedLearning as msl

Xnew = [[37.6695, 5.56588, 6.60943, 9.56798, 20.6567, 5.13102, 1.44630, 0.43651, 0.04982, 0.15489]]
hostname = 'ev3dev'
port = 22
username = 'robot' 
password = 'maker'

model = msl.trainingDecisionTree()
command = model.predict(Xnew)

try:
    client = ssh.connectionSSH(hostname, port, username, password)
    isConnected = True
    try:
        while isConnected:
            command = input('Enter command here \n')
            command = command.replace('\r', '')
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
    print ('no client found')
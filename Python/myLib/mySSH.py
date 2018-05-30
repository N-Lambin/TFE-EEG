import paramiko
import sys
import numpy as np
import time

#example of parameters
hostname = 'ev3dev'
port = 22
username = 'robot' 
password = 'maker'
nbytes = 4096
command = 'ls'

def connectionSSH(hostname, port, username, password):
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    return client

def commandSSH(client, command):
    try:
        stdout_data = []
        stderr_data = []
        session = client.open_channel(kind='session')
        nbytes = 4096 

        session.exec_command(command)

        while True:
            if session.recv_ready():
                stdout_data.append(session.recv(nbytes))
            if session.recv_stderr_ready():
                stderr_data.append(session.recv_stderr(nbytes))
            if session.exit_status_ready():
                break

        """ print ('exit status: '.join(np.array(session.recv_exit_status())))
        print (''.join(np.array(stdout_data)))
        print (''.join(np.array(stderr_data))) """

    finally:
        session.close()

def closeSSH(client):
    client.close()
    print ('Fermeture du client ssh')

def moveFrancis(client):
    ssh.commandSSH(client, './forward.sh')
    time.sleep(1)
    ssh.commandSSH(client, './backward.sh')
    time.sleep(1)
    ssh.commandSSH(client, './left.sh')
    time.sleep(1)
    ssh.commandSSH(client, './right.sh')
    time.sleep(1)
    ssh.commandSSH(client, './hold.sh')
    time.sleep(1)
    ssh.commandSSH(client, './release.sh')
    time.sleep(1)
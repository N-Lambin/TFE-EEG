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

        print ('exit status: ', session.recv_exit_status())
        print (' '.join(stdout_data))
        print (' '.join(stderr_data))

    finally:
        session.close()

def closeSSH(client):
    client.close()

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
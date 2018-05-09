from mySSH import connectionSSH, commandSSH, closeSSH
import string

hostname = 'ev3dev'
port = 22
username = 'robot' 
password = 'maker'

client = connectionSSH(hostname, port, username, password)

if (client):
    isConnected = True
    try:
        command = "export MC0=/sys/class/tacho-motor/motor0;\
        echo reset > $MC0/command;\
        echo 500 > $MC0/speed_sp;\
        run-for-time() {\
            echo run-forever > $MC0/command;\
            sleep $1;\
            echo stop > $MC0/command;\
        };\
        run-for-time 1"
        commandSSH(client, command)

        """ 
        command = "echo 500 > $MC0/speed_sp; echo stop $MC0/command"
        commandSSH(client, command)

        command = "export MC1=/sys/class/tacho-motor/motor1"
        commandSSH(client, command)
        command = "echo 1000 > $MC1/speed_sp"
        commandSSH(client, command)

        command = "export MC2=/sys/class/tacho-motor/motor2"
        commandSSH(client, command)
        command = "echo 1000 > $MC2/speed_sp"
        commandSSH(client, command)

        command = "run-for-time0() { echo run-forever > $MC0/command; sleep $1; echo stop > $MC0/command; }"
        commandSSH(client, command)
        command = "run-for-time1() { echo run-forever > $MC1/command; sleep $1; echo stop > $MC1/command; }"
        commandSSH(client, command)
        command = "run-for-time2() { echo run-forever > $MC2/command; sleep $1; echo stop > $MC2/command; }"
        commandSSH(client, command) """

    finally:
        closeSSH(client)
else:
    print('No client found')

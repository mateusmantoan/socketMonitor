import socket
import commands
import time

print('IP Server: ')
HOST = raw_input()
PORT = 2907
print('Frequency of monitoring (in seconds): ')
FREQUENCY = raw_input()

print('\nMonitoring host and sending msgs\n\n')

while True:
    mem = commands.getoutput('cat /proc/meminfo | grep Mem')
    disc = commands.getoutput('df --total -h | grep total')
    top = commands.getoutput("top -n 1 | sed -n '2,5p'")

    msg = '\n\nMEMORY INFORMATIONS:\n' + mem + '\n\nACTUAL STATE OF STORAGE DISC\n' + disc + '\n\nTOP CMD OUTPUT:\n' + top + '\n\n\n'
    msg_disc = 'ACTUAL STATE OF STORAGE DISC'
    msg_top = 'TOP CMD OUTPUT:'
    msg_users = 'USERS CURRENTLY LOGGED'

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    udp.sendto (msg, dest)
    udp.close()
    time.sleep(int(FREQUENCY))

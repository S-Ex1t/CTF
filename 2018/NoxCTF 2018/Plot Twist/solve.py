import socket
from mt19937predictor import MT19937Predictor

host = 'chal.noxale.com'
port = 5115
a = MT19937Predictor()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
for i in range(624):
	s.recv(64)
	send = ' ' * 16
	s.send(send)
	a.setrandbits(int(s.recv(64).split()[-1]),32)

s.recv(64)
send = str(a.getrandbits(32)).rjust(16,'0')
s.send(send)
print s.recv(64)

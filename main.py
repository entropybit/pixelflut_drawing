#!/usr/bin/python
import socket
import numpy as np
from time import sleep

# chose random color
r = lambda: np.random.randint(0,255)
color = str('%02X%02X%02X' % (r(),r(),r()))

print(" selected color is : " + str(color))



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('151.217.40.82', 1234))

def get_rand_point(X_RES, Y_RES):
	x = np.random.randint(0,X_RES)
	y = np.random.randint(0,Y_RES)

	return x,y

message_get_size = b'SIZE\n'

s.sendall(message_get_size)

data = s.recv(1024)
data = data.decode('utf-8')

print(data)

X_RES = int(data.split(" ")[1])
Y_RES = int(data.split(" ")[2].strip("\n'"))

def draw_pixel(x,y):

	x = int(x)
	y = int(y)
	message_send_pixel = 'PX ' + str(x) + ' '+ str(y) + ' ' + str(color) + '\n'
	#print(message_send_pixel)
	message_send_pixel = message_send_pixel.encode()
	s.sendall(message_send_pixel)

def draw_rect(x,y, w, h):
	for dx in range(w):
		for dy in range(h):
			draw_pixel(x+dx, y+dy)

	


def pingpong_point_drawing(w,h, x0, y0, X_MAX=X_RES, Y_MAX=Y_RES):

	x = x0
	y = y0

	dx = +1
	dy = +1 

	while True:
		draw_rect(x,y, w, w)
		
		if x + w + dx > X_MAX or x +dx <= 0:
			dx *= -1

		if y + h + dy > Y_MAX or y + dy <= 0:
			dy *= -1

		x += dx
		y += dy

		#print(" (" + str(x) + "," + str(y) +")")
	
		#sleep(0.00001)


			
		

if __name__=="__main__":

	# chose random starting postion

	x0 = np.random.randint(0, X_RES)
	y0 = np.random.randint(0, Y_RES)
	pingpong_point_drawing(10,10, x0, y0)		
		
		

				



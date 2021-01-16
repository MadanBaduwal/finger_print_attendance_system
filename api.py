from serial import Serial
import time


# # From arduino to python
# arduino = Serial('COM1', 115200, timeout=.1)
# while True:
# 	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
# 	if data:
# 		print (data)



# From python to arduino
arduino = Serial('/dev/ttyUSB0', 9600, timeout=.1)
time.sleep(1) #give the connection a second to settle

arduino.write(bytes('e\r\n','utf-8'))
while True:
	data = arduino.readline()
	if data:
		print(data)
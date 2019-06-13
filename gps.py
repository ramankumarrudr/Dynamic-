import serial
import datetime
ser = serial.Serial('/dev/ttyACM1',9600)
for i in range(1):
	se = ser.readline()
	se = se.decode('ascii','ignore')
	z = str(se)
	print(z+"\n")


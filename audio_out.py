from gtts import gTTS
import os
from playsound import playsound
from datetime import datetime
import serial
audios = [
	"Speed Limit 70",
	"Stop",
	"Dont Sound Horn",
	"No right turn allowed",
	"No U turn allowed",
	"Speed Limit 120",
	"Speed Limit 50",
]
#ser = serial.Serial('/dev/ttyACM1',9600)
#se = ser.readline()
#se = se.decode('ascii','ignore')
#z = str(se)


lan = 'en'

def audioOutput(i):
	for j in range(0,len(audios)):
		if i==j:
			obj = gTTS(text=audios[i],lang = lan , slow=False)
			now = datetime.now()
			
			timestamp = datetime.timestamp(now)
			print("Predicted Lable: ",audios[i],"timestamp : ",timestamp)#,"gps:",z )
			obj.save("audio.mp3")
			playsound('audio.mp3')
			




import serial 
import time

def setup(): 
	global s 
	s = serial.Serial("/dev/ttyS0", 57600) 

def getSensingData(): 
	sensingData = s.readline()
	print sensingData
	temperatureHumidityList = sensingData.split(":")
	print temperatureHumidityList
	print temperatureHumidityList[0]
	print temperatureHumidityList[1]

if __name__ == '__main__': 
	setup() 
	while True: 
		getSensingData()
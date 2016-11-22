import serial 
import time
s = None

# *********************************************************************
# open serial COM port to /dev/ttyS0, which maps to UART0(D0/D1)
# the baudrate is set to 57600 and should be the same as the one
# specified in the Arduino sketch uploaded to ATMega32U4.
# *********************************************************************

def setup(): 
  global s 
  s = serial.Serial("/dev/ttyS0", 57600) 

# *********************************************************************
# send "1" to the Arduino sketch on ATMega32U4.
# the sketch will turn on the LED attached to D13 on the board 
# send "0" to the sketch to turn off the LED
# *********************************************************************

def loop(): 

  s.write("1") 
  time.sleep(1) 
  s.write("0") 
  time.sleep(1) 

if __name__ == '__main__': 
  setup() 
  while True: 
    loop()
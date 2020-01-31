import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Motor1 = [21,20,16,12]
Motor2 = [6,13,19,26]

for pin in range(4):
	GPIO.setup(Motor1[pin],GPIO.OUT)
	GPIO.output(Motor1[pin],0)
	GPIO.setup(Motor2[pin],GPIO.OUT)
	GPIO.output(Motor2[pin],0)
	
seq = [ [1,0,0,0],
		[1,1,0,0],
		[0,1,0,0],
		[0,1,1,0],
		[0,0,1,0],
		[0,0,1,1],
		[0,0,0,1],
		[1,0,0,1] ]

while True:
	for i in range(512):
		for halfstep in range(8):
			for pin in range(4):
				GPIO.output(Motor1[pin], seq[halfstep][pin])
				GPIO.output(Motor2[pin], seq[7-halfstep][pin])			
			time.sleep(0.0006)  

GPIO.cleanup()


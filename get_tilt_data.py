from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
import time
import osc_pipe as op

def onAccelerationChange(self, acceleration, timestamp):
	#print("Acceleration: \t"+ str(acceleration[0])+ "  |  "+ str(acceleration[1])+ "  |  "+ str(acceleration[2]))
	#print("Timestamp: " + str(timestamp))
	#print("----------")
    #round(acceleration, 4)
    print(acceleration)
    data = [int(acceleration[0]*10000),int(acceleration[1]*10000)]
    learn = [float(data[0]),float(data[1])]
    op.send("127.0.0.1",6448, learn)

def main():
	accelerometer0 = Accelerometer()

	accelerometer0.setOnAccelerationChangeHandler(onAccelerationChange)

	accelerometer0.openWaitForAttachment(5000)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	accelerometer0.close()

main()

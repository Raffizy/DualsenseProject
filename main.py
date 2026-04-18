from pydualsense import *
import time
# get dualsense instance
ds = pydualsense()
# initialize controller and connect
ds.init()

print('Drive Simulation prototype')

last_square= False
last_cross= False

#switch Force
Force=1

ds.triggerR.setMode(TriggerModes.Pulse)
#debug command+ main loop
# loop until r1 is pressed to feel effect
while not ds.state.R1:
    ##gear shift simulation
    if ds.state.square and not last_square:
        Force += 1
        
        Force = min(Force, 6)
        print("Force set to ", Force)

    if ds.state.cross and not last_cross:
        Force -= 1
        Force = max(Force, 1)
        print("Force set to ", Force)

    last_square = ds.state.square
    last_cross = ds.state.cross
    #Set L trigger as to simulate break
    #ds.triggerL.setMode(TriggerModes.Rigid)
    #ds.triggerL.setForce(1, 255)

    # set R trigger to simulate road feel, clutch
    ds.triggerR.setForce(Force, 255)
    time.sleep(0.01)


# terminate the thread for message and close the device

ds.close()

print("Device Closed")
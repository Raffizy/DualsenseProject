
from pydualsense import pydualsense, TriggerModes

def cross_pressed(state):
    print(state)

ds = pydualsense() # open controller
ds.init() # initialize controller
state = "active"
ds.cross_pressed += cross_pressed
ds.light.setColorI(255,0,0) # set touchpad color to red
ds.triggerL.setMode(TriggerModes.Rigid)
ds.triggerL.setForce(1, 255)

if bool(state) == False:
    ds.close()
    # closing the controller   

 

from robodk.robolink import *
from robodk import *
import time

###establishing the connection with RoboDK Robot.
RDK = Robolink()

##configuring two different robots as robodk items
robot_1 = RDK.Item('Epson VT6')
#####robot_2 = RDK.Item('Robot_2')


###setting pose of the robot using joint values on each axis.
robot_1.setJoints([0,0,0,0,0,0])
time.sleep(10)
robot_1.setJoints(([-90,0,0,-90,-90,0]))

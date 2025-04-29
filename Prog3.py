from robodk.robolink import *
from robodk import *
import time

###establishing the connection with RoboDK Robot.
RDK = Robolink()

##configuring two different robots as robodk items
robot_1 = RDK.Item('Epson VT6')



##get the targets by target names
home = RDK.Item('Home_1')
p1 = RDK.Item('Target 2')
p2 = RDK.Item('Target 3')
p3 = RDK.Item('Target 4')


###setting robot speed
robot_1.setSpeed(200)

###moving robots to targets
robot_1.MoveJ(home)
robot_1.MoveL(p1)
robot_1.MoveL(p2)
robot_1.MoveL(p3)
robot_1.MoveJ(home)

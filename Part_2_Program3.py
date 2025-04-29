from robodk.robolink import *
from robodk.robomath import *
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
robot_1.setSpeed(800)


####using Pose() * transl function to compute the targets
for i in range(0,5):
    i = i*25
    corner1 = p3.Pose()*transl(0,0,i)
    corner2 = p3.Pose()*transl(125,0,i)
    corner3 = p3.Pose()*transl(125,125,i)
    corner4 = p3.Pose()*transl(0,125,i)

    robot_1.MoveL(corner1)
    robot_1.MoveL(corner2)
    robot_1.MoveL(corner3)
    robot_1.MoveL(corner4)
    robot_1.MoveL(corner1)

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




###Creating pose from Target
target_1_pose = p1.Pose()
print(target_1_pose)

###adding target and setting pose from progam directly

target7 = RDK.AddTarget('Target 7')

target7.setPose(KUKA_2_Pose([10,360,540,92,0,-180]))

robot_1.MoveL(target7)


target8 = RDK.AddTarget('Target 8')

target8.setPose(Fanuc_2_Pose([50,380,540,-180,0,92]))

robot_1.MoveL(target8)

import sys
import time
#print(sys.path)
sys.path.insert(0, r'D:\Documents\VScode\python\lib')
import jkrc

PI = 3.1415926
ABS = 0
INCR = 1

robot = jkrc.RC("192.168.0.5")

ret = robot.login()

robot.power_on()

robot.enable_robot()

if ret[0] == 0:
    print("login success")
else:
    print("login failed")

joint_pos_1=[-90 * PI / 180, 41 * PI / 180, 73 * PI / 180, 245 * PI / 180, 90 * PI / 180, 45 * PI / 180]
joint_pos_2=[-90 * PI / 180, 69 * PI / 180, 115 * PI / 180, 175 * PI / 180, 90 * PI / 180, -45 * PI / 180]

robot.joint_move(joint_pos=[-66 * PI / 180, 82 * PI / 180, 115 * PI / 180, 161 * PI / 180, 90 * PI / 180, -44 * PI / 180], move_mode=INCR, is_block=False ,speed=1)
print(1)
ret = robot.get_joint_position() 
ret_joint_pos = ret[1]
print(2)
robot.joint_move(joint_pos=ret_joint_pos, move_mode=ABS, is_block=False, speed=1)

for i in range(5):
	if (i %2 == 0):
		tmp = joint_pos_1
		print(11)
	else:
		tmp = joint_pos_2
		print(22)
	joint_pos = tmp
	robot.joint_move(joint_pos, ABS, True, 1)

robot.logout()
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

joint_pos_home=[0 * PI / 180, 60.9565 * PI / 180, 88.4566 * PI / 180, 120.587 * PI / 180, -90 * PI / 180, 3.50761e-15 * PI / 180]
joint_pos_place=[-90 * PI / 180, 60.9565 * PI / 180, 88.4566 * PI / 180, 120.587 * PI / 180, -90 * PI / 180, 3.50588e-15 * PI / 180]
'''
robot.joint_move(joint_pos=joint_pos_home, move_mode=ABS, is_block=False ,speed=1)
robot.joint_move(joint_pos=joint_pos_place, move_mode=ABS, is_block=False ,speed=1)

home = robot.kine_forward(joint_pos_home)[1]
place = robot.kine_forward(joint_pos_place)[1]

print("tcp home: ",home)
print("tcp place: ",place)

robot.linear_move(end_pos=home,move_mode=ABS,is_block = True,speed = 120)
robot.linear_move(end_pos=place,move_mode=ABS,is_block = True,speed = 120)
'''
home=[-200.00015221426375, 115.00990876026123, 482.314637114134, -3.141591727327405, 8.726725947953472e-07, 1.5707963000003808]
place=[115.01000213623045, 200.0000588382945, 482.3146371140525, 3.1415926, -0.0, 0.0]
x=100;y=265
robot.joint_move(joint_pos=joint_pos_home,move_mode=ABS,is_block = False,speed = 1)			#HOME
# robot.linear_move(end_pos=home,move_mode=ABS,is_block = True,speed = 60)					#Linear home
obj=home;obj[0]=obj[0]-x;obj[1]=obj[1]-y													#Cartesian pose obj

robot.linear_move(end_pos=obj,move_mode=ABS,is_block = False,speed = 120)					#Pick OBJ 1

# import ipdb; ipdb.set_trace()
robot.joint_move(joint_pos=joint_pos_home,move_mode=ABS,is_block = False,speed = 1)			#HOME
robot.joint_move(joint_pos=joint_pos_place,move_mode=ABS,is_block = False,speed = 1)			#PLACE
x=-100;y=-100
place_obj=place;place_obj[0]=place_obj[0]-x;place_obj[1]=place_obj[1]-y						#Cartesian pose place obj
robot.linear_move(end_pos=place_obj,move_mode=ABS,is_block = True,speed = 120)				#Place OBJ 1




# ret = robot.get_tcp_position() 
# if ret[0] == 0:
# 	print("the tcp position is :",ret[1]) 
# else:
# 	print("some things happend,the errcode is: ",ret[0])

# time.sleep(1)
robot.logout()
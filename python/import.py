import sys
import time

#print(sys.path)
sys.path.insert(0, r'D:\Documents\VScode\python\lib')

import jkrc
#COORD_BASE = 0     #Base coordinate system
#COORD_JOINT = 1    #Joint space
#COORD TOOL = 2     #Tool coordinate system

robot = jkrc.RC("192.168.0.4")#Replace the IP with IP robot that you are using currently

robot.login() #Log in

ret = robot.get_tcp_position() 
if ret[0] == 0:
    print("the tcp position is :", ret[1])
else:
    print("some things happend, the eercode is: ", ret[0])

robot.power_on()

robot.enable_robot()

ret = robot.get_sdk_version()
print("SDK version is:",ret[1])

robot.logout() #Log out


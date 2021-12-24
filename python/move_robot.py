#!/usr/bin/env python3

"""
NOTE:
"""

import sys
import time
#print(sys.path)
sys.path.insert(0, r'D:\Documents\VScode\python\lib')
import jkrc

PI = 3.1415926
ABS = 0
INCR = 1
IO_CABINET = 0
IO_TOOL = 1
IO_EXTEND = 2

IP = "192.168.0.2"
home = [-90 * PI / 180, 41 * PI / 180, 73 * PI / 180, 245 * PI / 180, 90 * PI / 180, 45 * PI / 180]
base_pos = [0 * PI / 180, 60.9565 * PI / 180, 88.4566 * PI / 180, 120.587 * PI / 180, -90 * PI / 180, 3.50761e-15 * PI / 180]

def move_to_target(obj,base=[0,0,0,0,0,0], x=0, y=0, w=0, z=0, def_speed = 60):
    ''' obj: is object of class RC. Object = jkrc.RC(IP)
        base: is the origin of the coordinate Descartes. Type: joint_pos
        x,y,w: error compared to base. x,y(mm); z(degree)
        z: height need to be reduced to pick up objects
    '''
    # print("base:",base)
    obj.joint_move(joint_pos=base, move_mode=ABS, is_block=False ,speed=1)
    base[5] = base[5] - w * PI / 180
    temp = list(obj.kine_forward(base)[1])
    temp[0] = temp[0] - x
    temp[1] = temp[1] - y
    target = temp
    obj.linear_move(end_pos=target,move_mode=ABS,is_block = True,speed = def_speed)
    # print(obj.get_tcp_position()[1])
    # print(target)
    while(obj.is_in_pos()[1]!=1):()
    """ state is equal to 1: The robot reaches the specified location
        state is equal to 0: The robot has not reached the specified location
    """
    target[2] = target[2] - z
    obj.linear_move(end_pos=target,move_mode=ABS,is_block = True,speed = def_speed)
    while(obj.is_in_pos()[1]!=1):()
    
def main(argv):
    robot = jkrc.RC(IP)
    ret = robot.login()
    robot.power_on()
    robot.enable_robot()
    if ret[0] == 0:
        print("login success")
    else:
        print("login failed")

    robot.set_digital_output(iotype = IO_CABINET,index = 14,value = 0)
    robot.set_digital_output(iotype = IO_CABINET,index = 15,value = 0)

    robot.joint_move(joint_pos=home, move_mode=ABS, is_block=False ,speed=1)

    move_to_target(obj=robot,base=base_pos,x=200,y=200,w=45,z=100,def_speed=120)
    robot.set_digital_output(iotype = IO_CABINET,index = 14,value = 1)
    
    robot.logout()
    print("log out")

if __name__ == "__main__":
    main(sys.argv)
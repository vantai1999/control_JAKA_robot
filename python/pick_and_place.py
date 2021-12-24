#!/usr/bin/env python3

"""
NOTE:
"""

import sys
import time
#print(sys.path)
sys.path.insert(0, r'D:\Documents\VScode\python\lib')
import jkrc

IP = "192.168.0.5"
PI = 3.1415926
ABS = 0
INCR = 1
IO_CABINET = 0
IO_TOOL = 1
IO_EXTEND = 2

def move_to():
    print("")

def main(argv):
    # My code here
    robot = jkrc.RC(IP)
    ret = robot.login()
    robot.power_on()
    robot.enable_robot()
    if ret[0] == 0:
        print("login success")
    else:
        print("login failed")

    factory = [-90 * PI / 180, 41 * PI / 180, 73 * PI / 180, 245 * PI / 180, 90 * PI / 180, 45 * PI / 180]
    robot.joint_move(joint_pos=factory, move_mode=ABS, is_block=False ,speed=1)
    robot.set_digital_output(iotype = IO_CABINET,index = 14,value = 0)
    robot.set_digital_output(iotype = IO_CABINET,index = 15,value = 0)
    home = [-90 * PI / 180, 69 * PI / 180, 115 * PI / 180, 175 * PI / 180, 90 * PI / 180, -45 * PI / 180]
    robot.joint_move(joint_pos=home, move_mode=ABS, is_block=False ,speed=1)
    NEWPOINT1 = [-66 * PI / 180, 82 * PI / 180, 115 * PI / 180, 161 * PI / 180, 90 * PI / 180, -44 * PI / 180]
    robot.joint_move(joint_pos=NEWPOINT1, move_mode=ABS, is_block=False ,speed=1)
    Pick = [-68 * PI / 180, 118 * PI / 180, 66 * PI / 180, 216 * PI / 180, 88 * PI / 180, -48 * PI / 180]
    robot.joint_move(joint_pos=Pick, move_mode=ABS, is_block=False ,speed=1)
    while(robot.get_joint_position()[1]!=Pick):()
    robot.set_digital_output(iotype = IO_CABINET,index = 14,value = 1)
    time.sleep(1)
    NEWPOINT2 = [-94 * PI / 180, 98 * PI / 180, 93 * PI / 180, 146 * PI / 180, 104 * PI / 180, -50 * PI / 180]
    robot.joint_move(joint_pos=NEWPOINT2, move_mode=ABS, is_block=False ,speed=1)
    sub_z_100mm = [-94 * PI / 180, 104 * PI / 180, 106 * PI / 180, 128 * PI / 180, 104 * PI / 180, -50 * PI / 180]
    robot.joint_move(joint_pos=sub_z_100mm, move_mode=ABS, is_block=False ,speed=1)
    while(robot.get_joint_position()[1]!=sub_z_100mm):()
    robot.set_digital_output(iotype = IO_CABINET,index = 14,value = 0)
    robot.joint_move(joint_pos=factory, move_mode=ABS, is_block=False ,speed=1)

    robot.logout()
    print("log out")

if __name__ == "__main__":
    main(sys.argv)

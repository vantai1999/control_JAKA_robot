import sys

sys.path.insert(0, r'D:\Documents\VScode\python\lib')
import jkrc

"""
robot = jkrc.RC("192.168.1.115") # Instantizing a robot object
robot.login() #Connect the robot controller
pass
robot.logout() #Disconnect the controller
"""

"""
robot = jkrc.RC("192.168.1.115") # Instantizing a robot object
robot.login() #Connect the robot controller
ret = robot.get_sdk_version()
print("SDK version is:",ret[1])
robot.logout() #Disconnect the controller
"""

"""
robot.power_on() #Turn on robot - delay about 8s
robot.power_off() #Turn off robot
robot.shut_down() #Shut down
"""





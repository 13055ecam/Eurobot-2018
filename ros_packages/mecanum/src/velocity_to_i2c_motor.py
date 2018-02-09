#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

from i2c import I2C

pub = None

def motor_front_left(vel):
    print vel
    robot_i2c.send(vel)

def motor_front_left(vel):
    print vel
    robot_i2c.send(vel)

def motor_front_left(vel):
    print vel
    robot_i2c.send(vel)

def motor_front_left(vel):
    print vel
    robot_i2c.send(vel)

if __name__ == '__main__':
    try:
        robot_i2c = I2C(0x05)
        rospy.init_node('velocity_to_i2c_motor')
        rospy.Subscriber('i2c/motor/fl', Float32, motor_front_left)
        rospy.Subscriber('i2c/motor/fr', Float32, motor_front_right)
        rospy.Subscriber('i2c/motor/bl', Float32, motor_back_left)
        rospy.Subscriber('i2c/motor/br', Float32, motor_back_right)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python3

import rospy
from std_msgs import msg
from SLERP.msg import Num

def slerper():
    pub = rospy.Publisher("function",Num, queue_size=20)
    rospy.init_node('slerper', anonymous=True)
    rate = rospy.Rate(10)


    while not rospy.is_shutdown():
        #a, b, c, d = input("Enter first quaternion values with comma between (1,0,0,0):").replace(",","")
        #w, x, y, z = input("Enter second quaternion values with comma between (0,1,0,0):").replace(",","") 
        #t = float(input("Enter interpolation value between 0 and 1: "))
        msg_to_publish = Num()
        msg_to_publish.q1.x = 1
        msg_to_publish.q1.y = 1
        msg_to_publish.q1.z = 1
        msg_to_publish.q1.w = 1
        msg_to_publish.q2.x = 1
        msg_to_publish.q2.y = 1
        msg_to_publish.q2.z = 1
        msg_to_publish.q2.w = 1
        msg_to_publish.t = 1
        rospy.loginfo(msg_to_publish)
        pub.publish(msg_to_publish)
        rate.sleep()


if __name__ == '__main__':
    try:
        slerper()
    except rospy.ROSInterruptException:
        pass
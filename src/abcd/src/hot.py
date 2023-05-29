#! /usr/bin/env python3

from std_srvs.srv import Empty, EmptyResponse
import rospy
import time

def hot_americano(req):
    rospy.loginfo("brewing coffee.")
    time.sleep(2)
    rospy.loginfo("adding water.")
    time.sleep(2)
    rospy.loginfo("Your hot americano is ready!")
    rospy.loginfo("=========================")
    return EmptyResponse()

def hot_cappuccino(req):
    rospy.loginfo("brewing coffee.")
    time.sleep(2)
    rospy.loginfo("adding milk.")
    time.sleep(2)
    rospy.loginfo("adding milk foam.")
    time.sleep(2)
    rospy.loginfo("Your hot cappuccino is ready!")
    rospy.loginfo("=========================")
    return EmptyResponse()

if __name__ == "__main__":
    rospy.init_node('service_hot_coffee_node')
    
    rospy.Service('hot_americano', Empty, hot_americano)
    rospy.Service('hot_cappuccino', Empty, hot_cappuccino)
    
    rospy.loginfo("Hot coffee node ready!")
    rospy.spin()
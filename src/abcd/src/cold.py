#! /usr/bin/env python3

from std_srvs.srv import Empty, EmptyResponse
import rospy
import time

def iced_caffe_latte(req):
    rospy.loginfo("brewing coffee.")
    time.sleep(2)
    rospy.loginfo("adding milk.")
    time.sleep(2)
    rospy.loginfo("adding ice.")
    time.sleep(2)
    rospy.loginfo("Your iced caffe latte is ready!")
    rospy.loginfo("=========================")
    return EmptyResponse()

def iced_americano(req):
    rospy.loginfo("brewing coffee.")
    time.sleep(2)
    rospy.loginfo("adding water.")
    time.sleep(2)
    rospy.loginfo("adding ice.")
    time.sleep(2)
    rospy.loginfo("Your iced americano is ready!")
    rospy.loginfo("=========================")
    return EmptyResponse()


if __name__ == "__main__":
    rospy.init_node('service_iced_coffee_node')
    
    rospy.Service('iced_caffe_latte', Empty, iced_caffe_latte)
    rospy.Service('iced_americano', Empty, iced_americano)
    
    rospy.loginfo("Iced coffee node ready!")
    rospy.spin()
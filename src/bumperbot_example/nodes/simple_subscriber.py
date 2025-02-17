#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

#create a callback
def callback(msg):
    #This function is called each time a new msg is published on the topic /chatter
    #The message that has been published in then passed as input to this function
    rospy.loginfo("New message received : %s",msg.data)
    
if __name__ == "__main__":
    #Inizialize a ros node 
    rospy.init_node("simple_publisher_py",anonymous=True)
    #Register a subscriber on the topic /chatter that will listen for string msg
    #when a new message is received, the callback function is triggered and starts its execution
    rospy.Subscriber("chatter",String,callback)
    #Keeps the node up and running
    rospy.spin()
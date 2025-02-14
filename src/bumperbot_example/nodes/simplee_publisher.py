#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


if __name__ == "__main__":
    #Inizialize a Ros node called talker
    rospy.init_node("simple_publisher_py",anonymous=True)
    
    #register a publiisher on the topic /chatter that will publish String messages
    pub = rospy.Publisher("chatter",String,queue_size=10)
    
    #register a publisher on the topic/chatter that will publish String messages
    rate = rospy.Rate(10) #rate is in Hertz
    counter = 0 
    
    #Keep going publishing messages until the ROS communication is alive
    while not rospy.is_shutdown():
        hello_msg = "Hello world from Python : %d" % counter
        pub.publish(hello_msg)
        #Wait the desired rate before publishing the next message
        rate.sleep()
        counter += 1
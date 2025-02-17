#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def plusMinus(n,arr):
   posCounter = 0 
   negCounter = 0 
   zeroCounter = 0 
   
   #Iterar sobre la lista
   for val in arr:
       if val > 0 :
           posCounter += 1
       elif val < 0 :
           negCounter += 1
       else:
           zeroCounter += 1
    #Evitar division por zero
   if n == 0:
       return 0,0,0
   
   #Retornar una tupla con los resultados
   resPos = posCounter / n
   resNeg = negCounter / n
   resZero = zeroCounter / n
   
   return resPos,resNeg,resZero
   
              
if __name__ == "__main__":
    #Inizialize a Ros node called talker
    rospy.init_node("simple_publisher_py",anonymous=True)
    
    #register a publiisher on the topic /chatter that will publish String messages
    pub = rospy.Publisher("chatter",String,queue_size=10)
    
    #register a publisher on the topic/chatter that will publish String messages
    rate = rospy.Rate(10) #rate is in Hertz
    counter = 0 
    
    #1. Create the list for the function
    numbers = [1,1,0,-1,-1]
    plusMinus(5,numbers)
    
    #Keep going publishing messages until the ROS communication is alive
    while not rospy.is_shutdown():
        hello_msg = "Hello world from Python : %d" % counter
        pub.publish(hello_msg)
        #Wait the desired rate before publishing the next message
        rate.sleep()
        counter += 1
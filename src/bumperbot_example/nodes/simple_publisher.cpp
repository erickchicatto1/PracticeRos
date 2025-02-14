#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sstream>


int main(int argc,char **argv){

    //Init a ros node called talker
    ros::init(argc,argv,"simple_publisher_cpp");
    ros::NodeHandle n; 

    //register a publisher on the topic /chatter that will publish string msg
    ros::Publisher pub = n.advertise<std_msgs::String>("chatter",10);

    //Define the frecuency for publishing the message
    ros::Rate rate(10);

    int counter = 0 ;

    //Keep going publishing mess until Ros communication is alive
    while(ros::ok()){

        std_msgs::String msg;
        std::stringstream ss;
        ss << "Hello world from C++"<<counter;
        msg.data = ss.str();
        pub.publish(msg);

        ros::spinOnce();
        // wait the desired rate before publishing the next message
        rate.sleep();
        ++counter;

    }

    return 0;
}

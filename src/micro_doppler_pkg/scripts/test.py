#!/usr/bin/env python

import rospy
from ti_mmwave_rospkg.msg import RadarScan

class MySimpleClass(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/ti_mmwave/radar_scan',RadarScan,self.sub_callback)
        self.radardata = RadarScan()

    def sub_callback(self,msg):
        self.radardata = msg
        print('hehe')
        rospy.loginfo('hello')
        #print("hello")

if __name__ =="__main__":
    rospy.init_node('hello')
    my_simple_class = MySimpleClass()
    rospy.spin()
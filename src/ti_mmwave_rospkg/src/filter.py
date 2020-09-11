#!/usr/bin/env python
import rospy
import math
import sys

from sensor_msgs.msg import PointCloud2
import std_msgs.msg
import sensor_msgs.point_cloud2 as pcl2

from ti_mmwave_rospkg.msg import RadarScan

class MySimpleClass(object):
    def __init__(self):
        self.pcl0_pub = rospy.Publisher("/my_pcl0_topic", PointCloud2,queue_size = 1)
        self.pcl1_pub = rospy.Publisher("/my_pcl1_topic", PointCloud2,queue_size = 1)
        self.sub = rospy.Subscriber('/ti_mmwave/radar_scan',RadarScan,self.sub_callback)
        #current frame data
        self.radar_0_data = []
        self.radar_0_intensity = [] 
        self.radar_1_data = []
        self.radar_1_intensity = [] 
        #elf.now_framenum = 0
        #self.cloud_points = []

    def sub_callback(self,msg):
        #header
        header = std_msgs.msg.Header()
        header.stamp = rospy.Time.now()
        #print(msg.header.frame_id)
        if msg.header.frame_id == '/ti_mmwave_0':
            if msg.point_id == 0:
                if len(self.radar_0_data) > 0:

                    #calculate intensity(filter)
                    normalized_intensity = []
                    #normalized_intensity = self.radar_0_intensity/max(self.radar_0_intensity)
                    #print(max(self.radar_0_intensity))
                    normalized_intensity = [x / max(self.radar_0_intensity) for x in self.radar_0_intensity]
                    xyz =[]
                    for i in range(len(normalized_intensity)):
                        xyz.append([self.radar_0_data[i][0],self.radar_0_data[i][1],self.radar_0_data[i][2]])

                    #create message
                    header.frame_id = 'pcl_0'
                    msg = pcl2.create_cloud_xyz32(header, xyz)
                    #print("pub")
                    
                    #publish
                    self.pcl0_pub.publish(msg)

                    #clean
                    self.radar_0_data =[]
                    self.radar_0_intensity = [] 
                else:
                    self.radar_0_data.append([msg.x, msg.y, msg.z])
                    self.radar_0_intensity.append(msg.intensity)
            else:
                self.radar_0_data.append([msg.x, msg.y, msg.z])
                self.radar_0_intensity.append(msg.intensity)
        else:    
            if msg.point_id == 0:
                if len(self.radar_1_data) > 0:

                    #calculate intensity(filter)
                    normalized_intensity = []
                    #print(max(self.radar_1_intensity))
                    #normalized_intensity = self.radar_1_intensity/max(self.radar_1_intensity)
                    normalized_intensity = [x / max(self.radar_1_intensity) for x in self.radar_1_intensity]
                    xyz =[]
                    for i in range(len(normalized_intensity)):
                        xyz.append([self.radar_1_data[i][0],self.radar_1_data[i][1],self.radar_1_data[i][2]])

                    #create message
                    header.frame_id = 'pcl_1'
                    msg = pcl2.create_cloud_xyz32(header, xyz)

                    #publish
                    self.pcl1_pub.publish(msg)

                    #clean
                    self.radar_1_data =[]
                    self.radar_1_intensity = [] 
                else:
                    self.radar_1_data.append([msg.x, msg.y, msg.z])
                    self.radar_1_intensity.append(msg.intensity)
            else:
                self.radar_1_data.append([msg.x, msg.y, msg.z])
                self.radar_1_intensity.append(msg.intensity)
        
        

if __name__ == '__main__':
    '''
    Sample code to publish a pcl2 with python
    '''
    rospy.init_node('pcl2_pub_example')
    rospy.loginfo("Initializing sample pcl2 publisher node...")
    #give time to roscore to make the connections
    #rospy.sleep(1.)
    my_simple_class = MySimpleClass()
    rospy.loginfo("happily publishing sample pointcloud.. !")
    rospy.spin()

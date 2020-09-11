#!/usr/bin/env python

import rospy
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
from ti_mmwave_rospkg.msg import RadarScan

class MySimpleClass(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/ti_mmwave/radar_scan',RadarScan,self.sub_callback)
        self.tmp_x = []
        self.tmp_y = []
        self.showflag = 0
        #self.fig, ax = plt.subplots()
        #self.sc = ax.scatter(self.tmp_x,self.tmp_y)


    def sub_callback(self,msg):
        if msg.point_id ==0:
            '''if not self.showflag:
                self.showflag = 1
                plt.show() '''
            #plt.scatter(self.tmp_x,self.tmp_y)
            
            
            #self.sc.set_offsets(np.c_[self.tmp_x,self.tmp_y])
            #self.fig.canvas.draw_idle()
            #plt.pause(0.1)
            self.tmp_x=[]
            self.tmp_y=[]
        self.tmp_x.append(msg.x)
        self.tmp_y.append(msg.y)

def animate(i):
    sc.set_offsets(np.c_[my_simple_class.tmp_x,my_simple_class.tmp_y])

if __name__ =="__main__":
    rospy.init_node('hello')
    my_simple_class = MySimpleClass()
    #plt.show()
    fig, ax = plt.subplots()
    x, y = [],[]
    sc = ax.scatter(x,y)
    plt.xlim(0,10)
    plt.ylim(-10,10)
    ani = matplotlib.animation.FuncAnimation(fig, animate, 
                frames=30, interval=100, repeat=True) 
    plt.show()
    rospy.spin()
   
    
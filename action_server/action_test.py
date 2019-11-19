#!/usr/bin/env python
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------
#Title: ActionServerNodeのデバッグ用ROSノード
#Author: Issei Iida
#Date: 2019/10/11
#Memo:
#---------------------------------------------------------------------

#Python関係ライブラリ
import sys
import time
#ROS関係ライブラリ
import rospy
import roslib

sys.path.insert(0, '/home/athome/catkin_ws/src/mimi_common_pkg/scripts/')
from common_action_client import *
from common_function import *

kc = KobukiControl()
def main():
    rospy.loginfo('Test ActionServer')
    #approachPersonAC()
    #findPersonAC()
<<<<<<< HEAD
    enterTheRoomAC(0.88)
=======
    kc.moveDistance(1.0)
>>>>>>> cfd9871b613afc58c277e948b63c395e7891988b
    rospy.loginfo('Finish test')

if __name__ == '__main__':
    try:
        rospy.init_node('action_test', anonymous = True)
        main()
    except rospy.ROSInterruptException:
        pass

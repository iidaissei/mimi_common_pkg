#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
#Title: 使用頻度が高い機能を纏めたPythonスクリプト
#Author: Issei Iida
#Date: 2019/09/07
#Memo: mimiの上(頭)から下(台車)の順に記述
#--------------------------------------------------------------------

#Python関係
import time
from yaml import load
#ROS関係
import rospy
import rosparam
import actionlib
from std_srvs.srv import Empty
from std_msgs.msg import String, Float64
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

#Grobal Publisher
pub_speak = rospy.Publisher('/tts', String, queue_size = 1)
pub_cmd_vel_mux = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size = 1)
pub_m6 = rospy.Publisher('/m6_controller/command', Float64, queue_size = 1)

#話す *発話エンジンはpicottsで設定する
def speak(phrase):
    print phrase
    pub_speak.publish(phrase)
    rospy.sleep(2.0)

#m6(首のサーボモータ)の制御
def m6Control(value):
    #念のため型変換
    data = Float64()
    data = value
    rospy.sleep(0.1)
    pub_m6.publish(data)
    rospy.loginfo("Changing m6 pose")

#kobukiの前進・後進
def linearControl(value):
    twist_cmd = Twist()
    twist_cmd.linear.x = value
    rospy.sleep(0.1)
    pub_cmd_vel_mux.publish(twist_cmd)

#kobukiの回転
def angularControl(value):
    twist_cmd = Twist()
    twist_cmd.angular.z = value
    rospy.sleep(0.1)
    pub_cmd_vel_mux.publish(twist_cmd)


#文字列をパラメータの/location_listから検索して位置座標を生成
def searchLocationName(target_name):
    rospy.loginfo("Search LocationName")
    #LocationListのyamlファイルを読み込む
    f = open('/home/issei/catkin_ws/src/mimi_common_pkg/config/common_function_params.yaml')
    file_data = load(f)
    f.close()
    print file_data
    #検索開始
    for i in range(len(file_data)):
        if target_name in file_data[i][0]:
            coordinate_list = []
            coordinate_list.append(file_data[i][1])
            coordinate_list.append(file_data[i][2])
            coordinate_list.append(file_data[i][3])
            coordinate_list.append(file_data[i][4])
            rospy.loginfo("Created LocationData")
            return coordinate_list
        elif i == len(file_data):
            rospy.loginfo("Not found <" + target_name + "> in LocationDict")
            return 'faild'

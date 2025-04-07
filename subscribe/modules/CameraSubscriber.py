import numpy as np
import rospy
import ros_numpy
from sensor_msgs.msg import Image
from std_msgs.msg import Int32, Int32MultiArray, Bool
import angle_interface as ai



class CameraSubscriber(object):
    def __init__(self):
        rospy.Subscriber("/camera/image_resize", Image, self.callback)

    def callback(self, data: Image):
        '''
        return image property:
            - shape              : (width, height, channel)
            - color channel order: (B,G,R)  (bgr8)
            - value range        : [0, 255] (uint8)
        '''
        self.data = ros_numpy.numpify(data)

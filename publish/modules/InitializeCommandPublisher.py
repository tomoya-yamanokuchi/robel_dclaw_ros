import rospy
import numpy as np
from std_msgs.msg import Int32MultiArray
from ...utils import ParameterObject


class InitializeCommandPublisher:
    def __init__(self, params: ParameterObject):
        # ------
        self.TOPIC_NAME : str = "/dclaw/initialize_ctrl/command"
        self.sleep_time_sec   = params.sleep_time_sec
        self.queue_size       = params.queue_size
        # -------
        self._msg = Int32MultiArray()
        self._pub = rospy.Publisher(
            name       = self.TOPIC_NAME,
            data_class = Int32MultiArray,
            queue_size = self.queue_size,
        )
        # -------
        self._num_joint_ctrl     = 9
        self._num_valve_position = 1
        self._num_command = (self._num_joint_ctrl + self._num_valve_position)


    def publish(self, initialize_command: np.ndarray):
        assert initialize_command.shape == (self._num_command,)
        # ---
        self._msg.data = tuple(initialize_command)
        self._pub.publish(self._msg)
        rospy.sleep(self.sleep_time_sec)



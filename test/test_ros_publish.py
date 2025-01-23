import numpy as np
from .. import ROSHandler
from ..utils import ParameterObject
from ..utils import get_initial_positions
from dynamixel_ros_service import Control


def run_tests():
    params = ParameterObject()
    params.sleep_time_sec = 0.2
    # ---
    ros_handler = ROSHandler(params)
    # ----
    ctrl = Control.from_resvec(resvec=get_initial_positions())
    ros_handler.publisher.publish_initialize_ctrl(ctrl)
    ros_handler.wait_initialization()
    # ----
    resvec = get_initial_positions()
    for i in range(20):
        ctrl = Control.from_resvec(resvec=resvec)
        ros_handler.publisher.publish_joint_ctrl(ctrl=ctrl)
        resvec += 10


if __name__ == "__main__":
    run_tests()

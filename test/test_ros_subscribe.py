import numpy as np
from .. import ROSHandler
from ..utils import ParameterObject
from ..utils import get_initial_positions
from dynamixel_ros_service import Orientation


def run_tests():
    params      = ParameterObject()
    ros_handler = ROSHandler(params)

    # ----
    ctrl = Orientation.from_resvec(resvec=get_initial_positions())
    ros_handler.publisher.publish_initialize_ctrl(ctrl)
    ros_handler.wait_initialization()

    # ----
    print("----------------------------------------------------------------------------")
    print(" is_initialize_finished = ", ros_handler.subscriber.initialization_state.data)
    print("        joint_positions = ", ros_handler.subscriber.joint_positions.data)
    print("       joint_velocities = ", ros_handler.subscriber.joint_velocities.data)
    print("         joint_currents = ", ros_handler.subscriber.joint_currents.data)
    print("           valve_moving = ", ros_handler.subscriber.valve_moving.data)
    print("         valve_position = ", ros_handler.subscriber.valve_position.data)
    print("----------------------------------------------------------------------------")
    print("        joint_positions = ", ros_handler.subscriber.get_joint_positions())
    print("         valve_position = ", ros_handler.subscriber.get_valve_position())
    print("----------------------------------------------------------------------------")


if __name__ == "__main__":
    run_tests()

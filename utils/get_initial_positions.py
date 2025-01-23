import numpy as np


def get_initial_positions():
    qpos_resolution = np.array(
        [2219, 1766, 2048,
         2083, 2094, 2048,
         2219, 1766, 2048], dtype=int
    )
    return qpos_resolution

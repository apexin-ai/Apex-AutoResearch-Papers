"""
Project 3D semantic occupancy to BEV (Bird's Eye View) 2D maps.
"""

import numpy as np


def voxel_to_bev(semantic_3d, binary_3d):
    """Project 3D voxel grid to 2D BEV along z-axis.

    The z-axis (axis=2) is the vertical/height axis.

    BEV binary: any z-layer has occupancy -> BEV cell is 1
    BEV semantic: highest priority class along z (max class ID wins)
        Priority order: target(3) > robot(2) > table(1) > free(0)

    Args:
        semantic_3d: (R, R, R) uint8
        binary_3d: (R, R, R) bool

    Returns:
        bev_semantic: (R, R) uint8
        bev_binary: (R, R) bool
    """
    bev_binary = binary_3d.any(axis=2)
    bev_semantic = semantic_3d.max(axis=2)
    return bev_semantic, bev_binary

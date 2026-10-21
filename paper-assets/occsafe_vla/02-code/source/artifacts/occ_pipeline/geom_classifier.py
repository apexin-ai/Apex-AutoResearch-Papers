"""
Classify MuJoCo geoms into semantic categories for occupancy labeling.

Categories:
  0 = free (background)
  1 = table
  2 = robot
  3 = target object
"""

import re

FREE = 0
TABLE = 1
ROBOT = 2
TARGET = 3

CATEGORY_NAMES = {FREE: "free", TABLE: "table", ROBOT: "robot", TARGET: "target"}

# Patterns matched against geom names (case-insensitive)
ROBOT_PATTERNS = [
    r"robot\d*",
    r"gripper",
    r"finger",
    r"link\d*",
    r"hand",
    r"panda",
    r"mount",
]

TABLE_PATTERNS = [
    r"table",
    r"wooden_cabinet",
    r"flat_stove",
    r"cabinet",
    r"stove",
    r"microwave",
    r"fridge",
]

SKIP_PATTERNS = [
    r"wall",
    r"floor",
    r"ground",
    r"arena",
]


def classify_geom(geom_name, body_name, geom_type):
    if geom_name is None:
        geom_name = ""
    if body_name is None:
        body_name = ""

    gn = geom_name.lower()
    bn = body_name.lower()

    if geom_type == 0:
        return None

    # Skip visual-only geoms (collision geoms cover the physical shape)
    if gn.endswith("_vis") or gn.endswith("_visual"):
        return None

    for pat in SKIP_PATTERNS:
        if re.search(pat, gn) or re.search(pat, bn):
            return None

    if bn == "world":
        return None

    for pat in ROBOT_PATTERNS:
        if re.search(pat, gn) or re.search(pat, bn):
            return ROBOT

    for pat in TABLE_PATTERNS:
        if re.search(pat, gn) or re.search(pat, bn):
            return TABLE

    return TARGET


def build_geom_class_map(sim):
    """Build geom_id -> semantic_class mapping for all geoms in the model.

    Args:
        sim: robosuite MjSim instance

    Returns:
        dict[int, int]: geom_id -> semantic category (0-3)
        Geoms that should be skipped are not included.
    """
    model = sim.model
    geom_map = {}

    for i in range(model.ngeom):
        geom_name = model.geom_id2name(i)
        body_id = model.geom_bodyid[i]
        body_name = model.body_id2name(body_id)
        geom_type = model.geom_type[i]

        cat = classify_geom(geom_name, body_name, geom_type)
        if cat is not None:
            geom_map[i] = cat

    return geom_map


def print_geom_classification(sim, geom_map):
    """Debug helper: print all geom classifications."""
    model = sim.model
    data = sim.data

    type_names = {
        0: "PLANE", 1: "HFIELD", 2: "SPHERE", 3: "CAPSULE",
        4: "ELLIPSOID", 5: "CYLINDER", 6: "BOX", 7: "MESH",
    }

    for i in range(model.ngeom):
        geom_name = model.geom_id2name(i) or f"unnamed_{i}"
        body_id = model.geom_bodyid[i]
        body_name = model.body_id2name(body_id) or f"body_{body_id}"
        geom_type = model.geom_type[i]
        pos = data.geom_xpos[i]
        cat = geom_map.get(i, None)
        cat_str = CATEGORY_NAMES.get(cat, "SKIP") if cat is not None else "SKIP"
        tname = type_names.get(geom_type, f"UNK({geom_type})")

        print(
            f"g[{i:3d}] {geom_name:45s} body={body_name:35s} "
            f"type={tname:8s} cat={cat_str:8s} "
            f"pos=[{pos[0]:.3f},{pos[1]:.3f},{pos[2]:.3f}]"
        )

"""Standalone text observation wrapper for Crafter (adapted from BALROG)."""
import itertools
from collections import defaultdict

import crafter
import numpy as np

ACTIONS = [
    "Noop", "Move West", "Move East", "Move North", "Move South",
    "Do", "Sleep", "Place Stone", "Place Table", "Place Furnace",
    "Place Plant", "Make Wood Pickaxe", "Make Stone Pickaxe",
    "Make Iron Pickaxe", "Make Wood Sword", "Make Stone Sword",
    "Make Iron Sword",
]

ACTION_NAME_TO_IDX = {a.lower().replace(" ", "_"): i for i, a in enumerate(ACTIONS)}
ACTION_NAME_TO_IDX.update({a: i for i, a in enumerate(ACTIONS)})

VITALS = ["health", "food", "drink", "energy"]

# Build id_to_item mapping at module load
_dummy = crafter.Env()
ID_TO_ITEM = ["None"] * 19
for name, ind in itertools.chain(
    _dummy._world._mat_ids.items(), _dummy._sem_view._obj_ids.items()
):
    n = str(name)
    if "objects." in n:
        n = n[n.find("objects.") + len("objects."):-2].lower()
    ID_TO_ITEM[ind] = n
PLAYER_IDX = ID_TO_ITEM.index("player")
del _dummy

MONSTER_IDS = {ID_TO_ITEM.index("zombie"), ID_TO_ITEM.index("skeleton")}
WATER_ID = ID_TO_ITEM.index("water")
TREE_ID = ID_TO_ITEM.index("tree")
COW_ID = ID_TO_ITEM.index("cow")
LAVA_ID = ID_TO_ITEM.index("lava")
STONE_ID = ID_TO_ITEM.index("stone")
PLANT_ID = ID_TO_ITEM.index("plant")


def _dir_str(dx, dy):
    parts = []
    if dy < 0:
        parts.append("north")
    elif dy > 0:
        parts.append("south")
    if dx < 0:
        parts.append("west")
    elif dx > 0:
        parts.append("east")
    dist = abs(dx) + abs(dy)
    return f"{dist} step{'s' if dist > 1 else ''} to your {'-'.join(parts)}" if parts else "at your location"


def describe_env(info, view_radius=4):
    px, py = info["player_pos"]
    semantic = info["semantic"]
    facing = info["player_facing"]

    fx = px + facing[0]
    fy = py + facing[1]
    h, w = semantic.shape
    if 0 <= fx < h and 0 <= fy < w:
        face_item = ID_TO_ITEM[semantic[fx, fy]]
    else:
        face_item = "nothing"
    face_str = f"You face {face_item} at your front."

    closest = {}
    for x in range(max(0, px - view_radius), min(h, px + view_radius + 1)):
        for y in range(max(0, py - view_radius), min(w, py + view_radius + 1)):
            idx = semantic[x, y]
            if idx == PLAYER_IDX or ID_TO_ITEM[idx] in ("grass", "sand", "path", "None"):
                continue
            name = ID_TO_ITEM[idx]
            dist = abs(x - px) + abs(y - py)
            if name not in closest or dist < closest[name][0]:
                closest[name] = (dist, x - px, y - py)

    if closest:
        lines = [f"- {name} {_dir_str(dx, dy)}" for name, (d, dx, dy) in sorted(closest.items(), key=lambda x: x[1][0])]
        see_str = "You see:\n" + "\n".join(lines)
    else:
        see_str = "You see nothing nearby."

    return see_str + "\n\n" + face_str


def describe_inventory(info):
    inv = info["inventory"]
    status = "Your status:\n" + "\n".join(f"- {v}: {inv[v]}/9" for v in VITALS)
    items = "\n".join(f"- {k}: {v}" for k, v in inv.items() if k not in VITALS and v > 0)
    inv_str = f"Your inventory:\n{items}" if items else "You have nothing in your inventory."
    return status + "\n\n" + inv_str


def describe_frame(info):
    status = ""
    if info.get("dead"):
        status = "You died.\n\n"
    elif info.get("sleeping"):
        status = "You are sleeping.\n\n"
    env_desc = describe_env(info)
    inv_desc = describe_inventory(info)
    return (status + env_desc).strip(), inv_desc.strip()


class CrafterTextWrapper:
    """Wraps crafter.Env to produce text observations."""

    def __init__(self, seed=None):
        kwargs = {"seed": seed} if seed is not None else {}
        self.env = crafter.Env(**kwargs)
        self.steps = 0

    def reset(self):
        self.env.reset()
        obs, reward, done, info = self.env.step(0)  # noop to get info
        self.steps = 1
        aug = self._augment_info(info)
        text_obs = self._make_text(aug)
        return text_obs, aug

    def step(self, action):
        if isinstance(action, str):
            action = self._parse_action(action)
        obs, reward, done, info = self.env.step(action)
        self.steps += 1
        aug = self._augment_info(info)
        text_obs = self._make_text(aug)
        return text_obs, reward, done, aug

    def _augment_info(self, info):
        aug = info.copy()
        aug["sleeping"] = self.env._player.sleeping
        aug["player_facing"] = self.env._player.facing
        aug["dead"] = self.env._player.health <= 0
        aug["view"] = self.env._view
        return aug

    def _make_text(self, info):
        env_desc, inv_desc = describe_frame(info)
        return env_desc + "\n\n" + inv_desc

    def _parse_action(self, action_str):
        s = action_str.strip().lower().replace(" ", "_")
        if s in ACTION_NAME_TO_IDX:
            return ACTION_NAME_TO_IDX[s]
        for name, idx in ACTION_NAME_TO_IDX.items():
            if s in name or name in s:
                return idx
        return 0  # noop fallback

    @property
    def action_space(self):
        return self.env.action_space

    @property
    def action_names(self):
        return ACTIONS

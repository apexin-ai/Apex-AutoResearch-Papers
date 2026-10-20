"""Deterministic heuristic agent for Crafter with ground-truth state access."""
import numpy as np
from crafter_text_wrapper import (
    MONSTER_IDS, WATER_ID, TREE_ID, COW_ID, LAVA_ID, STONE_ID, PLANT_ID,
    PLAYER_IDX, ID_TO_ITEM,
)

# action indices
NOOP, MOVE_W, MOVE_E, MOVE_N, MOVE_S = 0, 1, 2, 3, 4
DO, SLEEP = 5, 6
PLACE_STONE, PLACE_TABLE, PLACE_FURNACE, PLACE_PLANT = 7, 8, 9, 10
MAKE_WOOD_PICK, MAKE_STONE_PICK, MAKE_IRON_PICK = 11, 12, 13
MAKE_WOOD_SWORD, MAKE_STONE_SWORD, MAKE_IRON_SWORD = 14, 15, 16


def _find_nearest(semantic, player_pos, target_ids, max_radius=20):
    """Find nearest cell matching any target_id. Returns (dist, x, y) or None."""
    px, py = player_pos
    h, w = semantic.shape
    best = None
    for x in range(max(0, px - max_radius), min(h, px + max_radius + 1)):
        for y in range(max(0, py - max_radius), min(w, py + max_radius + 1)):
            if semantic[x, y] in target_ids:
                d = abs(x - px) + abs(y - py)
                if best is None or d < best[0]:
                    best = (d, x, y)
    return best


def _move_toward(px, py, tx, ty):
    """Return action to move from (px,py) toward (tx,ty)."""
    dx = tx - px
    dy = ty - py
    if abs(dx) >= abs(dy):
        return MOVE_E if dx > 0 else MOVE_W
    else:
        return MOVE_S if dy > 0 else MOVE_N


def _move_away_from(px, py, tx, ty):
    """Return action to move away from (tx,ty)."""
    dx = px - tx
    dy = py - ty
    if abs(dx) >= abs(dy):
        return MOVE_E if dx > 0 else MOVE_W
    else:
        return MOVE_S if dy > 0 else MOVE_N


def _is_adjacent(px, py, tx, ty):
    return abs(px - tx) + abs(py - ty) == 1


def _facing_target(facing, px, py, tx, ty):
    return px + facing[0] == tx and py + facing[1] == ty


def _face_action(px, py, tx, ty):
    """Return action that faces the target (move toward but we're adjacent)."""
    dx = tx - px
    dy = ty - py
    if dx == 1:
        return MOVE_E
    elif dx == -1:
        return MOVE_W
    elif dy == 1:
        return MOVE_S
    elif dy == -1:
        return MOVE_N
    return NOOP


def _nearby_monsters(semantic, px, py, radius=3):
    """Return list of (dist, x, y) for monsters within radius."""
    h, w = semantic.shape
    monsters = []
    for x in range(max(0, px - radius), min(h, px + radius + 1)):
        for y in range(max(0, py - radius), min(w, py + radius + 1)):
            if semantic[x, y] in MONSTER_IDS:
                d = abs(x - px) + abs(y - py)
                monsters.append((d, x, y))
    monsters.sort()
    return monsters


class CrafterDetAgent:
    """Survival-focused heuristic agent."""

    def __init__(self):
        self.explore_dir = 0
        self.explore_counter = 0
        self.has_placed_table = False

    def act(self, info):
        inv = info["inventory"]
        semantic = info["semantic"]
        px, py = info["player_pos"]
        facing = info.get("player_facing", (1, 0))
        health = inv["health"]
        food = inv["food"]
        drink = inv["drink"]
        energy = inv["energy"]
        wood = inv.get("wood", 0)
        stone_inv = inv.get("stone", 0)

        # P0: Flee from nearby monsters
        monsters = _nearby_monsters(semantic, px, py, radius=3)
        if monsters:
            closest = monsters[0]
            if closest[0] <= 2:
                has_sword = inv.get("wood_sword", 0) + inv.get("stone_sword", 0) + inv.get("iron_sword", 0)
                if has_sword and closest[0] == 1:
                    if _facing_target(facing, px, py, closest[1], closest[2]):
                        return DO
                    else:
                        return _face_action(px, py, closest[1], closest[2])
                return _move_away_from(px, py, closest[1], closest[2])

        # P1: Sleep if very low energy
        if energy <= 2:
            return SLEEP

        # P2: Drink if thirsty
        if drink <= 3:
            water = _find_nearest(semantic, (px, py), {WATER_ID})
            if water:
                _, wx, wy = water
                if _is_adjacent(px, py, wx, wy):
                    if _facing_target(facing, px, py, wx, wy):
                        return DO
                    else:
                        return _face_action(px, py, wx, wy)
                return _move_toward(px, py, wx, wy)

        # P3: Eat if hungry - find cow or plant
        if food <= 3:
            food_target = _find_nearest(semantic, (px, py), {COW_ID, PLANT_ID})
            if food_target:
                _, fx, fy = food_target
                if _is_adjacent(px, py, fx, fy):
                    if _facing_target(facing, px, py, fx, fy):
                        return DO
                    else:
                        return _face_action(px, py, fx, fy)
                return _move_toward(px, py, fx, fy)

        # P4: Plant sapling if have sapling and food < 6
        if food <= 5 and inv.get("sapling", 0) > 0:
            return PLACE_PLANT

        # P5: Gather wood if low
        if wood < 3:
            tree = _find_nearest(semantic, (px, py), {TREE_ID})
            if tree:
                _, tx, ty = tree
                if _is_adjacent(px, py, tx, ty):
                    if _facing_target(facing, px, py, tx, ty):
                        return DO
                    else:
                        return _face_action(px, py, tx, ty)
                return _move_toward(px, py, tx, ty)

        # P6: Place table if have wood and no table nearby
        table_id = ID_TO_ITEM.index("table")
        table_nearby = _find_nearest(semantic, (px, py), {table_id}, max_radius=5)
        if wood >= 2 and not table_nearby:
            return PLACE_TABLE

        # P7: Craft wood pickaxe if near table and have wood
        if table_nearby and inv.get("wood_pickaxe", 0) == 0 and wood >= 1:
            _, tx, ty = table_nearby
            if _is_adjacent(px, py, tx, ty):
                return MAKE_WOOD_PICK
            return _move_toward(px, py, tx, ty)

        # P8: Craft wood sword if near table and have wood
        if table_nearby and inv.get("wood_sword", 0) == 0 and wood >= 1:
            _, tx, ty = table_nearby
            if _is_adjacent(px, py, tx, ty):
                return MAKE_WOOD_SWORD
            return _move_toward(px, py, tx, ty)

        # P9: Gather stone if have pickaxe
        if inv.get("wood_pickaxe", 0) > 0 and stone_inv < 2:
            stone = _find_nearest(semantic, (px, py), {STONE_ID})
            if stone:
                _, sx, sy = stone
                if _is_adjacent(px, py, sx, sy):
                    if _facing_target(facing, px, py, sx, sy):
                        return DO
                    else:
                        return _face_action(px, py, sx, sy)
                return _move_toward(px, py, sx, sy)

        # P10: Explore
        explore_actions = [MOVE_N, MOVE_E, MOVE_S, MOVE_W]
        self.explore_counter += 1
        if self.explore_counter > 10:
            self.explore_counter = 0
            self.explore_dir = (self.explore_dir + 1) % 4
        return explore_actions[self.explore_dir]

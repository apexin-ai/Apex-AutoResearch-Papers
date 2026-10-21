#!/usr/bin/env python3
"""
MiniHack Deterministic Heuristic Agent
BFS shortest-path + survival heuristics for counterfactual baseline.

Strategy: parse glyph grid -> BFS to staircase -> survival overrides.
Serves as "always-deterministic" condition in episode-level counterfactual analysis.
"""

import numpy as np
from collections import deque
from typing import Dict, List, Optional, Set, Tuple

try:
    import nle.nethack as nethack
except ImportError:
    try:
        import nethack
    except ImportError:
        nethack = None

try:
    import gymnasium as gym
except ImportError:
    import gym

# ---------- blstats indices (NLE) ----------
BL_X = 0
BL_Y = 1
BL_HP = 10
BL_HPMAX = 11
BL_DEPTH = 12
BL_GOLD = 13
BL_AC = 16
BL_TIME = 19
BL_HUNGER = 21
BL_CONDITION = 24

# Hunger state thresholds
HUNGER_NOT_HUNGRY = 0
HUNGER_HUNGRY = 1
HUNGER_WEAK = 2
HUNGER_FAINTING = 3

# Direction deltas: (dy, dx) — row increases downward, col increases rightward
DIRECTION_DELTAS = {
    "N":  (-1,  0),
    "E":  ( 0,  1),
    "S":  ( 1,  0),
    "W":  ( 0, -1),
    "NE": (-1,  1),
    "NW": (-1, -1),
    "SE": ( 1,  1),
    "SW": ( 1, -1),
}
DELTA_TO_DIR = {v: k for k, v in DIRECTION_DELTAS.items()}

# Tile description keywords for walkable/goal detection
_WALKABLE_KEYWORDS = (
    "floor", "doorway", "open door", "corridor",
    "altar", "fountain", "sink", "throne",
    "grave", "ice", "air", "cloud",
    "staircase", "stairway", "ladder",
)
_WALL_KEYWORDS = ("wall", "rock", "stone", "tree", "bars")


# ------------------------------------------------------------------ #
#  Action mapper — translates direction/command names to env indices  #
# ------------------------------------------------------------------ #

def _extract_actions(env):
    """Try various ways to get the NLE action tuple from a (possibly wrapped) env."""
    if hasattr(env, "actions"):
        return env.actions
    if hasattr(env, "unwrapped"):
        uw = env.unwrapped
        for attr in ("actions", "_actions"):
            if hasattr(uw, attr):
                return getattr(uw, attr)
    e = env
    while hasattr(e, "env"):
        e = e.env
        if hasattr(e, "actions"):
            return e.actions
    return None


class ActionMapper:
    """Maps compass direction names and command names to env action indices."""

    _COMPASS_NAMES = ("N", "E", "S", "W", "NE", "NW", "SE", "SW")
    _COMMAND_NAMES = (
        "EAT", "PICKUP", "SEARCH", "KICK", "OPEN",
        "APPLY", "DESCEND", "WAIT", "PRAY",
    )

    def __init__(self, env):
        self.dir_to_idx: Dict[str, int] = {}
        self.cmd_to_idx: Dict[str, int] = {}
        self.n_actions = env.action_space.n if hasattr(env.action_space, "n") else 0
        self._build(env)

    def _build(self, env):
        actions = _extract_actions(env)
        if actions is None or nethack is None:
            self._fallback_mapping()
            return

        compass_ref = {}
        for name in self._COMPASS_NAMES:
            val = getattr(nethack.CompassDirection, name, None)
            if val is not None:
                compass_ref[name] = int(val)

        cmd_ref = {}
        for name in self._COMMAND_NAMES:
            val = getattr(nethack.Command, name, None)
            if val is not None:
                cmd_ref[name] = int(val)

        for idx, action in enumerate(actions):
            a = int(action)
            for name, val in compass_ref.items():
                if a == val:
                    self.dir_to_idx[name] = idx
            for name, val in cmd_ref.items():
                if a == val:
                    self.cmd_to_idx[name] = idx

    def _fallback_mapping(self):
        """Assume standard 8-direction layout when NLE introspection unavailable."""
        for i, name in enumerate(self._COMPASS_NAMES):
            if i < self.n_actions:
                self.dir_to_idx[name] = i

    def direction(self, name: str) -> Optional[int]:
        return self.dir_to_idx.get(name)

    def command(self, name: str) -> Optional[int]:
        return self.cmd_to_idx.get(name)

    def delta_to_action(self, dy: int, dx: int) -> Optional[int]:
        """Convert (dy, dx) movement delta to action index."""
        sy = (1 if dy > 0 else -1) if dy != 0 else 0
        sx = (1 if dx > 0 else -1) if dx != 0 else 0
        name = DELTA_TO_DIR.get((sy, sx))
        return self.dir_to_idx.get(name) if name else None


# ------------------------------------------------------------------ #
#  Map parser                                                         #
# ------------------------------------------------------------------ #

def _decode_screen_desc(raw) -> str:
    """Decode a single cell from screen_descriptions to a lowercase string."""
    if isinstance(raw, np.ndarray):
        return raw.tobytes().decode("latin-1").strip("\x00").strip().lower()
    return str(raw).strip().lower()


def _is_monster_glyph(glyph: int) -> bool:
    """Check if glyph represents a monster (including pets) using NLE constants."""
    if nethack is None:
        return False
    try:
        mon_off = int(nethack.GLYPH_MON_OFF)
        pet_off = int(nethack.GLYPH_PET_OFF)
        invis_off = int(nethack.GLYPH_INVIS_OFF)
        return (mon_off <= glyph < pet_off) or (pet_off <= glyph < invis_off)
    except AttributeError:
        return False


def _is_object_glyph(glyph: int) -> bool:
    if nethack is None:
        return False
    try:
        return int(nethack.GLYPH_OBJ_OFF) <= glyph < int(nethack.GLYPH_CMAP_OFF)
    except AttributeError:
        return False


def parse_map(obs: Dict) -> Dict:
    """Extract structured map info from a MiniHack observation dict."""
    glyphs = obs["glyphs"]
    blstats = obs["blstats"]
    screen_desc = obs.get("screen_descriptions")

    agent_col, agent_row = int(blstats[BL_X]), int(blstats[BL_Y])
    agent_pos = (agent_row, agent_col)

    hp = int(blstats[BL_HP])
    max_hp = int(blstats[BL_HPMAX])
    hunger = int(blstats[BL_HUNGER])
    game_time = int(blstats[BL_TIME])

    rows, cols = glyphs.shape
    walkable: Set[Tuple[int, int]] = set()
    monsters: Set[Tuple[int, int]] = set()
    items: Set[Tuple[int, int]] = set()
    goal: Optional[Tuple[int, int]] = None

    for r in range(rows):
        for c in range(cols):
            g = int(glyphs[r, c])
            if g == 0:
                continue

            tile = ""
            if screen_desc is not None:
                tile = _decode_screen_desc(screen_desc[r, c])

            is_walkable = False

            if tile:
                if "staircase down" in tile or "stairway down" in tile:
                    goal = (r, c)
                    is_walkable = True
                elif any(kw in tile for kw in _WALKABLE_KEYWORDS):
                    is_walkable = True
                elif any(kw in tile for kw in _WALL_KEYWORDS):
                    is_walkable = False
                elif tile and tile != "dark area":
                    is_walkable = True

            if _is_monster_glyph(g) and (r, c) != agent_pos:
                monsters.add((r, c))
                is_walkable = True

            if _is_object_glyph(g):
                items.add((r, c))
                is_walkable = True

            if is_walkable:
                walkable.add((r, c))

    walkable.add(agent_pos)

    return {
        "agent_pos": agent_pos,
        "goal": goal,
        "walkable": walkable,
        "monsters": monsters,
        "items": items,
        "hp": hp,
        "max_hp": max_hp,
        "hunger": hunger,
        "game_time": game_time,
    }


# ------------------------------------------------------------------ #
#  BFS pathfinding                                                    #
# ------------------------------------------------------------------ #

def bfs_path(
    start: Tuple[int, int],
    goal: Tuple[int, int],
    walkable: Set[Tuple[int, int]],
    avoid: Optional[Set[Tuple[int, int]]] = None,
) -> List[Tuple[int, int]]:
    """BFS shortest path. Returns positions from start (exclusive) to goal (inclusive)."""
    if start == goal:
        return [goal]
    avoid = avoid or set()
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (r, c), path = queue.popleft()
        for dr, dc in DIRECTION_DELTAS.values():
            nr, nc = r + dr, c + dc
            npos = (nr, nc)
            if npos in visited or npos not in walkable:
                continue
            if npos in avoid and npos != goal:
                continue
            visited.add(npos)
            new_path = path + [npos]
            if npos == goal:
                return new_path[1:]
            queue.append((npos, new_path))
    return []


# ------------------------------------------------------------------ #
#  Agent                                                              #
# ------------------------------------------------------------------ #

class DeterministicHeuristicAgent:
    """BFS pathfinder with survival heuristics for MiniHack navigation tasks."""

    def __init__(self, env):
        self.mapper = ActionMapper(env)
        self.explored: Set[Tuple[int, int]] = set()
        self.last_pos: Optional[Tuple[int, int]] = None
        self.stuck_count = 0
        self.step_count = 0

    def reset(self):
        self.explored.clear()
        self.last_pos = None
        self.stuck_count = 0
        self.step_count = 0

    # ---------- survival ----------

    def _adjacent_monsters(
        self, pos: Tuple[int, int], monsters: Set[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        adj = []
        r, c = pos
        for dr, dc in DIRECTION_DELTAS.values():
            if (r + dr, c + dc) in monsters:
                adj.append((r + dr, c + dc))
        return adj

    def _flee_action(
        self, pos: Tuple[int, int], monsters: Set[Tuple[int, int]],
        walkable: Set[Tuple[int, int]],
    ) -> Optional[int]:
        adj = self._adjacent_monsters(pos, monsters)
        if not adj:
            return None
        mr = sum(m[0] for m in adj) / len(adj)
        mc = sum(m[1] for m in adj) / len(adj)
        best, best_dist = None, -1.0
        r, c = pos
        for dr, dc in DIRECTION_DELTAS.values():
            nr, nc = r + dr, c + dc
            if (nr, nc) not in walkable or (nr, nc) in monsters:
                continue
            d = (nr - mr) ** 2 + (nc - mc) ** 2
            if d > best_dist:
                best_dist = d
                best = self.mapper.delta_to_action(dr, dc)
        return best

    def _survival_action(self, parsed: Dict) -> Optional[int]:
        hp_ratio = parsed["hp"] / max(parsed["max_hp"], 1)
        adj = self._adjacent_monsters(parsed["agent_pos"], parsed["monsters"])

        if adj and hp_ratio < 0.5:
            action = self._flee_action(
                parsed["agent_pos"], parsed["monsters"], parsed["walkable"]
            )
            if action is not None:
                return action

        if parsed["hunger"] >= HUNGER_WEAK:
            eat = self.mapper.command("EAT")
            if eat is not None:
                return eat

        if parsed["agent_pos"] in parsed["items"]:
            pickup = self.mapper.command("PICKUP")
            if pickup is not None:
                return pickup

        return None

    # ---------- exploration ----------

    def _exploration_target(
        self, pos: Tuple[int, int], walkable: Set[Tuple[int, int]]
    ) -> Optional[Tuple[int, int]]:
        best, best_dist = None, float("inf")
        for cell in walkable:
            if cell in self.explored:
                continue
            d = abs(cell[0] - pos[0]) + abs(cell[1] - pos[1])
            if 0 < d < best_dist:
                best_dist = d
                best = cell
        if best is not None:
            return best
        for cell in walkable:
            r, c = cell
            for dr, dc in DIRECTION_DELTAS.values():
                nb = (r + dr, c + dc)
                if nb not in walkable and nb not in self.explored:
                    d = abs(r - pos[0]) + abs(c - pos[1])
                    if d < best_dist:
                        best_dist = d
                        best = cell
        return best

    # ---------- main decision ----------

    def act(self, obs: Dict) -> int:
        self.step_count += 1
        parsed = parse_map(obs)
        pos = parsed["agent_pos"]
        goal = parsed["goal"]
        walkable = parsed["walkable"]
        monsters = parsed["monsters"]

        self.explored.add(pos)

        if self.last_pos == pos:
            self.stuck_count += 1
        else:
            self.stuck_count = 0
        self.last_pos = pos

        # Stuck breaker: try SEARCH, then KICK, then random
        if self.stuck_count >= 5:
            self.stuck_count = 0
            for cmd in ("SEARCH", "KICK", "OPEN"):
                a = self.mapper.command(cmd)
                if a is not None:
                    return a

        # Survival override
        surv = self._survival_action(parsed)
        if surv is not None:
            return surv

        # Standing on goal -> descend
        if goal and pos == goal:
            desc = self.mapper.command("DESCEND")
            if desc is not None:
                return desc

        # Pathfind to goal
        if goal:
            hp_ratio = parsed["hp"] / max(parsed["max_hp"], 1)
            avoid = monsters if hp_ratio < 0.7 else set()
            path = bfs_path(pos, goal, walkable, avoid=avoid)
            if not path and avoid:
                path = bfs_path(pos, goal, walkable)
            if path:
                action = self.mapper.delta_to_action(
                    path[0][0] - pos[0], path[0][1] - pos[1]
                )
                if action is not None:
                    return action

        # Explore toward nearest unseen cell
        target = self._exploration_target(pos, walkable)
        if target:
            hp_ratio = parsed["hp"] / max(parsed["max_hp"], 1)
            avoid = monsters if hp_ratio < 0.7 else set()
            path = bfs_path(pos, target, walkable, avoid=avoid)
            if not path and avoid:
                path = bfs_path(pos, target, walkable)
            if path:
                action = self.mapper.delta_to_action(
                    path[0][0] - pos[0], path[0][1] - pos[1]
                )
                if action is not None:
                    return action

        # Fallback: search or random
        search = self.mapper.command("SEARCH")
        if search is not None:
            return search

        import random
        r, c = pos
        dirs = list(DIRECTION_DELTAS.values())
        random.shuffle(dirs)
        for dr, dc in dirs:
            if (r + dr, c + dc) in walkable:
                a = self.mapper.delta_to_action(dr, dc)
                if a is not None:
                    return a
        return 0


# ------------------------------------------------------------------ #
#  Episode runner (standalone)                                        #
# ------------------------------------------------------------------ #

def _env_reset(env, seed=None):
    """Handle gym vs gymnasium reset() return value."""
    result = env.reset(seed=seed)
    if isinstance(result, tuple):
        return result[0]
    return result


def _env_step(env, action):
    """Handle gym vs gymnasium step() return value. Returns (obs, reward, done, info)."""
    result = env.step(action)
    if len(result) == 5:
        obs, reward, terminated, truncated, info = result
        return obs, reward, terminated or truncated, info
    return result


def run_episode(
    env, agent, seed: int = 42, max_steps: int = 500
) -> Dict:
    """Run one episode. Returns dict with score, died, goal_reached, steps, actions."""
    obs = _env_reset(env, seed=seed)
    agent.reset()

    total_reward = 0.0
    actions_taken = []

    for _ in range(max_steps):
        action = agent.act(obs)
        actions_taken.append(int(action))
        obs, reward, done, info = _env_step(env, action)
        total_reward += reward
        if done:
            break

    end_status = info.get("end_status", -1) if isinstance(info, dict) else -1
    died = total_reward < 0 or end_status == 1
    goal_reached = total_reward > 0 or end_status in (4, 5)

    return {
        "score": float(total_reward),
        "died": bool(died),
        "goal_reached": bool(goal_reached),
        "steps": len(actions_taken),
        "actions": actions_taken,
    }


# ------------------------------------------------------------------ #
#  Standalone test                                                    #
# ------------------------------------------------------------------ #

OBS_KEYS = ("glyphs", "blstats", "message", "screen_descriptions")

TASK_TYPES = [
    "MiniHack-Room-5x5-v0",
    "MiniHack-Room-15x15-v0",
    "MiniHack-Corridor-R3-v0",
    "MiniHack-Corridor-R5-v0",
    "MiniHack-River-v0",
]


def main():
    import argparse, json, sys

    parser = argparse.ArgumentParser(description="Run deterministic heuristic agent on MiniHack")
    parser.add_argument("--task", default="MiniHack-Room-5x5-v0", help="MiniHack task ID")
    parser.add_argument("--episodes", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42, help="Base seed")
    parser.add_argument("--max-steps", type=int, default=500)
    parser.add_argument("--output", default=None, help="JSONL output path")
    args = parser.parse_args()

    import minihack  # noqa: F401 — registers envs

    env = gym.make(args.task, observation_keys=OBS_KEYS)
    agent = DeterministicHeuristicAgent(env)

    results = []
    for ep in range(args.episodes):
        seed = args.seed + ep
        result = run_episode(env, agent, seed=seed, max_steps=args.max_steps)
        result["episode_id"] = ep
        result["task"] = args.task
        result["seed"] = seed
        result["strategy"] = "deterministic"
        results.append(result)
        status = "DIED" if result["died"] else ("GOAL" if result["goal_reached"] else "TIMEOUT")
        print(f"  ep={ep:3d}  seed={seed}  steps={result['steps']:4d}  "
              f"score={result['score']:+.1f}  {status}")

    env.close()

    if args.output:
        with open(args.output, "w") as f:
            for r in results:
                row = {k: v for k, v in r.items() if k != "actions"}
                f.write(json.dumps(row) + "\n")
        print(f"Saved {len(results)} episodes to {args.output}")

    wins = sum(1 for r in results if r["goal_reached"])
    deaths = sum(1 for r in results if r["died"])
    print(f"\nSummary: {wins}/{len(results)} wins, {deaths}/{len(results)} deaths")


if __name__ == "__main__":
    main()

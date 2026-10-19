#!/usr/bin/env python3
"""Generate mock trajectory and expert data, then run analyze_divergence.py to validate output."""

import json
import os
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
MOCK_TRAJ_DIR = SCRIPT_DIR / "mock_trajectories"
MOCK_EXPERT_FILE = SCRIPT_DIR / "mock_expert.json"
MOCK_OUTPUT_DIR = SCRIPT_DIR / "mock_output"

TASK_TYPES = [
    "pick_and_place",
    "pick_clean_then_place",
    "pick_heat_then_place",
    "pick_cool_then_place",
    "look_at_obj",
    "pick_two_obj",
]


def make_expert_actions(n_steps: int, task_idx: int) -> list[dict]:
    """Generate a synthetic expert conversation with n_steps actions."""
    msgs = [
        {"from": "human", "value": f"Your task is to: do task {task_idx}"},
        {"from": "gpt", "value": "OK, I will help."},
    ]
    for i in range(n_steps):
        msgs.append({"from": "gpt", "value": f"Thought: step {i}\nAction: go to shelf {i}"})
        msgs.append({"from": "human", "value": f"Observation: You see shelf {i}."})
    return msgs


def make_trajectory(task_idx: int, task_type: str, reward: bool,
                    expert_actions: list[str], diverge_at: int | None) -> dict:
    """Generate a synthetic trajectory.

    If reward=True, actions match expert exactly.
    If reward=False, diverge at diverge_at step.
    """
    game_file = f"data/json_2.1.1/train/{task_type}/trial_{task_idx:03d}/game.tw-pddl"

    msgs = [
        {"role": "user", "content": "System instruction..."},
        {"role": "assistant", "content": "OK"},
        {"role": "user", "content": f"Your task is to: do task {task_idx}"},
    ]

    n_steps = len(expert_actions)
    for i in range(n_steps):
        if not reward and diverge_at is not None and i >= diverge_at:
            msgs.append({"role": "assistant", "content": f"Thought: wrong step {i}\nAction: take apple {i} from counter {i}"})
        else:
            msgs.append({"role": "assistant", "content": f"Thought: step {i}\nAction: {expert_actions[i]}"})
        msgs.append({"role": "user", "content": f"Observation: You see something at step {i}."})

    if not reward:
        for extra in range(2):
            msgs.append({"role": "assistant", "content": f"Thought: floundering {extra}\nAction: look"})
            msgs.append({"role": "user", "content": "Observation: Nothing happened."})

    return {
        "task_id": task_idx,
        "task_type": task_type,
        "game_file": game_file,
        "reward": reward,
        "steps": n_steps + (0 if reward else 2),
        "conversations": msgs,
    }


def generate():
    MOCK_TRAJ_DIR.mkdir(parents=True, exist_ok=True)
    MOCK_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    experts = []
    trajectories = []

    for idx in range(20):
        task_type = TASK_TYPES[idx % len(TASK_TYPES)]
        n_steps = 5 + (idx % 8)
        expert_actions = [f"go to shelf {i}" for i in range(n_steps)]

        game_file = f"data/json_2.1.1/train/{task_type}/trial_{idx:03d}"
        experts.append({
            "game_file": game_file,
            "conversations": make_expert_actions(n_steps, idx),
        })

        if idx % 3 == 0:
            # success
            traj = make_trajectory(idx, task_type, True, expert_actions, None)
        elif idx == 19:
            # unmatched failure: use a game_file that won't match any expert
            traj = make_trajectory(idx, task_type, False, expert_actions, 2)
            traj["game_file"] = "data/json_2.1.1/train/unknown_type/trial_999/game.tw-pddl"
        else:
            # failure with divergence
            diverge_at = max(0, min(idx % n_steps, n_steps - 1))
            traj = make_trajectory(idx, task_type, False, expert_actions, diverge_at)

        trajectories.append(traj)

    with open(MOCK_EXPERT_FILE, "w") as f:
        json.dump(experts, f, indent=2)

    traj_file = MOCK_TRAJ_DIR / "train.jsonl"
    with open(traj_file, "w") as f:
        for t in trajectories:
            f.write(json.dumps(t) + "\n")

    print(f"Generated {len(experts)} experts -> {MOCK_EXPERT_FILE}")
    print(f"Generated {len(trajectories)} trajectories -> {traj_file}")
    return MOCK_TRAJ_DIR, MOCK_EXPERT_FILE, MOCK_OUTPUT_DIR


def validate(output_dir: Path) -> bool:
    ok = True

    # Check JSON
    json_path = output_dir / "divergence_summary.json"
    if not json_path.exists():
        print(f"FAIL: {json_path} not found")
        return False

    with open(json_path) as f:
        data = json.load(f)

    required_keys = ["basic", "per_task_type_sr", "divergence", "groups", "gamma", "expert_match"]
    for k in required_keys:
        if k not in data:
            print(f"FAIL: missing top-level key '{k}' in JSON")
            ok = False

    if ok:
        assert data["basic"]["total_episodes"] == 20, f"Expected 20 episodes, got {data['basic']['total_episodes']}"
        assert data["basic"]["success"] == 7, f"Expected 7 successes, got {data['basic']['success']}"
        assert data["divergence"]["d_stats"]["count"] > 0, "No divergence samples"
        assert data["divergence"]["unmatched_failures"] >= 1, "Expected at least 1 unmatched"
        for g in ["early", "mid", "late"]:
            assert g in data["groups"], f"Missing group '{g}'"
        print(f"JSON structure: OK ({len(required_keys)} top-level keys present)")
        print(f"  Episodes: {data['basic']['total_episodes']}, Success: {data['basic']['success']}")
        print(f"  Divergence samples: {data['divergence']['d_stats']['count']}")
        print(f"  Unmatched: {data['divergence']['unmatched_failures']}")
        print(f"  Groups: early={data['groups']['early']['count']}, "
              f"mid={data['groups']['mid']['count']}, late={data['groups']['late']['count']}")

    # Check LaTeX
    tex_path = output_dir / "divergence_tables.tex"
    if not tex_path.exists():
        print(f"FAIL: {tex_path} not found")
        return False

    with open(tex_path) as f:
        tex = f.read()

    for marker in [r"\begin{table}", r"\end{table}", r"\toprule", r"\bottomrule",
                   r"\midrule", r"\begin{tabular}", "tab:task_type_sr",
                   "tab:divergence_groups", "tab:gamma_dist"]:
        if marker not in tex:
            print(f"FAIL: LaTeX missing '{marker}'")
            ok = False

    if ok:
        table_count = tex.count(r"\begin{table}")
        print(f"LaTeX structure: OK ({table_count} tables)")

    return ok


def main():
    print("=" * 60)
    print("MOCK DIVERGENCE TEST")
    print("=" * 60)

    traj_dir, expert_file, output_dir = generate()

    script = PROJECT_ROOT / "scripts" / "analyze_divergence.py"
    cmd = [
        sys.executable, str(script),
        "--trajectory_dirs", str(traj_dir),
        "--expert_file", str(expert_file),
        "--output_dir", str(output_dir),
        "--gamma_min", "0.85",
        "--gamma_max", "0.97",
    ]

    print(f"\nRunning: {' '.join(cmd)}")
    print("-" * 60)
    result = subprocess.run(cmd, capture_output=False)
    print("-" * 60)

    if result.returncode != 0:
        print(f"\nFAIL: script exited with code {result.returncode}")
        sys.exit(1)

    print("\n--- Validation ---")
    if validate(output_dir):
        print("\nALL CHECKS PASSED")
    else:
        print("\nSOME CHECKS FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()

"""
Collect expert demonstrations by rolling out frozen π₀ in perturbed LIBERO environments.

Only successful episodes are saved. Two perturbation types are supported:
  - physical: vary robot initial state (init_states index 1-49)
  - spatial:  LIBERO-Plus _add_N distractor objects (default) or perturb_region fallback

Output: pickle files with (observations, actions, metadata) per episode.

Usage:
    # Physical perturbation dry-run
    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
        --perturbation_type physical --dry_run

    # Spatial perturbation dry-run (uses _add_N by default)
    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
        --perturbation_type spatial --dry_run

    # Spatial with legacy perturb_region mode
    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
        --perturbation_type spatial --spatial_mode perturb_region --dry_run

    # Full physical collection
    CUDA_VISIBLE_DEVICES=1 python collect_expert_demos.py \
        --perturbation_type physical
"""

import argparse
import collections
import copy
import logging
import math
import os
import pickle
import random
import re
import sys
import time
import types
from pathlib import Path
from typing import Any

import numpy as np
import torch

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
LIBERO_ENV_RESOLUTION = 256
MODEL_INPUT_RESOLUTION = 224
REPLAN_STEPS = 5
NUM_STEPS_WAIT = 10
MAX_STEPS = 220  # libero_spatial default

# 10 base tasks in libero_spatial (no perturbation suffix)
BASE_TASK_SUITE = "libero_spatial"

# Spatial perturbation grid: 10 configurations with varying XY shifts and yaw
# Magnitudes chosen to be noticeable but within feasible reach of the robot.
SPATIAL_PERTURBATION_CONFIGS = [
    {"delta_xy": ( 0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
    {"delta_xy": (-0.05,  0.00), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
    {"delta_xy": ( 0.00,  0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
    {"delta_xy": ( 0.00, -0.05), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
    {"delta_xy": ( 0.03,  0.03), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
    {"delta_xy": (-0.03, -0.03), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.0)},
    {"delta_xy": ( 0.04,  0.00), "delta_half_len": 0.01, "delta_yaw": (0.3, 0.0)},
    {"delta_xy": (-0.04,  0.00), "delta_half_len": 0.01, "delta_yaw": (-0.3, 0.0)},
    {"delta_xy": ( 0.00,  0.04), "delta_half_len": 0.0,  "delta_yaw": (0.0, 0.3)},
    {"delta_xy": ( 0.00, -0.04), "delta_half_len": 0.0,  "delta_yaw": (0.0, -0.3)},
]


# ---------------------------------------------------------------------------
# Geometry / image helpers (from libero_integration.py)
# ---------------------------------------------------------------------------

def _quat2axisangle(quat: np.ndarray) -> np.ndarray:
    """Quaternion [x,y,z,w] -> axis-angle [ax,ay,az]."""
    q = np.asarray(quat, dtype=np.float64)
    norm = np.linalg.norm(q)
    if norm < 1e-8:
        return np.zeros(3, dtype=np.float32)
    q /= norm
    sin_half = np.linalg.norm(q[:3])
    if sin_half < 1e-8:
        return np.zeros(3, dtype=np.float32)
    angle = 2.0 * math.atan2(sin_half, q[3])
    axis = q[:3] / sin_half
    return (axis * angle).astype(np.float32)


def _resize_with_pad(img: np.ndarray, size: int) -> np.ndarray:
    """Resize image with aspect-preserving padding to (size, size, 3) uint8."""
    try:
        from openpi_client.image_tools import resize_with_pad, convert_to_uint8
        return convert_to_uint8(resize_with_pad(img, size, size))
    except ImportError:
        from PIL import Image as PILImage
        h, w = img.shape[:2]
        scale = min(size / h, size / w)
        new_h, new_w = int(h * scale), int(w * scale)
        resized = np.array(
            PILImage.fromarray(img).resize((new_w, new_h), PILImage.BILINEAR)
        )
        canvas = np.zeros((size, size, 3), dtype=np.uint8)
        y0, x0 = (size - new_h) // 2, (size - new_w) // 2
        canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized
        return canvas


def obs_to_model_input(obs: dict, task_description: str) -> dict:
    """Convert LIBERO observation to the dict format expected by policy.infer()."""
    base_img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
    wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])

    base_img = _resize_with_pad(base_img, MODEL_INPUT_RESOLUTION)
    wrist_img = _resize_with_pad(wrist_img, MODEL_INPUT_RESOLUTION)

    state = np.concatenate([
        obs["robot0_eef_pos"].astype(np.float32),
        _quat2axisangle(obs["robot0_eef_quat"]),
        obs["robot0_gripper_qpos"].astype(np.float32),
    ])

    return {
        "observation/image": base_img,
        "observation/wrist_image": wrist_img,
        "observation/state": state,
        "prompt": task_description,
    }


def extract_obs_for_saving(obs: dict) -> dict:
    """Extract observation fields to save in demo data (images stored as uint8)."""
    return {
        "agentview_image": obs["agentview_image"].copy(),
        "robot0_eye_in_hand_image": obs["robot0_eye_in_hand_image"].copy(),
        "robot0_eef_pos": obs["robot0_eef_pos"].astype(np.float32).copy(),
        "robot0_eef_quat": obs["robot0_eef_quat"].astype(np.float32).copy(),
        "robot0_gripper_qpos": obs["robot0_gripper_qpos"].astype(np.float32).copy(),
    }


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def _ensure_openpi_imports():
    """Stub out lerobot (training-only dep) before importing OpenPI."""
    for mod in [
        "lerobot", "lerobot.common", "lerobot.common.datasets",
        "lerobot.common.datasets.lerobot_dataset",
    ]:
        if mod not in sys.modules:
            sys.modules[mod] = types.ModuleType(mod)


def load_pi0_policy(checkpoint_path: str, device: str) -> object:
    """Load pi0 policy via OpenPI. Returns the Policy object for inference."""
    _ensure_openpi_imports()
    from openpi.training import config as _config
    from openpi.policies import policy_config

    train_config = _config.get_config("pi0_libero")
    policy = policy_config.create_trained_policy(
        train_config, checkpoint_path, pytorch_device=device
    )
    log.info("Loaded pi0 policy on %s", device)
    return policy


# ---------------------------------------------------------------------------
# Task discovery
# ---------------------------------------------------------------------------

def find_base_tasks(bddl_dir: str, num_tasks: int = 10) -> list[dict]:
    """Find base (unperturbed) BDDL files in libero_spatial.

    Returns list of dicts with keys: name, bddl_path, init_states_path.
    """
    all_files = [f for f in os.listdir(bddl_dir) if f.endswith(".bddl")]

    base_names = []
    for f in sorted(all_files):
        name = f.replace(".bddl", "")
        # Skip any file with perturbation suffixes
        if re.search(
            r"(_add_\d+|_table_\d+|_tb_\d+|_light_\d+|_language_\d+"
            r"|_view_|_noise_|_level\d+| copy)",
            name,
        ):
            continue
        base_names.append(name)

    init_dir = bddl_dir.replace("bddl_files", "init_files")
    tasks = []
    for name in base_names[:num_tasks]:
        bddl_path = os.path.join(bddl_dir, f"{name}.bddl")
        init_path = os.path.join(init_dir, f"{name}.pruned_init")
        if not os.path.exists(init_path):
            log.warning("init_states not found for %s, skipping", name)
            continue
        tasks.append({
            "name": name,
            "bddl_path": bddl_path,
            "init_states_path": init_path,
        })

    log.info("Found %d base tasks", len(tasks))
    return tasks


def get_task_language(bddl_path: str) -> str:
    """Extract language instruction from a BDDL file."""
    from libero.libero.envs.bddl_utils import get_problem_info
    info = get_problem_info(bddl_path)
    return info["language_instruction"]


def discover_add_n_tasks(task_suite: str = BASE_TASK_SUITE) -> list[dict]:
    """Discover all _add_N (distractor-object) tasks from the LIBERO-Plus benchmark.

    Returns list of dicts with: idx, name, language, bddl_path, init_states.
    """
    from libero.libero import benchmark, get_libero_path
    benchmark_dict = benchmark.get_benchmark_dict()
    suite = benchmark_dict[task_suite]()
    bddl_root = Path(get_libero_path("bddl_files"))

    tasks = []
    skipped = 0
    for i in range(suite.n_tasks):
        task = suite.get_task(i)
        name = getattr(task, "name", "") or getattr(task, "bddl_file", "")
        if not re.search(r"_add_\d+$", name.replace(".bddl", "")):
            continue

        bddl_path = str(bddl_root / task.problem_folder / task.bddl_file)
        if not os.path.exists(bddl_path):
            log.warning("BDDL not found, skipping: %s", bddl_path)
            skipped += 1
            continue

        try:
            init_states = suite.get_task_init_states(i)
        except Exception:
            log.warning("init_states failed for %s, skipping", name)
            skipped += 1
            continue

        tasks.append({
            "idx": i,
            "name": name.replace(".bddl", ""),
            "language": task.language,
            "bddl_path": bddl_path,
            "init_states": init_states,
        })

    log.info(
        "Discovered %d _add_N tasks (%d skipped) from %s",
        len(tasks), skipped, task_suite,
    )
    return tasks


# ---------------------------------------------------------------------------
# Environment creation
# ---------------------------------------------------------------------------

def create_env(bddl_path: str) -> object:
    """Create a LIBERO OffScreenRenderEnv from a BDDL file."""
    from libero.libero.envs import OffScreenRenderEnv
    env = OffScreenRenderEnv(
        bddl_file_name=bddl_path,
        camera_heights=LIBERO_ENV_RESOLUTION,
        camera_widths=LIBERO_ENV_RESOLUTION,
    )
    return env


def create_spatial_bddl(
    base_bddl_path: str,
    perturbation_config: dict,
    output_dir: str,
) -> str:
    """Create a perturbed BDDL file by applying spatial perturbation to all regions.

    Returns the path to the new BDDL file.
    """
    sys.path.insert(0, "/root/LIBERO-plus/libero")
    from libero.randomizer.bddl_operators import (
        load_bddl_file,
        save_bddl_file,
        perturb_region_info,
    )

    spec = load_bddl_file(base_bddl_path)
    delta_xy = perturbation_config["delta_xy"]
    delta_half = perturbation_config["delta_half_len"]
    delta_yaw = perturbation_config["delta_yaw"]

    for i in range(len(spec.region_infos)):
        spec.region_infos[i] = perturb_region_info(
            spec.region_infos[i],
            delta_region_centroid_xy=delta_xy,
            delta_region_half_len=delta_half,
            delta_yaw_rotation=delta_yaw,
        )

    os.makedirs(output_dir, exist_ok=True)
    base_name = Path(base_bddl_path).stem
    dx, dy = delta_xy
    filename = f"{base_name}_spatial_dx{dx:.2f}_dy{dy:.2f}.bddl"
    _, filepath = save_bddl_file(spec, bddl_filename=filename, bddl_dirpath=output_dir)
    return filepath


# ---------------------------------------------------------------------------
# Episode rollout
# ---------------------------------------------------------------------------

def rollout_episode(
    policy: object,
    env: object,
    task_description: str,
    init_states: np.ndarray,
    init_state_idx: int,
    seed: int,
) -> dict[str, Any]:
    """Run one episode, collecting (obs, action) pairs.

    Returns dict with observations, actions, success, num_steps.
    """
    env.seed(seed)
    obs = env.set_init_state(init_states[init_state_idx])

    for _ in range(NUM_STEPS_WAIT):
        obs, _, _, _ = env.step(LIBERO_DUMMY_ACTION)

    all_obs = [extract_obs_for_saving(obs)]
    all_actions = []
    action_plan = collections.deque()
    step = 0
    success = False
    done = False

    while not done and step < MAX_STEPS:
        if len(action_plan) == 0:
            obs_dict = obs_to_model_input(obs, task_description)
            result = policy.infer(obs_dict)
            action_chunk = result["actions"]
            action_plan.extend(action_chunk[:REPLAN_STEPS])

        action = action_plan.popleft()
        if isinstance(action, torch.Tensor):
            action = action.cpu().numpy()
        action_np = np.asarray(action, dtype=np.float32)

        obs, reward, done, info = env.step(
            action_np.tolist() if hasattr(action_np, "tolist") else list(action_np)
        )
        step += 1

        all_obs.append(extract_obs_for_saving(obs))
        all_actions.append(action_np)

        if done or reward > 0:
            success = info.get("success", reward > 0)

    return {
        "observations": all_obs,
        "actions": np.stack(all_actions) if all_actions else np.zeros((0, 7)),
        "success": success,
        "num_steps": step,
    }


# ---------------------------------------------------------------------------
# Collection loops
# ---------------------------------------------------------------------------

def collect_physical(
    policy: object,
    tasks: list[dict],
    episodes_per_config: int,
    output_dir: str,
    dry_run: bool,
) -> dict:
    """Collect expert demos with physical (robot initial state) perturbation.

    Uses init_states indices 1-49 (index 0 is nominal).
    """
    os.makedirs(output_dir, exist_ok=True)
    stats = {"total": 0, "success": 0, "saved_files": []}

    init_state_indices = list(range(1, 50))  # 49 perturbed states
    if dry_run:
        tasks = tasks[:1]
        init_state_indices = [1]
        episodes_per_config = 1

    for task_info in tasks:
        task_name = task_info["name"]
        init_states = torch.load(task_info["init_states_path"], weights_only=False)
        language = get_task_language(task_info["bddl_path"])
        log.info("Task: %s (%d init_states available)", task_name, len(init_states))

        for idx in init_state_indices:
            if idx >= len(init_states):
                continue

            for ep in range(episodes_per_config):
                seed = hash((task_name, idx, ep)) % (2**31)
                stats["total"] += 1

                try:
                    env = create_env(task_info["bddl_path"])
                    result = rollout_episode(
                        policy, env, language, init_states, idx, seed
                    )
                    env.close()
                except Exception:
                    log.exception(
                        "Episode failed: task=%s idx=%d ep=%d", task_name, idx, ep
                    )
                    continue

                if result["success"]:
                    stats["success"] += 1
                    demo = {
                        "observations": result["observations"],
                        "actions": result["actions"],
                        "task_name": task_name,
                        "perturbation_config": {
                            "type": "physical",
                            "init_state_idx": idx,
                        },
                        "success": True,
                        "num_steps": result["num_steps"],
                    }
                    fname = f"{task_name}_initstate{idx}_ep{ep}.pkl"
                    fpath = os.path.join(output_dir, fname)
                    with open(fpath, "wb") as f:
                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
                    stats["saved_files"].append(fpath)

                rate = stats["success"] / stats["total"] * 100
                log.info(
                    "[physical] task=%s idx=%d ep=%d | %s | "
                    "cumulative %d/%d (%.1f%%)",
                    task_name, idx, ep,
                    "SUCCESS" if result["success"] else "FAIL",
                    stats["success"], stats["total"], rate,
                )

    return stats


def collect_spatial(
    policy: object,
    tasks: list[dict],
    episodes_per_config: int,
    output_dir: str,
    dry_run: bool,
) -> dict:
    """Collect expert demos with spatial (objects layout) perturbation.

    Applies 10 predefined spatial perturbation configs to each base task.
    """
    os.makedirs(output_dir, exist_ok=True)
    tmp_bddl_dir = os.path.join(output_dir, "_tmp_bddl")
    os.makedirs(tmp_bddl_dir, exist_ok=True)
    stats = {"total": 0, "success": 0, "saved_files": []}

    configs = SPATIAL_PERTURBATION_CONFIGS
    if dry_run:
        tasks = tasks[:1]
        configs = configs[:1]
        episodes_per_config = 1

    for task_info in tasks:
        task_name = task_info["name"]
        init_states = torch.load(task_info["init_states_path"], weights_only=False)
        log.info("Task: %s", task_name)

        for cfg_idx, cfg in enumerate(configs):
            try:
                perturbed_bddl = create_spatial_bddl(
                    task_info["bddl_path"], cfg, tmp_bddl_dir
                )
                language = get_task_language(perturbed_bddl)
            except Exception:
                log.exception(
                    "BDDL perturbation failed: task=%s cfg=%d", task_name, cfg_idx
                )
                continue

            for ep in range(episodes_per_config):
                seed = hash((task_name, cfg_idx, ep)) % (2**31)
                stats["total"] += 1

                try:
                    env = create_env(perturbed_bddl)
                    # Use nominal init_state (index 0) for spatial perturbation
                    result = rollout_episode(
                        policy, env, language, init_states, 0, seed
                    )
                    env.close()
                except Exception:
                    log.exception(
                        "Episode failed: task=%s cfg=%d ep=%d",
                        task_name, cfg_idx, ep,
                    )
                    continue

                if result["success"]:
                    stats["success"] += 1
                    demo = {
                        "observations": result["observations"],
                        "actions": result["actions"],
                        "task_name": task_name,
                        "perturbation_config": {
                            "type": "spatial",
                            "config_idx": cfg_idx,
                            "delta_xy": cfg["delta_xy"],
                            "delta_half_len": cfg["delta_half_len"],
                            "delta_yaw": cfg["delta_yaw"],
                        },
                        "success": True,
                        "num_steps": result["num_steps"],
                    }
                    fname = f"{task_name}_spatial{cfg_idx}_ep{ep}.pkl"
                    fpath = os.path.join(output_dir, fname)
                    with open(fpath, "wb") as f:
                        pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
                    stats["saved_files"].append(fpath)

                rate = stats["success"] / stats["total"] * 100
                log.info(
                    "[spatial] task=%s cfg=%d ep=%d | %s | "
                    "cumulative %d/%d (%.1f%%)",
                    task_name, cfg_idx, ep,
                    "SUCCESS" if result["success"] else "FAIL",
                    stats["success"], stats["total"], rate,
                )

    return stats


def collect_spatial_add_n(
    policy: object,
    episodes_per_task: int,
    output_dir: str,
    dry_run: bool,
) -> dict:
    """Collect expert demos using LIBERO-Plus _add_N distractor-object tasks.

    Each _add_N task is a pre-built BDDL with extra objects in the scene.
    208 tasks × 3 episodes = 624 rollouts.
    """
    os.makedirs(output_dir, exist_ok=True)
    stats = {"total": 0, "success": 0, "saved_files": [], "load_errors": 0}

    add_tasks = discover_add_n_tasks()
    if not add_tasks:
        log.error("No _add_N tasks found. Check LIBERO-Plus installation.")
        return stats

    if dry_run:
        add_tasks = add_tasks[:2]
        episodes_per_task = 1

    log.info(
        "Collecting spatial (_add_N): %d tasks × %d eps = %d rollouts",
        len(add_tasks), episodes_per_task, len(add_tasks) * episodes_per_task,
    )

    for task_info in add_tasks:
        task_name = task_info["name"]
        language = task_info["language"]
        init_states = task_info["init_states"]

        for ep in range(episodes_per_task):
            seed = hash((task_name, ep)) % (2**31)
            stats["total"] += 1

            try:
                env = create_env(task_info["bddl_path"])
                init_idx = ep % len(init_states)
                result = rollout_episode(
                    policy, env, language, init_states, init_idx, seed
                )
                env.close()
            except FileNotFoundError as e:
                stats["load_errors"] += 1
                log.warning("Asset missing for %s: %s", task_name, e)
                continue
            except Exception:
                log.exception("Episode failed: task=%s ep=%d", task_name, ep)
                continue

            if result["success"]:
                stats["success"] += 1
                demo = {
                    "observations": result["observations"],
                    "actions": result["actions"],
                    "task_name": task_name,
                    "perturbation_config": {
                        "type": "spatial_add_n",
                        "source_task_idx": task_info["idx"],
                    },
                    "success": True,
                    "num_steps": result["num_steps"],
                }
                fname = f"{task_name}_ep{ep}.pkl"
                fpath = os.path.join(output_dir, fname)
                with open(fpath, "wb") as f:
                    pickle.dump(demo, f, protocol=pickle.HIGHEST_PROTOCOL)
                stats["saved_files"].append(fpath)

            rate = stats["success"] / stats["total"] * 100
            log.info(
                "[spatial_add_n] task=%s ep=%d | %s | cumulative %d/%d (%.1f%%) | load_errors=%d",
                task_name, ep,
                "SUCCESS" if result["success"] else "FAIL",
                stats["success"], stats["total"], rate,
                stats["load_errors"],
            )

    return stats


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Collect expert demos from π₀ in perturbed LIBERO environments"
    )
    parser.add_argument(
        "--perturbation_type", type=str, required=True,
        choices=["physical", "spatial"],
    )
    parser.add_argument(
        "--spatial_mode", type=str, default="add_n",
        choices=["add_n", "perturb_region"],
        help="Spatial perturbation mode: add_n (LIBERO-Plus distractors, default) "
             "or perturb_region (legacy BDDL region shifts)",
    )
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--num_tasks", type=int, default=10)
    parser.add_argument("--episodes_per_config", type=int, default=3)
    parser.add_argument(
        "--output_dir", type=str, default=None,
        help="Override output directory (default: auto from perturbation_type)",
    )
    parser.add_argument(
        "--checkpoint", type=str,
        default="/root/autodl-tmp/checkpoints/pi0_base",
    )
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    if args.output_dir is None:
        args.output_dir = (
            f"/root/meta_brain_lora_routing/data/expert_demos/{args.perturbation_type}"
        )

    device = f"cuda:{args.gpu_id}"
    log.info(
        "Config: type=%s spatial_mode=%s device=%s num_tasks=%d eps_per_cfg=%d dry_run=%s",
        args.perturbation_type, args.spatial_mode, device, args.num_tasks,
        args.episodes_per_config, args.dry_run,
    )

    log.info("Loading π₀ from %s", args.checkpoint)
    policy = load_pi0_policy(args.checkpoint, device)

    t0 = time.time()

    if args.perturbation_type == "physical":
        from libero.libero import get_libero_path
        bddl_dir = os.path.join(get_libero_path("bddl_files"), BASE_TASK_SUITE)
        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)
        if not tasks:
            log.error("No base tasks found in %s", bddl_dir)
            sys.exit(1)
        stats = collect_physical(
            policy, tasks, args.episodes_per_config,
            args.output_dir, args.dry_run,
        )
    elif args.spatial_mode == "add_n":
        stats = collect_spatial_add_n(
            policy, args.episodes_per_config,
            args.output_dir, args.dry_run,
        )
    else:
        from libero.libero import get_libero_path
        bddl_dir = os.path.join(get_libero_path("bddl_files"), BASE_TASK_SUITE)
        tasks = find_base_tasks(bddl_dir, num_tasks=args.num_tasks)
        if not tasks:
            log.error("No base tasks found in %s", bddl_dir)
            sys.exit(1)
        stats = collect_spatial(
            policy, tasks, args.episodes_per_config,
            args.output_dir, args.dry_run,
        )

    elapsed = time.time() - t0

    total_size = sum(
        os.path.getsize(f) for f in stats["saved_files"] if os.path.exists(f)
    )
    log.info("=" * 60)
    log.info("Collection complete: %s", args.perturbation_type)
    log.info("  Total episodes:  %d", stats["total"])
    log.info("  Successful:      %d", stats["success"])
    log.info(
        "  Success rate:    %.1f%%",
        stats["success"] / max(stats["total"], 1) * 100,
    )
    log.info("  Files saved:     %d", len(stats["saved_files"]))
    log.info("  Total size:      %.1f MB", total_size / 1024 / 1024)
    log.info("  Elapsed:         %.1f min", elapsed / 60)
    log.info("  Output dir:      %s", args.output_dir)


if __name__ == "__main__":
    main()

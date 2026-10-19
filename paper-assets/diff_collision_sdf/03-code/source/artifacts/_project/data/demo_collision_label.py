"""
Demo Collision Labeling for SafeLIBERO Demo Curation Experiment.

Replays LIBERO demonstration episodes in SafeLIBERO (obstacle-augmented)
environments and labels each episode as collision-free or collision-containing
using the same obstacle displacement metric as evaluation (threshold = 1mm).

Two labeling methods:
  Method A (primary): MuJoCo replay — full-body collision detection via
    obstacle displacement tracking (identical to eval_safelibero.py).
  Method B (sanity check): SDF-based EE trajectory check — queries
    precomputed SDF grid at EE positions (EE-only, misses arm-link collisions).

Input:
  - LIBERO demo HDF5 files (via benchmark API)
  - SafeLIBERO environment configs (with obstacles)
  - (Optional) SDF ground truth .npz for Method B

Output:
  - collision_labels.json: per-episode labels with collision metadata
  - collision_label_summary.json: aggregate statistics per task

Usage:
    # Label all tasks in safelibero_object
    python demo_collision_label.py --suite safelibero_object --safety_level II

    # Label a single task
    python demo_collision_label.py --suite safelibero_object --task_id 0

    # Also run Method B (SDF sanity check)
    python demo_collision_label.py --suite safelibero_object \
        --sdf_path ./data/sdf_gt_object_chocolate.npz

    # Dry run (first 3 demos per task)
    python demo_collision_label.py --suite safelibero_object --max_demos 3
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone

import numpy as np

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["MUJOCO_GL"] = "egl"

COLLISION_THRESHOLD = 0.001  # 1mm, same as eval

OBSTACLE_NAMES = [
    "moka_pot_obstacle_1",
    "white_storage_box_obstacle_1",
    "milk_obstacle_1",
    "wine_bottle_obstacle_1",
    "red_coffee_mug_obstacle_1",
    "yellow_book_obstacle_1",
]

SUITE_TASKS = {
    "safelibero_spatial": [
        "pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate",
        "pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate",
    ],
    "safelibero_object": [
        "pick_up_the_orange_juice_and_place_it_in_the_basket",
        "pick_up_the_chocolate_pudding_and_place_it_in_the_basket",
        "pick_up_the_milk_and_place_it_in_the_basket",
        "pick_up_the_bbq_sauce_and_place_it_in_the_basket",
    ],
}


def parse_args():
    p = argparse.ArgumentParser(description="Demo Collision Labeling for SafeLIBERO")
    p.add_argument("--suite", type=str, required=True,
                   choices=list(SUITE_TASKS.keys()),
                   help="SafeLIBERO suite name")
    p.add_argument("--safety_level", type=str, default="II", choices=["I", "II"],
                   help="Obstacle density level")
    p.add_argument("--task_id", type=int, default=None,
                   help="Specific task index (None = all tasks)")
    p.add_argument("--max_demos", type=int, default=None,
                   help="Max demos per task (None = all). For dry runs.")
    p.add_argument("--sdf_path", type=str, default=None,
                   help="Path to SDF .npz for Method B sanity check")
    p.add_argument("--output_dir", type=str, default="./demo_labels",
                   help="Output directory for label JSON files")
    p.add_argument("--demo_hdf5_dir", type=str, default=None,
                   help="Directory containing LIBERO demo HDF5 files. "
                        "If None, uses benchmark API default path.")
    p.add_argument("--verbose", action="store_true")
    return p.parse_args()


def get_obstacle_positions(sim, obstacle_names):
    """Get current positions of all obstacle objects from MuJoCo sim.

    Mirrors eval_safelibero.py: tries body_name2id(name + '_main') first,
    falls back to joint-based qpos lookup.

    Returns:
        dict[str, np.ndarray]: obstacle name -> xyz position (3,)
    """
    positions = {}
    for name in obstacle_names:
        try:
            body_id = sim.model.body_name2id(name + "_main")
            pos = sim.data.body_xpos[body_id].copy()
            positions[name] = pos
        except Exception:
            try:
                joint_name = name + "_jnt0"
                joint_id = sim.model.joint_name2id(joint_name)
                qpos_addr = sim.model.jnt_qposadr[joint_id]
                pos = sim.data.qpos[qpos_addr:qpos_addr + 3].copy()
                positions[name] = pos
            except Exception:
                pass
    return positions


def check_collision(initial_positions, current_positions, threshold=COLLISION_THRESHOLD):
    """Check if any obstacle displaced beyond threshold.

    Returns:
        (bool, str|None, float): (hit, obstacle_name, displacement)
    """
    for name in initial_positions:
        if name in current_positions:
            displacement = np.linalg.norm(
                current_positions[name] - initial_positions[name]
            )
            if displacement > threshold:
                return True, name, displacement
    return False, None, 0.0


def load_demo_actions_hdf5(hdf5_path, task_id, max_demos=None):
    """Load demo actions from LIBERO HDF5 file.

    LIBERO stores demos as HDF5 with structure:
        data/demo_0/actions  [T, action_dim]
        data/demo_0/states   [T+1, state_dim]
        ...

    Returns:
        list[np.ndarray]: list of action arrays, each [T, action_dim]
    """
    import h5py

    with h5py.File(hdf5_path, "r") as f:
        demos = []
        demo_keys = sorted(
            [k for k in f["data"].keys() if k.startswith("demo_")],
            key=lambda x: int(x.split("_")[1])
        )
        if max_demos is not None:
            demo_keys = demo_keys[:max_demos]

        for key in demo_keys:
            actions = f["data"][key]["actions"][:]
            demos.append(actions)

    return demos


def load_demo_actions_from_benchmark(benchmark, task_id, max_demos=None):
    """Load demo actions via LIBERO benchmark API.

    The benchmark provides demo HDF5 paths through get_task_demonstration().
    Falls back to searching standard LIBERO data directories.

    Returns:
        list[np.ndarray]: list of action arrays
    """
    import h5py

    demo_file = benchmark.get_task_demonstration(task_id)
    logging.info("Loading demos from: %s", demo_file)

    with h5py.File(demo_file, "r") as f:
        demos = []
        demo_keys = sorted(
            [k for k in f["data"].keys() if k.startswith("demo_")],
            key=lambda x: int(x.split("_")[1])
        )
        if max_demos is not None:
            demo_keys = demo_keys[:max_demos]

        for key in demo_keys:
            actions = f["data"][key]["actions"][:]
            demos.append(actions)

    logging.info("Loaded %d demo episodes", len(demos))
    return demos


def label_single_demo(env, sim, actions, obstacle_names, init_state, ep_idx,
                      verbose=False):
    """Replay one demo and label collision status.

    Args:
        env: SafeLIBERO OffScreenRenderEnv instance
        sim: env.sim MuJoCo simulation
        actions: np.ndarray [T, action_dim] — demo action sequence
        obstacle_names: list of obstacle body names to track
        init_state: initial state array for env.set_init_state()
        ep_idx: episode index (for logging)
        verbose: log per-step info

    Returns:
        dict with collision label and metadata
    """
    env.reset()
    env.set_init_state(init_state)

    # Settle physics (same 5-step warmup as eval)
    for _ in range(5):
        env.step(np.zeros(actions.shape[1]))

    initial_positions = get_obstacle_positions(sim, obstacle_names)
    if not initial_positions:
        logging.warning("  Episode %d: no obstacles detected in sim", ep_idx)
        return {
            "episode": ep_idx,
            "collision_free": True,
            "collision_timestep": None,
            "collision_obstacle": None,
            "max_obstacle_displacement": 0.0,
            "total_steps": len(actions),
            "obstacles_found": 0,
            "warning": "no_obstacles_detected",
        }

    collided = False
    collision_timestep = None
    collision_obstacle = None
    max_displacement = 0.0
    per_obstacle_max_disp = {name: 0.0 for name in initial_positions}

    for t, action in enumerate(actions):
        env.step(action)

        current_positions = get_obstacle_positions(sim, obstacle_names)

        # Track max displacement per obstacle
        for name in initial_positions:
            if name in current_positions:
                d = np.linalg.norm(current_positions[name] - initial_positions[name])
                per_obstacle_max_disp[name] = max(per_obstacle_max_disp[name], d)
                max_displacement = max(max_displacement, d)

        # Check collision (only record first)
        if not collided:
            hit, hit_name, disp = check_collision(initial_positions, current_positions)
            if hit:
                collided = True
                collision_timestep = int(t)
                collision_obstacle = hit_name
                if verbose:
                    logging.info("  Episode %d: collision at step %d, "
                                 "obstacle=%s, displacement=%.4fm",
                                 ep_idx, t, hit_name, disp)

    result = {
        "episode": ep_idx,
        "collision_free": not collided,
        "collision_timestep": collision_timestep,
        "collision_obstacle": collision_obstacle,
        "max_obstacle_displacement": float(max_displacement),
        "per_obstacle_max_displacement": {k: float(v)
                                          for k, v in per_obstacle_max_disp.items()},
        "total_steps": len(actions),
        "obstacles_found": len(initial_positions),
    }

    if verbose or (ep_idx + 1) % 10 == 0:
        status = "CF" if not collided else f"CC(step={collision_timestep})"
        logging.info("  Episode %d/%d: %s, max_disp=%.4fm",
                     ep_idx, -1, status, max_displacement)

    return result


def sdf_check_ee_trajectory(demo_actions_or_states, sdf_path):
    """Method B: SDF-based EE trajectory collision check.

    Checks if the EE trajectory passes through obstacle volumes by querying
    the precomputed SDF grid. Only detects EE collisions (misses arm-link).

    Args:
        demo_actions_or_states: list of arrays, each [T, state_dim] where
            first 3 dims = ee_pos (x, y, z)
        sdf_path: path to .npz with query_points and sdf_values

    Returns:
        list[dict]: per-episode SDF check results
    """
    from scipy.interpolate import RegularGridInterpolator

    data = np.load(sdf_path)
    query_points = data["query_points"]  # [N, 3]
    sdf_values = data["sdf_values"]      # [N]

    # Build grid interpolator from scattered points
    # Determine grid structure from query_points
    xs = np.unique(query_points[:, 0])
    ys = np.unique(query_points[:, 1])
    zs = np.unique(query_points[:, 2])

    nx, ny, nz = len(xs), len(ys), len(zs)
    if nx * ny * nz != len(sdf_values):
        logging.warning("SDF grid is not regular (%d×%d×%d != %d points). "
                        "Skipping Method B.", nx, ny, nz, len(sdf_values))
        return None

    sdf_grid = sdf_values.reshape(nx, ny, nz)
    interpolator = RegularGridInterpolator(
        (xs, ys, zs), sdf_grid,
        method="linear", bounds_error=False, fill_value=1.0
    )

    results = []
    for ep_idx, states in enumerate(demo_actions_or_states):
        ee_traj = states[:, :3]  # [T, 3]
        sdf_vals = interpolator(ee_traj)
        ee_collides = bool(np.any(sdf_vals < 0))
        min_sdf = float(np.min(sdf_vals))

        first_collision_step = None
        if ee_collides:
            first_collision_step = int(np.argmax(sdf_vals < 0))

        results.append({
            "episode": ep_idx,
            "ee_collision_free": not ee_collides,
            "min_sdf_value": min_sdf,
            "first_ee_collision_step": first_collision_step,
        })

    return results


def label_task(env, benchmark, task_id, args):
    """Label all demos for a single task.

    Args:
        env: SafeLIBERO OffScreenRenderEnv
        benchmark: LIBERO benchmark instance
        task_id: task index
        args: parsed arguments

    Returns:
        dict with task-level labels and statistics
    """
    task = benchmark.get_task(task_id)
    language = task.language
    logging.info("=== Task %d: %s ===", task_id, language)

    # Load demo actions
    demos = load_demo_actions_from_benchmark(benchmark, task_id, args.max_demos)
    init_states = benchmark.get_task_init_states(task_id)
    n_init = init_states.shape[0]
    logging.info("  %d demos, %d init states", len(demos), n_init)

    episode_labels = []
    for ep_idx, actions in enumerate(demos):
        # Each demo uses its corresponding init state
        init_idx = ep_idx % n_init
        init_state = init_states[init_idx]

        label = label_single_demo(
            env, env.sim, actions, OBSTACLE_NAMES, init_state,
            ep_idx, verbose=args.verbose
        )
        episode_labels.append(label)

    # Aggregate stats
    n_total = len(episode_labels)
    n_cf = sum(1 for l in episode_labels if l["collision_free"])
    n_cc = n_total - n_cf
    cf_rate = n_cf / n_total if n_total > 0 else 0.0

    # Collision timing analysis
    collision_steps = [l["collision_timestep"] for l in episode_labels
                       if l["collision_timestep"] is not None]
    avg_collision_step = float(np.mean(collision_steps)) if collision_steps else None
    median_collision_step = float(np.median(collision_steps)) if collision_steps else None

    # Per-obstacle collision frequency
    obstacle_hit_counts = {}
    for l in episode_labels:
        if l["collision_obstacle"]:
            name = l["collision_obstacle"]
            obstacle_hit_counts[name] = obstacle_hit_counts.get(name, 0) + 1

    task_summary = {
        "task_id": task_id,
        "task_name": task.name,
        "language": language,
        "n_demos": n_total,
        "n_collision_free": n_cf,
        "n_collision_containing": n_cc,
        "collision_free_rate": float(cf_rate),
        "avg_collision_step": avg_collision_step,
        "median_collision_step": median_collision_step,
        "obstacle_hit_counts": obstacle_hit_counts,
        "episodes": episode_labels,
    }

    logging.info("  Results: %d CF / %d total (%.1f%% collision-free)",
                 n_cf, n_total, cf_rate * 100)
    if obstacle_hit_counts:
        logging.info("  Obstacle hits: %s", obstacle_hit_counts)

    return task_summary


def main():
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    logging.info("Demo Collision Labeling")
    logging.info("  Suite: %s, Safety level: %s", args.suite, args.safety_level)

    # Import LIBERO
    try:
        from libero.libero.benchmark import get_benchmark
        from libero.libero.envs import OffScreenRenderEnv
    except ImportError:
        logging.error("LIBERO not found. Install with: pip install libero")
        sys.exit(1)

    # Set up benchmark
    benchmark_cls = get_benchmark(args.suite)
    benchmark = benchmark_cls(task_order_index=0, safety_level=args.safety_level)

    if args.task_id is not None:
        task_ids = [args.task_id]
    else:
        task_ids = list(range(benchmark.get_num_tasks()))

    logging.info("  Tasks to label: %s", task_ids)

    all_task_results = []
    total_cf = 0
    total_demos = 0
    t_start = time.time()

    for tid in task_ids:
        # Create environment for this task
        bddl_path = benchmark.get_task_bddl_file_path(tid)
        env_args = {
            "bddl_file_name": bddl_path,
            "camera_heights": 64,   # minimal resolution (no rendering needed)
            "camera_widths": 64,
        }
        env = OffScreenRenderEnv(**env_args)

        task_result = label_task(env, benchmark, tid, args)
        all_task_results.append(task_result)

        total_cf += task_result["n_collision_free"]
        total_demos += task_result["n_demos"]

        env.close()

    elapsed = time.time() - t_start

    # Overall summary
    overall_cf_rate = total_cf / total_demos if total_demos > 0 else 0.0
    logging.info("=" * 60)
    logging.info("Overall: %d CF / %d total (%.1f%% collision-free)",
                 total_cf, total_demos, overall_cf_rate * 100)
    logging.info("Time: %.1f seconds", elapsed)

    # Method B: SDF sanity check (optional)
    sdf_check_results = None
    if args.sdf_path and os.path.exists(args.sdf_path):
        logging.info("Running Method B: SDF-based EE trajectory check...")
        # Collect EE states from demo observation/state (first 3 dims)
        all_ee_states = []
        for task_result in all_task_results:
            # Re-extract states from HDF5 for SDF check
            # (We need observation/state, not just actions)
            tid = task_result["task_id"]
            try:
                import h5py
                demo_file = benchmark.get_task_demonstration(tid)
                with h5py.File(demo_file, "r") as f:
                    demo_keys = sorted(
                        [k for k in f["data"].keys() if k.startswith("demo_")],
                        key=lambda x: int(x.split("_")[1])
                    )
                    if args.max_demos:
                        demo_keys = demo_keys[:args.max_demos]
                    for key in demo_keys:
                        # observation/state first 3 dims = ee_pos
                        states = f["data"][key]["obs"]["robot0_eef_pos"][:]
                        all_ee_states.append(
                            np.pad(states, ((0, 0), (0, max(0, 3 - states.shape[1])))))
            except Exception as e:
                logging.warning("Could not extract EE states for task %d: %s", tid, e)

        if all_ee_states:
            sdf_check_results = sdf_check_ee_trajectory(all_ee_states, args.sdf_path)
            if sdf_check_results:
                n_sdf_cf = sum(1 for r in sdf_check_results if r["ee_collision_free"])
                logging.info("  Method B: %d/%d EE-collision-free (%.1f%%)",
                             n_sdf_cf, len(sdf_check_results),
                             100 * n_sdf_cf / len(sdf_check_results))

                # Cross-compare Method A vs B
                n_both = len(sdf_check_results)
                method_a_flat = []
                for tr in all_task_results:
                    for ep in tr["episodes"]:
                        method_a_flat.append(ep["collision_free"])
                method_a_flat = method_a_flat[:n_both]

                agree = sum(1 for a, b in zip(method_a_flat, sdf_check_results)
                            if a == b["ee_collision_free"])
                logging.info("  A vs B agreement: %d/%d (%.1f%%)",
                             agree, n_both, 100 * agree / n_both)

                # Disagreement = arm-link collisions (A detects, B misses)
                arm_link_only = sum(
                    1 for a, b in zip(method_a_flat, sdf_check_results)
                    if not a and b["ee_collision_free"]
                )
                logging.info("  Arm-link-only collisions (A=CC, B=CF): %d", arm_link_only)

    # Save results
    os.makedirs(args.output_dir, exist_ok=True)

    # Full labels file
    output = {
        "metadata": {
            "suite": args.suite,
            "safety_level": args.safety_level,
            "collision_threshold": COLLISION_THRESHOLD,
            "obstacle_names": OBSTACLE_NAMES,
            "labeling_timestamp": datetime.now(timezone.utc).isoformat(),
            "elapsed_seconds": round(elapsed, 1),
            "method": "mujoco_replay",
        },
        "overall": {
            "total_demos": total_demos,
            "total_collision_free": total_cf,
            "total_collision_containing": total_demos - total_cf,
            "collision_free_rate": float(overall_cf_rate),
        },
        "tasks": all_task_results,
    }

    if sdf_check_results:
        output["sdf_sanity_check"] = {
            "sdf_path": args.sdf_path,
            "results": sdf_check_results,
        }

    labels_path = os.path.join(
        args.output_dir,
        f"collision_labels_{args.suite}_level{args.safety_level}.json"
    )
    with open(labels_path, "w") as f:
        json.dump(output, f, indent=2)
    logging.info("Labels saved to %s", labels_path)

    # Summary file (compact, for quick reference)
    summary = {
        "suite": args.suite,
        "safety_level": args.safety_level,
        "overall_cf_rate": round(overall_cf_rate, 4),
        "total_demos": total_demos,
        "per_task": [],
    }
    for tr in all_task_results:
        cf_indices = [ep["episode"] for ep in tr["episodes"] if ep["collision_free"]]
        cc_indices = [ep["episode"] for ep in tr["episodes"] if not ep["collision_free"]]
        summary["per_task"].append({
            "task_id": tr["task_id"],
            "task_name": tr["task_name"],
            "cf_rate": round(tr["collision_free_rate"], 4),
            "n_cf": tr["n_collision_free"],
            "n_cc": tr["n_collision_containing"],
            "cf_episode_indices": cf_indices,
            "cc_episode_indices": cc_indices,
        })

    summary_path = os.path.join(
        args.output_dir,
        f"collision_label_summary_{args.suite}_level{args.safety_level}.json"
    )
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    logging.info("Summary saved to %s", summary_path)


if __name__ == "__main__":
    main()

"""
Extract BEV occupancy from LIBERO-Spatial HDF5 demo files.

Usage:
    python extract_occupancy.py --task_id 0 --output_dir /root/occsafe_vla/occ_data/
    python extract_occupancy.py --all --output_dir /root/occsafe_vla/occ_data/
"""

import os
import sys
import time
import argparse

os.environ["MUJOCO_GL"] = "egl"

import numpy as np
import h5py
import mujoco

from geom_classifier import build_geom_class_map, print_geom_classification
from occupancy_3d import build_occupancy_3d
from bev_projection import voxel_to_bev

# --- Configuration ---
RESOLUTION = 64
# Workspace bounds (meters, world frame) — will be tuned after geom exploration
GRID_ORIGIN = np.array([-0.32, -0.32, 0.90])
GRID_EXTENT = np.array([0.64, 0.64, 0.64])


def create_env(bddl_file):
    """Create a LIBERO environment from a BDDL file."""
    from libero.libero.envs import OffScreenRenderEnv

    env_args = {
        "bddl_file_name": bddl_file,
        "camera_heights": 128,
        "camera_widths": 128,
    }
    env = OffScreenRenderEnv(**env_args)
    env.reset()
    return env


def extract_single_demo(sim, states, geom_class_map, grid_origin, grid_extent, resolution):
    """Extract BEV occupancy for all frames in a single demo.

    Args:
        sim: robosuite MjSim
        states: (T, state_dim) array of flattened MuJoCo states
        geom_class_map: geom_id -> semantic class
        grid_origin, grid_extent: workspace bounds
        resolution: voxel resolution per axis

    Returns:
        bev_semantic: (T, R, R) uint8
        bev_binary: (T, R, R) bool
        timing_ms: average ms per frame
    """
    T = len(states)
    bev_sem_list = []
    bev_bin_list = []
    times = []

    for t in range(T):
        t0 = time.time()

        # Restore MuJoCo state
        sim.set_state_from_flattened(states[t])
        sim.forward()

        # Build 3D occupancy
        sem_3d, bin_3d = build_occupancy_3d(
            sim, grid_origin, grid_extent, resolution, geom_class_map
        )

        # Project to BEV
        bev_sem, bev_bin = voxel_to_bev(sem_3d, bin_3d)
        bev_sem_list.append(bev_sem)
        bev_bin_list.append(bev_bin)

        dt = (time.time() - t0) * 1000
        times.append(dt)

        if t % 50 == 0 or t == T - 1:
            print(f"  frame {t}/{T}, {dt:.1f} ms/frame")

    bev_semantic = np.stack(bev_sem_list, axis=0)
    bev_binary = np.stack(bev_bin_list, axis=0)
    avg_ms = np.mean(times)

    return bev_semantic, bev_binary, avg_ms


def extract_from_hdf5(hdf5_path, env, output_path, max_demos=None):
    """Extract BEV occupancy from all demos in an HDF5 file.

    Args:
        hdf5_path: path to LIBERO demo HDF5
        env: initialized LIBERO env
        output_path: output HDF5 path
        max_demos: limit number of demos (for testing)
    """
    sim = env.sim
    geom_class_map = build_geom_class_map(sim)

    print(f"\n=== Geom classification ({len(geom_class_map)} geoms) ===")
    print_geom_classification(sim, geom_class_map)

    with h5py.File(hdf5_path, "r") as f_in:
        demo_keys = sorted(
            [k for k in f_in["data"].keys() if k.startswith("demo_")],
            key=lambda x: int(x.split("_")[1]),
        )
        if max_demos is not None:
            demo_keys = demo_keys[:max_demos]

        print(f"\nProcessing {len(demo_keys)} demos from {hdf5_path}")
        print(f"Grid: origin={GRID_ORIGIN}, extent={GRID_EXTENT}, res={RESOLUTION}")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with h5py.File(output_path, "w") as f_out:
            grp = f_out.create_group("data")
            # Store metadata
            f_out.attrs["grid_origin"] = GRID_ORIGIN
            f_out.attrs["grid_extent"] = GRID_EXTENT
            f_out.attrs["resolution"] = RESOLUTION
            f_out.attrs["source_hdf5"] = os.path.basename(hdf5_path)

            total_frames = 0
            all_times = []

            for demo_key in demo_keys:
                print(f"\n--- {demo_key} ---")
                states = f_in[f"data/{demo_key}/states"][:]
                print(f"  states shape: {states.shape}")

                bev_sem, bev_bin, avg_ms = extract_single_demo(
                    sim, states, geom_class_map,
                    GRID_ORIGIN, GRID_EXTENT, RESOLUTION,
                )

                demo_grp = grp.create_group(demo_key)
                demo_grp.create_dataset(
                    "bev_binary",
                    data=bev_bin,
                    dtype=np.bool_,
                    chunks=(1, RESOLUTION, RESOLUTION),
                    compression="gzip",
                    compression_opts=4,
                )
                demo_grp.create_dataset(
                    "bev_semantic",
                    data=bev_sem,
                    dtype=np.uint8,
                    chunks=(1, RESOLUTION, RESOLUTION),
                    compression="gzip",
                    compression_opts=4,
                )

                occ_rate = bev_bin.mean() * 100
                print(f"  BEV shape: {bev_bin.shape}, occ_rate: {occ_rate:.1f}%, avg: {avg_ms:.1f} ms/frame")

                total_frames += len(states)
                all_times.append(avg_ms)

            f_out.attrs["total_frames"] = total_frames
            f_out.attrs["avg_ms_per_frame"] = float(np.mean(all_times))

    print(f"\n=== Done ===")
    print(f"Total frames: {total_frames}")
    print(f"Average: {np.mean(all_times):.1f} ms/frame")
    print(f"Output: {output_path}")


def get_benchmark_info():
    """Get LIBERO-Spatial benchmark tasks and demo paths."""
    from libero.libero import benchmark, get_libero_path

    bench = benchmark.get_benchmark("libero_spatial")(0)
    n_tasks = bench.get_num_tasks()
    task_names = bench.get_task_names()

    ds_path = get_libero_path("datasets")

    tasks = []
    for i in range(n_tasks):
        demo_rel = bench.get_task_demonstration(i)
        demo_path = os.path.join(ds_path, demo_rel)
        bddl_path = bench.get_task_bddl_file_path(i)
        tasks.append({
            "id": i,
            "name": task_names[i],
            "demo_path": demo_path,
            "bddl_path": bddl_path,
        })

    return tasks


def main():
    parser = argparse.ArgumentParser(description="Extract BEV occupancy from LIBERO demos")
    parser.add_argument("--task_id", type=int, default=None, help="Single task ID (0-9)")
    parser.add_argument("--all", action="store_true", help="Process all tasks")
    parser.add_argument("--output_dir", type=str, default="/root/occsafe_vla/occ_data/")
    parser.add_argument("--data_dir", type=str, default=None,
                        help="Override LIBERO datasets directory")
    parser.add_argument("--max_demos", type=int, default=None, help="Limit demos per task")
    parser.add_argument("--explore_only", action="store_true",
                        help="Only print geom info, don't extract")
    args = parser.parse_args()

    tasks = get_benchmark_info()

    if args.data_dir:
        for t in tasks:
            fname = os.path.basename(t["demo_path"])
            suite = os.path.basename(os.path.dirname(t["demo_path"]))
            t["demo_path"] = os.path.join(args.data_dir, suite, fname)

    if args.all:
        task_ids = list(range(len(tasks)))
    elif args.task_id is not None:
        task_ids = [args.task_id]
    else:
        task_ids = [0]

    for tid in task_ids:
        task = tasks[tid]
        print(f"\n{'='*60}")
        print(f"Task {tid}: {task['name']}")
        print(f"BDDL: {task['bddl_path']}")
        print(f"Demo: {task['demo_path']}")
        print(f"{'='*60}")

        env = create_env(task["bddl_path"])

        if args.explore_only:
            geom_class_map = build_geom_class_map(env.sim)
            print_geom_classification(env.sim, geom_class_map)
            env.close()
            continue

        if not os.path.exists(task["demo_path"]):
            print(f"WARNING: Demo file not found: {task['demo_path']}")
            print("Skipping this task.")
            env.close()
            continue

        output_path = os.path.join(
            args.output_dir,
            f"occ_{os.path.basename(task['demo_path'])}",
        )

        extract_from_hdf5(
            task["demo_path"], env, output_path,
            max_demos=args.max_demos,
        )
        env.close()


if __name__ == "__main__":
    main()

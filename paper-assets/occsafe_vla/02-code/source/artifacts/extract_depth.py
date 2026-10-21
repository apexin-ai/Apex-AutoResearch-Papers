"""
Depth map extraction from LIBERO demos via MuJoCo rendering.

Input:  LIBERO raw demo HDF5 files containing data/{demo_key}/states
Output: HDF5 files with per-frame depth maps + depth_index.json

Depth values are linearized distances in meters from the camera plane,
produced by mujoco.Renderer with enable_depth_rendering(). NOT normalized
Z-buffer values — raw metric depth. Typical range ~0.5-4.0m for tabletop scenes.

Dependencies: mujoco >= 3.0, robosuite, libero, h5py, numpy
"""

import os
import sys
import time
import json
import argparse

os.environ["MUJOCO_GL"] = "egl"

import numpy as np
import h5py
import mujoco


def create_env(bddl_file, resolution):
    from libero.libero.envs import OffScreenRenderEnv
    env_args = {
        "bddl_file_name": bddl_file,
        "camera_heights": resolution,
        "camera_widths": resolution,
    }
    env = OffScreenRenderEnv(**env_args)
    env.reset()
    return env


def extract_single_demo(renderer, sim, states, data_ptr, camera_name):
    """Render depth for each frame in a demo trajectory.

    Returns:
        depth_maps: np.ndarray of shape (T, H, W), float32, metric depth in meters
        avg_ms: average time per frame in milliseconds
    """
    T = len(states)
    depth_list = []
    times = []

    for t in range(T):
        t0 = time.time()

        sim.set_state_from_flattened(states[t])
        sim.forward()

        renderer.update_scene(data_ptr, camera=camera_name)
        renderer.enable_depth_rendering()
        depth = renderer.render().copy()
        renderer.disable_depth_rendering()

        depth_list.append(depth)

        dt = (time.time() - t0) * 1000
        times.append(dt)

        if t % 50 == 0 or t == T - 1:
            print(f"  frame {t}/{T}, {dt:.1f} ms/frame")

    depth_maps = np.stack(depth_list, axis=0)
    avg_ms = np.mean(times)
    return depth_maps, avg_ms


def extract_from_hdf5(hdf5_path, env, output_path, resolution, camera_name, max_demos=None):
    sim = env.sim
    model_ptr = sim.model._model
    data_ptr = sim.data._data

    renderer = mujoco.Renderer(model_ptr, height=resolution, width=resolution)

    with h5py.File(hdf5_path, "r") as f_in:
        demo_keys = sorted(
            [k for k in f_in["data"].keys() if k.startswith("demo_")],
            key=lambda x: int(x.split("_")[1]),
        )
        if max_demos is not None:
            demo_keys = demo_keys[:max_demos]

        print(f"\nProcessing {len(demo_keys)} demos from {hdf5_path}")
        print(f"Camera: {camera_name}, Resolution: {resolution}x{resolution}")

        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

        demo_frame_counts = {}

        with h5py.File(output_path, "w") as f_out:
            grp = f_out.create_group("data")
            f_out.attrs["resolution"] = resolution
            f_out.attrs["camera"] = camera_name
            f_out.attrs["source_hdf5"] = os.path.basename(hdf5_path)
            f_out.attrs["depth_unit"] = "meters"

            total_frames = 0
            all_times = []

            for demo_key in demo_keys:
                print(f"\n--- {demo_key} ---")
                states = f_in[f"data/{demo_key}/states"][:]
                print(f"  states shape: {states.shape}")

                depth_maps, avg_ms = extract_single_demo(
                    renderer, sim, states, data_ptr, camera_name,
                )

                demo_grp = grp.create_group(demo_key)
                demo_grp.create_dataset(
                    "depth",
                    data=depth_maps,
                    dtype=np.float32,
                    chunks=(1, resolution, resolution),
                    compression="gzip",
                    compression_opts=4,
                )

                demo_frame_counts[demo_key] = len(states)
                print(
                    f"  depth shape: {depth_maps.shape}, "
                    f"range: [{depth_maps.min():.3f}, {depth_maps.max():.3f}] m, "
                    f"avg: {avg_ms:.1f} ms/frame"
                )

                total_frames += len(states)
                all_times.append(avg_ms)

            f_out.attrs["total_frames"] = total_frames
            f_out.attrs["avg_ms_per_frame"] = float(np.mean(all_times))

    renderer.close()

    print(f"\n=== Done ===")
    print(f"Total frames: {total_frames}")
    print(f"Average: {np.mean(all_times):.1f} ms/frame")
    print(f"Output: {output_path}")

    return demo_frame_counts


def get_benchmark_info():
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
        task_name = task_names[i]
        tasks.append({
            "id": i,
            "name": task_name,
            "demo_path": demo_path,
            "bddl_path": bddl_path,
        })
    return tasks


def main():
    parser = argparse.ArgumentParser(description="Extract depth maps from LIBERO demos")
    parser.add_argument("--task_id", type=int, default=None,
                        help="Single task ID to process")
    parser.add_argument("--all", action="store_true",
                        help="Process all tasks")
    parser.add_argument("--output_dir", type=str, default="/root/occsafe_vla/depth_data/",
                        help="Output directory for depth HDF5 files")
    parser.add_argument("--data_dir", type=str, default=None,
                        help="Override demo data directory")
    parser.add_argument("--resolution", type=int, default=64,
                        help="Depth map resolution (default: 64)")
    parser.add_argument("--camera", type=str, default="agentview",
                        help="Camera name for rendering (default: agentview)")
    parser.add_argument("--max_demos", type=int, default=None,
                        help="Max demos per task (for testing)")
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

    os.makedirs(args.output_dir, exist_ok=True)

    depth_index = {}

    for tid in task_ids:
        task = tasks[tid]
        print(f"\n{'='*60}")
        print(f"Task {tid}: {task['name']}")
        print(f"BDDL: {task['bddl_path']}")
        print(f"Demo: {task['demo_path']}")
        print(f"{'='*60}")

        if not os.path.exists(task["demo_path"]):
            print(f"WARNING: Demo file not found: {task['demo_path']}")
            continue

        try:
            env = create_env(task["bddl_path"], args.resolution)

            output_filename = f"depth_{os.path.basename(task['demo_path'])}"
            output_path = os.path.join(args.output_dir, output_filename)

            demo_frame_counts = extract_from_hdf5(
                task["demo_path"], env, output_path,
                resolution=args.resolution,
                camera_name=args.camera,
                max_demos=args.max_demos,
            )

            task_key = task["name"]
            depth_index[task_key] = {
                "depth_file": output_filename,
                "demos": demo_frame_counts,
            }

            env.close()
        except Exception as e:
            print(f"ERROR processing task {tid}: {e}")
            continue

    index_path = os.path.join(args.output_dir, "depth_index.json")
    if os.path.exists(index_path):
        with open(index_path, "r") as f:
            existing = json.load(f)
        existing.update(depth_index)
        depth_index = existing

    with open(index_path, "w") as f:
        json.dump(depth_index, f, indent=2)
    print(f"\nIndex saved to {index_path}")
    print(f"Total tasks in index: {len(depth_index)}")


if __name__ == "__main__":
    main()

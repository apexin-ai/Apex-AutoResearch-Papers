"""Per-step Action Divergence Analysis (v2): Same-checkpoint, pruning-only comparison.

Loads the SAME checkpoint for both runs. BASELINE does full forward (no pruning),
ACIS applies true_removal pruning at k=0.5. Pruning is the only variable.

Drives the environment with baseline actions while recording both models'
action outputs at each timestep (same observation). Produces divergence curves
and per-dimension breakdown.

Usage:
    python analyze_action_divergence_v2.py --gpu 2 --num_episodes 10 --task_ids 0,1,2
    python analyze_action_divergence_v2.py --gpu 2 --k_ratio 0.3 --checkpoint checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time as time_mod
from pathlib import Path

os.environ.setdefault("MUJOCO_GL", "egl")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("HF_HUB_OFFLINE", "1")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch

ARTIFACTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ARTIFACTS_DIR))
sys.path.insert(0, str(ARTIFACTS_DIR.parent))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

CHECKPOINT = "checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt"
CONFIG = "configs/libero_acis_stage1only_k07.yaml"

SUITE = "libero_object"
MAX_STEPS = 280
ACTION_HORIZON = 50
ACTION_DIM_NAMES = ["pos_x", "pos_y", "pos_z", "rot_x", "rot_y", "rot_z", "gripper"]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--gpu", type=int, default=2)
    p.add_argument("--num_episodes", type=int, default=10)
    p.add_argument("--task_ids", type=str, default="0,1,2")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output_dir", type=str, default="artifacts")
    p.add_argument("--checkpoint", type=str, default=CHECKPOINT)
    p.add_argument("--config", type=str, default=CONFIG)
    p.add_argument("--k_ratio", type=float, default=0.5)
    return p.parse_args()


def load_config(config_path: str) -> dict:
    import yaml
    config_path = Path(config_path)
    with open(config_path) as f:
        config = yaml.safe_load(f)
    if "_base_" in config:
        base_path = config_path.parent / config.pop("_base_")
        base_config = load_config(str(base_path))
        for k, v in config.items():
            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):
                base_config[k].update(v)
            else:
                base_config[k] = v
        return base_config
    return config


def load_model_pair(checkpoint: str, config_path: str, k_ratio: float, device):
    """Load the same checkpoint twice: once as baseline (no pruning), once for ACIS.

    Returns (baseline_policy, acis_policy, acis_wrapper, config).
    """
    from train import load_smolvla_policy, wrap_with_imm

    config = load_config(config_path)

    # --- Baseline: load via wrapper (to match state_dict keys), extract policy ---
    baseline_policy = load_smolvla_policy(config, device)
    baseline_wrapper = wrap_with_imm(baseline_policy, config)
    baseline_wrapper.to(device)
    ckpt = torch.load(checkpoint, map_location=device, weights_only=False)
    baseline_wrapper.load_state_dict(ckpt["model_state_dict"], strict=False)
    baseline_wrapper.eval()
    baseline_policy = baseline_wrapper.policy

    # --- ACIS: load via wrapper, override k_ratio ---
    acis_policy = load_smolvla_policy(config, device)
    acis_wrapper = wrap_with_imm(acis_policy, config)
    acis_wrapper.to(device)
    ckpt2 = torch.load(checkpoint, map_location=device, weights_only=False)
    acis_wrapper.load_state_dict(ckpt2["model_state_dict"], strict=False)
    acis_wrapper.k_ratio = k_ratio
    acis_wrapper.eval()
    acis_policy = acis_wrapper.policy

    log.info("Loaded same checkpoint for both runs: %s", checkpoint)
    log.info("Baseline: full forward (no pruning)")
    log.info("ACIS: true_removal, k_ratio=%.2f", k_ratio)

    return baseline_policy, acis_policy, acis_wrapper, config


# --- Observation / Action utilities ---

def quat_to_axis_angle(quat: np.ndarray) -> np.ndarray:
    q = quat.astype(np.float64)
    w = np.clip(q[3], -1.0, 1.0)
    den = np.sqrt(max(1.0 - w * w, 0.0))
    if den > 1e-10:
        angle = 2.0 * np.arccos(w)
        axis = q[:3] / den
        return (axis * angle).astype(np.float32)
    return np.zeros(3, dtype=np.float32)


def extract_state(obs: dict) -> np.ndarray:
    rs = obs["robot_state"]
    eef_pos = np.asarray(rs["eef"]["pos"], dtype=np.float32)
    eef_quat = np.asarray(rs["eef"]["quat"], dtype=np.float64)
    gripper_qpos = np.asarray(rs["gripper"]["qpos"], dtype=np.float32)
    eef_aa = quat_to_axis_angle(eef_quat)
    return np.concatenate([eef_pos, eef_aa, gripper_qpos])


def obs_to_batch(obs, task_text, tokenizer, camera_keys, device):
    batch = {}
    for cam_key in camera_keys:
        short_name = cam_key.split(".")[-1]
        img = obs["pixels"][short_name]
        img_t = torch.from_numpy(np.asarray(img)).permute(2, 0, 1).float() / 255.0
        img_t = img_t.unsqueeze(0)
        img_t = torch.flip(img_t, dims=[2, 3])
        batch[cam_key] = img_t.to(device)
    state = extract_state(obs)
    batch["observation.state"] = torch.from_numpy(state).unsqueeze(0).to(device)
    text = task_text if task_text.endswith("\n") else task_text + "\n"
    encoded = tokenizer(
        [text], padding="longest", max_length=48, truncation=True, return_tensors="pt",
    )
    batch["observation.language.tokens"] = encoded["input_ids"].to(device)
    batch["observation.language.attention_mask"] = encoded["attention_mask"].bool().to(device)
    return batch


def find_connector(model):
    for name, module in model.named_modules():
        if name.endswith(".connector") or "multi_modal_projector" in name:
            return module
    return None


@torch.no_grad()
def compute_acis_mask(wrapper, batch, device):
    bm = wrapper.base_model
    images, _ = wrapper.policy.prepare_images(batch)
    vis_tokens, _ = wrapper._get_visual_tokens(images)
    B = vis_tokens.shape[0]
    noise = bm.sample_noise(
        (B, bm.config.chunk_size, bm.config.max_action_dim), device
    )
    time = torch.ones(B, device=device)
    suffix_embs, _, _ = bm.embed_suffix(noise, time)
    scores = wrapper.acis(suffix_embs, vis_tokens)
    N_vis = vis_tokens.shape[1]
    k = max(1, int(N_vis * wrapper.k_ratio))
    _, topk_idx = torch.topk(scores, k, dim=-1)
    mask = torch.zeros(B, N_vis, device=device)
    mask.scatter_(1, topk_idx, 1.0)
    return mask


def register_acis_hook(connector, mask: torch.Tensor, method: str = "true_removal"):
    """Register forward hook on connector that prunes visual tokens.

    Uses the stateful offset approach from eval_success_rate_libero.py to handle
    multi-camera setups where the connector is called once per camera.
    """
    state = {"offset": 0}

    def hook_fn(module, input, output):
        tokens = output[0] if isinstance(output, tuple) else output
        if tokens.dim() != 3:
            return output
        n = tokens.shape[1]
        offset = state["offset"]
        if offset + n > mask.shape[1]:
            return output
        cam_mask = mask[:, offset:offset + n]
        state["offset"] = offset + n

        B, N, D = tokens.shape
        keep_mask = cam_mask[:B]

        if method == "true_removal":
            kept = keep_mask[0].bool()
            masked = tokens[:, kept, :]
        else:
            masked = tokens * keep_mask.unsqueeze(-1)

        if isinstance(output, tuple):
            return (masked,) + output[1:]
        return masked

    return connector.register_forward_hook(hook_fn)


@torch.no_grad()
def predict_actions(policy, batch):
    images, img_masks = policy.prepare_images(batch)
    state = policy.prepare_state(batch)
    lang_tokens = batch["observation.language.tokens"]
    lang_masks = batch["observation.language.attention_mask"]
    actions = policy.model.sample_actions(
        images, img_masks, lang_tokens, lang_masks, state
    )
    original_action_dim = policy.config.action_feature.shape[0]
    return actions[0, :, :original_action_dim]


def run_divergence_analysis(args):
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    task_ids = [int(x) for x in args.task_ids.split(",")]
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    log.info("Loading model pair from same checkpoint...")
    baseline_policy, acis_policy, acis_wrapper, config = load_model_pair(
        args.checkpoint, args.config, args.k_ratio, device
    )

    from train import get_tokenizer_from_policy
    tokenizer = get_tokenizer_from_policy(baseline_policy)

    camera_keys = config.get("dataset", {}).get("features", {}).get("cameras", [
        "observation.images.image", "observation.images.image2"
    ])

    acis_connector = find_connector(acis_policy.model)
    if acis_connector is None:
        raise RuntimeError("Cannot find connector for ACIS hook")

    from libero.libero import benchmark
    from lerobot.envs.libero import get_task_init_states, LiberoEnv

    bench_dict = benchmark.get_benchmark_dict()
    task_suite = bench_dict[SUITE]()

    all_results = {}

    for task_id in task_ids:
        task = task_suite.get_task(task_id)
        task_desc = task.language
        log.info("=== Task %d: %s ===", task_id, task_desc)

        env = LiberoEnv(
            task_suite=task_suite,
            task_id=task_id,
            task_suite_name=SUITE,
            camera_name="agentview_image,robot0_eye_in_hand_image",
            obs_type="pixels_agent_pos",
            observation_width=256,
            observation_height=256,
            init_states=True,
            n_envs=1,
            episode_index=0,
            control_mode="relative",
        )

        task_episodes = []

        for ep in range(args.num_episodes):
            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)
            baseline_chunk = None
            baseline_idx = 0
            acis_chunk = None
            acis_idx = 0
            episode_data = {
                "task_id": task_id,
                "task_desc": task_desc,
                "episode": ep,
                "timesteps": [],
            }

            for step in range(MAX_STEPS):
                batch = obs_to_batch(obs, task_desc, tokenizer, camera_keys, device)

                need_replan = (baseline_chunk is None or baseline_idx >= ACTION_HORIZON)

                if need_replan:
                    baseline_chunk = predict_actions(baseline_policy, batch)
                    baseline_idx = 0

                    mask = compute_acis_mask(acis_wrapper, batch, device)
                    hook_handle = register_acis_hook(acis_connector, mask, method="true_removal")
                    acis_chunk = predict_actions(acis_policy, batch)
                    hook_handle.remove()
                    acis_idx = 0

                baseline_action = baseline_chunk[baseline_idx].cpu().numpy().astype(np.float32)
                acis_action = acis_chunk[acis_idx].cpu().numpy().astype(np.float32)

                baseline_action_clipped = np.clip(baseline_action, -1.0, 1.0)
                acis_action_clipped = np.clip(acis_action, -1.0, 1.0)

                l2_dist = float(np.linalg.norm(baseline_action_clipped - acis_action_clipped))
                per_dim_diff = (baseline_action_clipped - acis_action_clipped).tolist()

                episode_data["timesteps"].append({
                    "step": step,
                    "baseline_action": baseline_action_clipped.tolist(),
                    "acis_action": acis_action_clipped.tolist(),
                    "l2_distance": l2_dist,
                    "per_dim_diff": per_dim_diff,
                })

                baseline_idx += 1
                acis_idx += 1

                obs, reward, terminated, truncated, info = env.step(baseline_action_clipped)

                if info.get("is_success", False) or terminated or truncated:
                    break

            task_episodes.append(episode_data)
            n_steps = len(episode_data["timesteps"])
            final_l2 = episode_data["timesteps"][-1]["l2_distance"] if n_steps > 0 else 0
            log.info("  Ep %d: %d steps, final L2=%.4f", ep, n_steps, final_l2)

        env.close()
        all_results[task_id] = task_episodes

    # --- Analysis ---
    log.info("Computing statistics...")
    analysis = compute_analysis(all_results)

    # Save raw data
    json_path = output_dir / "action_divergence_v2_data.json"
    with open(json_path, "w") as f:
        json.dump({
            "metadata": {
                "checkpoint": args.checkpoint,
                "config": args.config,
                "k_ratio": args.k_ratio,
                "pruning_method": "true_removal",
                "baseline_mode": "bypass (no pruning)",
                "num_episodes": args.num_episodes,
                "seed": args.seed,
            },
            "episodes": all_results,
            "analysis": analysis,
        }, f, indent=2)
    log.info("Raw data saved to %s", json_path)

    # Plot
    plot_divergence_curves(all_results, analysis, output_dir, args.k_ratio)
    log.info("Done.")


def compute_analysis(all_results: dict) -> dict:
    all_l2_curves = []
    all_per_dim_curves = []

    for task_id, episodes in all_results.items():
        for ep_data in episodes:
            steps = ep_data["timesteps"]
            l2_curve = [s["l2_distance"] for s in steps]
            per_dim = [s["per_dim_diff"] for s in steps]
            all_l2_curves.append(l2_curve)
            all_per_dim_curves.append(per_dim)

    max_len = max(len(c) for c in all_l2_curves) if all_l2_curves else 0

    padded_l2 = np.full((len(all_l2_curves), max_len), np.nan)
    for i, curve in enumerate(all_l2_curves):
        padded_l2[i, :len(curve)] = curve

    mean_l2 = np.nanmean(padded_l2, axis=0).tolist()
    std_l2 = np.nanstd(padded_l2, axis=0).tolist()

    first_step_l2 = [c[0] for c in all_l2_curves if len(c) > 0]
    avg_first_step = float(np.mean(first_step_l2)) if first_step_l2 else 0.0

    overall_mean_l2 = float(np.nanmean(padded_l2))

    n_dims = 7
    dim_abs_means = []
    for d in range(n_dims):
        dim_vals = []
        for per_dim_curve in all_per_dim_curves:
            for step_diff in per_dim_curve:
                if len(step_diff) > d:
                    dim_vals.append(abs(step_diff[d]))
        dim_abs_means.append(float(np.mean(dim_vals)) if dim_vals else 0.0)

    valid_mean = [v for v in mean_l2 if not np.isnan(v)]
    if len(valid_mean) > 10:
        x = np.arange(len(valid_mean))
        slope = float(np.polyfit(x, valid_mean, 1)[0])
    else:
        slope = 0.0

    return {
        "overall_mean_l2": overall_mean_l2,
        "first_step_mean_l2": avg_first_step,
        "l2_growth_rate_per_step": slope,
        "per_dim_mean_abs_diff": {
            ACTION_DIM_NAMES[i]: dim_abs_means[i] for i in range(min(n_dims, len(dim_abs_means)))
        },
        "mean_l2_curve": mean_l2,
        "std_l2_curve": std_l2,
        "num_episodes": len(all_l2_curves),
        "max_episode_length": max_len,
    }


def plot_divergence_curves(all_results: dict, analysis: dict, output_dir: Path,
                           k_ratio: float):
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    ax = axes[0]
    colors = plt.cm.tab10(np.linspace(0, 1, 10))
    task_ids = sorted(all_results.keys())

    for ti, task_id in enumerate(task_ids):
        episodes = all_results[task_id]
        for ep_data in episodes:
            steps = ep_data["timesteps"]
            l2_vals = [s["l2_distance"] for s in steps]
            ax.plot(l2_vals, alpha=0.2, color=colors[ti % 10], linewidth=0.8)

    mean_curve = analysis["mean_l2_curve"]
    std_curve = analysis["std_l2_curve"]
    x = np.arange(len(mean_curve))
    ax.plot(x, mean_curve, color="black", linewidth=2, label="Mean")
    mean_arr = np.array(mean_curve)
    std_arr = np.array(std_curve)
    valid = ~np.isnan(mean_arr)
    ax.fill_between(
        x[valid], (mean_arr - std_arr)[valid], (mean_arr + std_arr)[valid],
        alpha=0.15, color="black"
    )
    ax.set_xlabel("Timestep")
    ax.set_ylabel("L2 Action Distance")
    ax.set_title(f"Same ckpt: bypass vs ACIS true_removal k={k_ratio}")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    dim_data = analysis["per_dim_mean_abs_diff"]
    names = list(dim_data.keys())
    values = list(dim_data.values())
    bar_colors = ["#2196F3"] * 3 + ["#FF9800"] * 3 + ["#4CAF50"]
    ax.bar(names, values, color=bar_colors)
    ax.set_xlabel("Action Dimension")
    ax.set_ylabel("Mean |Difference|")
    ax.set_title("Per-Dimension Divergence")
    ax.set_xticklabels(names, rotation=45, ha="right")
    ax.grid(True, alpha=0.3, axis="y")

    ax = axes[2]
    for ti, task_id in enumerate(task_ids):
        episodes = all_results[task_id]
        task_l2s = []
        for ep_data in episodes:
            l2_vals = [s["l2_distance"] for s in ep_data["timesteps"]]
            task_l2s.append(l2_vals)
        max_t = max(len(c) for c in task_l2s)
        padded = np.full((len(task_l2s), max_t), np.nan)
        for i, c in enumerate(task_l2s):
            padded[i, :len(c)] = c
        task_mean = np.nanmean(padded, axis=0)
        task_desc = episodes[0]["task_desc"]
        short_desc = task_desc[:30] + "..." if len(task_desc) > 30 else task_desc
        ax.plot(task_mean, linewidth=1.5, label=f"T{task_id}: {short_desc}", color=colors[ti % 10])
    ax.set_xlabel("Timestep")
    ax.set_ylabel("L2 Action Distance")
    ax.set_title("Per-Task Mean Divergence")
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    pdf_path = output_dir / "action_divergence_v2_curve.pdf"
    plt.savefig(pdf_path, dpi=150, bbox_inches="tight")
    plt.savefig(output_dir / "action_divergence_v2_curve.png", dpi=150, bbox_inches="tight")
    plt.close()
    log.info("Plots saved to %s", pdf_path)

    fig2, ax2 = plt.subplots(figsize=(6, 3))
    ax2.axis("off")
    summary_text = (
        f"Action Divergence Summary (same ckpt, true_removal k={k_ratio})\n"
        f"{'='*55}\n"
        f"Overall mean L2:        {analysis['overall_mean_l2']:.4f}\n"
        f"First-step mean L2:     {analysis['first_step_mean_l2']:.4f}\n"
        f"L2 growth rate/step:    {analysis['l2_growth_rate_per_step']:.6f}\n"
        f"Num episodes:           {analysis['num_episodes']}\n"
        f"Max episode length:     {analysis['max_episode_length']}\n"
        f"\nImmediate divergence: {'YES' if analysis['first_step_mean_l2'] > 0.05 else 'gradual'}\n"
        f"Pattern: {'accumulating' if analysis['l2_growth_rate_per_step'] > 1e-4 else 'stable offset'}\n"
    )
    ax2.text(0.05, 0.95, summary_text, transform=ax2.transAxes, fontsize=9,
             verticalalignment="top", fontfamily="monospace")
    plt.tight_layout()
    plt.savefig(output_dir / "action_divergence_v2_summary.pdf", dpi=150, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    args = parse_args()
    run_divergence_analysis(args)

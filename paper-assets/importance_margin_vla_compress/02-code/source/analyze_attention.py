#!/usr/bin/env python3
"""
Attention Visualization for SmolVLA Full FT Baseline on LIBERO.

Analyzes whether vision tokens are uniformly attended by action tokens
during inference. Core analysis for the Negative Results Paper.

Usage:
    python analyze_attention.py --gpu 0
    python analyze_attention.py --gpu 0 --task_ids 0,3,7
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

import numpy as np
import torch
import torch.nn.functional as F

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

CHECKPOINT = "checkpoints/libero_full_ft_100k/checkpoint.pt"
CONFIG = "configs/libero_full_ft.yaml"
SUITE = "libero_object"
DEFAULT_TASK_IDS = [0, 3, 7]
N_VIS_PER_CAM = 64
N_CAMERAS = 2
N_VIS = N_VIS_PER_CAM * N_CAMERAS
CHUNK_SIZE = 50
ACTION_HORIZON = 50
MAX_STEPS = 280
ARTIFACTS = ROOT / "artifacts"


# ═══════════════════════════════════════════════════════════════════════════════
# Attention Capture
# ═══════════════════════════════════════════════════════════════════════════════

class AttentionCapture:
    """Monkey-patches eager_attention_forward to capture softmax probs."""

    def __init__(self):
        self.enabled = False
        self.captured = []

    def patch(self, vlm_expert):
        original = vlm_expert.eager_attention_forward
        cap = self

        def patched(attention_mask, batch_size, head_dim,
                    query_states, key_states, value_states):
            result = original(attention_mask, batch_size, head_dim,
                              query_states, key_states, value_states)
            if not cap.enabled:
                return result

            with torch.no_grad():
                num_att = vlm_expert.num_attention_heads
                num_kv = vlm_expert.num_key_value_heads
                groups = num_att // num_kv
                kv_len = key_states.shape[1]
                q_len = query_states.shape[1]

                k = key_states[:, :, :, None, :].expand(
                    batch_size, kv_len, num_kv, groups, head_dim
                ).reshape(batch_size, kv_len, num_att, head_dim)

                q = query_states.to(torch.float32).transpose(1, 2)
                kt = k.to(torch.float32).transpose(1, 2)

                aw = torch.matmul(q, kt.transpose(2, 3)) * (head_dim ** -0.5)
                big_neg = torch.finfo(aw.dtype).min
                masked = torch.where(
                    attention_mask[:, None, :, :], aw, big_neg
                )
                probs = F.softmax(masked, dim=-1)  # (B, H, Q, K)
                cap.captured.append({
                    "probs": probs[0].cpu().float(),  # (H, Q, K)
                    "q_len": q_len,
                    "k_len": kv_len,
                })
            return result

        vlm_expert.eager_attention_forward = patched

    def start(self):
        self.enabled = True
        self.captured = []

    def stop(self):
        self.enabled = False

    def extract_vision_attention(self, n_vis=N_VIS):
        """Get attention from action tokens to vision tokens.

        Filters for denoise-step calls (q_len == CHUNK_SIZE, k_len >= n_vis).
        Returns (H, n_vis) averaged over action tokens per call,
        or None if no qualifying calls.
        """
        per_call = []
        for rec in self.captured:
            if rec["q_len"] != CHUNK_SIZE:
                continue
            if rec["k_len"] < n_vis:
                continue
            probs = rec["probs"]  # (H, Q, K)
            vis = probs[:, :, :n_vis]  # (H, Q, n_vis)
            vis_mean = vis.mean(dim=1)  # (H, n_vis)
            per_call.append(vis_mean.numpy())

        if not per_call:
            return None
        return per_call


# ═══════════════════════════════════════════════════════════════════════════════
# Config
# ═══════════════════════════════════════════════════════════════════════════════

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


# ═══════════════════════════════════════════════════════════════════════════════
# Observation Processing (from eval_success_rate_libero.py)
# ═══════════════════════════════════════════════════════════════════════════════

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
        [text], padding="longest", max_length=48,
        truncation=True, return_tensors="pt",
    )
    batch["observation.language.tokens"] = encoded["input_ids"].to(device)
    batch["observation.language.attention_mask"] = encoded["attention_mask"].bool().to(device)
    return batch


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


# ═══════════════════════════════════════════════════════════════════════════════
# Visualization
# ═══════════════════════════════════════════════════════════════════════════════

def compute_entropy(p):
    p = np.asarray(p, dtype=np.float64)
    p = p / p.sum()
    p = p[p > 0]
    return -np.sum(p * np.log2(p))


def plot_heatmap(stacked, save_path, n_vis=N_VIS):
    """stacked: (n_calls, H, n_vis)"""
    n_calls, H, _ = stacked.shape

    avg_heads = stacked.mean(axis=1)  # (n_calls, n_vis)

    fig, axes = plt.subplots(1, 2, figsize=(16, 8),
                             gridspec_kw={"width_ratios": [3, 1]})

    ax = axes[0]
    im = ax.imshow(avg_heads, aspect="auto", cmap="viridis",
                   interpolation="nearest")
    ax.set_xlabel("Vision Token Index", fontsize=11)
    ax.set_ylabel("Attention Layer Call Index", fontsize=11)
    ax.set_title("Action → Vision Token Attention\n"
                 "(averaged over heads and action tokens)", fontsize=12)
    ax.axvline(x=N_VIS_PER_CAM - 0.5, color="red", lw=1.5, ls="--", alpha=0.8)
    ax.text(N_VIS_PER_CAM // 2, -2.5, "Camera 1 (agentview)",
            ha="center", fontsize=9, color="red")
    ax.text(N_VIS_PER_CAM + N_VIS_PER_CAM // 2, -2.5, "Camera 2 (wrist)",
            ha="center", fontsize=9, color="red")
    plt.colorbar(im, ax=ax, shrink=0.7, label="Attention Weight")

    ax2 = axes[1]
    token_avg = avg_heads.mean(axis=0)
    colors = ["steelblue"] * N_VIS_PER_CAM + ["coral"] * N_VIS_PER_CAM
    ax2.barh(range(n_vis), token_avg, color=colors, height=1.0, edgecolor="none")
    ax2.set_xlabel("Mean Attention Weight", fontsize=11)
    ax2.set_ylabel("Vision Token Index", fontsize=11)
    ax2.set_title("Per-Token\nAttention", fontsize=12)
    ax2.invert_yaxis()
    ax2.axhline(y=N_VIS_PER_CAM - 0.5, color="red", lw=1.5, ls="--")

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.savefig(str(save_path).replace(".pdf", ".png"), dpi=150,
                bbox_inches="tight")
    plt.close()
    log.info("Saved: %s", save_path)


def plot_distribution(stacked, save_path, n_vis=N_VIS):
    """stacked: (n_calls, H, n_vis)"""
    n_calls, H, _ = stacked.shape
    max_ent = np.log2(n_vis)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # ── 1. Per-token attention bar chart ──
    ax = axes[0, 0]
    token_avg = stacked.mean(axis=(0, 1))  # (n_vis,)
    token_std = stacked.mean(axis=1).std(axis=0)
    colors = ["steelblue"] * N_VIS_PER_CAM + ["coral"] * N_VIS_PER_CAM
    ax.bar(range(n_vis), token_avg, color=colors, width=1.0,
           edgecolor="none", alpha=0.8)
    ax.fill_between(range(n_vis),
                    np.maximum(token_avg - token_std, 0),
                    token_avg + token_std,
                    alpha=0.2, color="gray")
    ax.axvline(x=N_VIS_PER_CAM - 0.5, color="red", lw=1.5, ls="--")
    uniform = 1.0 / n_vis
    ax.axhline(y=uniform, color="green", lw=1, ls=":",
               label=f"Uniform = {uniform:.4f}")
    ax.set_xlabel("Vision Token Index")
    ax.set_ylabel("Mean Attention Weight")
    ax.set_title("Per-Vision-Token Attention Distribution")
    ax.legend(fontsize=8)

    # ── 2. Entropy histogram ──
    ax = axes[0, 1]
    entropies = []
    for i in range(n_calls):
        for h in range(H):
            entropies.append(compute_entropy(stacked[i, h]))
    entropies = np.array(entropies)
    mean_ent = entropies.mean()
    ax.hist(entropies, bins=40, color="steelblue", edgecolor="white", alpha=0.8)
    ax.axvline(x=max_ent, color="red", lw=2, ls="--",
               label=f"Max entropy = {max_ent:.2f}")
    ax.axvline(x=mean_ent, color="orange", lw=2, ls="--",
               label=f"Mean = {mean_ent:.2f} ({mean_ent/max_ent:.1%})")
    ax.set_xlabel("Entropy (bits)")
    ax.set_ylabel("Count")
    ax.set_title(f"Attention Entropy\n"
                 f"(uniformity = {mean_ent/max_ent:.1%} of max)")
    ax.legend(fontsize=8)

    # ── 3. Camera-wise split ──
    ax = axes[1, 0]
    cam1 = stacked[:, :, :N_VIS_PER_CAM].mean()
    cam2 = stacked[:, :, N_VIS_PER_CAM:].mean()
    total = cam1 + cam2
    bars = ax.bar(
        ["Camera 1\n(agentview)", "Camera 2\n(wrist)"],
        [cam1 / total, cam2 / total],
        color=["steelblue", "coral"], edgecolor="black", lw=0.5
    )
    for bar, val in zip(bars, [cam1 / total, cam2 / total]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                f"{val:.1%}", ha="center", fontsize=10)
    ax.set_ylabel("Fraction of Vision Attention")
    ax.set_title("Camera-wise Attention Split")
    ax.set_ylim(0, 1)
    ax.axhline(y=0.5, color="green", lw=1, ls=":", label="Equal = 0.5")
    ax.legend(fontsize=8)

    # ── 4. Per-head entropy ──
    ax = axes[1, 1]
    head_avg = stacked.mean(axis=0)  # (H, n_vis)
    head_ent = np.array([compute_entropy(head_avg[h]) for h in range(H)])
    ax.bar(range(H), head_ent, color="steelblue", edgecolor="white")
    ax.axhline(y=max_ent, color="red", lw=1, ls="--",
               label=f"Max = {max_ent:.1f}")
    ax.set_xlabel("Attention Head")
    ax.set_ylabel("Entropy (bits)")
    ax.set_title("Per-Head Attention Entropy")
    ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.savefig(str(save_path).replace(".pdf", ".png"), dpi=150,
                bbox_inches="tight")
    plt.close()
    log.info("Saved: %s", save_path)


def plot_per_task_comparison(task_data, save_path, n_vis=N_VIS):
    """task_data: dict {task_id: (n_calls, H, n_vis)}"""
    n_tasks = len(task_data)
    fig, axes = plt.subplots(1, n_tasks, figsize=(6 * n_tasks, 4),
                             sharey=True)
    if n_tasks == 1:
        axes = [axes]

    for ax, (tid, stacked) in zip(axes, sorted(task_data.items())):
        token_avg = stacked.mean(axis=(0, 1))
        colors = ["steelblue"] * N_VIS_PER_CAM + ["coral"] * N_VIS_PER_CAM
        ax.bar(range(n_vis), token_avg, color=colors, width=1.0,
               edgecolor="none", alpha=0.8)
        ax.axvline(x=N_VIS_PER_CAM - 0.5, color="red", lw=1.5, ls="--")
        ent = compute_entropy(token_avg)
        max_ent = np.log2(n_vis)
        ax.set_title(f"Task {tid}\nEntropy={ent:.2f}/{max_ent:.2f} "
                     f"({ent/max_ent:.1%})")
        ax.set_xlabel("Vision Token Index")
        if ax == axes[0]:
            ax.set_ylabel("Mean Attention Weight")

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.savefig(str(save_path).replace(".pdf", ".png"), dpi=150,
                bbox_inches="tight")
    plt.close()
    log.info("Saved: %s", save_path)


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

def parse_args():
    p = argparse.ArgumentParser(
        description="Attention visualization for SmolVLA on LIBERO")
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--checkpoint", type=str, default=CHECKPOINT)
    p.add_argument("--config", type=str, default=CONFIG)
    p.add_argument("--suite", type=str, default=SUITE)
    p.add_argument("--task_ids", type=str,
                   default=",".join(map(str, DEFAULT_TASK_IDS)))
    p.add_argument("--max_steps", type=int, default=MAX_STEPS)
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


def main():
    args = parse_args()
    device = torch.device(f"cuda:{args.gpu}")
    task_ids = [int(x) for x in args.task_ids.split(",")]
    ARTIFACTS.mkdir(parents=True, exist_ok=True)

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    # ── Load model ──
    log.info("Loading model from %s ...", args.checkpoint)
    from train import load_smolvla_policy, get_tokenizer_from_policy
    config = load_config(args.config)
    policy = load_smolvla_policy(config, device)
    ckpt = torch.load(args.checkpoint, map_location=device, weights_only=False)
    policy.load_state_dict(ckpt["model_state_dict"], strict=False)
    policy.eval()

    vlm_expert = policy.model.vlm_with_expert
    log.info("num_attention_heads=%d  num_key_value_heads=%d  "
             "num_vlm_layers=%d  attention_mode=%s",
             vlm_expert.num_attention_heads,
             vlm_expert.num_key_value_heads,
             vlm_expert.num_vlm_layers,
             vlm_expert.attention_mode)

    tokenizer = get_tokenizer_from_policy(policy)
    ds_cfg = config.get("dataset", {})
    camera_keys = ds_cfg.get("features", {}).get("cameras", [
        "observation.images.image", "observation.images.image2"
    ])

    # ── Patch attention ──
    cap = AttentionCapture()
    cap.patch(vlm_expert)
    log.info("Attention capture patched")

    # ── LIBERO setup ──
    from libero.libero import benchmark
    from lerobot.envs.libero import get_task_init_states, LiberoEnv

    bench_dict = benchmark.get_benchmark_dict()
    task_suite = bench_dict[args.suite]()

    log.info("Suite '%s': %d tasks, analyzing %s",
             args.suite, len(task_suite.tasks), task_ids)

    # ── Run episodes and capture attention ──
    all_per_call = []          # aggregated across tasks
    task_level = {}            # per-task data
    metadata = {
        "checkpoint": args.checkpoint,
        "config": args.config,
        "suite": args.suite,
        "task_ids": task_ids,
        "n_vis_per_cam": N_VIS_PER_CAM,
        "n_cameras": N_CAMERAS,
        "num_attention_heads": vlm_expert.num_attention_heads,
        "num_vlm_layers": vlm_expert.num_vlm_layers,
    }

    for task_id in task_ids:
        task = task_suite.get_task(task_id)
        task_desc = task.language
        log.info("── Task %d: %s ──", task_id, task_desc)

        env = LiberoEnv(
            task_suite=task_suite,
            task_id=task_id,
            task_suite_name=args.suite,
            camera_name="agentview_image,robot0_eye_in_hand_image",
            obs_type="pixels_agent_pos",
            observation_width=256,
            observation_height=256,
            init_states=True,
            n_envs=1,
            episode_index=0,
            control_mode="relative",
        )

        obs, info = env.reset(seed=args.seed + task_id * 1000)
        action_chunk = None
        action_idx = 0
        n_predictions = 0
        task_per_call = []

        for step in range(args.max_steps):
            if action_chunk is None or action_idx >= ACTION_HORIZON:
                batch = obs_to_batch(
                    obs, task_desc, tokenizer, camera_keys, device
                )

                cap.start()
                action_chunk = predict_actions(policy, batch)
                cap.stop()

                vis_attn = cap.extract_vision_attention(n_vis=N_VIS)
                if vis_attn is not None:
                    task_per_call.extend(vis_attn)
                    all_per_call.extend(vis_attn)
                    n_predictions += 1

                action_idx = 0

            action = action_chunk[action_idx].cpu().numpy().astype(np.float32)
            action = np.clip(action, -1.0, 1.0)
            action_idx += 1

            obs, reward, terminated, truncated, info = env.step(action)

            if info.get("is_success", False):
                log.info("  Task %d: SUCCESS at step %d", task_id, step + 1)
                break
            if terminated or truncated:
                log.info("  Task %d: ended at step %d", task_id, step + 1)
                break

        env.close()

        if task_per_call:
            task_stacked = np.stack(task_per_call)
            task_level[task_id] = task_stacked
            ent = compute_entropy(task_stacked.mean(axis=(0, 1)))
            max_ent = np.log2(N_VIS)
            log.info("  Task %d: %d predict calls, %d attn captures, "
                     "entropy=%.2f/%.2f (%.1f%%)",
                     task_id, n_predictions, len(task_per_call),
                     ent, max_ent, 100 * ent / max_ent)
        else:
            log.warning("  Task %d: no attention captured!", task_id)

    # ── Aggregate and save ──
    if not all_per_call:
        log.error("No attention data captured. Exiting.")
        return

    stacked = np.stack(all_per_call)  # (total_calls, H, N_VIS)
    log.info("Total captured: %d attention snapshots, shape=%s",
             len(all_per_call), stacked.shape)

    token_avg = stacked.mean(axis=(0, 1))
    overall_ent = compute_entropy(token_avg)
    max_ent = np.log2(N_VIS)
    log.info("Overall entropy: %.2f / %.2f (%.1f%% of max uniform)",
             overall_ent, max_ent, 100 * overall_ent / max_ent)

    cam1_frac = stacked[:, :, :N_VIS_PER_CAM].mean() / (
        stacked[:, :, :N_VIS_PER_CAM].mean() +
        stacked[:, :, N_VIS_PER_CAM:].mean()
    )
    log.info("Camera split: cam1=%.1f%%, cam2=%.1f%%",
             100 * cam1_frac, 100 * (1 - cam1_frac))

    # Save raw data
    save_dict = {
        "stacked": stacked,
        "token_avg": token_avg,
        "entropy": overall_ent,
        "max_entropy": max_ent,
    }
    for tid, tdata in task_level.items():
        save_dict[f"task_{tid}"] = tdata

    npz_path = ARTIFACTS / "attention_data.npz"
    np.savez_compressed(str(npz_path), **save_dict)
    log.info("Saved raw data: %s", npz_path)

    meta_path = ARTIFACTS / "attention_metadata.json"
    metadata["overall_entropy"] = float(overall_ent)
    metadata["max_entropy"] = float(max_ent)
    metadata["uniformity_ratio"] = float(overall_ent / max_ent)
    metadata["cam1_fraction"] = float(cam1_frac)
    metadata["n_attention_captures"] = len(all_per_call)
    metadata["stacked_shape"] = list(stacked.shape)
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=2)
    log.info("Saved metadata: %s", meta_path)

    # ── Generate plots ──
    plot_heatmap(stacked, str(ARTIFACTS / "attention_heatmap.pdf"))
    plot_distribution(stacked, str(ARTIFACTS / "attention_distribution.pdf"))
    if len(task_level) > 1:
        plot_per_task_comparison(
            task_level, str(ARTIFACTS / "attention_per_task.pdf"))

    log.info("Done. Key finding: entropy = %.2f / %.2f (%.1f%% uniform)",
             overall_ent, max_ent, 100 * overall_ent / max_ent)
    if overall_ent / max_ent > 0.9:
        log.info("CONCLUSION: Vision tokens are nearly uniformly attended. "
                 "This explains why removing ANY token causes degradation.")
    else:
        log.info("CONCLUSION: Vision attention is NOT uniform. "
                 "Some tokens receive disproportionate attention.")


if __name__ == "__main__":
    main()

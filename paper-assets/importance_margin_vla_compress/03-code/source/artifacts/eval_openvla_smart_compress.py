"""LIBERO Success Rate Evaluation for OpenVLA Smart Compress models.

Usage:
    python eval_openvla_smart_compress.py \
        --n_queries 32 \
        --checkpoint_path checkpoints/openvla_sc_m32/checkpoint.pt \
        --suite libero_object \
        --num_episodes 50 \
        --gpu 0

Loads OpenVLA + VisionTokenCompressor checkpoint, runs LIBERO simulation,
reports per-task and overall success rates with Wilson CIs.
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
from PIL import Image

ARTIFACTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ARTIFACTS_DIR))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

SUITE_MAX_STEPS = {
    "libero_spatial": 280,
    "libero_object": 280,
    "libero_goal": 300,
    "libero_10": 520,
    "libero_90": 400,
}


def parse_args():
    p = argparse.ArgumentParser(description="LIBERO eval for OpenVLA Smart Compress")
    p.add_argument("--n_queries", type=int, required=True,
                   help="M: number of compressed vision tokens")
    p.add_argument("--checkpoint_path", type=str, required=True)
    p.add_argument("--suite", type=str, default="libero_object",
                   choices=list(SUITE_MAX_STEPS.keys()))
    p.add_argument("--num_episodes", type=int, default=50)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_steps", type=int, default=None)
    p.add_argument("--output", type=str, default=None)
    p.add_argument("--task_ids", type=str, default=None,
                   help="Comma-separated task IDs to evaluate (default: all)")
    p.add_argument("--model_path", type=str, default="openvla/openvla-7b",
                   help="Base OpenVLA model path")
    return p.parse_args()


def load_model(args, device):
    """Load OpenVLA base model + VTC compressor from checkpoint."""
    from transformers import AutoModelForVision2Seq, AutoProcessor
    from openvla_vtc_adapter import OpenVLASmartCompressWrapper, OpenVLAActionTokenizer

    ckpt = torch.load(args.checkpoint_path, map_location=device, weights_only=False)

    config = ckpt.get("config", {})
    model_path = config.get("model", {}).get("pretrained", args.model_path)
    dtype_str = config.get("model", {}).get("dtype", "float32")
    dtype_map = {"float32": torch.float32, "bfloat16": torch.bfloat16, "float16": torch.float16}
    torch_dtype = dtype_map.get(dtype_str, torch.float32)

    log.info("Loading OpenVLA from %s", model_path)
    model = AutoModelForVision2Seq.from_pretrained(
        model_path,
        torch_dtype=torch_dtype,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
    )
    processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

    compress_config = config.get("compressor", {"num_queries": args.n_queries})
    compress_config["num_queries"] = args.n_queries

    wrapper = OpenVLASmartCompressWrapper(model, processor, compress_config=compress_config)
    wrapper.to(device)

    if "compressor_state_dict" in ckpt:
        missing, unexpected = wrapper.load_state_dict(ckpt["compressor_state_dict"], strict=False)
    else:
        missing, unexpected = wrapper.load_state_dict(ckpt["model_state_dict"], strict=False)
    if missing:
        log.warning("Missing keys (%d): %s", len(missing), missing[:10])
    if unexpected:
        log.warning("Unexpected keys (%d): %s", len(unexpected), unexpected[:10])
    if not missing and not unexpected:
        log.info("Checkpoint loaded with strict match")
    wrapper.eval()

    log.info("OpenVLASmartCompressWrapper loaded: M=%d, compressor params=%d",
             args.n_queries,
             sum(p.numel() for p in wrapper.compressor.parameters()))

    # Action tokenizer
    action_stats = config.get("dataset", {}).get("action_stats", None)
    min_action = torch.tensor(action_stats["min"]) if action_stats else None
    max_action = torch.tensor(action_stats["max"]) if action_stats else None
    action_tokenizer = OpenVLAActionTokenizer(
        processor.tokenizer, min_action=min_action, max_action=max_action,
    )

    return wrapper, processor, action_tokenizer, config


# ---- LIBERO env helpers ----

def quat_to_axis_angle(quat):
    q = quat.astype(np.float64)
    w = np.clip(q[3], -1.0, 1.0)
    den = np.sqrt(max(1.0 - w * w, 0.0))
    if den > 1e-10:
        angle = 2.0 * np.arccos(w)
        axis = q[:3] / den
        return (axis * angle).astype(np.float32)
    return np.zeros(3, dtype=np.float32)


OPENVLA_PROMPT_TEMPLATE = "In: What action should the robot take to {task}?\nOut:"


def obs_to_inputs(obs, task_text, processor, camera_keys, device):
    """Convert LIBERO observation to OpenVLA model inputs."""
    # Extract images
    pixel_values_list = []
    for cam_key in camera_keys:
        img_key = cam_key.replace("observation.images.", "")
        img = obs.get(img_key, obs.get(cam_key, None))
        if img is None:
            for k, v in obs.items():
                if img_key in k and isinstance(v, np.ndarray):
                    img = v
                    break
        if img is None:
            raise ValueError(f"Camera {cam_key} not found in observation keys: {list(obs.keys())}")

        if isinstance(img, np.ndarray):
            if img.dtype == np.float32 or img.dtype == np.float64:
                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)
            pil_img = Image.fromarray(img)
        else:
            pil_img = img

        proc_out = processor.image_processor(images=[pil_img], return_tensors="pt")
        pixel_values_list.append(proc_out["pixel_values"].to(device))

    # Tokenize prompt (no action tokens for inference)
    prompt = OPENVLA_PROMPT_TEMPLATE.format(task=task_text)
    text_out = processor.tokenizer(
        [prompt],
        return_tensors="pt",
        add_special_tokens=True,
    )
    input_ids = text_out["input_ids"].to(device)
    attention_mask = text_out["attention_mask"].to(device)

    # Insert image tokens if not present
    from openvla_vtc_adapter import OpenVLASmartCompressWrapper
    img_tok_id = OpenVLASmartCompressWrapper(None, processor, {}).image_token_id
    if not (input_ids == img_tok_id).any():
        n_img = 256 * len(camera_keys)
        B = 1
        img_ids = torch.full((B, n_img), img_tok_id, dtype=torch.long, device=device)
        input_ids = torch.cat([input_ids[:, :1], img_ids, input_ids[:, 1:]], dim=1)
        img_mask = torch.ones(B, n_img, dtype=torch.long, device=device)
        attention_mask = torch.cat([attention_mask[:, :1], img_mask, attention_mask[:, 1:]], dim=1)

    pixel_values = pixel_values_list if len(pixel_values_list) > 1 else pixel_values_list[0]

    return {
        "pixel_values": pixel_values,
        "input_ids": input_ids,
        "attention_mask": attention_mask,
    }


@torch.no_grad()
def predict_action(wrapper, inputs, action_tokenizer):
    """Run inference and return continuous action (action_dim,)."""
    actions = wrapper.predict_action_continuous(
        pixel_values=inputs["pixel_values"],
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        action_tokenizer=action_tokenizer,
        max_new_tokens=7,
    )
    return actions[0]  # (action_dim,) single sample


def wilson_ci(successes, total, z=1.96):
    if total == 0:
        return 0.0, 0.0, 0.0
    p_hat = successes / total
    denom = 1 + z**2 / total
    center = (p_hat + z**2 / (2 * total)) / denom
    margin = z * np.sqrt((p_hat * (1 - p_hat) + z**2 / (4 * total)) / total) / denom
    return center, max(0, center - margin), min(1, center + margin)


# ---- main evaluation loop ----

def get_task_init_states(task_suite, task_id):
    """Get initial states for a LIBERO task."""
    try:
        from libero.libero.benchmark import get_init_states
        return get_init_states(task_suite, task_id)
    except ImportError:
        return None


def run_evaluation(args):
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    log.info("Device: %s", device)

    wrapper, processor, action_tokenizer, config = load_model(args, device)

    ds_cfg = config.get("dataset", {})
    cameras = ds_cfg.get("features", {}).get(
        "cameras", ["observation.images.image"]
    )

    # LIBERO setup
    from libero.libero.benchmark import get_benchmark
    benchmark = get_benchmark(args.suite)()
    num_tasks = benchmark.n_tasks

    if args.task_ids:
        task_ids = [int(x) for x in args.task_ids.split(",")]
    else:
        task_ids = list(range(num_tasks))

    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 300)
    output_path = Path(args.output) if args.output else (
        Path("eval_results")
        / f"openvla_sc_m{args.n_queries}_{args.suite}_ep{args.num_episodes}.json"
    )

    log.info("Suite: %s | Tasks: %s | Episodes: %d | Max steps: %d",
             args.suite, task_ids, args.num_episodes, max_steps)

    from libero.libero.envs import LiberoEnv

    total_successes = 0
    total_episodes = 0
    all_task_results = {}

    for task_id in task_ids:
        task_suite = benchmark
        task = benchmark.get_task(task_id)
        task_desc = task.language
        log.info("--- Task %d: %s ---", task_id, task_desc)

        env = LiberoEnv(
            task_suite=task_suite,
            task_id=task_id,
            task_suite_name=args.suite,
            camera_name="agentview_image,robot0_eye_in_hand_image",
            obs_type="pixels_agent_pos",
            observation_width=256,
            observation_height=256,
            init_states=True,
            n_envs=args.num_episodes,
            episode_index=0,
            control_mode="relative",
        )

        task_successes = []
        task_lengths = []

        for ep in range(args.num_episodes):
            obs, info = env.reset(seed=args.seed + task_id * 1000 + ep)
            success = False

            for step in range(max_steps):
                inputs = obs_to_inputs(obs, task_desc, processor, cameras, device)
                action = predict_action(wrapper, inputs, action_tokenizer)
                action_np = action.cpu().numpy().astype(np.float32)
                action_np = np.clip(action_np, -1.0, 1.0)

                obs, reward, terminated, truncated, info = env.step(action_np)

                if info.get("is_success", False):
                    success = True
                    break
                if terminated or truncated:
                    break

            ep_steps = step + 1
            task_successes.append(success)
            task_lengths.append(ep_steps)
            log.info("  Ep %d/%d | %s | steps=%d",
                     ep + 1, args.num_episodes,
                     "SUCCESS" if success else "FAIL", ep_steps)

        env.close()

        n_succ = sum(task_successes)
        n_total = len(task_successes)
        sr = n_succ / n_total if n_total > 0 else 0.0

        all_task_results[task_id] = {
            "task_id": task_id,
            "task_description": task_desc,
            "success_count": n_succ,
            "total_episodes": n_total,
            "success_rate": round(sr, 4),
            "mean_steps": round(float(np.mean(task_lengths)), 1),
        }
        total_successes += n_succ
        total_episodes += n_total
        log.info("  Task %d SR: %d/%d (%.1f%%)", task_id, n_succ, n_total, sr * 100)

    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0
    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)

    log.info("=" * 60)
    log.info("SUITE: %s | M=%d (OpenVLA Smart Compress)", args.suite, args.n_queries)
    log.info("Overall SR: %d/%d (%.1f%%)", total_successes, total_episodes, overall_sr * 100)
    log.info("95%% Wilson CI: [%.1f%%, %.1f%%]", ci_lo * 100, ci_hi * 100)
    for tid, tr in sorted(all_task_results.items()):
        log.info("  Task %d: %.0f%% (%d/%d) -- %s",
                 tid, tr["success_rate"] * 100, tr["success_count"],
                 tr["total_episodes"], tr["task_description"])
    log.info("=" * 60)

    summary = {
        "model": "openvla_smart_compress",
        "suite": args.suite,
        "n_queries": args.n_queries,
        "checkpoint": args.checkpoint_path,
        "total_episodes": total_episodes,
        "total_successes": total_successes,
        "overall_success_rate": round(overall_sr, 4),
        "wilson_ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
        "num_episodes_per_task": args.num_episodes,
        "max_steps": max_steps,
        "seed": args.seed,
        "per_task": all_task_results,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=2)
    log.info("Results saved to %s", output_path)

    return summary


if __name__ == "__main__":
    args = parse_args()
    run_evaluation(args)

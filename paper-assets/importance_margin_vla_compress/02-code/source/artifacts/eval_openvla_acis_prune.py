"""OpenVLA Attention-based Importance Score (ACIS) Pruning Evaluation on LIBERO.

Two-pass inference per step:
  1. Scoring pass: prefill forward with output_attentions=True
     → aggregate LLM attention to compute per-vision-token importance
  2. Pruning + generation: rebuild input with top-k vision tokens → generate action

Usage:
    CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python eval_openvla_acis_prune.py \
        --model_path /root/autodl-tmp/openvla-libero-object \
        --suite libero_object \
        --keep_ratio 0.5 \
        --num_episodes 50 \
        --seed 42
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

sys.path.insert(0, str(Path(__file__).resolve().parent))

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

OPENVLA_PROMPT_TEMPLATE = "In: What action should the robot take to {task}?\nOut:"


def parse_args():
    p = argparse.ArgumentParser(description="OpenVLA ACIS pruning eval on LIBERO")
    p.add_argument("--model_path", type=str, required=True,
                   help="Path to fine-tuned OpenVLA checkpoint dir")
    p.add_argument("--suite", type=str, default="libero_object",
                   choices=list(SUITE_MAX_STEPS.keys()))
    p.add_argument("--keep_ratio", type=float, default=0.5,
                   help="Fraction of vision tokens to keep (0.5 = keep 50%%)")
    p.add_argument("--num_episodes", type=int, default=50,
                   help="Episodes per task")
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_steps", type=int, default=None)
    p.add_argument("--output", type=str, default=None)
    p.add_argument("--task_ids", type=str, default=None,
                   help="Comma-separated task IDs (default: all)")
    p.add_argument("--attn_aggregation", type=str, default="mean_all",
                   choices=["mean_all", "last_layer", "last_4_layers"],
                   help="How to aggregate attention across layers")
    return p.parse_args()


# --- Model loading ---

def load_model(model_path: str, device: torch.device):
    from transformers import AutoModelForImageTextToText, AutoProcessor

    log.info("Loading OpenVLA from %s", model_path)
    model = AutoModelForImageTextToText.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
    )
    model = model.to(device).eval()
    processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

    n_params = sum(p.numel() for p in model.parameters())
    log.info("Model loaded: %.1fB params, dtype=%s", n_params / 1e9, model.dtype)
    return model, processor


# --- Vision feature extraction ---

@torch.no_grad()
def extract_vision_features(model, pixel_values: torch.Tensor) -> torch.Tensor:
    patch_features = model.vision_backbone(pixel_values)
    projected = model.projector(patch_features)
    return projected  # (B, N_vis, D)


# --- Attention importance scoring ---

def compute_attention_importance(
    attentions: tuple,
    n_vis: int,
    aggregation: str = "mean_all",
) -> torch.Tensor:
    """Per-vision-token importance from LLM attention weights.

    Sequence layout: [BOS, vis_1, ..., vis_N, text_1, ..., text_T]
    Vision tokens at positions 1..n_vis.
    Importance = avg attention FROM text tokens TO vision tokens.
    """
    if aggregation == "last_layer":
        layers = [attentions[-1]]
    elif aggregation == "last_4_layers":
        layers = attentions[-4:]
    else:
        layers = attentions

    device = layers[0].device
    importance = torch.zeros(1, n_vis, device=device, dtype=torch.float32)

    for layer_attn in layers:
        # (B, H, S, S) → avg over heads → (B, S, S)
        avg_attn = layer_attn.float().mean(dim=1)
        # text tokens attend to vision tokens
        text_to_vis = avg_attn[:, n_vis + 1:, 1:n_vis + 1]  # (B, T_text, N_vis)
        importance += text_to_vis.mean(dim=1)  # (B, N_vis)

    importance /= len(layers)
    return importance


# --- Action decoding ---

def decode_action(model, action_token_ids: np.ndarray) -> np.ndarray:
    """Decode discrete action token IDs to continuous actions (unnormalized)."""
    vocab_size = model.config.text_config.vocab_size - model.config.pad_to_multiple_of
    bins = np.linspace(-1, 1, model.config.n_action_bins)
    bin_centers = (bins[:-1] + bins[1:]) / 2.0

    discretized = vocab_size - action_token_ids
    discretized = np.clip(discretized - 1, a_min=0, a_max=bin_centers.shape[0] - 1)
    normalized_actions = bin_centers[discretized]

    unnorm_key = next(iter(model.norm_stats.keys()))
    action_stats = model.norm_stats[unnorm_key]["action"]
    mask = action_stats.get("mask", np.ones_like(action_stats["q01"], dtype=bool))
    action_high = np.array(action_stats["q99"])
    action_low = np.array(action_stats["q01"])
    actions = np.where(
        mask,
        0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,
        normalized_actions,
    )
    return actions


# --- ACIS pruned prediction ---

@torch.no_grad()
def predict_action_acis(
    model,
    processor,
    obs_image: Image.Image,
    task_text: str,
    device: torch.device,
    keep_ratio: float = 0.5,
    attn_agg: str = "mean_all",
) -> np.ndarray:
    """Predict action with attention-based vision token pruning."""
    # 1. Process image
    proc_out = processor.image_processor(images=[obs_image], return_tensors="pt")
    pixel_values = proc_out["pixel_values"].to(device, dtype=model.dtype)

    # 2. Tokenize prompt
    prompt = OPENVLA_PROMPT_TEMPLATE.format(task=task_text)
    text_out = processor.tokenizer(
        [prompt], return_tensors="pt", add_special_tokens=True,
    )
    input_ids = text_out["input_ids"].to(device)

    # Add special empty token (29871) to match training format
    if input_ids[0, -1].item() != 29871:
        input_ids = torch.cat(
            [input_ids, torch.tensor([[29871]], device=device)], dim=1,
        )

    # 3. Extract vision features
    vision_features = extract_vision_features(model, pixel_values)  # (1, N_vis, D)
    N_vis = vision_features.shape[1]

    # 4. Get text embeddings
    text_embeds = model.get_input_embeddings()(input_ids)  # (1, T, D)

    # 5. Build full multimodal input: [BOS, vis_1..vis_N, text_1..text_T]
    full_embeds = torch.cat([
        text_embeds[:, :1, :],   # BOS
        vision_features,          # all vision tokens
        text_embeds[:, 1:, :],   # rest of text
    ], dim=1)
    full_mask = torch.ones(1, full_embeds.shape[1], dtype=torch.long, device=device)

    # 6. Scoring pass
    outputs = model.language_model(
        inputs_embeds=full_embeds,
        attention_mask=full_mask,
        output_attentions=True,
        return_dict=True,
        use_cache=False,
    )

    # 7. Compute importance and select top-k
    importance = compute_attention_importance(outputs.attentions, N_vis, attn_agg)
    k = max(1, int(N_vis * keep_ratio))
    _, topk_indices = torch.topk(importance, k, dim=-1)
    topk_sorted = topk_indices.sort(dim=-1).values
    pruned_vision = vision_features[:, topk_sorted[0], :]

    # Free attention memory
    del outputs

    # 8. Build pruned multimodal input
    pruned_embeds = torch.cat([
        text_embeds[:, :1, :],   # BOS
        pruned_vision,            # kept vision tokens
        text_embeds[:, 1:, :],   # text
    ], dim=1)
    pruned_mask = torch.ones(1, pruned_embeds.shape[1], dtype=torch.long, device=device)

    # 9. Generate action tokens
    generated = model.language_model.generate(
        inputs_embeds=pruned_embeds,
        attention_mask=pruned_mask,
        max_new_tokens=7,
        do_sample=False,
    )

    # 10. Extract and decode action
    action_ids = generated[0, pruned_embeds.shape[1]:]
    action_ids = action_ids[:7].cpu().numpy()
    action = decode_action(model, action_ids)
    return action


# --- Utilities ---

def wilson_ci(k: int, n: int, z: float = 1.96):
    if n == 0:
        return 0.0, 0.0, 0.0
    p_hat = k / n
    denom = 1 + z ** 2 / n
    center = (p_hat + z ** 2 / (2 * n)) / denom
    margin = z * ((p_hat * (1 - p_hat) / n + z ** 2 / (4 * n ** 2)) ** 0.5) / denom
    return p_hat, max(0.0, center - margin), min(1.0, center + margin)


# --- Main eval loop ---

def run_evaluation(args):
    device = torch.device(f"cuda:{args.gpu}")
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    model, processor = load_model(args.model_path, device)
    action_dim = model.get_action_dim()

    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 280)

    # Output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = (
            Path(__file__).resolve().parent
            / "eval_results"
            / f"openvla_acis_k{args.keep_ratio:.2f}_{args.suite}.json"
        )

    # Setup LIBERO
    from libero.libero import benchmark as bm
    benchmark = bm.get_benchmark(args.suite)()

    task_ids = list(range(benchmark.n_tasks))
    if args.task_ids:
        task_ids = [int(x) for x in args.task_ids.split(",")]

    log.info("=== OpenVLA ACIS Pruning Eval ===")
    log.info("Model: %s", args.model_path)
    log.info("Suite: %s | keep_ratio: %.2f | attn_agg: %s",
             args.suite, args.keep_ratio, args.attn_aggregation)
    log.info("Tasks: %s | episodes/task: %d | max_steps: %d",
             task_ids, args.num_episodes, max_steps)

    from libero.libero.envs import LiberoEnv

    total_successes = 0
    total_episodes = 0
    all_task_results = {}

    eval_start = time_mod.time()

    for task_id in task_ids:
        task = benchmark.get_task(task_id)
        task_desc = task.language
        log.info("--- Task %d: %s ---", task_id, task_desc)

        env = LiberoEnv(
            task_suite=benchmark,
            task_id=task_id,
            task_suite_name=args.suite,
            camera_name="agentview_image",
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
                # Extract image from obs
                img = obs.get("agentview_image", None)
                if img is None:
                    for k, v in obs.items():
                        if "agentview" in k and isinstance(v, np.ndarray):
                            img = v
                            break
                if img is None:
                    raise ValueError(f"agentview image not found in obs keys: {list(obs.keys())}")

                if img.dtype in (np.float32, np.float64):
                    img = (np.clip(img, 0, 1) * 255).astype(np.uint8)
                pil_img = Image.fromarray(img)

                # Predict action with ACIS pruning
                action = predict_action_acis(
                    model, processor, pil_img, task_desc, device,
                    keep_ratio=args.keep_ratio,
                    attn_agg=args.attn_aggregation,
                )
                action = np.clip(action, -1.0, 1.0).astype(np.float32)

                obs, reward, terminated, truncated, info = env.step(action)

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

    elapsed = time_mod.time() - eval_start
    overall_sr = total_successes / total_episodes if total_episodes > 0 else 0.0
    _, ci_lo, ci_hi = wilson_ci(total_successes, total_episodes)

    log.info("=" * 60)
    log.info("SUITE: %s | MODE: acis_prune | keep_ratio: %.2f | attn_agg: %s",
             args.suite, args.keep_ratio, args.attn_aggregation)
    log.info("Overall SR: %d/%d (%.1f%%)", total_successes, total_episodes, overall_sr * 100)
    log.info("95%% Wilson CI: [%.1f%%, %.1f%%]", ci_lo * 100, ci_hi * 100)
    for tid, tr in sorted(all_task_results.items()):
        log.info("  Task %d: %.0f%% (%d/%d) -- %s",
                 tid, tr["success_rate"] * 100, tr["success_count"],
                 tr["total_episodes"], tr["task_description"])
    log.info("Elapsed: %.1f min", elapsed / 60)
    log.info("=" * 60)

    summary = {
        "model": "openvla",
        "model_path": args.model_path,
        "mode": "acis_prune",
        "suite": args.suite,
        "keep_ratio": args.keep_ratio,
        "attn_aggregation": args.attn_aggregation,
        "total_episodes": total_episodes,
        "total_successes": total_successes,
        "overall_success_rate": round(overall_sr, 4),
        "wilson_ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
        "num_episodes_per_task": args.num_episodes,
        "max_steps": max_steps,
        "seed": args.seed,
        "elapsed_seconds": round(elapsed, 1),
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

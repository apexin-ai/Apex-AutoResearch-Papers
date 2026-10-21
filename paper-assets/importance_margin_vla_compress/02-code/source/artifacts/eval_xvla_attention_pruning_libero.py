"""X-VLA Attention-based Vision Token Pruning Evaluation on LIBERO.

Uses BART encoder self-attention scores to identify important vision tokens,
then prunes less important ones from the encoder output. Three scoring modes:
  - attention_last:    importance from last encoder layer attention (column-sum)
  - attention_mean:    importance averaged across all encoder layers (column-sum)
  - attention_rollout: attention rollout across layers (Abnar & Zuidema, 2020)

Key difference from L2/random pruning: all vision tokens pass through the BART
encoder (so attention context is complete), then pruning happens on the encoder
output before it enters the SoftPromptedTransformer action head.

Evaluation protocol identical to eval_xvla_pruning_libero.py.

Usage:
    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_attention_pruning_libero.py \
        --model_path /path/to/X-VLA-Libero \
        --suite libero_object \
        --keep_ratio 0.5 \
        --mode attention_rollout \
        --num_episodes 50 \
        --gpu 0
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time as time_mod
from pathlib import Path
from functools import wraps

os.environ.setdefault("MUJOCO_GL", "egl")

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
    "libero_spatial": 800,
    "libero_object": 800,
    "libero_goal": 800,
    "libero_10": 900,
    "libero_90": 800,
}

EPS = 1e-6


def parse_args():
    p = argparse.ArgumentParser(description="X-VLA attention-based pruning eval on LIBERO")
    p.add_argument("--model_path", type=str, default="2toINF/X-VLA-Libero",
                   help="HuggingFace model path or local dir")
    p.add_argument("--suite", type=str, default="libero_object",
                   choices=list(SUITE_MAX_STEPS.keys()))
    p.add_argument("--keep_ratio", type=float, default=1.0,
                   help="Fraction of vision tokens to keep (1.0 = no pruning)")
    p.add_argument("--num_episodes", type=int, default=50)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max_steps", type=int, default=None)
    p.add_argument("--output", type=str, default=None)
    p.add_argument("--task_ids", type=str, default=None)
    p.add_argument("--domain_id", type=int, default=3)
    p.add_argument("--denoise_steps", type=int, default=10,
                   help="Flow matching denoising steps")
    p.add_argument("--mode", type=str, default="attention_last",
                   choices=["attention_last", "attention_mean", "attention_rollout"],
                   help="Attention-based pruning method")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Attention importance scoring
# ---------------------------------------------------------------------------

def compute_attention_importance(attentions, n_vision, mode):
    """Compute per-vision-token importance from encoder attention weights.

    The merged sequence layout is [vision_tokens (N), text_tokens (L)].
    Importance is the column-sum of the attention matrix restricted to vision
    columns: how much total attention each vision token receives from all
    positions across all heads.

    Args:
        attentions: tuple of L_layers tensors, each [B, H, S, S] (post-softmax)
        n_vision: number of vision token positions (first n_vision in sequence)
        mode: 'attention_last' | 'attention_mean' | 'attention_rollout'

    Returns:
        [B, n_vision] importance scores (higher = more important)
    """
    if mode == "attention_last":
        attn = attentions[-1].float().mean(dim=1)  # [B, S, S]
        importance = attn[:, :, :n_vision].sum(dim=1)  # [B, n_vision]

    elif mode == "attention_mean":
        attn = torch.stack(attentions, dim=0).float().mean(dim=0).mean(dim=1)  # [B, S, S]
        importance = attn[:, :, :n_vision].sum(dim=1)  # [B, n_vision]

    elif mode == "attention_rollout":
        B = attentions[0].shape[0]
        S = attentions[0].shape[-1]
        device = attentions[0].device

        result = torch.eye(S, device=device, dtype=torch.float32).unsqueeze(0).expand(B, -1, -1).clone()

        for attn_layer in attentions:
            attn_mean = attn_layer.float().mean(dim=1)  # [B, S, S]
            # Account for residual connection: 0.5 * attention + 0.5 * identity
            eye = torch.eye(S, device=device, dtype=torch.float32).unsqueeze(0)
            attn_res = 0.5 * attn_mean + 0.5 * eye
            attn_res = attn_res / attn_res.sum(dim=-1, keepdim=True).clamp(min=EPS)
            result = torch.bmm(attn_res, result)

        importance = result[:, :, :n_vision].sum(dim=1)  # [B, n_vision]

    else:
        raise ValueError(f"Unknown attention mode: {mode}")

    return importance


# ---------------------------------------------------------------------------
# Attention-based pruning installation
# ---------------------------------------------------------------------------

def install_attention_pruning(model, keep_ratio: float, mode: str):
    """Monkey-patch model.forward_vlm to run BART encoder with output_attentions,
    then prune vision tokens from the encoder output based on attention scores."""
    if keep_ratio >= 1.0:
        log.info("keep_ratio=%.2f, no pruning applied", keep_ratio)
        return

    def patched_forward_vlm(input_ids, pixel_values, image_mask):
        B, V = pixel_values.shape[:2]
        flat_mask = image_mask.view(-1).to(torch.bool)
        flat_images = pixel_values.flatten(0, 1)

        num_valid = int(flat_mask.sum().item())
        if num_valid == 0:
            raise ValueError("At least one image view must be valid per batch.")

        valid_images = flat_images[flat_mask]
        valid_feats = model.vlm._encode_image(valid_images)
        N, D = valid_feats.shape[1:]

        image_features = valid_feats.new_zeros((B * V, N, D))
        image_features[flat_mask] = valid_feats
        image_features = image_features.view(B, V, N, D)

        inputs_embeds = model.vlm.get_input_embeddings()(input_ids)

        merged_embeds, attention_mask = model.vlm._merge_input_ids_with_image_features(
            image_features[:, 0], inputs_embeds,
        )

        encoder_output = model.vlm.language_model.model.encoder(
            attention_mask=attention_mask,
            inputs_embeds=merged_embeds,
            output_attentions=True,
            return_dict=True,
        )
        enc_out = encoder_output.last_hidden_state   # [B, N+L, D_enc]
        attentions = encoder_output.attentions         # tuple of [B, H, N+L, N+L]

        k = max(1, int(keep_ratio * N))
        if k < N:
            importance = compute_attention_importance(attentions, N, mode)
            _, top_indices = importance.topk(k, dim=-1)
            top_indices_sorted = top_indices.sort(dim=-1).values  # [B, k]

            vision_out = enc_out[:, :N, :]   # [B, N, D_enc]
            text_out = enc_out[:, N:, :]     # [B, L, D_enc]

            D_enc = enc_out.shape[-1]
            pruned_vision = vision_out.gather(
                1, top_indices_sorted.unsqueeze(-1).expand(-1, -1, D_enc)
            )  # [B, k, D_enc]

            enc_out = torch.cat([pruned_vision, text_out], dim=1)  # [B, k+L, D_enc]

        aux_visual_inputs = image_features[:, 1:].reshape(B, -1, D)
        return {"vlm_features": enc_out, "aux_visual_inputs": aux_visual_inputs}

    model.forward_vlm = patched_forward_vlm
    log.info("Attention pruning installed: keep_ratio=%.2f, mode=%s", keep_ratio, mode)


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def load_model(model_path: str, device: torch.device):
    model_dir = str(Path(model_path).resolve())
    sys.path.insert(0, model_dir)

    from configuration_xvla import XVLAConfig
    from modeling_xvla import XVLA
    from processing_xvla import XVLAProcessor
    from safetensors.torch import load_file

    log.info("Loading X-VLA from %s", model_dir)
    config = XVLAConfig.from_pretrained(model_dir)
    model = XVLA(config)

    safetensors_path = Path(model_dir) / "model.safetensors"
    if safetensors_path.exists():
        state_dict = load_file(str(safetensors_path))
    else:
        import torch as _torch
        state_dict = _torch.load(Path(model_dir) / "pytorch_model.bin", map_location="cpu")
    model.load_state_dict(state_dict, strict=False)
    model = model.to(device).eval()

    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)
    if processor.tokenizer.pad_token is None:
        processor.tokenizer.pad_token = "<pad>"
        processor.tokenizer.pad_token_id = 1

    n_params = sum(p.numel() for p in model.parameters())
    log.info("Model loaded: %.1fM params, dtype=%s", n_params / 1e6, model.dtype)
    return model, processor


# ---------------------------------------------------------------------------
# 6D rotation utilities (following X-VLA's convention)
# ---------------------------------------------------------------------------

def mat_to_rot6d(R: np.ndarray) -> np.ndarray:
    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)


def rot6d_to_axis_angle(r6d: np.ndarray) -> np.ndarray:
    import robosuite.utils.transform_utils as T

    single = r6d.ndim == 1
    if single:
        r6d = r6d[None, :]

    a1 = r6d[:, 0:3]
    a2 = r6d[:, 3:6]

    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS)
    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)
    b2_orth = a2 - dot_prod * b1
    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS)
    b3 = np.cross(b1, b2, axis=-1)

    R = np.stack([b1, b2, b3], axis=-1)

    results = []
    for i in range(R.shape[0]):
        quat = T.mat2quat(R[i])
        aa = T.quat2axisangle(quat)
        results.append(aa)

    result = np.stack(results, axis=0)
    return result[0] if single else result


# ---------------------------------------------------------------------------
# Observation processing
# ---------------------------------------------------------------------------

def extract_proprio_20d(env) -> np.ndarray:
    robot = env.env.robots[0]
    ee_pos = robot.controller.ee_pos.copy()
    ee_ori_mat = robot.controller.ee_ori_mat.copy()
    ee_rot6d = mat_to_rot6d(ee_ori_mat)

    arm1 = np.concatenate([ee_pos, ee_rot6d, np.array([0.0], dtype=np.float32)])
    arm2 = np.zeros(10, dtype=np.float32)
    return np.concatenate([arm1, arm2])


def decode_action_20d_to_7d(action_20d: np.ndarray) -> np.ndarray:
    single = action_20d.ndim == 1
    if single:
        action_20d = action_20d[None, :]

    pos = action_20d[:, :3]
    rot6d = action_20d[:, 3:9]
    grip = action_20d[:, 9:10]

    axis_angle = rot6d_to_axis_angle(rot6d)
    grip_disc = np.where(grip > 0.5, 1.0, -1.0)

    result = np.concatenate([pos, axis_angle, grip_disc], axis=-1).astype(np.float32)
    return result[0] if single else result


def get_images_from_obs(obs) -> list:
    images = []
    for cam_name in ["agentview_image", "robot0_eye_in_hand_image"]:
        img = obs.get(cam_name, None)
        if img is None:
            for k, v in obs.items():
                if cam_name in k and isinstance(v, np.ndarray):
                    img = v
                    break
        if img is not None:
            if img.dtype in (np.float32, np.float64):
                img = (np.clip(img, 0, 1) * 255).astype(np.uint8)
            if cam_name == "agentview_image":
                img = np.flip(np.flip(img, 0), 1).copy()
            images.append(Image.fromarray(img))
    return images


@torch.no_grad()
def predict_actions(model, processor, images, task_desc, proprio_20d, domain_id,
                    device, denoise_steps=10):
    inputs = processor(images=images, language_instruction=task_desc)

    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32).unsqueeze(0).to(device)
    domain_t = torch.tensor([domain_id], dtype=torch.long).to(device)

    for k, v in inputs.items():
        if isinstance(v, torch.Tensor):
            if v.is_floating_point():
                inputs[k] = v.to(device=device, dtype=torch.float32)
            else:
                inputs[k] = v.to(device=device)

    actions = model.generate_actions(
        input_ids=inputs["input_ids"],
        image_input=inputs["image_input"],
        image_mask=inputs["image_mask"],
        proprio=proprio_t,
        domain_id=domain_t,
        steps=denoise_steps,
    )

    return actions.squeeze(0).float().cpu().numpy()


def wilson_ci(successes, total, z=1.96):
    if total == 0:
        return 0.0, 0.0, 1.0
    p = successes / total
    denom = 1 + z ** 2 / total
    center = (p + z ** 2 / (2 * total)) / denom
    spread = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * total)) / total) / denom
    return center, max(0.0, center - spread), min(1.0, center + spread)


def run_evaluation(args):
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    max_steps = args.max_steps or SUITE_MAX_STEPS.get(args.suite, 800)
    output_path = Path(args.output or
                       f"eval_results/xvla_attn_{args.mode}_k{args.keep_ratio}_{args.suite}.json")

    log.info("Suite: %s | Device: %s | keep_ratio=%.2f | mode=%s | Episodes/task: %d | Max steps: %d",
             args.suite, device, args.keep_ratio, args.mode, args.num_episodes, max_steps)

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    t0 = time_mod.time()
    model, processor = load_model(args.model_path, device)
    log.info("Model loaded in %.1fs", time_mod.time() - t0)

    dummy_img = torch.randn(1, 3, 224, 224, device=device)
    with torch.no_grad():
        dummy_feats = model.vlm._encode_image(dummy_img)
    n_vis_tokens = dummy_feats.shape[1]
    k_tokens = max(1, int(args.keep_ratio * n_vis_tokens))
    log.info("Vision tokens: %d total, keeping %d (%.0f%%)",
             n_vis_tokens, k_tokens, args.keep_ratio * 100)

    install_attention_pruning(model, args.keep_ratio, args.mode)

    num_actions_per_chunk = model.num_actions

    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv

    task_suite = benchmark.get_benchmark(args.suite)()
    n_tasks = task_suite.n_tasks

    if args.task_ids:
        task_id_list = [int(x) for x in args.task_ids.split(",")]
    else:
        task_id_list = list(range(n_tasks))

    eval_start = time_mod.time()
    all_task_results = {}
    total_successes = 0
    total_episodes = 0

    for task_id in task_id_list:
        task = task_suite.get_task(task_id)
        task_desc = task.language
        task_bddl = os.path.join(
            get_libero_path("bddl_files"), task.problem_folder, task.bddl_file
        )
        log.info("--- Task %d: %s ---", task_id, task_desc)

        init_states = task_suite.get_task_init_states(task_id)

        task_successes = []
        task_lengths = []

        for ep in range(args.num_episodes):
            env = OffScreenRenderEnv(
                bddl_file_name=task_bddl,
                camera_heights=256,
                camera_widths=256,
            )
            env.seed(args.seed + ep + 100)
            obs = env.reset()

            init_state_id = ep % init_states.shape[0]
            obs = env.set_init_state(init_states[init_state_id])

            for _ in range(10):
                neutral = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0], dtype=np.float32)
                obs, _, _, _ = env.step(neutral)

            for robot in env.env.robots:
                robot.controller.use_delta = False

            action_queue = []
            proprio_state = None
            success = False

            for step_idx in range(max_steps):
                if not action_queue:
                    proprio_20d = extract_proprio_20d(env)
                    if proprio_state is not None:
                        proprio_20d[:9] = proprio_state[:9]

                    images = get_images_from_obs(obs)
                    if not images:
                        raise ValueError(f"No images found in obs keys: {list(obs.keys())}")

                    raw_actions = predict_actions(
                        model, processor, images, task_desc, proprio_20d,
                        args.domain_id, device, args.denoise_steps,
                    )

                    proprio_state = proprio_20d.copy()
                    proprio_state[:9] = raw_actions[-1, :9].copy()

                    actions_7d = decode_action_20d_to_7d(raw_actions)
                    action_queue = list(actions_7d)

                action = action_queue.pop(0)
                obs, reward, done, info = env.step(action)

                if done or reward > 0.5:
                    success = True
                    break

            ep_steps = step_idx + 1
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
    _, ci_lo, ci_hi = wilson_ci(successes=total_successes, total=total_episodes)

    log.info("=" * 60)
    log.info("SUITE: %s | MODEL: xvla | mode: %s | keep_ratio: %.2f",
             args.suite, args.mode, args.keep_ratio)
    log.info("Overall SR: %d/%d (%.1f%%)", total_successes, total_episodes, overall_sr * 100)
    log.info("95%% Wilson CI: [%.1f%%, %.1f%%]", ci_lo * 100, ci_hi * 100)
    for tid, tr in sorted(all_task_results.items()):
        log.info("  Task %d: %.0f%% (%d/%d) -- %s",
                 tid, tr["success_rate"] * 100, tr["success_count"],
                 tr["total_episodes"], tr["task_description"])
    log.info("Elapsed: %.1f min", elapsed / 60)
    log.info("=" * 60)

    summary = {
        "model": "xvla",
        "model_path": args.model_path,
        "mode": args.mode,
        "suite": args.suite,
        "keep_ratio": args.keep_ratio,
        "n_vision_tokens_original": n_vis_tokens,
        "n_vision_tokens_kept": k_tokens,
        "total_episodes": total_episodes,
        "total_successes": total_successes,
        "overall_success_rate": round(overall_sr, 4),
        "wilson_ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
        "num_episodes_per_task": args.num_episodes,
        "max_steps": max_steps,
        "num_actions_per_chunk": num_actions_per_chunk,
        "domain_id": args.domain_id,
        "denoise_steps": args.denoise_steps,
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

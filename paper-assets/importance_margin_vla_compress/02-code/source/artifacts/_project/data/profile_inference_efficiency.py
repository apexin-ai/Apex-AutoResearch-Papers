"""Inference efficiency profiling for VLA token pruning.

Measures latency, GPU memory, and throughput across different keep ratios
for OpenVLA, Pi0.5, and X-VLA on LIBERO environments.

Usage:
    # OpenVLA with L2 norm pruning, sweep k_ratios
    python profile_inference_efficiency.py --model openvla --method l2norm \
        --k_ratios 1.0,0.9,0.7,0.5,0.3 --suite libero_object --num_episodes 50

    # Pi0.5 baseline (no pruning)
    python profile_inference_efficiency.py --model pi05 --method baseline \
        --suite libero_object --num_episodes 50

    # X-VLA random pruning
    python profile_inference_efficiency.py --model xvla --method random \
        --k_ratios 1.0,0.9,0.7,0.5 --suite libero_object --num_episodes 50

Input:
    --model: openvla / pi05 / xvla
    --method: baseline / random / l2norm / attention (attention only for openvla)
    --k_ratios: comma-separated keep ratios (default: 1.0,0.95,0.9,0.85,0.7,0.5,0.3)
    --suite: LIBERO suite name
    --num_episodes: episodes to sample (for latency profiling, not full eval)
    --warmup_steps: steps to skip before recording (default: 10)
    --seed, --gpu, --output

Output CSV:
    model,method,k_ratio,suite,latency_mean_ms,latency_std_ms,memory_peak_mb,throughput_sps,num_steps

Dependencies:
    - OpenVLA: transformers 4.40.1 (from /root/autodl-tmp/openvla_deps),
               openvla-repo (from /root/autodl-tmp/openvla-repo)
    - Pi0.5:   lerobot with PI05Policy
    - X-VLA:   configuration_xvla, modeling_xvla, processing_xvla (in model dir)
    - All:     libero, torch, numpy, PIL
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import logging
import math
import os
import sys
import time
import types
from collections import deque
from pathlib import Path

os.environ["MUJOCO_GL"] = "egl"
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("HF_HUB_OFFLINE", "1")

import numpy as np
import torch
from PIL import Image

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
}

# X-VLA uses longer horizons
XVLA_SUITE_MAX_STEPS = {
    "libero_spatial": 800,
    "libero_object": 800,
    "libero_goal": 800,
    "libero_10": 900,
}

DEFAULT_K_RATIOS = [1.0, 0.95, 0.9, 0.85, 0.7, 0.5, 0.3]


def parse_args():
    p = argparse.ArgumentParser(description="Profile VLA inference efficiency")
    p.add_argument("--model", type=str, required=True,
                   choices=["openvla", "pi05", "xvla"])
    p.add_argument("--method", type=str, default="baseline",
                   choices=["baseline", "random", "l2norm", "attention"])
    p.add_argument("--k_ratios", type=str, default="1.0,0.95,0.9,0.85,0.7,0.5,0.3")
    p.add_argument("--suite", type=str, default="libero_object")
    p.add_argument("--num_episodes", type=int, default=50)
    p.add_argument("--warmup_steps", type=int, default=10)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--output", type=str, default="profile_results.csv")
    # Model-specific paths
    p.add_argument("--model_path", type=str, default=None,
                   help="Override default model checkpoint path")
    p.add_argument("--unnorm_key", type=str, default="libero_object",
                   help="OpenVLA unnormalization key")
    p.add_argument("--replan_steps", type=int, default=5,
                   help="Pi0.5 action chunk replan interval")
    p.add_argument("--denoise_steps", type=int, default=10,
                   help="X-VLA flow matching denoising steps")
    p.add_argument("--domain_id", type=int, default=3,
                   help="X-VLA domain id for LIBERO")
    return p.parse_args()


class LatencyTracker:
    """Records per-step latency with CUDA synchronization."""

    def __init__(self, device):
        self.device = device
        self.latencies = []
        self._start = 0.0

    def start(self):
        torch.cuda.synchronize(self.device)
        self._start = time.perf_counter()

    def end(self):
        torch.cuda.synchronize(self.device)
        elapsed = (time.perf_counter() - self._start) * 1000.0
        self.latencies.append(elapsed)

    def get_stats(self):
        arr = np.array(self.latencies)
        return {
            "latency_mean_ms": float(np.mean(arr)),
            "latency_std_ms": float(np.std(arr)),
            "throughput_sps": float(1000.0 / np.mean(arr)) if np.mean(arr) > 0 else 0.0,
            "num_steps": len(arr),
        }


# ---------------------------------------------------------------------------
# OpenVLA
# ---------------------------------------------------------------------------

def _load_openvla(model_path, device):
    sys.path.insert(0, "/root/autodl-tmp/openvla_deps")
    sys.path.insert(0, "/root/autodl-tmp/openvla-repo/prismatic/extern")

    hf_dir = "/root/autodl-tmp/openvla-repo/prismatic/extern/hf"
    init_path = os.path.join(hf_dir, "__init__.py")
    if not os.path.exists(init_path):
        open(init_path, "w").close()

    from hf.configuration_prismatic import OpenVLAConfig
    from hf.modeling_prismatic import OpenVLAForActionPrediction
    from hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor
    from transformers import AutoTokenizer

    config = OpenVLAConfig.from_pretrained(model_path)
    vla = OpenVLAForActionPrediction.from_pretrained(
        model_path, config=config, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True,
    ).to(device)
    with open(os.path.join(model_path, "dataset_statistics.json")) as f:
        vla.norm_stats = json.load(f)
    vla.eval()

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    image_processor = PrismaticImageProcessor.from_pretrained(model_path)
    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)
    return vla, processor


def _install_openvla_pruning(vla, method, k_ratio):
    """Install pruning hook on OpenVLA projector. Returns hook handle or None."""
    if method == "baseline" or k_ratio >= 1.0:
        return None

    class _RandomHook:
        def __init__(self, k_ratio):
            self.k_ratio = k_ratio
            self.logged = False

        def __call__(self, module, input, output):
            B, N, D = output.shape
            keep = int(N * self.k_ratio)
            indices = torch.randperm(N)[:keep].sort().values.to(output.device)
            pruned = output[:, indices, :]
            if not self.logged:
                log.info("[Pruning] %d -> %d vision tokens (random, k=%.2f)", N, keep, self.k_ratio)
                self.logged = True
            return pruned

    class _L2NormHook:
        def __init__(self, k_ratio):
            self.k_ratio = k_ratio
            self.logged = False

        def __call__(self, module, input, output):
            B, N, D = output.shape
            keep = int(N * self.k_ratio)
            norms = torch.norm(output.float(), dim=-1)
            _, indices = torch.topk(norms, keep, dim=-1)
            indices = indices.sort(dim=-1).values
            pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))
            if not self.logged:
                log.info("[Pruning] %d -> %d vision tokens (l2norm, k=%.2f)", N, keep, self.k_ratio)
                self.logged = True
            return pruned

    class _AttentionHook:
        def __init__(self, k_ratio, vla):
            self.k_ratio = k_ratio
            self.vla = vla
            self.logged = False

        def __call__(self, module, input, output):
            import torch.nn.functional as F
            B, N, D = output.shape
            keep = max(1, int(N * self.k_ratio))
            if keep >= N:
                return output

            lm = self.vla.language_model.model
            position_ids = torch.arange(N, device=output.device).unsqueeze(0).expand(B, -1)
            hidden = output
            all_attn = []

            with torch.no_grad():
                for layer_idx in range(min(2, len(lm.layers))):
                    layer = lm.layers[layer_idx]
                    normed = layer.input_layernorm(hidden)
                    head_dim = layer.self_attn.head_dim
                    n_q_heads = layer.self_attn.num_heads
                    n_kv_heads = layer.self_attn.num_key_value_heads

                    q = layer.self_attn.q_proj(normed).view(B, N, n_q_heads, head_dim).transpose(1, 2)
                    k = layer.self_attn.k_proj(normed).view(B, N, n_kv_heads, head_dim).transpose(1, 2)
                    v = layer.self_attn.v_proj(normed).view(B, N, n_kv_heads, head_dim).transpose(1, 2)

                    cos, sin = layer.self_attn.rotary_emb(v, position_ids)
                    from transformers.models.llama.modeling_llama import rotate_half
                    q_embed = (q * cos) + (rotate_half(q) * sin)
                    k_embed = (k * cos) + (rotate_half(k) * sin)

                    if n_kv_heads != n_q_heads:
                        n_rep = n_q_heads // n_kv_heads
                        k_embed = k_embed.repeat_interleave(n_rep, dim=1)
                        v = v.repeat_interleave(n_rep, dim=1)

                    attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)
                    attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)
                    all_attn.append(attn_weights)

                    attn_out = torch.matmul(attn_weights.to(v.dtype), v)
                    attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)
                    attn_out = layer.self_attn.o_proj(attn_out)
                    hidden = hidden + attn_out
                    normed2 = layer.post_attention_layernorm(hidden)
                    mlp_out = layer.mlp(normed2)
                    hidden = hidden + mlp_out

            avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)
            importance = avg_attn.sum(dim=1)
            _, indices = torch.topk(importance, keep, dim=-1)
            indices = indices.sort(dim=-1).values
            pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))
            if not self.logged:
                log.info("[Pruning] %d -> %d vision tokens (attention, k=%.2f)", N, keep, self.k_ratio)
                self.logged = True
            return pruned

    hook_cls = {"random": _RandomHook, "l2norm": _L2NormHook, "attention": _AttentionHook}[method]
    if method == "attention":
        hook = hook_cls(k_ratio, vla)
    else:
        hook = hook_cls(k_ratio)
    return vla.projector.register_forward_hook(hook)


def _openvla_preprocess_image(obs, center_crop=True):
    img = obs["agentview_image"][::-1, ::-1]
    pil_img = Image.fromarray(img)
    buf = io.BytesIO()
    pil_img.save(buf, format="JPEG")
    buf.seek(0)
    pil_img = Image.open(buf).convert("RGB").resize((224, 224), Image.LANCZOS)
    if center_crop:
        w, h = pil_img.size
        new_w = int(w * math.sqrt(0.9))
        new_h = int(h * math.sqrt(0.9))
        left, top = (w - new_w) // 2, (h - new_h) // 2
        pil_img = pil_img.crop((left, top, left + new_w, top + new_h)).resize((w, h), Image.LANCZOS)
    return pil_img


def _openvla_get_action(vla, processor, image, task_label, unnorm_key, device):
    prompt = f"In: What action should the robot take to {task_label.lower()}?\nOut:"
    inputs = processor(prompt, image).to(device, dtype=torch.bfloat16)
    action = vla.predict_action(**inputs, unnorm_key=unnorm_key, do_sample=False)
    return action


def _normalize_and_invert_gripper(action):
    action[..., -1] = 2 * action[..., -1] - 1
    action[..., -1] = np.sign(action[..., -1])
    action[..., -1] *= -1.0
    return action


def profile_openvla(args, k_ratios):
    device = torch.device(f"cuda:{args.gpu}")
    model_path = args.model_path or "/root/autodl-tmp/openvla-libero-object"
    max_steps = SUITE_MAX_STEPS.get(args.suite, 280)

    log.info("Loading OpenVLA from %s ...", model_path)
    vla, processor = _load_openvla(model_path, device)

    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    task_suite = benchmark.get_benchmark_dict()[args.suite]()
    n_tasks = task_suite.n_tasks

    results = []
    for k_ratio in k_ratios:
        method = "baseline" if k_ratio >= 1.0 else args.method
        log.info("=== OpenVLA method=%s k_ratio=%.2f ===", method, k_ratio)

        hook_handle = _install_openvla_pruning(vla, method, k_ratio)

        tracker = LatencyTracker(device)
        global_step = 0

        torch.cuda.reset_peak_memory_stats(device)

        for task_id in range(n_tasks):
            task = task_suite.get_task(task_id)
            task_desc = task.language
            bddl = os.path.join(
                get_libero_path("bddl_files"), task.problem_folder, task.bddl_file
            )
            env = OffScreenRenderEnv(bddl_file_name=bddl, camera_heights=256, camera_widths=256)
            env.seed(args.seed)
            init_states = task_suite.get_task_init_states(task_id)

            eps_this_task = min(args.num_episodes, len(init_states))
            for ep in range(eps_this_task):
                env.reset()
                obs = env.set_init_state(init_states[ep])

                for _ in range(10):
                    obs, _, _, _ = env.step([0, 0, 0, 0, 0, 0, -1])

                for t in range(max_steps):
                    img = _openvla_preprocess_image(obs)

                    tracker.start()
                    action = _openvla_get_action(vla, processor, img, task_desc, args.unnorm_key, device)
                    tracker.end()

                    global_step += 1
                    action = _normalize_and_invert_gripper(action)
                    obs, reward, done, info = env.step(action.tolist())
                    if done:
                        break

            env.close()

        memory_peak_mb = torch.cuda.max_memory_allocated(device) / (1024 ** 2)

        # Discard warmup steps
        if len(tracker.latencies) > args.warmup_steps:
            tracker.latencies = tracker.latencies[args.warmup_steps:]

        stats = tracker.get_stats()
        row = {
            "model": "openvla",
            "method": method,
            "k_ratio": k_ratio,
            "suite": args.suite,
            "latency_mean_ms": round(stats["latency_mean_ms"], 2),
            "latency_std_ms": round(stats["latency_std_ms"], 2),
            "memory_peak_mb": round(memory_peak_mb, 1),
            "throughput_sps": round(stats["throughput_sps"], 2),
            "num_steps": stats["num_steps"],
        }
        results.append(row)
        log.info("Result: %s", row)

        if hook_handle is not None:
            hook_handle.remove()

    return results


# ---------------------------------------------------------------------------
# Pi0.5
# ---------------------------------------------------------------------------

def _pi05_prune_tokens_random(img_emb, keep_ratio):
    bsize, n_tokens, dim = img_emb.shape
    n_keep = max(1, int(n_tokens * keep_ratio))
    indices = torch.randperm(n_tokens)[:n_keep].sort().values.to(img_emb.device)
    return img_emb[:, indices, :], n_keep


def _pi05_prune_tokens_l2norm(img_emb, keep_ratio):
    bsize, n_tokens, dim = img_emb.shape
    n_keep = max(1, int(n_tokens * keep_ratio))
    norms = torch.norm(img_emb[0].float(), dim=-1)
    _, topk_idx = torch.topk(norms, n_keep)
    topk_idx = topk_idx.sort().values
    return img_emb[:, topk_idx, :], n_keep


def _load_pi05(model_path, device, method, keep_ratio):
    os.environ.setdefault("HF_HOME", "/root/autodl-tmp/.hf_cache")
    torch._dynamo.config.disable = True

    from lerobot.policies.pi05.modeling_pi05 import PI05Policy
    policy = PI05Policy.from_pretrained(model_path)

    paligemma_expert = policy.model.paligemma_with_expert

    def patched_embed_image(self, image):
        out_dtype = image.dtype
        if image.dtype != torch.float32:
            image = image.to(torch.float32)
        image_outputs = self.paligemma.model.vision_tower(image)
        selected_image_feature = image_outputs.last_hidden_state
        features = self.paligemma.model.multi_modal_projector(selected_image_feature)
        if features.dtype != out_dtype:
            features = features.to(out_dtype)
        return features

    paligemma_expert.embed_image = types.MethodType(patched_embed_image, paligemma_expert)
    policy = policy.to(device)
    policy.eval()

    N_PATCHES = (224 // 14) ** 2

    prune_fn = None
    if method == "random":
        prune_fn = _pi05_prune_tokens_random
    elif method == "l2norm":
        prune_fn = _pi05_prune_tokens_l2norm

    if prune_fn is not None and keep_ratio < 1.0:
        def pruned_embed_prefix(self_model, images, img_masks, tokens, masks):
            embs = []
            pad_masks_list = []
            att_masks = []
            for img, img_mask in zip(images, img_masks, strict=True):
                img_emb = self_model.paligemma_with_expert.embed_image(img)
                bsize, num_img_embs, dim = img_emb.shape
                img_emb, n_keep = prune_fn(img_emb, keep_ratio)
                embs.append(img_emb)
                pad_masks_list.append(img_mask[:, None].expand(bsize, n_keep))
                att_masks += [0] * n_keep
            lang_emb = self_model.paligemma_with_expert.embed_language_tokens(tokens)
            embs.append(lang_emb)
            pad_masks_list.append(masks)
            att_masks += [0] * lang_emb.shape[1]
            embs = torch.cat(embs, dim=1)
            pad_masks_cat = torch.cat(pad_masks_list, dim=1)
            att_masks_t = torch.tensor(att_masks, dtype=torch.bool, device=pad_masks_cat.device)
            att_masks_t = att_masks_t[None, :].expand(bsize, len(att_masks))
            return embs, pad_masks_cat, att_masks_t

        policy.model.embed_prefix = types.MethodType(pruned_embed_prefix, policy.model)
        log.info("Pi0.5 pruning installed: method=%s keep_ratio=%.2f", method, keep_ratio)

    from lerobot.policies.factory import make_pre_post_processors
    preprocess, postprocess = make_pre_post_processors(
        policy.config, model_path,
        preprocessor_overrides={"device_processor": {"device": str(device)}},
    )
    return policy, preprocess, postprocess


def _quat_to_axisangle(quat):
    q = quat.copy()
    q[3] = np.clip(q[3], -1.0, 1.0)
    den = np.sqrt(1.0 - q[3] ** 2)
    if abs(den) < 1e-8:
        return np.zeros(3, dtype=np.float32)
    return (q[:3] * 2.0 * np.arccos(q[3]) / den).astype(np.float32)


def profile_pi05(args, k_ratios):
    device = torch.device(f"cuda:{args.gpu}")
    model_path = args.model_path or "/root/autodl-tmp/pi05_libero_finetuned"
    max_steps = SUITE_MAX_STEPS.get(args.suite, 280)

    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    task_suite = benchmark.get_benchmark_dict()[args.suite]()
    n_tasks = task_suite.n_tasks

    results = []
    for k_ratio in k_ratios:
        method = "baseline" if k_ratio >= 1.0 else args.method
        log.info("=== Pi0.5 method=%s k_ratio=%.2f ===", method, k_ratio)

        policy, preprocess, postprocess = _load_pi05(model_path, device, method, k_ratio)

        tracker = LatencyTracker(device)
        global_step = 0

        torch.cuda.reset_peak_memory_stats(device)

        for task_id in range(n_tasks):
            task = task_suite.get_task(task_id)
            task_desc = task.language
            init_states = task_suite.get_task_init_states(task_id)
            bddl = str(Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file)
            env = OffScreenRenderEnv(bddl_file_name=bddl, camera_heights=256, camera_widths=256)
            env.seed(args.seed)

            eps_this_task = min(args.num_episodes, len(init_states))
            for ep in range(eps_this_task):
                env.reset()
                obs = env.set_init_state(init_states[ep])
                for _ in range(10):
                    obs, _, _, _ = env.step([0.0] * 6 + [-1.0])

                action_queue = deque()
                for t in range(max_steps):
                    if not action_queue:
                        base_img = obs["agentview_image"]
                        wrist_img = obs["robot0_eye_in_hand_image"]
                        base_t = torch.from_numpy(base_img.copy()).permute(2, 0, 1).float() / 255.0
                        base_t = torch.flip(base_t, dims=[1, 2])
                        wrist_t = torch.from_numpy(wrist_img.copy()).permute(2, 0, 1).float() / 255.0
                        wrist_t = torch.flip(wrist_t, dims=[1, 2])

                        eef_pos = obs["robot0_eef_pos"]
                        eef_quat = obs["robot0_eef_quat"]
                        gripper_qpos = obs["robot0_gripper_qpos"]
                        state = np.concatenate([
                            eef_pos, _quat_to_axisangle(eef_quat), gripper_qpos
                        ]).astype(np.float32)
                        state_t = torch.from_numpy(state)

                        raw_obs = {
                            "observation.images.image": base_t,
                            "observation.images.image2": wrist_t,
                            "observation.state": state_t,
                            "task": task_desc,
                        }
                        batch = preprocess(raw_obs)

                        tracker.start()
                        with torch.no_grad():
                            actions = policy.predict_action_chunk(batch)
                        tracker.end()

                        actions_unnorm = postprocess(actions)
                        action_np = actions_unnorm[0].cpu().numpy()
                        for a in action_np[:args.replan_steps]:
                            action_queue.append(a[:7])

                        global_step += 1

                    action = action_queue.popleft()
                    obs, reward, done, info = env.step(action.tolist())
                    if done:
                        break

            env.close()

        memory_peak_mb = torch.cuda.max_memory_allocated(device) / (1024 ** 2)

        if len(tracker.latencies) > args.warmup_steps:
            tracker.latencies = tracker.latencies[args.warmup_steps:]

        stats = tracker.get_stats()
        row = {
            "model": "pi05",
            "method": method,
            "k_ratio": k_ratio,
            "suite": args.suite,
            "latency_mean_ms": round(stats["latency_mean_ms"], 2),
            "latency_std_ms": round(stats["latency_std_ms"], 2),
            "memory_peak_mb": round(memory_peak_mb, 1),
            "throughput_sps": round(stats["throughput_sps"], 2),
            "num_steps": stats["num_steps"],
        }
        results.append(row)
        log.info("Result: %s", row)

        # Free model for next k_ratio (Pi0.5 patching is not easily reversible)
        del policy
        torch.cuda.empty_cache()

    return results


# ---------------------------------------------------------------------------
# X-VLA
# ---------------------------------------------------------------------------

EPS_XVLA = 1e-6


def _load_xvla(model_path, device):
    model_dir = str(Path(model_path).resolve())
    sys.path.insert(0, model_dir)

    from configuration_xvla import XVLAConfig
    from modeling_xvla import XVLA
    from processing_xvla import XVLAProcessor
    from safetensors.torch import load_file

    config = XVLAConfig.from_pretrained(model_dir)
    model = XVLA(config)

    safetensors_path = Path(model_dir) / "model.safetensors"
    if safetensors_path.exists():
        state_dict = load_file(str(safetensors_path))
    else:
        state_dict = torch.load(Path(model_dir) / "pytorch_model.bin", map_location="cpu")
    model.load_state_dict(state_dict, strict=False)
    model = model.to(device).eval()

    processor = XVLAProcessor.from_pretrained(model_dir, trust_remote_code=True)
    if processor.tokenizer.pad_token is None:
        processor.tokenizer.pad_token = "<pad>"
        processor.tokenizer.pad_token_id = 1

    return model, processor


def _install_xvla_pruning(model, keep_ratio, mode):
    from functools import wraps

    if keep_ratio >= 1.0:
        return

    original_encode = model.vlm._encode_image

    @wraps(original_encode)
    def pruned_encode(pixel_values):
        features = original_encode(pixel_values)
        N = features.shape[1]
        k = max(1, int(keep_ratio * N))
        if k >= N:
            return features
        if mode == "l2norm":
            norms = features.norm(dim=-1)
            _, indices = norms.topk(k, dim=-1)
        elif mode == "random":
            indices = torch.stack([
                torch.randperm(N)[:k] for _ in range(features.shape[0])
            ], dim=0)
        else:
            return features
        indices_sorted = indices.sort(dim=-1).values.to(features.device)
        pruned = features.gather(
            1, indices_sorted.unsqueeze(-1).expand(-1, -1, features.shape[-1])
        )
        return pruned

    model.vlm._encode_image = pruned_encode
    model._original_encode_image = original_encode
    log.info("X-VLA pruning installed: keep_ratio=%.2f mode=%s", keep_ratio, mode)


def _xvla_restore_encode(model):
    if hasattr(model, "_original_encode_image"):
        model.vlm._encode_image = model._original_encode_image
        del model._original_encode_image


def _xvla_mat_to_rot6d(R):
    return np.concatenate([R[:3, 0], R[:3, 1]], axis=-1).astype(np.float32)


def _xvla_rot6d_to_axis_angle(r6d):
    import robosuite.utils.transform_utils as T
    single = r6d.ndim == 1
    if single:
        r6d = r6d[None, :]
    a1 = r6d[:, 0:3]
    a2 = r6d[:, 3:6]
    b1 = a1 / (np.linalg.norm(a1, axis=-1, keepdims=True) + EPS_XVLA)
    dot_prod = np.sum(b1 * a2, axis=-1, keepdims=True)
    b2_orth = a2 - dot_prod * b1
    b2 = b2_orth / (np.linalg.norm(b2_orth, axis=-1, keepdims=True) + EPS_XVLA)
    b3 = np.cross(b1, b2, axis=-1)
    R = np.stack([b1, b2, b3], axis=-1)
    results = []
    for i in range(R.shape[0]):
        quat = T.mat2quat(R[i])
        aa = T.quat2axisangle(quat)
        results.append(aa)
    result = np.stack(results, axis=0)
    return result[0] if single else result


def _xvla_extract_proprio_20d(env):
    robot = env.env.robots[0]
    ee_pos = robot.controller.ee_pos.copy()
    ee_ori_mat = robot.controller.ee_ori_mat.copy()
    rot6d = _xvla_mat_to_rot6d(ee_ori_mat)
    arm1 = np.concatenate([ee_pos, rot6d, np.array([0.0], dtype=np.float32)])
    arm2 = np.zeros(10, dtype=np.float32)
    return np.concatenate([arm1, arm2])


def _xvla_get_images_from_obs(obs):
    images = []
    for key in ["agentview_image", "robot0_eye_in_hand_image"]:
        if key in obs:
            img = obs[key]
            img = img[::-1, ::-1]
            pil = Image.fromarray(img).convert("RGB")
            images.append(pil)
    return images


def _xvla_predict_actions(model, processor, images, task_desc, proprio_20d,
                          domain_id, device, denoise_steps):
    inputs = processor(
        images=images,
        text=task_desc,
        return_tensors="pt",
        padding=True,
    )
    inputs = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

    proprio_t = torch.tensor(proprio_20d, dtype=torch.float32, device=device).unsqueeze(0)
    domain_t = torch.tensor([domain_id], dtype=torch.long, device=device)

    with torch.no_grad():
        actions = model.predict_action(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            image_mask=inputs["image_mask"],
            proprio=proprio_t,
            domain_id=domain_t,
            steps=denoise_steps,
        )
    return actions.squeeze(0).float().cpu().numpy()


def _xvla_decode_action_20d_to_7d(raw_actions):
    results = []
    for act in raw_actions:
        pos = act[:3]
        rot6d = act[3:9]
        grip = act[9]
        aa = _xvla_rot6d_to_axis_angle(rot6d)
        action_7d = np.concatenate([pos, aa, [grip]])
        results.append(action_7d.astype(np.float32))
    return np.array(results)


def profile_xvla(args, k_ratios):
    device = torch.device(f"cuda:{args.gpu}")
    model_path = args.model_path or "/root/autodl-tmp/X-VLA-Libero"
    max_steps = XVLA_SUITE_MAX_STEPS.get(args.suite, 800)

    log.info("Loading X-VLA from %s ...", model_path)
    model, processor = _load_xvla(model_path, device)

    num_actions_per_chunk = model.num_actions

    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    task_suite = benchmark.get_benchmark(args.suite)()
    n_tasks = task_suite.n_tasks

    results = []
    for k_ratio in k_ratios:
        method = "baseline" if k_ratio >= 1.0 else args.method
        log.info("=== X-VLA method=%s k_ratio=%.2f ===", method, k_ratio)

        _xvla_restore_encode(model)
        _install_xvla_pruning(model, k_ratio, method)

        tracker = LatencyTracker(device)
        global_step = 0

        torch.cuda.reset_peak_memory_stats(device)

        for task_id in range(n_tasks):
            task = task_suite.get_task(task_id)
            task_desc = task.language
            task_bddl = os.path.join(
                get_libero_path("bddl_files"), task.problem_folder, task.bddl_file
            )
            init_states = task_suite.get_task_init_states(task_id)

            eps_this_task = min(args.num_episodes, len(init_states))
            for ep in range(eps_this_task):
                env = OffScreenRenderEnv(
                    bddl_file_name=task_bddl, camera_heights=256, camera_widths=256,
                )
                env.seed(args.seed + ep + 100)
                obs = env.reset()
                init_state_id = ep % init_states.shape[0]
                obs = env.set_init_state(init_states[init_state_id])

                for _ in range(10):
                    obs, _, _, _ = env.step(np.array([0.0] * 6 + [-1.0], dtype=np.float32))

                for robot in env.env.robots:
                    robot.controller.use_delta = False

                action_queue = []
                proprio_state = None

                for step_idx in range(max_steps):
                    if not action_queue:
                        proprio_20d = _xvla_extract_proprio_20d(env)
                        if proprio_state is not None:
                            proprio_20d[:9] = proprio_state[:9]

                        images = _xvla_get_images_from_obs(obs)

                        tracker.start()
                        raw_actions = _xvla_predict_actions(
                            model, processor, images, task_desc, proprio_20d,
                            args.domain_id, device, args.denoise_steps,
                        )
                        tracker.end()

                        proprio_state = proprio_20d.copy()
                        proprio_state[:9] = raw_actions[-1, :9].copy()

                        actions_7d = _xvla_decode_action_20d_to_7d(raw_actions)
                        action_queue = list(actions_7d)
                        global_step += 1

                    action = action_queue.pop(0)
                    obs, reward, done, info = env.step(action)

                    if done or reward > 0.5:
                        break

                env.close()

        memory_peak_mb = torch.cuda.max_memory_allocated(device) / (1024 ** 2)

        if len(tracker.latencies) > args.warmup_steps:
            tracker.latencies = tracker.latencies[args.warmup_steps:]

        stats = tracker.get_stats()
        row = {
            "model": "xvla",
            "method": method,
            "k_ratio": k_ratio,
            "suite": args.suite,
            "latency_mean_ms": round(stats["latency_mean_ms"], 2),
            "latency_std_ms": round(stats["latency_std_ms"], 2),
            "memory_peak_mb": round(memory_peak_mb, 1),
            "throughput_sps": round(stats["throughput_sps"], 2),
            "num_steps": stats["num_steps"],
        }
        results.append(row)
        log.info("Result: %s", row)

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

PROFILE_FN = {
    "openvla": profile_openvla,
    "pi05": profile_pi05,
    "xvla": profile_xvla,
}


def main():
    args = parse_args()
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    k_ratios = [float(x) for x in args.k_ratios.split(",")]
    log.info("Model: %s | Method: %s | k_ratios: %s | Suite: %s | Episodes: %d",
             args.model, args.method, k_ratios, args.suite, args.num_episodes)

    profile_fn = PROFILE_FN[args.model]
    results = profile_fn(args, k_ratios)

    fieldnames = [
        "model", "method", "k_ratio", "suite",
        "latency_mean_ms", "latency_std_ms", "memory_peak_mb",
        "throughput_sps", "num_steps",
    ]
    output_path = args.output
    write_header = not os.path.exists(output_path)
    with open(output_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        for row in results:
            writer.writerow(row)

    log.info("Results appended to %s (%d rows)", output_path, len(results))

    for row in results:
        log.info("  %s %s k=%.2f: %.1f±%.1f ms, %.0f MB, %.1f sps (%d steps)",
                 row["model"], row["method"], row["k_ratio"],
                 row["latency_mean_ms"], row["latency_std_ms"],
                 row["memory_peak_mb"], row["throughput_sps"], row["num_steps"])


if __name__ == "__main__":
    main()

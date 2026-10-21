#!/usr/bin/env python
"""Position-preserving ablation: token pruning vs zero-masking on π0.5.

Ablation question: does performance drop from pruning come from information loss
or positional distortion?

  - pruning (existing): physically remove low-importance tokens → sequence shorter,
    positions shift
  - zero_mask (new): keep all tokens at original positions, but set values of
    low-importance tokens to zero → sequence length unchanged, positions preserved

Experimental groups (libero_object, k=0.9):
  1. pruning   + random  → 9.0%  (existing data)
  2. zero_mask + random  → ?     (this script)
  3. pruning   + l2norm  → 98.2% (existing data)
  4. zero_mask + l2norm  → ?     (this script)

Interpretation:
  - zero_mask ≈ pruning → information loss is the main cause
  - zero_mask >> pruning → positional distortion is the main cause

Usage:
    python eval_pi05_zeromask_ablation.py --prune_mode zero_mask_random --keep_ratio 0.9
    python eval_pi05_zeromask_ablation.py --prune_mode zero_mask_l2norm --keep_ratio 0.9
    python eval_pi05_zeromask_ablation.py --prune_mode random --keep_ratio 0.9
    python eval_pi05_zeromask_ablation.py --prune_mode l2norm --keep_ratio 0.9
    python eval_pi05_zeromask_ablation.py --prune_mode none
"""

import argparse
import json
import os
import sys
import time as time_mod
import types
import logging
from pathlib import Path
from collections import deque

os.environ["MUJOCO_GL"] = "egl"
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_TOKEN"] = "[REDACTED_HF_TOKEN]"

import numpy as np
import torch
import torch._dynamo; torch._dynamo.config.disable = True
from safetensors.torch import load_file

logging.basicConfig(level=logging.INFO, force=True, format="%(asctime)s %(message)s")
log = logging.getLogger(__name__)

SUITE_CONFIG = {
    "libero_object":  {"name": "libero_object",  "max_steps": 280},
    "libero_spatial":  {"name": "libero_spatial",  "max_steps": 400},
    "libero_goal":     {"name": "libero_goal",     "max_steps": 400},
    "libero_10":       {"name": "libero_10",       "max_steps": 520},
}

PRUNE_MODES = ["none", "random", "l2norm", "zero_mask_random", "zero_mask_l2norm"]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model_path", type=str, default="/root/autodl-tmp/pi05_libero_finetuned")
    p.add_argument("--suite", type=str, default="libero_object", choices=list(SUITE_CONFIG))
    p.add_argument("--prune_mode", type=str, default="none", choices=PRUNE_MODES)
    p.add_argument("--keep_ratio", type=float, default=1.0)
    p.add_argument("--n_episodes", type=int, default=50)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--replan_steps", type=int, default=5)
    p.add_argument("--output_dir", type=str,
                   default="/root/autodl-tmp/importance_margin_vla_compress/eval_results")
    return p.parse_args()


# --------------- Token pruning (physical removal) ---------------

def prune_tokens_random(img_emb, keep_ratio):
    bsize, n_tokens, dim = img_emb.shape
    n_keep = max(1, int(n_tokens * keep_ratio))
    indices = torch.randperm(n_tokens)[:n_keep].sort().values.to(img_emb.device)
    if not hasattr(prune_tokens_random, "_logged"):
        print(f"[PRUNE-DIAG] random: n_keep={n_keep}/{n_tokens}, first_indices={indices[:5].tolist()}")
        prune_tokens_random._logged = True
    return img_emb[:, indices, :], n_keep


def prune_tokens_l2norm(img_emb, keep_ratio):
    bsize, n_tokens, dim = img_emb.shape
    n_keep = max(1, int(n_tokens * keep_ratio))
    norms = torch.norm(img_emb[0].float(), dim=-1)
    _, topk_idx = torch.topk(norms, n_keep)
    topk_idx = topk_idx.sort().values
    if not hasattr(prune_tokens_l2norm, "_logged"):
        print(f"[PRUNE-DIAG] l2norm: n_keep={n_keep}/{n_tokens}, first_indices={topk_idx[:5].tolist()}")
        prune_tokens_l2norm._logged = True
    return img_emb[:, topk_idx, :], n_keep


# --------------- Zero-masking (position-preserving) ---------------

def zeromask_tokens_random(img_emb, keep_ratio):
    """Zero out randomly selected tokens while preserving all positions."""
    bsize, n_tokens, dim = img_emb.shape
    n_keep = max(1, int(n_tokens * keep_ratio))
    keep_indices = torch.randperm(n_tokens)[:n_keep].sort().values.to(img_emb.device)
    mask = torch.zeros(n_tokens, dtype=torch.bool, device=img_emb.device)
    mask[keep_indices] = True
    out = img_emb.clone()
    out[:, ~mask, :] = 0.0
    if not hasattr(zeromask_tokens_random, "_logged"):
        n_zeroed = n_tokens - n_keep
        print(f"[ZEROMASK-DIAG] random: keep={n_keep}/{n_tokens}, zeroed={n_zeroed}, "
              f"shape_unchanged={out.shape}")
        zeromask_tokens_random._logged = True
    return out, n_tokens  # sequence length unchanged


def zeromask_tokens_l2norm(img_emb, keep_ratio):
    """Zero out low-L2-norm tokens while preserving all positions."""
    bsize, n_tokens, dim = img_emb.shape
    n_keep = max(1, int(n_tokens * keep_ratio))
    norms = torch.norm(img_emb[0].float(), dim=-1)
    _, topk_idx = torch.topk(norms, n_keep)
    mask = torch.zeros(n_tokens, dtype=torch.bool, device=img_emb.device)
    mask[topk_idx] = True
    out = img_emb.clone()
    out[:, ~mask, :] = 0.0
    if not hasattr(zeromask_tokens_l2norm, "_logged"):
        n_zeroed = n_tokens - n_keep
        print(f"[ZEROMASK-DIAG] l2norm: keep={n_keep}/{n_tokens}, zeroed={n_zeroed}, "
              f"shape_unchanged={out.shape}")
        zeromask_tokens_l2norm._logged = True
    return out, n_tokens  # sequence length unchanged


def get_prune_fn(prune_mode):
    return {
        "random": prune_tokens_random,
        "l2norm": prune_tokens_l2norm,
        "zero_mask_random": zeromask_tokens_random,
        "zero_mask_l2norm": zeromask_tokens_l2norm,
    }.get(prune_mode, None)


def main():
    args = parse_args()
    DEVICE = "cuda:0"
    suite_cfg = SUITE_CONFIG[args.suite]

    log.info(f"Config: suite={args.suite}, prune={args.prune_mode}, keep={args.keep_ratio}, "
             f"eps={args.n_episodes}, gpu={args.gpu}")

    log.info(f"Loading π0.5 from {args.model_path} ...")
    from lerobot.policies.pi05.modeling_pi05 import PI05Policy
    policy = PI05Policy.from_pretrained(args.model_path)

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
    log.info("Patched embed_image")

    policy = policy.to(DEVICE)
    policy.eval()
    log.info(f"Model: {sum(p.numel() for p in policy.parameters())/1e6:.1f}M params")

    N_PATCHES = (224 // 14) ** 2
    log.info(f"Vision tokens: {N_PATCHES}/image, 3 slots -> {N_PATCHES*3} total")

    prune_fn = get_prune_fn(args.prune_mode)
    is_zeromask = args.prune_mode.startswith("zero_mask")

    if prune_fn is not None:
        def pruned_embed_prefix(self_model, images, img_masks, tokens, masks):
            embs = []
            pad_masks_list = []
            att_masks = []

            for img, img_mask in zip(images, img_masks, strict=True):
                img_emb = self_model.paligemma_with_expert.embed_image(img)
                bsize, num_img_embs, dim = img_emb.shape

                img_emb, n_out = prune_fn(img_emb, args.keep_ratio)

                embs.append(img_emb)
                pad_masks_list.append(img_mask[:, None].expand(bsize, n_out))
                att_masks += [0] * n_out

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
        n_keep = max(1, int(N_PATCHES * args.keep_ratio))
        mode_label = "ZERO-MASK" if is_zeromask else "PRUNE"
        log.info(f"{mode_label}: {args.prune_mode}, keep {n_keep}/{N_PATCHES} tokens/image "
                 f"(seq_len={'unchanged' if is_zeromask else f'{n_keep*3} total'})")

    from lerobot.policies.factory import make_pre_post_processors
    preprocess, postprocess = make_pre_post_processors(
        policy.config,
        args.model_path,
        preprocessor_overrides={"device_processor": {"device": str(DEVICE)}},
    )
    log.info("Preprocessor/postprocessor loaded")

    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv

    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    task_suite = benchmark.get_benchmark_dict()[suite_cfg["name"]]()
    n_tasks = task_suite.n_tasks
    max_steps = suite_cfg["max_steps"]
    log.info(f"Suite: {args.suite}, {n_tasks} tasks, max_steps={max_steps}")

    def quat_to_axisangle(quat):
        q = quat.copy()
        if q[3] > 1.0: q[3] = 1.0
        elif q[3] < -1.0: q[3] = -1.0
        den = np.sqrt(1.0 - q[3]**2)
        if abs(den) < 1e-8:
            return np.zeros(3, dtype=np.float32)
        return (q[:3] * 2.0 * np.arccos(q[3]) / den).astype(np.float32)

    total_success = 0
    total_episodes = 0
    results = {
        "config": {
            "model": "pi05", "ckpt": args.model_path, "suite": args.suite,
            "prune_mode": args.prune_mode, "keep_ratio": args.keep_ratio,
            "n_eps_per_task": args.n_episodes, "seed": args.seed,
            "vision_tokens_per_image": N_PATCHES,
            "total_vision_tokens": N_PATCHES * 3,
            "n_keep_per_image": max(1, int(N_PATCHES * args.keep_ratio)) if prune_fn else N_PATCHES,
            "is_zeromask": is_zeromask,
            "ablation": "position-preserving" if is_zeromask else "token-pruning",
        },
        "per_task": {},
    }

    t_start = time_mod.time()
    for task_id in range(n_tasks):
        task = task_suite.get_task(task_id)
        init_states = task_suite.get_task_init_states(task_id)
        bddl = Path(get_libero_path("bddl_files")) / task.problem_folder / task.bddl_file
        env = OffScreenRenderEnv(bddl_file_name=str(bddl),
                                 camera_heights=256, camera_widths=256)
        env.seed(args.seed)
        task_desc = task.language
        task_successes = 0

        for ep in range(args.n_episodes):
            env.reset()
            obs = env.set_init_state(init_states[ep])
            for _ in range(10):
                obs, _, _, _ = env.step([0.0]*6 + [-1.0])

            done = False
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
                        eef_pos, quat_to_axisangle(eef_quat), gripper_qpos
                    ]).astype(np.float32)
                    state_t = torch.from_numpy(state)

                    raw_obs = {
                        "observation.images.image": base_t,
                        "observation.images.image2": wrist_t,
                        "observation.state": state_t,
                        "task": task_desc,
                    }
                    batch = preprocess(raw_obs)

                    with torch.no_grad():
                        actions = policy.predict_action_chunk(batch)

                    actions_unnorm = postprocess(actions)
                    action_np = actions_unnorm[0].cpu().numpy()

                    for a in action_np[:args.replan_steps]:
                        action_queue.append(a[:7])

                action = action_queue.popleft()
                obs, reward, done, info = env.step(action.tolist())
                if done:
                    task_successes += 1
                    total_success += 1
                    break

            total_episodes += 1

            if (ep + 1) % 10 == 0:
                log.info(f"  T{task_id} [{task_desc[:40]}] ep={ep+1}: "
                         f"{task_successes}/{ep+1}={task_successes/(ep+1)*100:.0f}%")

        task_sr = task_successes / args.n_episodes
        results["per_task"][task_desc] = {"id": task_id, "sr": task_sr, "n": task_successes}
        elapsed = time_mod.time() - t_start
        log.info(f"Task {task_id}: SR={task_sr*100:.1f}% | "
                 f"Total: {total_success}/{total_episodes}={total_success/total_episodes*100:.1f}% | "
                 f"Time: {elapsed/60:.1f}min")
        env.close()

    results["overall_sr"] = total_success / total_episodes
    results["total_successes"] = total_success
    results["total_episodes"] = total_episodes
    results["elapsed_min"] = (time_mod.time() - t_start) / 60

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    if args.prune_mode == "none":
        fname = f"pi05_baseline_{args.suite}_seed{args.seed}.json"
    else:
        fname = f"pi05_{args.prune_mode}_k{args.keep_ratio:.2f}_{args.suite}_seed{args.seed}.json"
    out_path = out_dir / fname
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    log.info(f"\n{'='*60}")
    log.info(f"RESULT: {args.suite} mode={args.prune_mode} keep={args.keep_ratio} "
             f"SR={results['overall_sr']*100:.1f}%")
    log.info(f"Saved: {out_path}")
    log.info(f"{'='*60}")


if __name__ == "__main__":
    main()

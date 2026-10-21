#!/usr/bin/env python
"""Pi0.5 LIBERO eval with vision token pruning (random / l2norm / none).

Usage:
    python eval_pi05_pruning_libero.py --suite libero_object --prune_mode none
    python eval_pi05_pruning_libero.py --suite libero_object --prune_mode random --keep_ratio 0.5
    python eval_pi05_pruning_libero.py --suite libero_spatial --prune_mode l2norm --keep_ratio 0.7
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

_episode_mask_cache = {}

SUITE_CONFIG = {
    "libero_object":  {"name": "libero_object",  "max_steps": 280},
    "libero_spatial":  {"name": "libero_spatial",  "max_steps": 280},
    "libero_goal":     {"name": "libero_goal",     "max_steps": 300},
    "libero_10":       {"name": "libero_10",       "max_steps": 520},
}


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model_path", type=str, default="/root/autodl-tmp/pi05_libero_finetuned")
    p.add_argument("--suite", type=str, default="libero_object", choices=list(SUITE_CONFIG))
    p.add_argument("--prune_mode", type=str, default="none", choices=["none", "random", "l2norm", "attention", "zero_mask_random", "zero_mask_l2norm"])
    p.add_argument("--keep_ratio", type=float, default=1.0)
    p.add_argument("--n_episodes", type=int, default=50)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--replan_steps", type=int, default=5)
    p.add_argument("--output_dir", type=str,
                   default="/root/autodl-tmp/importance_margin_vla_compress/eval_results")
    p.add_argument("--fixed_mask", action="store_true")
    return p.parse_args()


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
        print(f"[PRUNE-DIAG] l2norm: n_keep={n_keep}/{n_tokens}, first_indices={topk_idx.sort().values[:5].tolist()}")
        prune_tokens_l2norm._logged = True
    return img_emb[:, topk_idx, :], n_keep


def zero_mask_tokens_random(img_emb, keep_ratio):
    """Zero out random tokens instead of removing — isolates information loss from position shift."""
    bsize, n_tokens, dim = img_emb.shape
    n_keep = max(1, int(n_tokens * keep_ratio))
    indices_keep = torch.randperm(n_tokens)[:n_keep].sort().values.to(img_emb.device)
    mask = torch.zeros(n_tokens, device=img_emb.device)
    mask[indices_keep] = 1.0
    result = img_emb * mask[None, :, None]
    if not hasattr(zero_mask_tokens_random, "_logged"):
        print(f"[ZEROMASK-DIAG] random: n_keep={n_keep}/{n_tokens}, n_zeroed={n_tokens - n_keep}")
        zero_mask_tokens_random._logged = True
    return result, n_tokens


def zero_mask_tokens_l2norm(img_emb, keep_ratio):
    """Zero out low-L2-norm tokens instead of removing — isolates information loss from position shift."""
    bsize, n_tokens, dim = img_emb.shape
    n_keep = max(1, int(n_tokens * keep_ratio))
    norms = torch.norm(img_emb[0].float(), dim=-1)
    _, topk_idx = torch.topk(norms, n_keep)
    mask = torch.zeros(n_tokens, device=img_emb.device)
    mask[topk_idx] = 1.0
    result = img_emb * mask[None, :, None]
    if not hasattr(zero_mask_tokens_l2norm, "_logged"):
        n_zeroed = n_tokens - n_keep
        zeroed_norms = norms[mask == 0]
        print(f"[ZEROMASK-DIAG] l2norm: n_keep={n_keep}/{n_tokens}, n_zeroed={n_zeroed}, "
              f"zeroed_norm_range=[{zeroed_norms.min():.3f}, {zeroed_norms.max():.3f}]")
        zero_mask_tokens_l2norm._logged = True
    return result, n_tokens


def compute_attention_importance_probe(img_embs, lang_emb, lm, n_probe_layers=2):
    """Run first n_probe_layers of the LLM to get attention-based importance for vision tokens.

    Importance = avg attention from language tokens -> each vision token,
    averaged across probe layers and all heads.
    """
    import torch.nn.functional as F
    from transformers.models.gemma import modeling_gemma as _gemma

    all_vis = torch.cat(img_embs, dim=1)
    total_vis = all_vis.shape[1]
    full_embs = torch.cat([all_vis, lang_emb], dim=1)
    B, S, D = full_embs.shape

    position_ids = torch.arange(S, device=full_embs.device).unsqueeze(0).expand(B, -1)
    _model_dtype = lm.layers[0].self_attn.q_proj.weight.dtype
    hidden = full_embs.to(_model_dtype)
    all_attn = []

    with torch.no_grad():
        for layer_idx in range(min(n_probe_layers, len(lm.layers))):
            layer = lm.layers[layer_idx]
            normed = layer.input_layernorm(hidden)
            if isinstance(normed, tuple):
                normed = normed[0]

            head_dim = layer.self_attn.head_dim
            q = layer.self_attn.q_proj(normed)
            k = layer.self_attn.k_proj(normed)
            v = layer.self_attn.v_proj(normed)

            n_q_heads = q.shape[-1] // head_dim
            n_kv_heads = k.shape[-1] // head_dim

            q = q.view(B, S, n_q_heads, head_dim).transpose(1, 2)
            k = k.view(B, S, n_kv_heads, head_dim).transpose(1, 2)
            v = v.view(B, S, n_kv_heads, head_dim).transpose(1, 2)

            cos, sin = lm.rotary_emb(v, position_ids)
            q, k = _gemma.apply_rotary_pos_emb(q, k, cos, sin, unsqueeze_dim=1)

            if n_kv_heads != n_q_heads:
                n_rep = n_q_heads // n_kv_heads
                k = k.repeat_interleave(n_rep, dim=1)
                v = v.repeat_interleave(n_rep, dim=1)

            scaling = layer.self_attn.scaling
            attn_weights = torch.matmul(q, k.transpose(-2, -1)) * scaling
            attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)
            all_attn.append(attn_weights)

            attn_out = torch.matmul(attn_weights.to(v.dtype), v)
            attn_out = attn_out.transpose(1, 2).reshape(B, S, n_q_heads * head_dim)
            attn_out = layer.self_attn.o_proj(attn_out)
            hidden = hidden + attn_out

            normed2 = layer.post_attention_layernorm(hidden)
            if isinstance(normed2, tuple):
                normed2 = normed2[0]
            normed2 = normed2.to(_model_dtype)
            mlp_out = layer.mlp(normed2)
            hidden = hidden + mlp_out

    avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, S, S]
    lang_to_vis = avg_attn[:, total_vis:, :total_vis]  # [B, L, V]
    vis_importance = lang_to_vis.mean(dim=1)  # [B, V]
    return vis_importance


def main():
    args = parse_args()
    DEVICE = f"cuda:{args.gpu}"
    suite_cfg = SUITE_CONFIG[args.suite]

    log.info(f"Config: suite={args.suite}, prune={args.prune_mode}, keep={args.keep_ratio}, "
             f"eps={args.n_episodes}, gpu={args.gpu}")

    log.info(f"Loading pi0.5 from {args.model_path} ...")
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

    prune_fn = None
    if args.prune_mode == "random":
        prune_fn = prune_tokens_random
    elif args.prune_mode == "l2norm":
        prune_fn = prune_tokens_l2norm
    elif args.prune_mode == "zero_mask_random":
        prune_fn = zero_mask_tokens_random
    elif args.prune_mode == "zero_mask_l2norm":
        prune_fn = zero_mask_tokens_l2norm

    # Always override embed_prefix to avoid double lang_emb scaling.
    # GemmaTextScaledWordEmbedding already applies * sqrt(hidden_size) in embed_tokens();
    # the default PI05Pytorch.embed_prefix applies it again, breaking the model.
    def fixed_embed_prefix(self_model, images, img_masks, tokens, masks):
        embs = []
        pad_masks_list = []
        att_masks = []

        for img, img_mask in zip(images, img_masks, strict=True):
            img_emb = self_model.paligemma_with_expert.embed_image(img)
            bsize, num_img_embs, dim = img_emb.shape

            if prune_fn is not None and args.prune_mode != "attention":
                img_emb, num_img_embs = prune_fn(img_emb, args.keep_ratio)

            embs.append(img_emb)
            pad_masks_list.append(img_mask[:, None].expand(bsize, num_img_embs))
            att_masks += [0] * num_img_embs

        lang_emb = self_model.paligemma_with_expert.embed_language_tokens(tokens)
        embs.append(lang_emb)
        pad_masks_list.append(masks)
        att_masks += [0] * lang_emb.shape[1]

        embs = torch.cat(embs, dim=1)
        pad_masks_cat = torch.cat(pad_masks_list, dim=1)
        att_masks_t = torch.tensor(att_masks, dtype=torch.bool, device=pad_masks_cat.device)
        att_masks_t = att_masks_t[None, :].expand(bsize, len(att_masks))

        return embs, pad_masks_cat, att_masks_t

    policy.model.embed_prefix = types.MethodType(fixed_embed_prefix, policy.model)
    if prune_fn is not None and args.prune_mode != "attention":
        n_keep = max(1, int(N_PATCHES * args.keep_ratio))
        if args.prune_mode.startswith("zero_mask"):
            n_zeroed = N_PATCHES - n_keep
            log.info(f"Zero-mask: {args.prune_mode}, zeroing {n_zeroed}/{N_PATCHES} tokens/image "
                     f"(shape unchanged, {n_zeroed*3} zeroed total)")
        else:
            log.info(f"Pruning: {args.prune_mode}, keep {n_keep}/{N_PATCHES} tokens/image "
                     f"({n_keep*3} total)")
    else:
        log.info("Baseline mode (no pruning), embed_prefix fixed")


    if args.prune_mode == "attention":
        n_keep = max(1, int(N_PATCHES * args.keep_ratio))

        def pruned_embed_prefix_attn(self_model, images, img_masks, tokens, masks):
            img_embs = []
            for img, img_mask in zip(images, img_masks, strict=True):
                img_emb = self_model.paligemma_with_expert.embed_image(img)
                img_embs.append(img_emb)
            lang_emb = self_model.paligemma_with_expert.embed_language_tokens(tokens)

            lm = self_model.paligemma_with_expert.paligemma.model.language_model
            vis_importance = compute_attention_importance_probe(img_embs, lang_emb, lm)

            embs = []
            pad_masks_list = []
            att_masks = []
            start_idx = 0
            bsize = img_embs[0].shape[0]

            for i, (img_emb, img_mask) in enumerate(zip(img_embs, img_masks)):
                n_tokens = img_emb.shape[1]
                n_keep_cur = max(1, int(n_tokens * args.keep_ratio))
                scores = vis_importance[0, start_idx:start_idx + n_tokens]
                _, topk_idx = torch.topk(scores, n_keep_cur)
                topk_idx = topk_idx.sort().values

                if not hasattr(pruned_embed_prefix_attn, "_logged"):
                    print(f"[PRUNE-DIAG] attention: n_keep={n_keep_cur}/{n_tokens}, "
                          f"score_range=[{scores.min():.6f}, {scores.max():.6f}], "
                          f"first_indices={topk_idx[:5].tolist()}")
                    pruned_embed_prefix_attn._logged = True

                embs.append(img_emb[:, topk_idx, :])
                pad_masks_list.append(img_mask[:, None].expand(bsize, n_keep_cur))
                att_masks += [0] * n_keep_cur
                start_idx += n_tokens

            embs.append(lang_emb)
            pad_masks_list.append(masks)
            att_masks += [0] * lang_emb.shape[1]

            embs = torch.cat(embs, dim=1)
            pad_masks_cat = torch.cat(pad_masks_list, dim=1)
            att_masks_t = torch.tensor(att_masks, dtype=torch.bool, device=pad_masks_cat.device)
            att_masks_t = att_masks_t[None, :].expand(bsize, len(att_masks))
            return embs, pad_masks_cat, att_masks_t

        policy.model.embed_prefix = types.MethodType(pruned_embed_prefix_attn, policy.model)
        log.info(f"Pruning: attention, keep {n_keep}/{N_PATCHES} tokens/image "
                 f"({n_keep*3} total, 2-layer probe)")

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
    log.info(f"RESULT: {args.suite} prune={args.prune_mode} keep={args.keep_ratio} "
             f"SR={results['overall_sr']*100:.1f}%")
    log.info(f"Saved: {out_path}")
    log.info(f"{'='*60}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Gradient decomposition of world model loss w.r.t. dt_embedding.

Decomposes ∇_{θ_dt} L_wm into per-loss-term contributions:
  - L_obs: observation decoder (height + orientations + velocity)
  - L_reward: reward prediction head
  - L_KL: KL divergence (dyn_scale * dyn_loss + rep_scale * rep_loss)
  - L_cont: continuation head (reported separately)

Reports L2 norms and percentage contributions.
"""

import sys
import os
import math
import copy
import numpy as np
import torch
from types import SimpleNamespace
from pathlib import Path

PROJECT_DIR = "/root/autodl-tmp/event-gated-adaptive-horizon"
sys.path.insert(0, PROJECT_DIR)

import models
import networks
import tools
import yaml


def deep_merge(base, override):
    result = copy.deepcopy(base)
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = copy.deepcopy(v)
    return result


def convert_str_numbers(cfg):
    if isinstance(cfg, dict):
        return {k: convert_str_numbers(v) for k, v in cfg.items()}
    if isinstance(cfg, list):
        return [convert_str_numbers(v) for v in cfg]
    if isinstance(cfg, str):
        try:
            val = float(cfg)
            if val == int(val) and 'e' not in cfg.lower() and '.' not in cfg:
                return int(val)
            return val
        except ValueError:
            return cfg
    return cfg


def build_config(device="cpu"):
    with open(os.path.join(PROJECT_DIR, "configs.yaml")) as f:
        cfgs = yaml.safe_load(f)

    cfg = copy.deepcopy(cfgs["defaults"])
    cfg = deep_merge(cfg, cfgs["dmc_proprio"])
    cfg = convert_str_numbers(cfg)

    cfg["gate_enabled"] = True
    cfg["gate_max_dt"] = 8
    cfg["gate_subsample_max_dt"] = 8
    cfg["gate_subsample_min_dt"] = 1
    cfg["gate_fixed_dt"] = 0
    cfg["gate_type"] = "gumbel"
    cfg["dt_emb_freeze"] = False
    cfg["reward_dt_emb_detach"] = False
    cfg["full_sgs"] = False
    cfg["device"] = device
    cfg["precision"] = 32
    cfg["compile"] = False
    cfg["num_actions"] = 6

    return SimpleNamespace(**cfg)


def build_spaces():
    class Space:
        def __init__(self, shape):
            self.shape = shape

    obs_space = SimpleNamespace(spaces={
        "height": Space((1,)),
        "orientations": Space((14,)),
        "velocity": Space((9,)),
    })
    act_space = SimpleNamespace(shape=(6,))
    return obs_space, act_space


def load_batch(episode_dir, batch_size=16, batch_length=64, rng=None):
    eps_files = sorted(Path(episode_dir).glob("*.npz"))
    if rng is None:
        rng = np.random.RandomState(42)

    keys = ["height", "orientations", "velocity", "action", "reward",
            "is_first", "is_terminal", "discount"]
    batch = {k: [] for k in keys}

    indices = rng.choice(len(eps_files), size=batch_size, replace=True)
    for i in indices:
        ep = np.load(str(eps_files[i]))
        T = ep["action"].shape[0]
        start = rng.randint(0, max(1, T - batch_length))
        end = start + batch_length

        for key in keys:
            batch[key].append(ep[key][start:end])

    for key in keys:
        batch[key] = np.stack(batch[key], axis=0)

    batch["is_first"][:, 0] = True
    return batch


def run_decomposition(checkpoint_path, episode_dir, device="cpu", n_batches=10):
    config = build_config()
    config.device = device
    obs_space, act_space = build_spaces()

    wm = models.WorldModel(obs_space, act_space, step=0, config=config)

    ckpt = torch.load(checkpoint_path, map_location=device)
    wm_state = {k[4:]: v for k, v in ckpt["agent_state_dict"].items()
                if k.startswith("_wm.")}
    wm.load_state_dict(wm_state, strict=True)
    wm.to(device)
    wm.eval()

    dt_param = wm.dynamics._dt_embedding.weight
    if dt_param is None:
        print("ERROR: No dt_embedding in this checkpoint")
        return

    rng = np.random.RandomState(42)
    results = {"obs": [], "reward": [], "kl": [], "cont": []}

    for bi in range(n_batches):
        batch = load_batch(episode_dir, batch_size=16, batch_length=64, rng=rng)
        data = wm.preprocess(batch)

        data, dt_labels = tools.subsample_variable_dt(
            data, config.gate_max_dt, config.discount,
            effective_max_dt=float(config.gate_subsample_max_dt),
            min_dt=config.gate_subsample_min_dt,
        )

        for p in wm.parameters():
            p.requires_grad_(True)

        embed = wm.encoder(data)
        post, prior = wm.dynamics.observe(
            embed, data["action"], data["is_first"], dt_labels=dt_labels
        )

        kl_loss, kl_value, dyn_loss, rep_loss = wm.dynamics.kl_loss(
            post, prior, config.kl_free, config.dyn_scale, config.rep_scale
        )
        mean_kl = torch.mean(kl_loss)

        feat = wm.dynamics.get_feat(post)

        decoder_preds = wm.heads["decoder"](feat)
        obs_loss_sum = torch.zeros(1, device=device)
        for name, pred in decoder_preds.items():
            obs_loss_sum = obs_loss_sum + torch.mean(-pred.log_prob(data[name]))

        reward_pred = wm.heads["reward"](feat)
        mean_reward = torch.mean(-reward_pred.log_prob(data["reward"]))

        cont_pred = wm.heads["cont"](feat)
        mean_cont = torch.mean(-cont_pred.log_prob(data["cont"]))

        grad_obs = torch.autograd.grad(
            obs_loss_sum, dt_param, retain_graph=True, allow_unused=True)[0]
        grad_reward = torch.autograd.grad(
            mean_reward, dt_param, retain_graph=True, allow_unused=True)[0]
        grad_kl = torch.autograd.grad(
            mean_kl, dt_param, retain_graph=True, allow_unused=True)[0]
        grad_cont = torch.autograd.grad(
            mean_cont, dt_param, retain_graph=True, allow_unused=True)[0]

        norms = {}
        for name, g in [("obs", grad_obs), ("reward", grad_reward),
                        ("kl", grad_kl), ("cont", grad_cont)]:
            norms[name] = g.norm().item() if g is not None else 0.0
            results[name].append(norms[name])

        total = sum(norms.values())
        print(f"  batch {bi}: obs={norms['obs']:.6f} ({norms['obs']/total*100:.1f}%), "
              f"reward={norms['reward']:.6f} ({norms['reward']/total*100:.1f}%), "
              f"kl={norms['kl']:.6f} ({norms['kl']/total*100:.1f}%), "
              f"cont={norms['cont']:.6f} ({norms['cont']/total*100:.1f}%)")

        for p in wm.parameters():
            p.requires_grad_(False)

    avg = {k: np.mean(v) for k, v in results.items()}
    std = {k: np.std(v) for k, v in results.items()}
    total = sum(avg.values())

    print(f"\n{'='*60}")
    print(f"Checkpoint: {checkpoint_path}")
    print(f"Batches: {n_batches}, batch_size=16, batch_length=64")
    print(f"{'='*60}")
    print(f"{'Component':<12} {'‖∇‖₂ (mean±std)':<24} {'%':>8}")
    print(f"{'-'*44}")
    for name in ["obs", "reward", "kl", "cont"]:
        pct = avg[name] / total * 100
        print(f"{name:<12} {avg[name]:.6f} ± {std[name]:.6f}   {pct:>6.1f}%")
    print(f"{'total':<12} {total:.6f}")

    obs_combined = avg["obs"] + avg["cont"]
    total_3 = obs_combined + avg["reward"] + avg["kl"]
    print(f"\n3-way (obs+cont grouped as 'obs decoder'):")
    print(f"  obs+cont: {obs_combined:.6f} ({obs_combined/total_3*100:.1f}%)")
    print(f"  reward:   {avg['reward']:.6f} ({avg['reward']/total_3*100:.1f}%)")
    print(f"  KL:       {avg['kl']:.6f} ({avg['kl']/total_3*100:.1f}%)")

    return avg, std


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--episode_dir", required=True)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--n_batches", type=int, default=10)
    args = parser.parse_args()

    run_decomposition(args.checkpoint, args.episode_dir,
                      device=args.device, n_batches=args.n_batches)

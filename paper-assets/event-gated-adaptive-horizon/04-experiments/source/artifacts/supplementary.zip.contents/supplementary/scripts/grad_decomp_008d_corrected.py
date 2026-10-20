#!/usr/bin/env python3
"""Gradient decomposition with CORRECT 008d config: gate_fixed_dt=2, gate_subsample_max_dt=2."""

import sys, os, json, copy, math
import numpy as np
import torch
from types import SimpleNamespace
from pathlib import Path

PROJECT_DIR = "/root/autodl-tmp/event-gated-adaptive-horizon"
sys.path.insert(0, PROJECT_DIR)

import models, networks, tools, yaml

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

def build_config(device="cpu", gate_fixed_dt=2, gate_subsample_max_dt=2, gate_subsample_min_dt=1):
    with open(os.path.join(PROJECT_DIR, "configs.yaml")) as f:
        cfgs = yaml.safe_load(f)
    cfg = copy.deepcopy(cfgs["defaults"])
    cfg = deep_merge(cfg, cfgs["dmc_proprio"])
    cfg = convert_str_numbers(cfg)
    cfg["gate_enabled"] = True
    cfg["gate_max_dt"] = 8
    cfg["gate_subsample_max_dt"] = gate_subsample_max_dt
    cfg["gate_subsample_min_dt"] = gate_subsample_min_dt
    cfg["gate_fixed_dt"] = gate_fixed_dt
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

def compute_grads(checkpoint_path, episode_dir, device="cpu", n_batches=50,
                  gate_fixed_dt=2, gate_subsample_max_dt=2, gate_subsample_min_dt=1):
    config = build_config(device=device, gate_fixed_dt=gate_fixed_dt,
                          gate_subsample_max_dt=gate_subsample_max_dt,
                          gate_subsample_min_dt=gate_subsample_min_dt)
    obs_space, act_space = build_spaces()
    wm = models.WorldModel(obs_space, act_space, step=0, config=config)
    ckpt = torch.load(checkpoint_path, map_location=device)
    wm_state = {k[4:]: v for k, v in ckpt["agent_state_dict"].items()
                if k.startswith("_wm.")}
    wm.load_state_dict(wm_state, strict=True)
    wm.to(device)
    wm.eval()

    dt_param = wm.dynamics._dt_embedding.weight

    rng = np.random.RandomState(42)
    results = {"obs": [], "reward": [], "kl": [], "cont": []}

    kl_free = getattr(config, 'kl_free', 1.0)
    dyn_scale = getattr(config, 'dyn_scale', 0.5)
    rep_scale = getattr(config, 'rep_scale', 0.1)

    # Replicate training-time subsample logic
    bst_max_dt = 2 if config.gate_type == 'bernoulli_st' else config.gate_max_dt
    if config.gate_subsample_max_dt > 0:
        subsample_eff_dt = float(config.gate_subsample_max_dt)
    else:
        subsample_eff_dt = float(gate_fixed_dt) if gate_fixed_dt > 0 else float(bst_max_dt)

    print(f"Config: gate_fixed_dt={gate_fixed_dt}, gate_subsample_max_dt={gate_subsample_max_dt}")
    print(f"Subsample effective_max_dt={subsample_eff_dt}, min_dt={gate_subsample_min_dt}")
    print(f"bst_max_dt={bst_max_dt}")

    for bi in range(n_batches):
        batch = load_batch(episode_dir, batch_size=16, batch_length=64, rng=rng)
        data = wm.preprocess(batch)

        data, dt_labels = tools.subsample_variable_dt(
            data, bst_max_dt, config.discount,
            effective_max_dt=subsample_eff_dt,
            min_dt=int(gate_subsample_min_dt))

        for p in wm.parameters():
            p.requires_grad_(True)

        embed = wm.encoder(data)
        post, prior = wm.dynamics.observe(
            embed, data["action"], data["is_first"], dt_labels=dt_labels)

        kl_loss, kl_value, _, _ = wm.dynamics.kl_loss(post, prior, kl_free, dyn_scale, rep_scale)
        kl_loss_mean = kl_loss.mean()

        feat = wm.dynamics.get_feat(post)

        decoder_preds = wm.heads["decoder"](feat)
        obs_losses = []
        for obs_key in ["height", "orientations", "velocity"]:
            if obs_key in decoder_preds and obs_key in data:
                obs_losses.append(-decoder_preds[obs_key].log_prob(data[obs_key]).mean())
        obs_loss = sum(obs_losses)

        reward_pred = wm.heads["reward"](feat)
        reward_loss = -reward_pred.log_prob(data["reward"]).mean()

        cont_pred = wm.heads["cont"](feat)
        cont_loss = -cont_pred.log_prob(data["cont"]).mean()

        for loss_name, loss_val in [("obs", obs_loss), ("reward", reward_loss),
                                     ("kl", kl_loss_mean), ("cont", cont_loss)]:
            wm.zero_grad()
            dt_param.requires_grad_(True)
            if dt_param.grad is not None:
                dt_param.grad.zero_()
            loss_val.backward(retain_graph=True)
            if dt_param.grad is not None:
                results[loss_name].append(dt_param.grad.norm().item())
            else:
                results[loss_name].append(0.0)
            dt_param.requires_grad_(False)

        for p in wm.parameters():
            p.requires_grad_(False)

        if bi % 10 == 0:
            norms = {k: results[k][-1] for k in results}
            total_b = sum(norms.values())
            if total_b > 0:
                print(f"  Batch {bi+1}/{n_batches}: obs={norms['obs']/total_b*100:.1f}% "
                      f"reward={norms['reward']/total_b*100:.1f}% "
                      f"kl={norms['kl']/total_b*100:.1f}% cont={norms['cont']/total_b*100:.1f}%")

    avg = {k: float(np.mean(v)) for k, v in results.items()}
    std = {k: float(np.std(v)) for k, v in results.items()}
    total = sum(avg.values())
    pcts = {k: avg[k] / total * 100 if total > 0 else 0 for k in avg}
    return {"avg_norms": avg, "std_norms": std, "percentages": pcts, "total_norm": total}


def main():
    device = "cuda:1"

    checkpoints = [
        ("008d_55K", "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8",
         "latest.pt", 55000),
        ("009e_112K", "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1",
         "latest.pt", 112000),
    ]

    # Wrong config (old measurement) for comparison
    wrong_config = {"gate_fixed_dt": 0, "gate_subsample_max_dt": 8, "gate_subsample_min_dt": 1}
    # Correct config (actual 008d training)
    correct_config = {"gate_fixed_dt": 2, "gate_subsample_max_dt": 2, "gate_subsample_min_dt": 1}

    output = {
        "exp_id": "008d_gradient_decomposition_corrected",
        "description": "Gradient decomposition with CORRECT 008d config (gate_fixed_dt=2, gate_subsample_max_dt=2). Previous measurement used wrong config (gate_fixed_dt=0, gate_max_dt=8).",
        "config_used": correct_config,
        "config_source": "from scripts/multi_seed_runs.sh: --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8",
        "wrong_config_reference": wrong_config,
        "n_batches": 50,
        "steps": []
    }

    for exp_name, logdir, ckpt_name, step in checkpoints:
        ckpt_path = f"{logdir}/{ckpt_name}"
        episode_dir = f"{logdir}/train_eps"
        if not os.path.exists(ckpt_path):
            print(f"Skipping {exp_name}: checkpoint not found")
            continue
        if not os.path.exists(episode_dir):
            episode_dir = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8/train_eps"

        print(f"\n{'='*60}")
        print(f"=== {exp_name} (step={step}) with CORRECT config ===")
        print(f"{'='*60}")

        result_correct = compute_grads(ckpt_path, episode_dir, device=device, n_batches=50,
                                       **correct_config)

        print(f"\n--- Now running with WRONG config for comparison ---")
        result_wrong = compute_grads(ckpt_path, episode_dir, device=device, n_batches=50,
                                     **wrong_config)

        entry = {
            "exp_name": exp_name,
            "step": step,
            "correct_config": {
                "obs_pct": round(result_correct["percentages"]["obs"], 1),
                "reward_pct": round(result_correct["percentages"]["reward"], 1),
                "kl_pct": round(result_correct["percentages"]["kl"], 1),
                "cont_pct": round(result_correct["percentages"]["cont"], 1),
                "obs_norm": result_correct["avg_norms"]["obs"],
                "reward_norm": result_correct["avg_norms"]["reward"],
                "kl_norm": result_correct["avg_norms"]["kl"],
                "cont_norm": result_correct["avg_norms"]["cont"],
                "obs_std": result_correct["std_norms"]["obs"],
                "reward_std": result_correct["std_norms"]["reward"],
                "kl_std": result_correct["std_norms"]["kl"],
                "cont_std": result_correct["std_norms"]["cont"],
            },
            "wrong_config": {
                "obs_pct": round(result_wrong["percentages"]["obs"], 1),
                "reward_pct": round(result_wrong["percentages"]["reward"], 1),
                "kl_pct": round(result_wrong["percentages"]["kl"], 1),
                "cont_pct": round(result_wrong["percentages"]["cont"], 1),
                "obs_norm": result_wrong["avg_norms"]["obs"],
                "reward_norm": result_wrong["avg_norms"]["reward"],
                "kl_norm": result_wrong["avg_norms"]["kl"],
                "cont_norm": result_wrong["avg_norms"]["cont"],
            },
        }
        output["steps"].append(entry)

        print(f"\n{'='*60}")
        print(f"SUMMARY {exp_name}:")
        print(f"  CORRECT (fixed_dt=2): obs={entry['correct_config']['obs_pct']}% "
              f"reward={entry['correct_config']['reward_pct']}% "
              f"kl={entry['correct_config']['kl_pct']}% "
              f"cont={entry['correct_config']['cont_pct']}%")
        print(f"  WRONG   (fixed_dt=0): obs={entry['wrong_config']['obs_pct']}% "
              f"reward={entry['wrong_config']['reward_pct']}% "
              f"kl={entry['wrong_config']['kl_pct']}% "
              f"cont={entry['wrong_config']['cont_pct']}%")

    out_path = f"{PROJECT_DIR}/artifacts/analysis/gradient_decomposition_008d_corrected.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to: {out_path}")
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()

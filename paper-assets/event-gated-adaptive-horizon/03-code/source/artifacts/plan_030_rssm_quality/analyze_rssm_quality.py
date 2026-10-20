#!/usr/bin/env python3
"""Plan_030: RSSM Prediction Quality — dt=1 vs dt=2 Transitions

Compare RSSM observation/reward reconstruction loss between dt=1 and dt=2
for exp_078 (CIVO, s0) vs exp_088 (no CIVO, s1).
"""

import sys, os, json, pathlib, math
import numpy as np

os.environ["MUJOCO_GL"] = "egl"
os.environ["PYOPENGL_PLATFORM"] = "egl"
os.environ["MUJOCO_EGL_DEVICE_ID"] = "1"

PROJECT_DIR = "/root/autodl-tmp/event-gated-adaptive-horizon"
sys.path.insert(0, PROJECT_DIR)

import torch
import ruamel.yaml as yaml
import gym.spaces as spaces

import tools
import networks
import models

DEVICE = "cuda:1"
BATCH_SIZE = 16
BATCH_LENGTH = 64
NUM_BATCHES = 50

EXPERIMENTS = {
    "exp_078_civo": f"{PROJECT_DIR}/logdir/exp_078_cheetah_008d_s0",
    "exp_088_nocivo": f"{PROJECT_DIR}/logdir/exp_088_cheetah_008d_s1",
}


def build_config():
    raw = yaml.YAML(typ="safe").load(open(f"{PROJECT_DIR}/configs.yaml").read())
    cfg = {}
    for section in ["defaults", "dmc_proprio"]:
        for k, v in raw[section].items():
            if isinstance(v, dict) and k in cfg and isinstance(cfg[k], dict):
                cfg[k].update(v)
            else:
                cfg[k] = v

    cfg["gate_enabled"] = True
    cfg["gate_fixed_dt"] = 2
    cfg["task"] = "dmc_cheetah_run"
    cfg["device"] = DEVICE
    cfg["precision"] = 32
    cfg["compile"] = False
    cfg["num_actions"] = 6
    cfg["batch_size"] = BATCH_SIZE
    cfg["batch_length"] = BATCH_LENGTH

    class Config:
        pass
    config = Config()
    for k, v in cfg.items():
        setattr(config, k, v)
    return config


def build_obs_space():
    return spaces.Dict({
        "position": spaces.Box(-np.inf, np.inf, shape=(8,), dtype=np.float32),
        "velocity": spaces.Box(-np.inf, np.inf, shape=(9,), dtype=np.float32),
    })


def build_act_space():
    return spaces.Box(-1.0, 1.0, shape=(6,), dtype=np.float32)


def load_world_model(config, logdir):
    obs_space = build_obs_space()
    act_space = build_act_space()
    wm = models.WorldModel(obs_space, act_space, 0, config)
    wm = wm.to(config.device)

    checkpoint = torch.load(f"{logdir}/latest.pt", map_location=config.device)
    agent_sd = checkpoint["agent_state_dict"]

    wm_sd = {}
    prefix = "_wm."
    for k, v in agent_sd.items():
        if k.startswith(prefix):
            wm_sd[k[len(prefix):]] = v

    missing, unexpected = wm.load_state_dict(wm_sd, strict=False)
    if missing:
        print(f"  Missing keys: {missing}")
    if unexpected:
        print(f"  Unexpected keys: {unexpected}")
    wm.eval()
    return wm


def load_episodes(logdir, limit=30000):
    train_dir = pathlib.Path(logdir) / "train_eps"
    return tools.load_episodes(train_dir, limit=limit)


def make_batches(episodes, num_batches, batch_length, seed=42):
    sampler = tools.sample_episodes(episodes, batch_length, seed=seed)
    batches = []
    for _ in range(num_batches):
        batch = []
        for _ in range(BATCH_SIZE):
            batch.append(next(sampler))
        data = {}
        for key in batch[0].keys():
            data[key] = np.stack([b[key] for b in batch], 0)
        batches.append(data)
    return batches


def subsample_dt2(data, discount=0.997):
    """Deterministic dt=2 subsampling of a batch."""
    B, T = data["action"].shape[:2]
    indices = list(range(0, T, 2))
    T_sub = len(indices)

    data_sub = {}
    for key in data:
        arr = data[key]
        if arr.ndim >= 2:
            data_sub[key] = arr[:, indices]
        else:
            data_sub[key] = arr

    reward_cum = np.zeros((B, T_sub), dtype=np.float64)
    cont_sub = np.ones((B, T_sub), dtype=np.float32)
    for i, t_start in enumerate(indices[:-1]):
        t_end = min(t_start + 2, T)
        for b in range(B):
            r_slice = data["reward"][b, t_start:t_end]
            gamma_powers = discount ** np.arange(t_end - t_start)
            reward_cum[b, i] = (gamma_powers * r_slice).sum()
            if "is_terminal" in data:
                cont_slice = 1.0 - data["is_terminal"][b, t_start:t_end].astype(np.float32)
                cont_sub[b, i] = cont_slice.min()

    data_sub["reward"] = reward_cum
    return data_sub, T_sub


@torch.no_grad()
def compute_losses(wm, data_np, dt_value, config):
    """Run RSSM forward pass and compute per-step losses."""
    data = {
        k: torch.tensor(v, device=config.device, dtype=torch.float32)
        for k, v in data_np.items()
    }
    if "image" in data:
        del data["image"]
    if "discount" in data:
        data["discount"] *= config.discount
        data["discount"] = data["discount"].unsqueeze(-1)
    data["cont"] = (1.0 - data["is_terminal"]).unsqueeze(-1)

    B, T = data["action"].shape[:2]
    dt_labels = torch.full((B, T), dt_value, dtype=torch.long, device=config.device)

    embed = wm.encoder(data)
    post, prior = wm.dynamics.observe(
        embed, data["action"], data["is_first"], dt_labels=dt_labels
    )

    kl_free = config.kl_free
    dyn_scale = config.dyn_scale
    rep_scale = config.rep_scale
    kl_loss, kl_value, dyn_loss, rep_loss = wm.dynamics.kl_loss(
        post, prior, kl_free, dyn_scale, rep_scale
    )

    feat = wm.dynamics.get_feat(post)
    losses = {}
    for name, head in wm.heads.items():
        pred = head(feat)
        if isinstance(pred, dict):
            for pname, pdist in pred.items():
                if pname in data:
                    losses[pname] = -pdist.log_prob(data[pname]).detach().cpu().numpy()
        else:
            if name in data:
                losses[name] = -pred.log_prob(data[name]).detach().cpu().numpy()

    prior_dist = wm.dynamics.get_dist(prior)
    post_dist = wm.dynamics.get_dist(post)

    return {
        "kl_value": kl_value.detach().cpu().numpy(),
        "kl_loss": kl_loss.detach().cpu().numpy(),
        "dyn_loss": dyn_loss.detach().cpu().numpy(),
        "rep_loss": rep_loss.detach().cpu().numpy(),
        "prior_ent": prior_dist.entropy().detach().cpu().numpy(),
        "post_ent": post_dist.entropy().detach().cpu().numpy(),
        **losses,
    }


def aggregate_stats(all_losses):
    """Compute mean ± std for each metric across all batches."""
    combined = {}
    for batch_losses in all_losses:
        for key, val in batch_losses.items():
            if key not in combined:
                combined[key] = []
            combined[key].append(val.mean())
    return {k: (float(np.mean(v)), float(np.std(v))) for k, v in combined.items()}


def main():
    print("=" * 60)
    print("Plan_030: RSSM Prediction Quality — dt=1 vs dt=2")
    print("=" * 60)

    config = build_config()
    results = {}

    for exp_name, logdir in EXPERIMENTS.items():
        print(f"\n{'=' * 50}")
        print(f"Experiment: {exp_name}")
        print(f"  Logdir: {logdir}")

        print("  Loading world model...")
        wm = load_world_model(config, logdir)

        print("  Loading episodes...")
        episodes = load_episodes(logdir, limit=30000)
        print(f"  Loaded {len(episodes)} episodes")

        print(f"  Preparing {NUM_BATCHES} batches (batch_size={BATCH_SIZE}, length={BATCH_LENGTH})...")
        batches = make_batches(episodes, NUM_BATCHES, BATCH_LENGTH, seed=42)

        # --- dt=1 analysis ---
        print("  Running dt=1 analysis...")
        dt1_losses = []
        for i, batch in enumerate(batches):
            losses = compute_losses(wm, batch, dt_value=1, config=config)
            dt1_losses.append(losses)
            if (i + 1) % 10 == 0:
                print(f"    batch {i + 1}/{NUM_BATCHES}")
        dt1_stats = aggregate_stats(dt1_losses)

        # --- dt=2 analysis ---
        print("  Running dt=2 analysis...")
        dt2_losses = []
        for i, batch in enumerate(batches):
            batch_sub, T_sub = subsample_dt2(batch, discount=config.discount)
            losses = compute_losses(wm, batch_sub, dt_value=2, config=config)
            dt2_losses.append(losses)
            if (i + 1) % 10 == 0:
                print(f"    batch {i + 1}/{NUM_BATCHES}")
        dt2_stats = aggregate_stats(dt2_losses)

        results[exp_name] = {"dt1": dt1_stats, "dt2": dt2_stats}

        print(f"\n  Results for {exp_name}:")
        print(f"  {'Metric':<20} {'dt=1 (mean±std)':<25} {'dt=2 (mean±std)':<25} {'Δ(dt2-dt1)':<15}")
        print(f"  {'-' * 85}")
        all_keys = sorted(set(list(dt1_stats.keys()) + list(dt2_stats.keys())))
        for key in all_keys:
            if key in dt1_stats and key in dt2_stats:
                m1, s1 = dt1_stats[key]
                m2, s2 = dt2_stats[key]
                delta = m2 - m1
                print(f"  {key:<20} {m1:>8.4f} ± {s1:<8.4f}   {m2:>8.4f} ± {s2:<8.4f}   {delta:>+8.4f}")

        del wm
        torch.cuda.empty_cache()

    # --- Cross-experiment comparison ---
    print(f"\n{'=' * 60}")
    print("Cross-experiment comparison (dt=2 metrics):")
    print(f"{'Metric':<20} {'exp_078 (CIVO)':<25} {'exp_088 (no CIVO)':<25} {'Δ(CIVO-noCIVO)':<15}")
    print(f"{'-' * 85}")

    exp_keys = list(results.keys())
    if len(exp_keys) == 2:
        dt2_a = results[exp_keys[0]]["dt2"]
        dt2_b = results[exp_keys[1]]["dt2"]
        all_keys = sorted(set(list(dt2_a.keys()) + list(dt2_b.keys())))
        for key in all_keys:
            if key in dt2_a and key in dt2_b:
                m_a, s_a = dt2_a[key]
                m_b, s_b = dt2_b[key]
                delta = m_a - m_b
                print(f"{key:<20} {m_a:>8.4f} ± {s_a:<8.4f}   {m_b:>8.4f} ± {s_b:<8.4f}   {delta:>+8.4f}")

    # Save results
    out_path = "/tmp/plan_030_rssm_quality_results.json"
    serializable = {}
    for exp, exp_data in results.items():
        serializable[exp] = {}
        for dt_key, stats in exp_data.items():
            serializable[exp][dt_key] = {
                k: {"mean": v[0], "std": v[1]} for k, v in stats.items()
            }
    with open(out_path, "w") as f:
        json.dump(serializable, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()

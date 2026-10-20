"""
Value Distribution vs Realized Returns: V(s) calibration analysis.
Compares collapsed (008d) vs healthy (008a) experiments.
Uses batched RSSM observe() for efficiency.
"""
import sys
import json
import argparse
import pathlib
import numpy as np
from glob import glob

import torch

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import ruamel.yaml as yaml
import networks
import models
import tools

def log(msg):
    print(msg, flush=True)


def load_config(overrides=None):
    config_path = PROJECT_ROOT / "configs.yaml"
    configs = yaml.safe_load(config_path.read_text())
    defaults = configs["defaults"]
    for key, value in configs["dmc_proprio"].items():
        if isinstance(value, dict) and key in defaults and isinstance(defaults[key], dict):
            defaults[key].update(value)
        else:
            defaults[key] = value
    if overrides:
        for key, value in overrides.items():
            if isinstance(value, dict) and key in defaults and isinstance(defaults[key], dict):
                defaults[key].update(value)
            else:
                defaults[key] = value

    class Config:
        pass
    cfg = Config()
    for k, v in defaults.items():
        setattr(cfg, k, v)
    return cfg


def build_model(config, obs_shapes, num_actions, device="cpu"):
    import gymnasium.spaces as spaces
    obs_space = spaces.Dict({
        k: spaces.Box(-np.inf, np.inf, shape=v, dtype=np.float32)
        for k, v in obs_shapes.items()
    })
    act_space = spaces.Box(-1.0, 1.0, shape=(num_actions,), dtype=np.float32)
    config.num_actions = num_actions
    config.device = device
    wm = models.WorldModel(obs_space, act_space, 0, config)
    behavior = models.ImagBehavior(config, wm)
    return wm, behavior


def load_checkpoint(wm, behavior, ckpt_path, device="cpu"):
    ckpt = torch.load(str(ckpt_path), map_location=device)
    full_sd = ckpt["agent_state_dict"]

    wm_sd = {k[4:]: v for k, v in full_sd.items() if k.startswith("_wm.")}
    wm.load_state_dict(wm_sd)

    beh_sd = {k[len("_task_behavior."):]: v
              for k, v in full_sd.items() if k.startswith("_task_behavior.")}
    behavior.load_state_dict(beh_sd)


def load_episodes(ep_dir, max_eps=10):
    files = sorted(glob(str(pathlib.Path(ep_dir) / "*.npz")))
    if not files:
        raise FileNotFoundError(f"No .npz files in {ep_dir}")
    if len(files) > max_eps:
        indices = np.linspace(0, len(files) - 1, max_eps, dtype=int)
        files = [files[i] for i in indices]
    return [dict(np.load(f)) for f in files]


def compute_mc_returns(rewards, discount=0.997):
    T = len(rewards)
    returns = np.zeros(T)
    G = 0.0
    for t in range(T - 1, -1, -1):
        G = rewards[t] + discount * G
        returns[t] = G
    return returns


@torch.no_grad()
def compute_values_batch(wm, value_net, episodes, device="cpu"):
    """Process episodes through world model using batched observe()."""
    wm.eval()
    value_net.eval()

    all_values = []
    all_mc_returns = []

    # Process episodes in batches of 4
    batch_size = min(4, len(episodes))
    for batch_start in range(0, len(episodes), batch_size):
        batch_eps = episodes[batch_start:batch_start + batch_size]
        B = len(batch_eps)
        T = min(ep["reward"].shape[0] for ep in batch_eps)

        # Stack observations into (B, T, ...) tensors
        obs_dict = {}
        for k in ["height", "orientations", "velocity"]:
            arrs = []
            for ep in batch_eps:
                v = ep[k][:T]
                if v.ndim == 1:
                    v = v[:, None]
                arrs.append(v)
            obs_dict[k] = torch.tensor(np.stack(arrs), dtype=torch.float32, device=device)

        actions = torch.tensor(
            np.stack([ep["action"][:T] for ep in batch_eps]),
            dtype=torch.float32, device=device
        )
        is_first = torch.tensor(
            np.stack([ep["is_first"][:T].astype(np.float32) for ep in batch_eps]),
            dtype=torch.float32, device=device
        )

        # Encode: concat sorted keys, symlog, MLP
        sorted_keys = sorted(obs_dict.keys())
        obs_cat = torch.cat([obs_dict[k] for k in sorted_keys], dim=-1)  # (B, T, 24)
        obs_cat = tools.symlog(obs_cat)
        embed = wm.encoder._mlp(obs_cat)  # (B, T, 1024)

        # Run RSSM observe (batched)
        post, _ = wm.dynamics.observe(embed, actions, is_first)

        # Get features and compute values
        feat = wm.dynamics.get_feat(post)  # (B, T, 1536)
        value_dist = value_net(feat)
        values = value_dist.mode().squeeze(-1).cpu().numpy()  # (B, T)

        # Compute MC returns
        for i in range(B):
            rewards = batch_eps[i]["reward"][:T]
            mc_ret = compute_mc_returns(rewards, discount=0.997)

            # Skip first 5 and last 50 timesteps
            valid = slice(5, T - 50)
            all_values.append(values[i, valid])
            all_mc_returns.append(mc_ret[valid])

        log(f"  Batch {batch_start//batch_size + 1}/{(len(episodes)-1)//batch_size + 1} done")

    return np.concatenate(all_values), np.concatenate(all_mc_returns)


def compute_metrics(values, mc_returns):
    bias = values - mc_returns
    safe_ret = np.where(np.abs(mc_returns) < 1e-6, 1e-6, mc_returns)
    return {
        "n_samples": int(len(values)),
        "v_pred_mean": float(np.mean(values)),
        "v_pred_std": float(np.std(values)),
        "mc_return_mean": float(np.mean(mc_returns)),
        "mc_return_std": float(np.std(mc_returns)),
        "bias_mean": float(np.mean(bias)),
        "bias_std": float(np.std(bias)),
        "bias_median": float(np.median(bias)),
        "rmse": float(np.sqrt(np.mean(bias**2))),
        "overestimation_rate": float(np.mean(values > mc_returns)),
        "correlation": float(np.corrcoef(values, mc_returns)[0, 1]) if len(values) > 1 else 0.0,
        "ratio_mean": float(np.mean(values / safe_ret)),
        "ratio_median": float(np.median(values / safe_ret)),
    }


def plot_results(results, output_path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    color_map = {"008d (collapsed)": "#F44336", "008a (healthy)": "#2196F3"}
    fallback = ["#F44336", "#2196F3", "#4CAF50", "#FF9800"]

    # Panel 1: Scatter
    ax = axes[0]
    all_min, all_max = float("inf"), float("-inf")
    for i, (label, data) in enumerate(results.items()):
        c = color_map.get(label, fallback[i % len(fallback)])
        v, g = data["values"], data["mc_returns"]
        if len(v) > 2000:
            idx = np.random.RandomState(42).choice(len(v), 2000, replace=False)
            v_p, g_p = v[idx], g[idx]
        else:
            v_p, g_p = v, g
        ax.scatter(g_p, v_p, alpha=0.12, s=10, c=c, label=label, rasterized=True)
        all_min = min(all_min, np.percentile(g_p, 1), np.percentile(v_p, 1))
        all_max = max(all_max, np.percentile(g_p, 99), np.percentile(v_p, 99))

    margin = (all_max - all_min) * 0.08
    lims = [all_min - margin, all_max + margin]
    ax.plot(lims, lims, "k--", alpha=0.6, linewidth=1.2, label="y=x")
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    ax.set_xlabel("Monte Carlo Return $G_t$")
    ax.set_ylabel("Value Prediction $V(s_t)$")
    ax.set_title("Value Calibration: V(s) vs MC Return", fontweight="bold")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, alpha=0.3)

    # Panel 2: Bias histogram
    ax = axes[1]
    for i, (label, data) in enumerate(results.items()):
        c = color_map.get(label, fallback[i % len(fallback)])
        bias = data["values"] - data["mc_returns"]
        ax.hist(bias, bins=80, alpha=0.45, color=c, label=label, density=True)
        ax.axvline(np.mean(bias), color=c, linestyle="--", linewidth=1.8,
                    label=f"mean={np.mean(bias):.1f}")
    ax.axvline(0, color="black", linestyle="-", linewidth=1, alpha=0.5)
    ax.set_xlabel("Bias: $V(s) - G_t$")
    ax.set_ylabel("Density")
    ax.set_title("Value Estimation Bias", fontweight="bold")
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3)

    # Panel 3: Metrics table
    ax = axes[2]
    ax.axis("off")
    rows = [
        ("n_samples", "N samples"),
        ("v_pred_mean", "V(s) mean"),
        ("mc_return_mean", "G_t mean"),
        ("bias_mean", "Bias mean"),
        ("bias_median", "Bias median"),
        ("rmse", "RMSE"),
        ("overestimation_rate", "Overest. rate"),
        ("ratio_mean", "V/G ratio"),
        ("correlation", "Correlation"),
    ]
    cell_text = []
    for mk, display in rows:
        row = [display]
        for label in results:
            val = results[label]["metrics"][mk]
            if mk == "n_samples":
                row.append(f"{val:,}")
            elif mk == "overestimation_rate":
                row.append(f"{val:.1%}")
            else:
                row.append(f"{val:.2f}")
        cell_text.append(row)

    table = ax.table(
        cellText=cell_text,
        colLabels=["Metric"] + list(results.keys()),
        loc="center", cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.0, 1.5)
    for (r, c), cell in table.get_celld().items():
        if r == 0:
            cell.set_facecolor("#E0E0E0")
            cell.set_text_props(fontweight="bold")
        if r > 0 and cell_text[r-1][0] == "Overest. rate" and c > 0:
            val = results[list(results.keys())[c-1]]["metrics"]["overestimation_rate"]
            if val > 0.8:
                cell.set_facecolor("#FFCDD2")
            elif val < 0.6:
                cell.set_facecolor("#C8E6C9")
    ax.set_title("Calibration Metrics", fontweight="bold", pad=20)

    plt.tight_layout()
    plt.savefig(str(output_path), dpi=150, bbox_inches="tight")
    png = str(output_path).replace(".pdf", ".png")
    plt.savefig(png, dpi=150, bbox_inches="tight")
    plt.close()
    log(f"Saved: {output_path} and {png}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoints", nargs="+", required=True)
    parser.add_argument("--labels", nargs="+", required=True)
    parser.add_argument("--n_episodes", type=int, default=10)
    parser.add_argument("--device", type=str, default="cpu")
    parser.add_argument("--output", type=str, default="artifacts/value_vs_returns.pdf")
    args = parser.parse_args()

    config = load_config({"device": args.device, "compile": False, "gate_enabled": True})

    obs_shapes = {"height": (1,), "orientations": (14,), "velocity": (9,)}
    num_actions = 6

    results = {}
    for ckpt_path, label in zip(args.checkpoints, args.labels):
        ckpt_path = pathlib.Path(ckpt_path)
        log(f"\n{'='*60}")
        log(f"Processing: {label} ({ckpt_path})")

        ep_dir = ckpt_path.parent / "train_eps"
        episodes = load_episodes(ep_dir, max_eps=args.n_episodes)
        log(f"  Loaded {len(episodes)} episodes")

        log("  Building model...")
        wm, behavior = build_model(config, obs_shapes, num_actions, device=args.device)
        wm.to(args.device)
        behavior.to(args.device)

        log("  Loading checkpoint...")
        load_checkpoint(wm, behavior, ckpt_path, device=args.device)

        log("  Computing V(s) and MC returns...")
        values, mc_returns = compute_values_batch(wm, behavior.value, episodes, device=args.device)

        metrics = compute_metrics(values, mc_returns)
        results[label] = {"values": values, "mc_returns": mc_returns, "metrics": metrics}

        log(f"\n  Results for {label}:")
        for k, v in metrics.items():
            if k == "n_samples":
                log(f"    {k}: {v:,}")
            elif k == "overestimation_rate":
                log(f"    {k}: {v:.1%}")
            else:
                log(f"    {k}: {v:.4f}")

        del wm, behavior

    output_path = pathlib.Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    log("\nPlotting...")
    plot_results(results, output_path)

    json_path = str(output_path).replace(".pdf", ".json")
    with open(json_path, "w") as f:
        json.dump({label: data["metrics"] for label, data in results.items()}, f, indent=2)
    log(f"Saved metrics: {json_path}")


if __name__ == "__main__":
    main()

"""exp_064: Value Distribution Analysis — V(s) vs Monte Carlo Return.

Compares critic value predictions against actual MC returns from replay buffer
to detect value overestimation caused by trained dt_embedding (CIVO).

Models:
  - baseline_s1: dt=1 baseline (no gate, no dt_embedding)
  - exp_008d_subsample_on_h8: gate + trained dt_embedding (collapsed CIVO)
  - exp_008f_no_dt_embed_subsample_on_h8: gate + dt_embed_dim=0 (control)
"""
import argparse
import sys
import os
import json
import numpy as np
from pathlib import Path
from types import SimpleNamespace
from collections import OrderedDict

os.environ["MUJOCO_GL"] = "osmesa"
os.environ["PYOPENGL_PLATFORM"] = "osmesa"

import torch
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

CODE_DIR = Path("/root/autodl-tmp/event-gated-adaptive-horizon")
sys.path.insert(0, str(CODE_DIR))

import models
import networks
import tools

NUM_EPISODES = 150
OBS_KEYS = ["height", "orientations", "velocity"]
OBS_SHAPES = OrderedDict([
    ("height", (1,)),
    ("orientations", (14,)),
    ("velocity", (9,)),
])
NUM_ACTIONS = 6
DISCOUNT = 0.997


def make_config(device, gate_enabled, gate_max_dt=8, gate_dt_embed_dim=32):
    return SimpleNamespace(
        device=device, precision=32,
        dyn_hidden=512, dyn_deter=512, dyn_stoch=32, dyn_discrete=32,
        dyn_rec_depth=1, dyn_mean_act="none", dyn_std_act="sigmoid2",
        dyn_min_std=0.1, unimix_ratio=0.01, initial="learned",
        num_actions=NUM_ACTIONS, units=512, act="SiLU", norm=True,
        encoder=dict(
            mlp_keys=".*", cnn_keys="$^", act="SiLU", norm=True,
            cnn_depth=32, kernel_size=4, minres=4,
            mlp_layers=5, mlp_units=1024, symlog_inputs=True,
        ),
        decoder=dict(
            mlp_keys=".*", cnn_keys="$^", act="SiLU", norm=True,
            cnn_depth=32, kernel_size=4, minres=4,
            mlp_layers=5, mlp_units=1024, cnn_sigmoid=False,
            image_dist="mse", vector_dist="symlog_mse", outscale=1.0,
        ),
        reward_head=dict(layers=2, dist="symlog_disc", loss_scale=1.0, outscale=0.0),
        cont_head=dict(layers=2, loss_scale=1.0, outscale=1.0),
        critic=dict(layers=2, dist="symlog_disc", slow_target=True,
                    slow_target_update=1, slow_target_fraction=0.02,
                    lr=3e-5, eps=1e-5, grad_clip=100.0, outscale=0.0),
        grad_heads=["decoder", "reward", "cont"],
        model_lr=1e-4, opt_eps=1e-8, grad_clip=1000, weight_decay=0.0, opt="adam",
        gate_enabled=gate_enabled, gate_max_dt=gate_max_dt,
        gate_dt_embed_dim=gate_dt_embed_dim,
        gate_hidden_units=256, gate_hidden_layers=2,
        gate_tau_init=5.0, gate_tau_final=0.5, gate_tau_anneal_steps=200000,
        gate_loss_weight=1.0,
        gate_entropy_bonus_init=0.1, gate_entropy_bonus_final=0.01,
        gate_curriculum_phase1=50000, gate_curriculum_phase2=150000,
        discount=DISCOUNT, discount_lambda=0.95,
        compile=False,
        dt_emb_freeze=False,
        gate_type="gumbel",
        gate_fixed_dt=0,
        reward_EMA=True,
        dual_critic=False,
        wide_critic=False,
        narrow_dual_critic=False,
    )


class FakeSpace:
    def __init__(self, shapes_dict):
        self.spaces = OrderedDict()
        for k, v in shapes_dict.items():
            self.spaces[k] = SimpleNamespace(shape=v)


def load_world_model(ckpt_path, config):
    obs_space = FakeSpace(OBS_SHAPES)
    act_space = SimpleNamespace(shape=(NUM_ACTIONS,))
    wm = models.WorldModel(obs_space, act_space, 0, config)
    ckpt = torch.load(ckpt_path, map_location=config.device)
    wm_state = {k[4:]: v for k, v in ckpt["agent_state_dict"].items()
                if k.startswith("_wm.")}
    wm.load_state_dict(wm_state, strict=True)
    wm.eval()
    wm.to(config.device)
    return wm


def load_value_head(ckpt_path, config, device):
    if config.dyn_discrete:
        feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter
    else:
        feat_size = config.dyn_stoch + config.dyn_deter
    value = networks.MLP(
        feat_size,
        (255,),
        config.critic["layers"],
        config.units,
        config.act,
        config.norm,
        config.critic["dist"],
        outscale=config.critic["outscale"],
        device=device,
        name="Value",
    )
    ckpt = torch.load(ckpt_path, map_location=device)
    value_state = {}
    for k, v in ckpt["agent_state_dict"].items():
        if k.startswith("_task_behavior.value."):
            new_k = k[len("_task_behavior.value."):]
            value_state[new_k] = v
    value.load_state_dict(value_state, strict=True)
    value.eval()
    value.to(device)
    return value


def load_episodes(episodes_dir, num_episodes):
    files = sorted(Path(episodes_dir).glob("*.npz"))
    if len(files) > num_episodes:
        files = files[-num_episodes:]
    return [dict(np.load(f)) for f in files]


def compute_mc_returns(rewards, discount):
    T = len(rewards)
    mc_returns = np.zeros(T)
    for t in range(T - 2, -1, -1):
        mc_returns[t] = rewards[t + 1] + discount * mc_returns[t + 1]
    return mc_returns


@torch.no_grad()
def analyze_model(wm, value_head, episodes, device, has_dt_emb, discount):
    all_v_preds = []
    all_mc_returns = []
    all_timesteps = []

    for ep_idx, ep in enumerate(episodes):
        T = ep["action"].shape[0]
        if T <= 15:
            continue

        mc_rets = compute_mc_returns(ep["reward"], discount)

        obs = {k: torch.tensor(ep[k], dtype=torch.float32, device=device).unsqueeze(0)
               for k in OBS_KEYS}
        action = torch.tensor(ep["action"], dtype=torch.float32, device=device).unsqueeze(0)
        is_first = torch.zeros(1, T, dtype=torch.float32, device=device)
        is_first[:, 0] = 1.0

        embed = wm.encoder(obs)
        dt_labels = torch.ones(1, T, dtype=torch.long, device=device) if has_dt_emb else None
        post, _ = wm.dynamics.observe(embed, action, is_first, dt_labels=dt_labels)

        feat = wm.dynamics.get_feat(post)
        v_dist = value_head(feat)
        v_pred = v_dist.mode().squeeze(-1).squeeze(0).cpu().numpy()

        start, end = 5, T - 10
        if end <= start:
            continue
        all_v_preds.extend(v_pred[start:end])
        all_mc_returns.extend(mc_rets[start:end])
        all_timesteps.extend(range(start, end))

    return np.array(all_v_preds), np.array(all_mc_returns), np.array(all_timesteps)


def compute_stats(v_preds, mc_returns):
    diff = v_preds - mc_returns
    valid = mc_returns != 0
    ratio = np.full_like(v_preds, np.nan)
    ratio[valid] = v_preds[valid] / mc_returns[valid]

    stats = {
        "n_samples": len(v_preds),
        "v_pred_mean": float(np.mean(v_preds)),
        "v_pred_std": float(np.std(v_preds)),
        "mc_return_mean": float(np.mean(mc_returns)),
        "mc_return_std": float(np.std(mc_returns)),
        "bias_mean": float(np.mean(diff)),
        "bias_std": float(np.std(diff)),
        "bias_median": float(np.median(diff)),
        "rmse": float(np.sqrt(np.mean(diff ** 2))),
        "overestimation_rate": float(np.mean(diff > 0)),
        "ratio_mean": float(np.nanmean(ratio)),
        "ratio_std": float(np.nanstd(ratio)),
        "ratio_median": float(np.nanmedian(ratio)),
        "ratio_95th": float(np.nanpercentile(ratio, 95)),
        "ratio_5th": float(np.nanpercentile(ratio, 5)),
        "correlation": float(np.corrcoef(v_preds, mc_returns)[0, 1])
            if len(v_preds) > 1 else 0.0,
    }
    return stats


def make_figure(results, outdir):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    model_order = ["baseline_s1", "exp_008d_subsample_on_h8",
                    "exp_008f_no_dt_embed_subsample_on_h8"]
    titles = [
        "Baseline (dt=1, no gate)",
        "Trained dt_emb (CIVO collapsed)",
        "No dt_emb control (dt_embed_dim=0)",
    ]

    global_min = float("inf")
    global_max = float("-inf")
    for name in model_order:
        if name in results and "v_preds" in results[name]:
            v = results[name]["v_preds"]
            mc = results[name]["mc_returns"]
            global_min = min(global_min, np.min(v), np.min(mc))
            global_max = max(global_max, np.max(v), np.max(mc))

    pad = (global_max - global_min) * 0.05
    lim = (global_min - pad, global_max + pad)

    for idx, (name, title) in enumerate(zip(model_order, titles)):
        ax = axes[idx]
        if name not in results or "v_preds" not in results[name]:
            ax.set_title(f"{title}\n(no data)")
            ax.set_xlim(lim)
            ax.set_ylim(lim)
            continue

        v = results[name]["v_preds"]
        mc = results[name]["mc_returns"]
        stats = results[name]["stats"]

        hb = ax.hexbin(mc, v, gridsize=60, cmap="YlOrRd", mincnt=1,
                       norm=LogNorm())
        ax.plot(lim, lim, "k--", lw=1.5, alpha=0.7, label="Perfect calibration")

        ax.set_xlim(lim)
        ax.set_ylim(lim)
        ax.set_xlabel("MC Return (actual)", fontsize=12)
        if idx == 0:
            ax.set_ylabel("V(s) prediction", fontsize=12)
        ax.set_title(title, fontsize=11, fontweight="bold")
        ax.set_aspect("equal")

        textstr = (
            f"Bias: {stats['bias_mean']:.2f} ± {stats['bias_std']:.2f}\n"
            f"RMSE: {stats['rmse']:.2f}\n"
            f"Overest: {stats['overestimation_rate']:.1%}\n"
            f"V/MC: {stats['ratio_mean']:.3f} (p95={stats['ratio_95th']:.3f})\n"
            f"r = {stats['correlation']:.3f}"
        )
        ax.text(0.03, 0.97, textstr, transform=ax.transAxes, fontsize=8,
                verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

        plt.colorbar(hb, ax=ax, label="Count", shrink=0.8)

    fig.suptitle("Value Calibration: V(s) vs Monte Carlo Return",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()

    for fmt in ["pdf", "png"]:
        fig.savefig(outdir / f"value_distribution.{fmt}",
                    dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Figures saved to {outdir}", flush=True)


def make_ratio_histogram(results, outdir):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    model_order = ["baseline_s1", "exp_008d_subsample_on_h8",
                    "exp_008f_no_dt_embed_subsample_on_h8"]
    titles = [
        "Baseline (dt=1)",
        "Trained dt_emb (CIVO)",
        "No dt_emb control",
    ]
    colors = ["#2196F3", "#F44336", "#4CAF50"]

    for idx, (name, title, color) in enumerate(zip(model_order, titles, colors)):
        ax = axes[idx]
        if name not in results or "v_preds" not in results[name]:
            ax.set_title(f"{title}\n(no data)")
            continue

        v = results[name]["v_preds"]
        mc = results[name]["mc_returns"]
        valid = mc != 0
        ratio = v[valid] / mc[valid]
        ratio_clipped = np.clip(ratio, -5, 10)

        ax.hist(ratio_clipped, bins=100, color=color, alpha=0.7, edgecolor="black",
                linewidth=0.3)
        ax.axvline(x=1.0, color="black", linestyle="--", lw=1.5,
                   label="Perfect (ratio=1)")
        ax.axvline(x=np.median(ratio), color="red", linestyle="-", lw=1.5,
                   label=f"Median={np.median(ratio):.3f}")
        ax.set_xlabel("V(s) / MC Return", fontsize=12)
        if idx == 0:
            ax.set_ylabel("Count", fontsize=12)
        ax.set_title(title, fontsize=11, fontweight="bold")
        ax.legend(fontsize=8)

    fig.suptitle("Distribution of V(s) / MC Return Ratio",
                 fontsize=14, fontweight="bold", y=1.02)
    fig.tight_layout()
    for fmt in ["pdf", "png"]:
        fig.savefig(outdir / f"value_ratio_histogram.{fmt}",
                    dpi=200, bbox_inches="tight")
    plt.close(fig)


def make_bias_vs_timestep(results, outdir):
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    model_order = ["baseline_s1", "exp_008d_subsample_on_h8",
                    "exp_008f_no_dt_embed_subsample_on_h8"]
    labels = ["Baseline (dt=1)", "Trained dt_emb (CIVO)", "No dt_emb control"]
    colors = ["#2196F3", "#F44336", "#4CAF50"]

    for name, label, color in zip(model_order, labels, colors):
        if name not in results or "v_preds" not in results[name]:
            continue
        v = results[name]["v_preds"]
        mc = results[name]["mc_returns"]
        ts = results[name]["timesteps"]
        bias = v - mc

        unique_ts = np.unique(ts)
        mean_bias = []
        std_bias = []
        for t in unique_ts:
            mask = ts == t
            mean_bias.append(np.mean(bias[mask]))
            std_bias.append(np.std(bias[mask]))
        mean_bias = np.array(mean_bias)
        std_bias = np.array(std_bias)

        ax.plot(unique_ts, mean_bias, color=color, label=label, lw=2)
        ax.fill_between(unique_ts, mean_bias - std_bias, mean_bias + std_bias,
                        color=color, alpha=0.15)

    ax.axhline(y=0, color="black", linestyle="--", lw=1, alpha=0.5)
    ax.set_xlabel("Timestep in Episode", fontsize=12)
    ax.set_ylabel("V(s) - MC Return (bias)", fontsize=12)
    ax.set_title("Value Estimation Bias vs Episode Timestep", fontsize=13,
                 fontweight="bold")
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    for fmt in ["pdf", "png"]:
        fig.savefig(outdir / f"value_bias_vs_timestep.{fmt}",
                    dpi=200, bbox_inches="tight")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()
    device = args.device

    print(f"Device: {device}", flush=True)

    logdir = Path("/root/autodl-tmp/event-gated-adaptive-horizon/logdir")
    outdir = logdir / "exp_064_value_distribution"
    outdir.mkdir(exist_ok=True)

    model_configs = OrderedDict([
        ("baseline_s1", {
            "ckpt": logdir / "baseline_s1" / "latest.pt",
            "episodes": logdir / "baseline_s1" / "train_eps",
            "gate_enabled": False,
            "gate_dt_embed_dim": 0,
            "description": "dt=1 only baseline, no gate, no dt_embedding",
        }),
        ("exp_008d_subsample_on_h8", {
            "ckpt": logdir / "exp_008d_subsample_on_h8" / "latest.pt",
            "episodes": logdir / "exp_008d_subsample_on_h8" / "train_eps",
            "gate_enabled": True,
            "gate_dt_embed_dim": 32,
            "description": "gate_enabled + trained dt_embedding (collapsed CIVO)",
        }),
        ("exp_008f_no_dt_embed_subsample_on_h8", {
            "ckpt": logdir / "exp_008f_no_dt_embed_subsample_on_h8" / "latest.pt",
            "episodes": logdir / "exp_008f_no_dt_embed_subsample_on_h8" / "train_eps",
            "gate_enabled": True,
            "gate_dt_embed_dim": 0,
            "description": "gate + dt_embed_dim=0 control (no dt embedding)",
        }),
    ])

    results = {}

    for name, mcfg in model_configs.items():
        ckpt_path = mcfg["ckpt"]
        episodes_dir = mcfg["episodes"]

        if not ckpt_path.exists():
            print(f"SKIP {name}: no checkpoint at {ckpt_path}", flush=True)
            results[name] = {"error": f"checkpoint not found: {str(ckpt_path)}"}
            continue
        if not episodes_dir.exists():
            print(f"SKIP {name}: no episodes at {episodes_dir}", flush=True)
            results[name] = {"error": f"no episode data: {str(episodes_dir)}"}
            continue

        print(f"\n{'='*60}", flush=True)
        print(f"Model: {name}", flush=True)
        print(f"  {mcfg['description']}", flush=True)

        config = make_config(
            device=device,
            gate_enabled=mcfg["gate_enabled"],
            gate_dt_embed_dim=mcfg["gate_dt_embed_dim"],
        )

        try:
            wm = load_world_model(ckpt_path, config)
            value_head = load_value_head(ckpt_path, config, device)
            has_dt_emb = wm.dynamics._dt_embedding is not None
            episodes = load_episodes(episodes_dir, NUM_EPISODES)
            print(f"  {len(episodes)} episodes loaded, has_dt_emb={has_dt_emb}",
                  flush=True)

            v_preds, mc_returns, timesteps = analyze_model(
                wm, value_head, episodes, device, has_dt_emb, DISCOUNT)
            stats = compute_stats(v_preds, mc_returns)

            results[name] = {
                "v_preds": v_preds,
                "mc_returns": mc_returns,
                "timesteps": timesteps,
                "stats": stats,
                "config": {
                    "gate_enabled": mcfg["gate_enabled"],
                    "dt_embed_dim": mcfg["gate_dt_embed_dim"],
                    "description": mcfg["description"],
                },
            }

            print(f"\n  Statistics:", flush=True)
            print(f"    N samples:         {stats['n_samples']}", flush=True)
            print(f"    V(s) mean:         {stats['v_pred_mean']:.4f}", flush=True)
            print(f"    MC return mean:    {stats['mc_return_mean']:.4f}", flush=True)
            print(f"    Bias (V-MC):       {stats['bias_mean']:.4f} ± {stats['bias_std']:.4f}",
                  flush=True)
            print(f"    RMSE:              {stats['rmse']:.4f}", flush=True)
            print(f"    Overestimation:    {stats['overestimation_rate']:.1%}", flush=True)
            print(f"    V/MC ratio:        {stats['ratio_mean']:.4f} (median={stats['ratio_median']:.4f})",
                  flush=True)
            print(f"    Ratio 95th pctl:   {stats['ratio_95th']:.4f}", flush=True)
            print(f"    Correlation:       {stats['correlation']:.4f}", flush=True)

            del wm, value_head
            torch.cuda.empty_cache()

        except Exception as e:
            import traceback
            traceback.print_exc()
            results[name] = {"error": str(e)}

    # Generate figures
    print(f"\n{'='*60}", flush=True)
    print("Generating figures...", flush=True)
    make_figure(results, outdir)
    make_ratio_histogram(results, outdir)
    make_bias_vs_timestep(results, outdir)

    # Cross-model comparison
    print(f"\n{'='*60}", flush=True)
    print("CROSS-MODEL COMPARISON", flush=True)
    print(f"{'='*60}", flush=True)

    header = f"{'Model':<45} {'Bias':>10} {'RMSE':>10} {'Overest%':>10} {'V/MC':>10} {'r':>8}"
    print(header, flush=True)
    print("-" * len(header), flush=True)
    for name, res in results.items():
        if "error" in res:
            print(f"{name:<45} ERROR: {res['error']}", flush=True)
            continue
        s = res["stats"]
        print(f"{name:<45} {s['bias_mean']:>10.3f} {s['rmse']:>10.3f} "
              f"{s['overestimation_rate']:>9.1%} {s['ratio_mean']:>10.3f} "
              f"{s['correlation']:>8.3f}", flush=True)

    # Key findings
    base = results.get("baseline_s1", {})
    civo = results.get("exp_008d_subsample_on_h8", {})
    ctrl = results.get("exp_008f_no_dt_embed_subsample_on_h8", {})

    if all("stats" in r for r in [base, civo, ctrl]):
        print(f"\n{'='*60}", flush=True)
        print("KEY FINDINGS", flush=True)
        print(f"{'='*60}", flush=True)

        bs = base["stats"]
        cs = civo["stats"]
        cts = ctrl["stats"]

        if cs["bias_mean"] > bs["bias_mean"] * 1.2:
            print(f"  >> VALUE OVERESTIMATION CONFIRMED in CIVO model", flush=True)
            print(f"     CIVO bias ({cs['bias_mean']:.3f}) vs baseline ({bs['bias_mean']:.3f}): "
                  f"{cs['bias_mean']/max(abs(bs['bias_mean']), 1e-6):.1f}x", flush=True)
        if cs["overestimation_rate"] > bs["overestimation_rate"]:
            print(f"  >> CIVO overestimation rate ({cs['overestimation_rate']:.1%}) > "
                  f"baseline ({bs['overestimation_rate']:.1%})", flush=True)
        if cts["bias_mean"] < cs["bias_mean"]:
            print(f"  >> Control (no dt_emb) has lower bias ({cts['bias_mean']:.3f}) "
                  f"than CIVO ({cs['bias_mean']:.3f})", flush=True)
            print(f"     => dt_embedding is the source of overestimation", flush=True)

    # Save results (without numpy arrays)
    json_results = {}
    for name, res in results.items():
        if "error" in res:
            json_results[name] = res
        else:
            json_results[name] = {
                "stats": res["stats"],
                "config": res["config"],
            }

    output = {
        "experiment": "exp_064_value_distribution",
        "analysis": "V(s) vs Monte Carlo return — value overestimation diagnosis",
        "discount": DISCOUNT,
        "num_episodes": NUM_EPISODES,
        "models": list(json_results.keys()),
        "results": json_results,
    }

    out_path = outdir / "results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

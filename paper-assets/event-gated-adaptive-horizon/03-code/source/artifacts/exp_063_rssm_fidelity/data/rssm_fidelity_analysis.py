"""exp_063: RSSM Fidelity Analysis — dt=1 vs dt=2 prediction quality gap.

Quantifies whether RSSM can faithfully predict multi-step (dt=2) transitions.
Tests:
  - dt=1 single-step: img_step(dt=1) -> compare with obs_{t+1}
  - dt=2 single-step (dt_emb models only): img_step(dt=2) -> compare with obs_{t+2}
  - dt=2 chained: 2x img_step(dt=1) -> compare with obs_{t+2}

Models:
  - baseline_s1: pure dt=1 baseline (no gate, no dt_embedding)
  - exp_008d_subsample_on_h8: gate_enabled + trained dt_embedding (collapsed)
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

CODE_DIR = Path("/root/autodl-tmp/event-gated-adaptive-horizon")
sys.path.insert(0, str(CODE_DIR))

import models
import networks
import tools

NUM_EPISODES = 20
OBS_KEYS = ["height", "orientations", "velocity"]
OBS_SHAPES = OrderedDict([
    ("height", (1,)),
    ("orientations", (14,)),
    ("velocity", (9,)),
])
NUM_ACTIONS = 6


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
        grad_heads=["decoder", "reward", "cont"],
        model_lr=1e-4, opt_eps=1e-8, grad_clip=1000, weight_decay=0.0, opt="adam",
        gate_enabled=gate_enabled, gate_max_dt=gate_max_dt,
        gate_dt_embed_dim=gate_dt_embed_dim,
        gate_hidden_units=256, gate_hidden_layers=2,
        gate_tau_init=5.0, gate_tau_final=0.5, gate_tau_anneal_steps=200000,
        gate_loss_weight=1.0,
        gate_entropy_bonus_init=0.1, gate_entropy_bonus_final=0.01,
        gate_curriculum_phase1=50000, gate_curriculum_phase2=150000,
        discount=0.997,
        compile=False,
        dt_emb_freeze=False,
        gate_type="gumbel",
        gate_fixed_dt=0,
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


def load_episodes(episodes_dir, num_episodes):
    files = sorted(Path(episodes_dir).glob("*.npz"))
    if len(files) > num_episodes:
        files = files[-num_episodes:]
    return [dict(np.load(f)) for f in files]


def decode_obs(wm, feat):
    pred = wm.heads["decoder"](feat)
    result = {}
    for k in OBS_KEYS:
        if hasattr(pred[k], "mode"):
            result[k] = pred[k].mode()
        elif hasattr(pred[k], "mean"):
            result[k] = pred[k].mean
        else:
            result[k] = pred[k]
    return result


def pred_reward(wm, feat):
    r = wm.heads["reward"](feat)
    if hasattr(r, "mode"):
        return r.mode()
    elif hasattr(r, "mean"):
        return r.mean
    return r


@torch.no_grad()
def analyze_model(wm, episodes, device, has_dt_emb):
    results = {}

    test_configs = [
        ("dt1_single", 1, "single"),
        ("dt2_chained", 2, "chained"),
    ]
    if has_dt_emb:
        test_configs.append(("dt2_single", 2, "single"))

    for test_name, target_dt, mode in test_configs:
        obs_mse_per_key = {k: [] for k in OBS_KEYS}
        obs_mae_per_key = {k: [] for k in OBS_KEYS}
        reward_mae_list = []

        for ep in episodes:
            T = ep["action"].shape[0]
            if T <= 10 + target_dt:
                continue

            obs = {k: torch.tensor(ep[k], dtype=torch.float32, device=device).unsqueeze(0)
                   for k in OBS_KEYS}
            action = torch.tensor(ep["action"], dtype=torch.float32, device=device).unsqueeze(0)
            reward = torch.tensor(ep["reward"], dtype=torch.float32, device=device).unsqueeze(0)
            is_first = torch.zeros(1, T, dtype=torch.float32, device=device)
            is_first[:, 0] = 1.0

            embed = wm.encoder(obs)
            dt_labels = torch.ones(1, T, dtype=torch.long, device=device) if has_dt_emb else None
            post, _ = wm.dynamics.observe(embed, action, is_first, dt_labels=dt_labels)

            num_test = min(T - 10 - target_dt, 40)

            for t in range(5, 5 + num_test):
                target_t = t + target_dt
                if target_t >= T:
                    continue

                state_t = {k: v[:, t] for k, v in post.items()}

                if mode == "single" and has_dt_emb and target_dt > 1:
                    dt_val = torch.tensor([target_dt], dtype=torch.long, device=device)
                    state_pred = wm.dynamics.img_step(state_t, action[:, t], dt=dt_val)
                elif mode == "chained":
                    state_pred = state_t
                    for step in range(target_dt):
                        act_idx = t + step
                        if act_idx >= T:
                            break
                        dt_val = torch.tensor([1], dtype=torch.long, device=device) if has_dt_emb else None
                        state_pred = wm.dynamics.img_step(state_pred, action[:, act_idx], dt=dt_val)
                else:
                    dt_val = torch.tensor([1], dtype=torch.long, device=device) if has_dt_emb else None
                    state_pred = wm.dynamics.img_step(state_t, action[:, t], dt=dt_val)

                feat = wm.dynamics.get_feat(state_pred)
                pred_obs = decode_obs(wm, feat)
                pred_rew = pred_reward(wm, feat)

                for k in OBS_KEYS:
                    target = obs[k][:, target_t]
                    pred_val = pred_obs[k]
                    obs_mse_per_key[k].append(((pred_val - target) ** 2).mean().item())
                    obs_mae_per_key[k].append((pred_val - target).abs().mean().item())

                target_rew = reward[:, target_t]
                reward_mae_list.append((pred_rew - target_rew).abs().mean().item())

        results[test_name] = {
            "obs_mse": {k: float(np.mean(v)) if v else 0.0
                       for k, v in obs_mse_per_key.items()},
            "obs_mse_total": float(np.mean([np.mean(v) for v in obs_mse_per_key.values() if v]))
                            if any(v for v in obs_mse_per_key.values()) else 0.0,
            "obs_mae": {k: float(np.mean(v)) if v else 0.0
                       for k, v in obs_mae_per_key.items()},
            "obs_mae_total": float(np.mean([np.mean(v) for v in obs_mae_per_key.values() if v]))
                            if any(v for v in obs_mae_per_key.values()) else 0.0,
            "reward_mae": float(np.mean(reward_mae_list)) if reward_mae_list else 0.0,
            "n_samples": len(reward_mae_list),
            "mode": mode,
            "target_dt": target_dt,
        }

    dt1 = results.get("dt1_single", {})
    dt2c = results.get("dt2_chained", {})
    dt2s = results.get("dt2_single", {})

    gaps = {}
    if dt1.get("obs_mse_total", 0) > 0:
        if dt2c.get("obs_mse_total", 0) > 0:
            gaps["chained_dt2_over_dt1"] = {
                "obs_mse_ratio": dt2c["obs_mse_total"] / dt1["obs_mse_total"],
                "reward_mae_ratio": dt2c["reward_mae"] / dt1["reward_mae"]
                                    if dt1["reward_mae"] > 0 else float("inf"),
            }
        if dt2s.get("obs_mse_total", 0) > 0:
            gaps["single_dt2_over_dt1"] = {
                "obs_mse_ratio": dt2s["obs_mse_total"] / dt1["obs_mse_total"],
                "reward_mae_ratio": dt2s["reward_mae"] / dt1["reward_mae"]
                                    if dt1["reward_mae"] > 0 else float("inf"),
            }
    if dt2s.get("obs_mse_total", 0) > 0 and dt2c.get("obs_mse_total", 0) > 0:
        gaps["single_over_chained_dt2"] = {
            "obs_mse_ratio": dt2s["obs_mse_total"] / dt2c["obs_mse_total"],
            "reward_mae_ratio": dt2s["reward_mae"] / dt2c["reward_mae"]
                                if dt2c["reward_mae"] > 0 else float("inf"),
        }
    results["fidelity_gaps"] = gaps

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()
    device = args.device

    print(f"Device: {device}", flush=True)

    logdir = Path("/root/autodl-tmp/event-gated-adaptive-horizon/logdir")
    outdir = logdir / "exp_063_rssm_fidelity"
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
    ])

    all_results = {}

    for name, mcfg in model_configs.items():
        ckpt_path = mcfg["ckpt"]
        episodes_dir = mcfg["episodes"]

        if not ckpt_path.exists():
            print(f"SKIP {name}: no checkpoint at {ckpt_path}", flush=True)
            all_results[name] = {"error": f"checkpoint not found: {ckpt_path}"}
            continue
        if not episodes_dir.exists():
            print(f"SKIP {name}: no episodes at {episodes_dir}", flush=True)
            all_results[name] = {"error": f"no episode data: {episodes_dir}"}
            continue

        print(f"\n{'='*60}", flush=True)
        print(f"Model: {name}", flush=True)
        print(f"  {mcfg['description']}", flush=True)
        print(f"  ckpt: {ckpt_path}", flush=True)

        config = make_config(
            device=device,
            gate_enabled=mcfg["gate_enabled"],
            gate_dt_embed_dim=mcfg["gate_dt_embed_dim"],
        )

        try:
            wm = load_world_model(ckpt_path, config)
            has_dt_emb = wm.dynamics._dt_embedding is not None
            episodes = load_episodes(episodes_dir, NUM_EPISODES)
            print(f"  {len(episodes)} episodes loaded, has_dt_emb={has_dt_emb}", flush=True)

            res = analyze_model(wm, episodes, device, has_dt_emb)
            res["config"] = {
                "gate_enabled": mcfg["gate_enabled"],
                "dt_embed_dim": mcfg["gate_dt_embed_dim"],
                "experiment": name,
                "description": mcfg["description"],
            }
            all_results[name] = res

            print(f"\n  Results:", flush=True)
            for test_k in ["dt1_single", "dt2_chained", "dt2_single"]:
                if test_k in res:
                    d = res[test_k]
                    print(f"    {test_k}: obs_mse={d['obs_mse_total']:.6f}  "
                          f"reward_mae={d['reward_mae']:.6f}  (n={d['n_samples']})",
                          flush=True)
                    print(f"      per-key MSE: "
                          + "  ".join(f"{k}={d['obs_mse'][k]:.6f}" for k in OBS_KEYS),
                          flush=True)

            if "fidelity_gaps" in res:
                print(f"\n  Fidelity gaps:", flush=True)
                for gk, gv in res["fidelity_gaps"].items():
                    print(f"    {gk}: obs_mse={gv['obs_mse_ratio']:.3f}x  "
                          f"reward={gv['reward_mae_ratio']:.3f}x", flush=True)

            del wm
            torch.cuda.empty_cache()

        except Exception as e:
            import traceback
            traceback.print_exc()
            all_results[name] = {"error": str(e)}

    print(f"\n{'='*60}", flush=True)
    print("CROSS-MODEL COMPARISON", flush=True)
    print(f"{'='*60}", flush=True)

    header = f"{'Model':<35} {'Test':<15} {'Obs MSE':>10} {'Reward MAE':>12} {'N':>6}"
    print(header, flush=True)
    print("-" * len(header), flush=True)
    for name, res in all_results.items():
        if "error" in res:
            print(f"{name:<35} ERROR: {res['error']}", flush=True)
            continue
        for test_k in ["dt1_single", "dt2_chained", "dt2_single"]:
            if test_k in res:
                d = res[test_k]
                print(f"{name:<35} {test_k:<15} {d['obs_mse_total']:>10.6f} "
                      f"{d['reward_mae']:>12.6f} {d['n_samples']:>6}", flush=True)

    if ("baseline_s1" in all_results and "error" not in all_results["baseline_s1"]
            and "exp_008d_subsample_on_h8" in all_results
            and "error" not in all_results["exp_008d_subsample_on_h8"]):
        base = all_results["baseline_s1"]
        coll = all_results["exp_008d_subsample_on_h8"]

        print(f"\n{'='*60}", flush=True)
        print("KEY FINDINGS", flush=True)
        print(f"{'='*60}", flush=True)

        base_gap = base.get("fidelity_gaps", {}).get("chained_dt2_over_dt1", {})
        coll_gap_s = coll.get("fidelity_gaps", {}).get("single_dt2_over_dt1", {})
        coll_gap_c = coll.get("fidelity_gaps", {}).get("chained_dt2_over_dt1", {})
        coll_sc = coll.get("fidelity_gaps", {}).get("single_over_chained_dt2", {})

        if base_gap:
            print(f"  Baseline dt2/dt1 (chained): obs_mse={base_gap.get('obs_mse_ratio', 0):.3f}x  "
                  f"reward={base_gap.get('reward_mae_ratio', 0):.3f}x", flush=True)
        if coll_gap_s:
            print(f"  Collapsed dt2/dt1 (single): obs_mse={coll_gap_s.get('obs_mse_ratio', 0):.3f}x  "
                  f"reward={coll_gap_s.get('reward_mae_ratio', 0):.3f}x", flush=True)
        if coll_gap_c:
            print(f"  Collapsed dt2/dt1 (chained): obs_mse={coll_gap_c.get('obs_mse_ratio', 0):.3f}x  "
                  f"reward={coll_gap_c.get('reward_mae_ratio', 0):.3f}x", flush=True)
        if coll_sc:
            print(f"  Collapsed single/chained dt2: obs_mse={coll_sc.get('obs_mse_ratio', 0):.3f}x  "
                  f"reward={coll_sc.get('reward_mae_ratio', 0):.3f}x", flush=True)

        if coll_gap_s.get("obs_mse_ratio", 0) > 1.2:
            print("\n  >> FIDELITY GAP CONFIRMED: collapsed model's dt=2 single-step "
                  f"prediction is {coll_gap_s['obs_mse_ratio']:.1f}x worse than dt=1.",
                  flush=True)
            print("  >> Even after training on dt=2 transitions, RSSM cannot faithfully "
                  "predict multi-step dynamics.", flush=True)
            print("  >> This supports the 'delusional critic' hypothesis: critic trained "
                  "on inaccurate imagined dt=2 rollouts develops overestimated values.",
                  flush=True)

    output = {
        "experiment": "exp_063_rssm_fidelity",
        "analysis": "RSSM prediction quality gap: dt=1 vs dt=2 (baseline vs collapsed)",
        "methodology": {
            "dt1_single": "From posterior state_t, 1 img_step (dt=1), compare decoded obs with obs_{t+1}",
            "dt2_single": "From posterior state_t, 1 img_step (dt=2 via embedding), compare with obs_{t+2}",
            "dt2_chained": "From posterior state_t, 2 sequential img_steps (dt=1 each), compare with obs_{t+2}",
        },
        "models": list(all_results.keys()),
        "results": all_results,
    }

    out_path = outdir / "results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()

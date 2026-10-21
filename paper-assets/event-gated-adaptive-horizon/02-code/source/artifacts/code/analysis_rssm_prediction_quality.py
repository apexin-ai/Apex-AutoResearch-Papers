"""RSSM Prediction Quality Analysis: dt=1 vs dt=2+
Quantifies observation prediction error when RSSM makes single-step vs multi-step predictions.
Supports models with and without dt_embedding.
Run on CPU to avoid interfering with active training jobs.
"""
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

CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR))

import models
import networks
import tools

DEVICE = "cpu"
NUM_EPISODES = 15
MAX_DT_TEST = 4

OBS_KEYS = ["height", "orientations", "velocity"]
OBS_SHAPES = OrderedDict([
    ("height", (1,)),
    ("orientations", (14,)),
    ("velocity", (9,)),
])
NUM_ACTIONS = 6


def make_config(gate_enabled, gate_max_dt=8, gate_dt_embed_dim=32):
    return SimpleNamespace(
        device=DEVICE, precision=32,
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

    ckpt = torch.load(ckpt_path, map_location=DEVICE)
    wm_state = {k[4:]: v for k, v in ckpt["agent_state_dict"].items() if k.startswith("_wm.")}
    wm.load_state_dict(wm_state, strict=True)
    wm.eval()
    return wm


def load_episodes(episodes_dir, num_episodes):
    files = sorted(Path(episodes_dir).glob("*.npz"))
    if len(files) > num_episodes:
        files = files[-num_episodes:]
    return [dict(np.load(f)) for f in files]


@torch.no_grad()
def analyze_model(wm, episodes, max_dt_test=MAX_DT_TEST):
    has_dt_emb = wm.dynamics._dt_embedding is not None
    results = {}

    for dt in range(1, max_dt_test + 1):
        obs_mse_per_key = {k: [] for k in OBS_KEYS}
        obs_mae_per_key = {k: [] for k in OBS_KEYS}
        reward_mae_list = []
        nll_per_key = {k: [] for k in OBS_KEYS}

        for ep in episodes:
            T = ep["action"].shape[0]
            if T <= dt + 2:
                continue

            obs = {k: torch.tensor(ep[k], dtype=torch.float32, device=DEVICE).unsqueeze(0) for k in OBS_KEYS}
            action = torch.tensor(ep["action"], dtype=torch.float32, device=DEVICE).unsqueeze(0)
            is_first = torch.tensor(ep["is_first"], dtype=torch.float32, device=DEVICE).unsqueeze(0)
            reward = torch.tensor(ep["reward"], dtype=torch.float32, device=DEVICE).unsqueeze(0)

            embed = wm.encoder(obs)
            post, _ = wm.dynamics.observe(embed, action, is_first)

            valid_T = T - dt
            post_flat = {k: v[0, :valid_T] for k, v in post.items()}
            action_flat = action[0, :valid_T]

            if has_dt_emb:
                dt_tensor = torch.full((valid_T,), dt, dtype=torch.long, device=DEVICE)
                pred_state = wm.dynamics.img_step(post_flat, action_flat, dt=dt_tensor, sample=False)
            else:
                pred_state = wm.dynamics.img_step(post_flat, action_flat, sample=False)

            feat = wm.dynamics.get_feat(pred_state).unsqueeze(0)
            pred_obs_dists = wm.heads["decoder"](feat)

            for k in OBS_KEYS:
                target = obs[k][:, dt:dt + valid_T]
                predicted = pred_obs_dists[k].mode()
                mse = ((predicted - target) ** 2).mean(dim=-1).mean().item()
                mae = (predicted - target).abs().mean(dim=-1).mean().item()
                nll = -pred_obs_dists[k].log_prob(target).mean().item()
                obs_mse_per_key[k].append(mse)
                obs_mae_per_key[k].append(mae)
                nll_per_key[k].append(nll)

            pred_reward_dist = wm.heads["reward"](feat)
            pred_reward = pred_reward_dist.mode()
            if pred_reward.dim() == 3:
                pred_reward = pred_reward.squeeze(-1)
            target_reward = reward[:, dt:dt + valid_T]
            reward_mae_list.append((pred_reward - target_reward).abs().mean().item())

        results[f"dt{dt}"] = {
            "obs_mse": {k: float(np.mean(v)) for k, v in obs_mse_per_key.items()},
            "obs_mse_total": float(np.mean([np.mean(v) for v in obs_mse_per_key.values()])),
            "obs_mae": {k: float(np.mean(v)) for k, v in obs_mae_per_key.items()},
            "obs_mae_total": float(np.mean([np.mean(v) for v in obs_mae_per_key.values()])),
            "obs_nll": {k: float(np.mean(v)) for k, v in nll_per_key.items()},
            "obs_nll_total": float(np.mean([np.mean(v) for v in nll_per_key.values()])),
            "reward_mae": float(np.mean(reward_mae_list)),
        }

    if "dt1" in results and "dt2" in results:
        results["fidelity_gap"] = {
            "obs_mse_ratio_dt2_over_dt1": results["dt2"]["obs_mse_total"] / max(results["dt1"]["obs_mse_total"], 1e-10),
            "obs_nll_ratio_dt2_over_dt1": results["dt2"]["obs_nll_total"] / max(abs(results["dt1"]["obs_nll_total"]), 1e-10),
            "reward_mae_ratio_dt2_over_dt1": results["dt2"]["reward_mae"] / max(results["dt1"]["reward_mae"], 1e-10),
            "per_key_mse_ratio": {
                k: results["dt2"]["obs_mse"][k] / max(results["dt1"]["obs_mse"][k], 1e-10)
                for k in OBS_KEYS
            },
        }

    return results


def main():
    logdir_root = Path("/root/autodl-tmp/event-gated-adaptive-horizon/logdir")

    model_configs = OrderedDict([
        ("baseline_s1", dict(gate_enabled=False, gate_max_dt=8, gate_dt_embed_dim=32)),
        ("exp_008d_subsample_on_h8", dict(gate_enabled=True, gate_max_dt=8, gate_dt_embed_dim=32)),
        ("exp_008f_no_dt_embed_subsample_on_h8", dict(gate_enabled=True, gate_max_dt=8, gate_dt_embed_dim=0)),
    ])

    all_results = {}

    for name, mcfg in model_configs.items():
        ckpt_path = logdir_root / name / "latest.pt"
        episodes_dir = logdir_root / name / "train_eps"

        if not ckpt_path.exists():
            print(f"SKIP {name}: no checkpoint")
            all_results[name] = {"error": "checkpoint not found"}
            continue
        if not episodes_dir.exists():
            print(f"SKIP {name}: no episodes")
            all_results[name] = {"error": "no episode data"}
            continue

        print(f"\n=== {name} ===")
        config = make_config(**mcfg)

        try:
            wm = load_world_model(ckpt_path, config)
            episodes = load_episodes(episodes_dir, NUM_EPISODES)
            print(f"  {len(episodes)} episodes loaded, has_dt_emb={wm.dynamics._dt_embedding is not None}")

            res = analyze_model(wm, episodes)
            res["config"] = {"gate_enabled": mcfg["gate_enabled"], "dt_embed_dim": mcfg["gate_dt_embed_dim"]}
            all_results[name] = res

            for dt_k in sorted(k for k in res if k.startswith("dt")):
                d = res[dt_k]
                print(f"  {dt_k}: obs_mse={d['obs_mse_total']:.6f}  reward_mae={d['reward_mae']:.4f}")
            if "fidelity_gap" in res:
                g = res["fidelity_gap"]
                print(f"  gap dt2/dt1: obs_mse={g['obs_mse_ratio_dt2_over_dt1']:.2f}x  reward={g['reward_mae_ratio_dt2_over_dt1']:.2f}x")

            del wm
        except Exception as e:
            import traceback
            traceback.print_exc()
            all_results[name] = {"error": str(e)}

    # Conclusion
    lines = []
    for name in model_configs:
        res = all_results.get(name, {})
        gap = res.get("fidelity_gap", {}).get("obs_mse_ratio_dt2_over_dt1")
        if gap is not None:
            lines.append(f"{name}: dt2/dt1 obs MSE ratio = {gap:.2f}x")

    bg = all_results.get("baseline_s1", {}).get("fidelity_gap", {}).get("obs_mse_ratio_dt2_over_dt1")
    dg = all_results.get("exp_008d_subsample_on_h8", {}).get("fidelity_gap", {}).get("obs_mse_ratio_dt2_over_dt1")
    ng = all_results.get("exp_008f_no_dt_embed_subsample_on_h8", {}).get("fidelity_gap", {}).get("obs_mse_ratio_dt2_over_dt1")

    if bg is not None and dg is not None:
        if dg < bg:
            lines.append(f"dt_embedding reduces fidelity gap ({dg:.2f}x vs baseline {bg:.2f}x), but dt=2 prediction is still worse than dt=1.")
        else:
            lines.append(f"dt_embedding does NOT reduce fidelity gap ({dg:.2f}x vs baseline {bg:.2f}x).")

    if dg is not None and ng is not None:
        lines.append(f"dt_embed ablation: with={dg:.2f}x, without={ng:.2f}x")

    dt1_baseline = all_results.get("baseline_s1", {}).get("dt1", {}).get("obs_mse_total")
    dt2_baseline = all_results.get("baseline_s1", {}).get("dt2", {}).get("obs_mse_total")
    if dt1_baseline and dt2_baseline and dt2_baseline > dt1_baseline * 1.3:
        lines.append(
            "RSSM prediction quality degrades for dt>1 transitions. "
            "This supports C2 (delusional critic): the world model is less accurate "
            "at multi-step transitions, leading to value overestimation when the critic "
            "trusts dt>1 imagined trajectories."
        )

    conclusion = "\n".join(lines) if lines else "Insufficient data for conclusion."

    output = {
        "analysis": "RSSM prediction quality: dt=1 vs dt=2",
        "description": (
            "Measures observation reconstruction MSE/MAE and reward prediction MAE "
            "from RSSM posterior states at varying temporal gaps. "
            "For models WITH dt_embedding, img_step is conditioned on dt. "
            "For models WITHOUT, prediction is always dt=1 style (dt param ignored). "
            "Fidelity gap = dt2_error / dt1_error."
        ),
        "models_analyzed": list(all_results.keys()),
        "results": all_results,
        "conclusion": conclusion,
    }

    out_path = logdir_root / "analysis_rssm_prediction_quality.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()

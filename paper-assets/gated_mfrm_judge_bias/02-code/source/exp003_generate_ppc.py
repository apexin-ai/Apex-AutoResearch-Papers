"""Generate posterior predictive samples for exp-003b G-MFRM.

Loads existing InferenceData (DataTree), runs Predictive with subsampled
posterior, saves new file with posterior_predictive group, and generates
a PPC diagnostic plot.
"""
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["JAX_PLATFORMS"] = "cuda,cpu"
os.environ["XLA_PYTHON_CLIENT_PREALLOCATE"] = "false"
os.environ["XLA_PYTHON_CLIENT_MEM_FRACTION"] = "0.25"

import sys
sys.path.insert(0, "/root/gated_mfrm_judge_bias/exp003")

import numpy as np
import jax
import jax.numpy as jnp
import numpyro
from numpyro.infer import Predictive
import xarray as xr
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from data_loader import load_data
from models import _gmfrm_model

IDATA_PATH = "/root/gated_mfrm_judge_bias/exp003/output_003b/joint_gmfrm_idata.nc"
OUTPUT_PATH = "/root/gated_mfrm_judge_bias/exp003/output_003b/joint_gmfrm_idata_with_ppc.nc"
PPC_PLOT_PATH = "/root/gated_mfrm_judge_bias/artifacts/exp003b_diagnostics/ppc.pdf"
N_PPC = 1000

numpyro.set_host_device_count(1)


def main():
    # 1. Load InferenceData
    print("Loading InferenceData...")
    dt = xr.open_datatree(IDATA_PATH)
    posterior = dt["posterior"].dataset
    print(f"  Posterior: {dict(posterior.dims)}")

    # 2. Load original data
    print("\nLoading original data...")
    data = load_data(
        "/root/gated_mfrm_judge_bias/exp001/results",
        "/root/gated_mfrm_judge_bias/exp002/results/exposure_scores.csv",
    )
    print(f"  N={data['N']}, I={data['I']}, J={data['J']}, n_obs={data['n_obs']}")

    # 3. Extract posterior samples (flatten chain × draw)
    print("\nExtracting posterior samples...")
    sample_vars = ["theta_raw", "b", "d_raw", "sigma_c", "c_raw"]
    samples = {}
    for var in sample_vars:
        arr = posterior[var].values
        flat = arr.reshape((-1,) + arr.shape[2:])
        samples[var] = jnp.array(flat)
        print(f"  {var}: {arr.shape} -> {flat.shape}")

    n_total = samples["theta_raw"].shape[0]
    print(f"  Total posterior samples: {n_total}")

    # 4. Subsample
    rng = np.random.default_rng(42)
    idx = np.sort(rng.choice(n_total, size=N_PPC, replace=False))
    sub_samples = {k: v[idx] for k, v in samples.items()}
    print(f"  Subsampled to {N_PPC}")

    # 5. Prepare model inputs
    model_idx = jnp.array(data["model_idx"])
    item_idx = jnp.array(data["item_idx"])
    judge_idx = jnp.array(data["judge_idx"])
    e = jnp.array(data["e_i"], dtype=jnp.float32)

    # 6. Run Predictive (y=None to sample obs instead of conditioning)
    print("\nRunning Predictive...")
    predictive = Predictive(
        _gmfrm_model,
        posterior_samples=sub_samples,
        return_sites=["obs"],
    )
    ppc = predictive(
        jax.random.PRNGKey(0),
        model_idx=model_idx,
        item_idx=item_idx,
        judge_idx=judge_idx,
        y=None,
        e=e,
        N=data["N"],
        I=data["I"],
        J=data["J"],
    )

    obs_ppc = np.asarray(ppc["obs"])
    print(f"  PPC shape: {obs_ppc.shape}")
    print(f"  PPC mean win rate: {obs_ppc.mean():.4f}")
    print(f"  Observed mean win rate: {data['y'].mean():.4f}")

    # 7. Build posterior_predictive DataTree group
    ppc_ds = xr.Dataset(
        {"obs": (["chain", "draw", "obs_dim_0"], obs_ppc[np.newaxis, :, :].astype(np.float32))},
        coords={
            "chain": [0],
            "draw": np.arange(N_PPC),
            "obs_dim_0": np.arange(obs_ppc.shape[1]),
        },
        attrs={
            "created_at": str(np.datetime64("now")),
            "creation_library": "ArviZ",
            "creation_library_version": "1.1.0",
            "inference_library": "numpyro",
            "sample_dims": ["chain", "draw"],
        },
    )

    # 8. Save new DataTree with posterior_predictive
    print("\nSaving...")
    dt_new = dt.copy()
    dt_new["posterior_predictive"] = xr.DataTree(dataset=ppc_ds)
    dt_new.to_netcdf(OUTPUT_PATH)
    file_mb = os.path.getsize(OUTPUT_PATH) / 1024 / 1024
    print(f"  Saved: {OUTPUT_PATH} ({file_mb:.1f} MB)")

    # 9. Verify
    print("\nVerification:")
    dt_verify = xr.open_datatree(OUTPUT_PATH)
    print(dt_verify)

    # 10. PPC plot
    print("\nGenerating PPC plot...")
    os.makedirs(os.path.dirname(PPC_PLOT_PATH), exist_ok=True)

    observed_y = data["y"]
    obs_win_rate = observed_y.mean()

    # Per-draw win rates
    ppc_win_rates = obs_ppc.mean(axis=1)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # Left: histogram of PPC win rates vs observed
    axes[0].hist(ppc_win_rates, bins=40, density=True, alpha=0.7, color="steelblue", label="PPC draws")
    axes[0].axvline(obs_win_rate, color="red", linewidth=2, label=f"Observed ({obs_win_rate:.3f})")
    axes[0].set_xlabel("Mean win rate per draw")
    axes[0].set_ylabel("Density")
    axes[0].set_title("PPC: Overall win rate")
    axes[0].legend()

    # Right: per-model PPC win rates vs observed
    model_names = data["model_names"]
    model_idx_np = data["model_idx"]
    n_models = data["N"]
    obs_model_wr = []
    ppc_model_wr_mean = []
    ppc_model_wr_low = []
    ppc_model_wr_high = []

    for n in range(n_models):
        mask = model_idx_np == n
        obs_model_wr.append(observed_y[mask].mean())
        model_ppc = obs_ppc[:, mask].mean(axis=1)
        ppc_model_wr_mean.append(model_ppc.mean())
        ppc_model_wr_low.append(np.percentile(model_ppc, 2.5))
        ppc_model_wr_high.append(np.percentile(model_ppc, 97.5))

    y_pos = np.arange(n_models)
    axes[1].barh(y_pos, obs_model_wr, height=0.4, alpha=0.7, color="red", label="Observed")
    axes[1].errorbar(
        ppc_model_wr_mean, y_pos,
        xerr=[np.array(ppc_model_wr_mean) - np.array(ppc_model_wr_low),
              np.array(ppc_model_wr_high) - np.array(ppc_model_wr_mean)],
        fmt="o", color="steelblue", capsize=3, label="PPC (95% CI)"
    )
    axes[1].set_yticks(y_pos)
    short_names = [n.split("/")[-1][:20] for n in model_names]
    axes[1].set_yticklabels(short_names, fontsize=8)
    axes[1].set_xlabel("Win rate")
    axes[1].set_title("PPC: Per-model win rate")
    axes[1].legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(PPC_PLOT_PATH, bbox_inches="tight")
    print(f"  PPC plot saved: {PPC_PLOT_PATH}")

    print("\nDone.")


if __name__ == "__main__":
    main()

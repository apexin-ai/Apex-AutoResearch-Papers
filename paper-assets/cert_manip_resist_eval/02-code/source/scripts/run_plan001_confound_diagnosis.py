#!/usr/bin/env python3
"""Plan 001: K_eff vs eta_max confound diagnosis across all C(15,3) panels."""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import itertools
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from scipy import stats

from src.utils import setup_logging
from src.unified_data_loader import (
    ALL_MODELS, LOCAL_MODELS, API_MODELS, DATASETS, ATTACKS,
    PLAN001_DIR, SCORES_DIR,
    load_all_scores, load_pairs, load_mi_data, load_api_asr,
)

logger = setup_logging("plan001_confound")


def compute_asr_from_scores(clean_scores, attacked_scores, pairs):
    n_flips = 0
    n_total = 0
    for clean, attacked, pair in zip(clean_scores, attacked_scores, pairs):
        gt = pair.get("ground_truth_winner")
        cw = clean.get("winner") if isinstance(clean, dict) else None
        aw = attacked.get("winner") if isinstance(attacked, dict) else None
        if cw == gt:
            n_total += 1
            if aw != gt:
                n_flips += 1
    return n_flips / max(n_total, 1)


def compute_all_individual_asr(clean, attacked, pairs):
    """Compute per-model ASR from loaded scores and pairs.

    Returns: {ds: {atk: {model_id: asr}}}
    """
    asr_data = {}
    for ds in DATASETS:
        asr_data[ds] = {}
        for atk in ATTACKS:
            asr_data[ds][atk] = {}
            for mid in ALL_MODELS:
                if mid not in clean[ds] or mid not in attacked[ds][atk]:
                    continue
                if ds not in pairs:
                    continue
                asr = compute_asr_from_scores(
                    clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
                )
                asr_data[ds][atk][mid] = asr
    # Overlay pre-computed API ASR (from individual files) where available
    api_asr = load_api_asr()
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid, asr in api_asr.get(ds, {}).get(atk, {}).items():
                if mid not in asr_data[ds][atk]:
                    asr_data[ds][atk][mid] = asr
    return asr_data


def mi_based_keff(mi_matrix_np, model_indices):
    K = len(model_indices)
    if K <= 1:
        return 1.0
    keff = 0.0
    for i_idx in model_indices:
        term = 1.0
        for j_idx in model_indices:
            if i_idx != j_idx:
                term += np.exp(-2 * mi_matrix_np[i_idx, j_idx])
        keff += term
    return keff / K


def classify_panel(model_ids):
    n_api = sum(1 for m in model_ids if m in API_MODELS)
    if n_api == 3:
        return "all_api"
    elif n_api == 0:
        return "all_local"
    elif n_api == 2:
        return "2api_1local"
    else:
        return "1api_2local"


PANEL_COLORS = {
    "all_api": "#e74c3c",
    "all_local": "#2ecc71",
    "2api_1local": "#e67e22",
    "1api_2local": "#3498db",
}

PANEL_LABELS = {
    "all_api": "3 API",
    "all_local": "3 Local",
    "2api_1local": "2 API + 1 Local",
    "1api_2local": "1 API + 2 Local",
}


def run_confound_analysis(mi_data, asr_data):
    models = mi_data["models"]
    model_to_idx = {m: i for i, m in enumerate(models)}
    conditions = {}

    for ds in DATASETS:
        mi_mat = np.array(mi_data["mi_matrix"][ds])

        for attack in ATTACKS:
            cond_key = f"{ds}×{attack}"
            model_asrs = asr_data.get(ds, {}).get(attack, {})

            if len(model_asrs) < 3:
                logger.warning(
                    f"  {cond_key}: only {len(model_asrs)} models have ASR, "
                    f"need >=3 for panel construction. Skipping."
                )
                conditions[cond_key] = {
                    "pearson_r": None,
                    "p_value": None,
                    "verdict": "INSUFFICIENT_DATA",
                    "n_panels": 0,
                    "n_models_with_asr": len(model_asrs),
                }
                continue

            available_models = [
                m for m in models if m in model_asrs
            ]

            keffs = []
            eta_maxs = []
            panel_types = []

            for combo in itertools.combinations(available_models, 3):
                indices = [model_to_idx[m] for m in combo]
                keff = mi_based_keff(mi_mat, indices)
                eta_max = max(model_asrs[m] for m in combo)

                keffs.append(keff)
                eta_maxs.append(eta_max)
                panel_types.append(classify_panel(combo))

            keffs = np.array(keffs)
            eta_maxs = np.array(eta_maxs)

            if len(keffs) < 3 or np.std(keffs) < 1e-10 or np.std(eta_maxs) < 1e-10:
                r, p = 0.0, 1.0
            else:
                r, p = stats.pearsonr(keffs, eta_maxs)

            if r < -0.7:
                verdict = "CONFOUND_SEVERE"
            elif r <= -0.5:
                verdict = "CONFOUND_MODERATE"
            else:
                verdict = "CONFOUND_BROKEN"

            conditions[cond_key] = {
                "pearson_r": float(r),
                "p_value": float(p),
                "verdict": verdict,
                "n_panels": len(keffs),
                "n_models_with_asr": len(available_models),
                "keffs": keffs.tolist(),
                "eta_maxs": eta_maxs.tolist(),
                "panel_types": panel_types,
            }
            logger.info(
                f"  {cond_key}: r={r:.3f}, p={p:.4f}, "
                f"verdict={verdict}, n_panels={len(keffs)}"
            )

    return conditions


def plot_scatter_grid(conditions, output_path):
    valid_conds = {
        k: v for k, v in conditions.items()
        if v.get("pearson_r") is not None
    }
    n = len(valid_conds)
    if n == 0:
        logger.warning("No valid conditions to plot")
        return

    if n <= 6:
        nrows, ncols = 2, 3
    elif n <= 9:
        nrows, ncols = 3, 3
    else:
        nrows, ncols = 3, 4

    fig, axes = plt.subplots(
        nrows, ncols,
        figsize=(5 * ncols, 4 * nrows),
        squeeze=False,
    )

    for idx, (cond_key, cond_data) in enumerate(sorted(valid_conds.items())):
        row, col = divmod(idx, ncols)
        ax = axes[row][col]

        keffs = np.array(cond_data["keffs"])
        eta_maxs = np.array(cond_data["eta_maxs"])
        panel_types = cond_data["panel_types"]
        r = cond_data["pearson_r"]
        verdict = cond_data["verdict"]

        plotted_labels = set()
        for pt in ["all_local", "1api_2local", "2api_1local", "all_api"]:
            mask = [t == pt for t in panel_types]
            if not any(mask):
                continue
            k_sub = keffs[mask]
            e_sub = eta_maxs[mask]
            label = PANEL_LABELS[pt] if pt not in plotted_labels else None
            ax.scatter(
                k_sub, e_sub,
                c=PANEL_COLORS[pt],
                alpha=0.4, s=12, label=label,
                edgecolors="none",
            )
            plotted_labels.add(pt)

        verdict_color = {
            "CONFOUND_SEVERE": "#e74c3c",
            "CONFOUND_MODERATE": "#e67e22",
            "CONFOUND_BROKEN": "#27ae60",
        }.get(verdict, "#333")

        ax.set_title(
            f"{cond_key}\nr = {r:.3f}  [{verdict}]",
            fontsize=9,
            color=verdict_color,
        )
        ax.set_xlabel("K_eff", fontsize=8)
        ax.set_ylabel("eta_max (individual ASR)", fontsize=8)
        ax.tick_params(labelsize=7)

        if len(keffs) >= 3 and np.std(keffs) > 1e-10:
            z = np.polyfit(keffs, eta_maxs, 1)
            x_line = np.linspace(keffs.min(), keffs.max(), 50)
            ax.plot(x_line, np.polyval(z, x_line), "k--", alpha=0.3, linewidth=1)

        if idx == 0:
            ax.legend(fontsize=6, loc="best", framealpha=0.7)

    for idx in range(len(valid_conds), nrows * ncols):
        row, col = divmod(idx, ncols)
        axes[row][col].set_visible(False)

    fig.suptitle(
        "K_eff vs eta_max Confound Diagnosis (15 models, K=3 panels)",
        fontsize=12, y=1.02,
    )
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    logger.info(f"Scatter plot saved to {output_path}")


def main():
    logger.info("=== Plan 001: K_eff vs eta_max Confound Diagnosis ===")

    logger.info("Loading MI matrix...")
    mi_data = load_mi_data()

    logger.info("Loading scores and computing ASR...")
    clean, attacked = load_all_scores()
    pairs = load_pairs()
    asr_data = compute_all_individual_asr(clean, attacked, pairs)

    for ds in DATASETS:
        for attack in ATTACKS:
            models_with_asr = list(asr_data.get(ds, {}).get(attack, {}).keys())
            logger.info(f"  {ds}×{attack}: {len(models_with_asr)} models")

    logger.info("\nRunning confound analysis...")
    conditions = run_confound_analysis(mi_data, asr_data)

    scatter_path = PLAN001_DIR / "confound_scatter.png"
    plot_scatter_grid(conditions, scatter_path)

    r_values = [
        v["pearson_r"] for v in conditions.values()
        if v.get("pearson_r") is not None
    ]
    if r_values:
        mean_r = float(np.mean(r_values))
        if mean_r < -0.7:
            overall = "CONFOUND_SEVERE"
        elif mean_r <= -0.5:
            overall = "CONFOUND_MODERATE"
        else:
            overall = "CONFOUND_BROKEN"
    else:
        mean_r = None
        overall = "INSUFFICIENT_DATA"

    output_conditions = {}
    for k, v in conditions.items():
        output_conditions[k] = {
            "pearson_r": v.get("pearson_r"),
            "p_value": v.get("p_value"),
            "verdict": v.get("verdict"),
            "n_panels": v.get("n_panels"),
            "n_models_with_asr": v.get("n_models_with_asr"),
        }

    output = {
        "conditions": output_conditions,
        "scatter_plots": str(scatter_path),
        "overall_verdict": overall,
        "mean_r": mean_r,
    }

    output_path = PLAN001_DIR / "confound_diagnosis.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info(f"\nDiagnosis saved to {output_path}")

    print("\n" + "=" * 70)
    print("CONFOUND DIAGNOSIS SUMMARY")
    print("=" * 70)
    for cond_key, cond in sorted(output_conditions.items()):
        r = cond["pearson_r"]
        v = cond["verdict"]
        n = cond["n_panels"]
        r_str = f"{r:.3f}" if r is not None else "N/A"
        print(f"  {cond_key:40s}  r={r_str:>7s}  {v:20s}  ({n} panels)")
    print(f"\n  Overall: mean_r={'N/A' if mean_r is None else f'{mean_r:.3f}'}, verdict={overall}")
    print("=" * 70)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Compute panel ASR distributions for K=3,5,7 and generate box+strip plots."""

import json
import sys
from pathlib import Path
from itertools import combinations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results")
PLAN001_DIR = RESULTS_DIR / "plan001"
SCORES_DIR = PLAN001_DIR / "individual_scores"
CKPT_FILES = [
    RESULTS_DIR / "_taxonomy_checkpoint.json",
    RESULTS_DIR / "_step2v3_checkpoint.json",
]

LOCAL_MODELS = [
    "qwen2.5-72b", "llama3.1-70b", "mistral-large",
    "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b",
]
API_MODELS = [
    "claude-opus-4-6", "gpt-5.5", "gemini-3.1-pro-preview", "gpt-4.1",
    "claude-sonnet-4-6", "gpt-4.1-nano", "gemini-3.5-flash",
    "gpt-4.1-mini", "claude-3-haiku",
]
ALL_MODELS = LOCAL_MODELS + API_MODELS
N_MODELS = len(ALL_MODELS)

DATASETS = ["mmlu", "arc_challenge"]
ATTACKS = [
    "score_manipulation", "position_bias", "verbosity_bias",
    "authority_bias", "sycophancy", "prompt_injection",
]
ATTACK_LABELS = {
    "score_manipulation": "Score Manip.",
    "position_bias": "Position Bias",
    "verbosity_bias": "Verbosity Bias",
    "authority_bias": "Authority Bias",
    "sycophancy": "Sycophancy",
    "prompt_injection": "Prompt Inject.",
}
K_VALUES = [3, 5, 7]
N_SAMPLES = 300

OUTPUT_DIR = Path("/tmp/fig_output")
OUTPUT_DIR.mkdir(exist_ok=True)

WINNER_MAP = {"A": 0, "B": 1, "tie": 2}


def _invert_winners(scores):
    swap = {"A": "B", "B": "A", "tie": "tie"}
    return [{**s, "winner": swap.get(s.get("winner", "tie"), "tie")} for s in scores]


def load_all_data():
    clean = {ds: {} for ds in DATASETS}
    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}
    pairs = {}

    for ckpt_path in CKPT_FILES:
        if not ckpt_path.exists():
            continue
        print(f"  Loading {ckpt_path.name}...", flush=True)
        with open(ckpt_path) as f:
            data = json.load(f)
        if "pairs" in data and not pairs:
            for ds in DATASETS:
                if ds in data["pairs"]:
                    pairs[ds] = data["pairs"][ds][:N_SAMPLES]
        for ds in DATASETS:
            for mid, scores in data.get("clean_scores", {}).get(ds, {}).items():
                if mid not in clean[ds]:
                    clean[ds][mid] = scores[:N_SAMPLES]
        for ds in DATASETS:
            for atk in ATTACKS:
                for mid, scores in (
                    data.get("attacked_scores", {}).get(ds, {}).get(atk, {}).items()
                ):
                    if mid not in attacked[ds][atk]:
                        if atk == "position_bias":
                            scores = _invert_winners(scores)
                        attacked[ds][atk][mid] = scores[:N_SAMPLES]

    if SCORES_DIR.exists():
        print("  Loading individual scores...", flush=True)
        for mid in ALL_MODELS:
            for ds in DATASETS:
                fp = SCORES_DIR / f"{mid}__{ds}__clean.json"
                if fp.exists() and mid not in clean[ds]:
                    with open(fp) as f:
                        clean[ds][mid] = json.load(f).get("scores", [])[:N_SAMPLES]
                for atk in ATTACKS:
                    fp = SCORES_DIR / f"{mid}__{ds}__{atk}.json"
                    if fp.exists() and mid not in attacked[ds][atk]:
                        with open(fp) as f:
                            scores = json.load(f).get("scores", [])[:N_SAMPLES]
                        if atk == "position_bias":
                            scores = _invert_winners(scores)
                        attacked[ds][atk][mid] = scores[:N_SAMPLES]

    return clean, attacked, pairs


def encode_winners(scores_dict, models, n_samples):
    arr = np.full((len(models), n_samples), 2, dtype=np.int8)
    for i, mid in enumerate(models):
        if mid in scores_dict:
            for j, s in enumerate(scores_dict[mid][:n_samples]):
                arr[i, j] = WINNER_MAP.get(s.get("winner", "tie"), 2)
    return arr


def majority_vote_batch(panel_winners):
    K, N = panel_winners.shape
    count_A = (panel_winners == 0).sum(axis=0)
    count_B = (panel_winners == 1).sum(axis=0)
    max_count = np.maximum(np.maximum(count_A, count_B), (panel_winners == 2).sum(axis=0))
    a_max = count_A == max_count
    b_max = count_B == max_count
    results = np.full(N, 2, dtype=np.int8)
    results[b_max] = 1
    results[a_max] = 0
    return results


def compute_panel_asr(clean_arr, attacked_arr, gt_arr, panel_indices):
    clean_v = majority_vote_batch(clean_arr[panel_indices])
    attacked_v = majority_vote_batch(attacked_arr[panel_indices])
    clean_correct = clean_v == gt_arr
    n_total = clean_correct.sum()
    if n_total == 0:
        return 0.0
    n_flips = (clean_correct & (attacked_v != gt_arr)).sum()
    return float(n_flips) / float(n_total)


def main():
    print("Loading data...", flush=True)
    clean, attacked, pairs = load_all_data()

    missing = []
    for mid in ALL_MODELS:
        for ds in DATASETS:
            if mid not in clean[ds]:
                missing.append(f"clean:{ds}/{mid}")
            for atk in ATTACKS:
                if mid not in attacked[ds][atk]:
                    missing.append(f"attacked:{ds}/{atk}/{mid}")
    if missing:
        print(f"WARNING: {len(missing)} missing entries:")
        for m in missing[:20]:
            print(f"  {m}")

    gt_mapping = {"A": 0, "B": 1}
    gt = {}
    for ds in DATASETS:
        gt[ds] = np.array(
            [gt_mapping.get(p["ground_truth_winner"], 2) for p in pairs[ds][:N_SAMPLES]],
            dtype=np.int8,
        )

    print("Encoding winner arrays...", flush=True)
    clean_enc = {}
    attacked_enc = {}
    for ds in DATASETS:
        clean_enc[ds] = encode_winners(clean[ds], ALL_MODELS, N_SAMPLES)
        attacked_enc[ds] = {}
        for atk in ATTACKS:
            attacked_enc[ds][atk] = encode_winners(
                attacked[ds][atk], ALL_MODELS, N_SAMPLES
            )

    results = {atk: {k: [] for k in K_VALUES} for atk in ATTACKS}

    for K in K_VALUES:
        combos = list(combinations(range(N_MODELS), K))
        print(f"K={K}: {len(combos)} panels", flush=True)

        for atk in ATTACKS:
            asrs = []
            for panel in combos:
                panel_arr = np.array(panel)
                ds_asrs = []
                for ds in DATASETS:
                    asr = compute_panel_asr(
                        clean_enc[ds], attacked_enc[ds][atk], gt[ds], panel_arr
                    )
                    ds_asrs.append(asr)
                asrs.append(np.mean(ds_asrs))

            results[atk][K] = asrs
            print(
                f"  {atk} K={K}: mean={np.mean(asrs):.4f} std={np.std(asrs):.4f} "
                f"med={np.median(asrs):.4f} [{np.min(asrs):.4f}, {np.max(asrs):.4f}]",
                flush=True,
            )

    save_data = {}
    for atk in ATTACKS:
        save_data[atk] = {}
        for K in K_VALUES:
            vals = results[atk][K]
            save_data[atk][str(K)] = {
                "values": vals,
                "n_panels": len(vals),
                "mean": float(np.mean(vals)),
                "std": float(np.std(vals)),
                "median": float(np.median(vals)),
                "min": float(np.min(vals)),
                "max": float(np.max(vals)),
            }
    with open(OUTPUT_DIR / "panel_asr_distributions.json", "w") as f:
        json.dump(save_data, f, indent=2)
    print(f"\nSaved JSON to {OUTPUT_DIR / 'panel_asr_distributions.json'}", flush=True)

    # ── Plot ──
    print("Generating plot...", flush=True)
    K_COLORS = {3: "#90CAF9", 5: "#1E88E5", 7: "#0D47A1"}

    fig, axes = plt.subplots(1, 6, figsize=(12, 4), sharey=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})

    rng = np.random.default_rng(42)

    for ax_idx, atk in enumerate(ATTACKS):
        ax = axes[ax_idx]
        positions = [0, 1, 2]

        for k_idx, K in enumerate(K_VALUES):
            data = np.array(results[atk][K])
            color = K_COLORS[K]
            pos = positions[k_idx]

            bp = ax.boxplot(
                [data],
                positions=[pos],
                widths=0.55,
                patch_artist=True,
                boxprops=dict(facecolor=color, edgecolor="black", linewidth=0.5, alpha=0.7),
                medianprops=dict(color="black", linewidth=1.2),
                whiskerprops=dict(linewidth=0.7),
                capprops=dict(linewidth=0.7),
                showfliers=False,
            )

            n_show = min(len(data), 500)
            if len(data) > n_show:
                idx = rng.choice(len(data), n_show, replace=False)
            else:
                idx = np.arange(len(data))
            jitter = rng.uniform(-0.15, 0.15, len(idx))
            ax.scatter(
                pos + jitter,
                data[idx],
                c=color,
                alpha=0.25,
                s=6,
                edgecolors="none",
                zorder=3,
            )

        ax.set_xticks(positions)
        ax.set_xticklabels([f"K={K}" for K in K_VALUES], fontsize=8)
        ax.set_title(ATTACK_LABELS[atk], fontsize=9, fontweight="bold")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(axis="y", labelsize=8)

    axes[0].set_ylabel("Panel ASR", fontsize=9)

    fig.tight_layout(w_pad=1.0)
    fig.savefig(OUTPUT_DIR / "fig_asr_distribution.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(OUTPUT_DIR / "fig_asr_distribution.png", dpi=300, bbox_inches="tight")
    print(f"Saved to {OUTPUT_DIR}/fig_asr_distribution.pdf/.png", flush=True)
    plt.close()


if __name__ == "__main__":
    main()

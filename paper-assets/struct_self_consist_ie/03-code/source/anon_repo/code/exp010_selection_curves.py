#!/usr/bin/env python3
"""exp-010: Selection Curves — Best-of-N comparison across signals.

Generates paper-quality figure showing macro F1 vs N for each selection signal.
Subplots: (a) NER SciERC, (b) RE SciERC, (c) NER CoNLL-2003.
"""

from __future__ import annotations

import json
import os
import sys
import time
from collections import Counter

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../code"))
from consistency import (
    _ner_soft_jaccard_pair,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

# ── Configuration ──────────────────────────────────────────────────

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "scierc_ner": {
        "path": f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
        "subtask": "ner",
        "max_n": 16,
        "title": "(a) NER — SciERC",
        "filter_fn": None,
    },
    "scierc_re": {
        "path": f"{BASE}/output/exp_008_re_n16_v2/samples.jsonl",
        "subtask": "re",
        "max_n": 16,
        "title": "(b) RE — SciERC",
        "filter_fn": lambda inst: len(inst["gold"].get("relations", [])) > 0,
    },
    "conll_ner": {
        "path": f"{BASE}/output/exp002_conll2003/samples.jsonl",
        "subtask": "ner",
        "max_n": 8,
        "title": "(c) NER — CoNLL-2003",
        "filter_fn": None,
    },
}

N_REPEATS = 10
SEED = 42

SELECTION_SIGNALS = ["SJ", "FK", "logprob", "voting_conf", "EM", "random", "oracle"]

OUTPUT_DIR = f"{BASE}/output/exp010_selection_curves"
FIG_DIR = os.path.join(OUTPUT_DIR, "figures")

# ── Data loading ───────────────────────────────────────────────────

def load_data(path: str) -> list[dict]:
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


# ── Precomputation ─────────────────────────────────────────────────

def precompute_pairwise_sj(instance: dict, subtask: str) -> np.ndarray:
    samples = instance["samples"]
    N = len(samples)
    field = "entities" if subtask == "ner" else "relations"
    pair_fn = _ner_soft_jaccard_pair if subtask == "ner" else _re_soft_jaccard_pair
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            score = pair_fn(samples[i].get(field, []), samples[j].get(field, []))
            matrix[i][j] = score
            matrix[j][i] = score
    np.fill_diagonal(matrix, 1.0)
    return matrix


def precompute_pairwise_surface(instance: dict, subtask: str) -> np.ndarray:
    samples = instance["samples"]
    N = len(samples)
    key_sets = [_extract_surface_keys(s, subtask) for s in samples]
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            score = inter / union if union > 0 else 1.0
            matrix[i][j] = score
            matrix[j][i] = score
    np.fill_diagonal(matrix, 1.0)
    return matrix


def precompute_per_sample_f1(instance: dict, subtask: str) -> list[float]:
    gold = instance["gold"]
    return [per_instance_f1(s, gold, subtask=subtask) for s in instance["samples"]]


# ── Per-sample signal selection ────────────────────────────────────

def select_best_sample(
    signal: str,
    indices: list[int],
    sj_matrix: np.ndarray,
    surface_matrix: np.ndarray,
    logprobs: list[float],
    surface_keys: list[frozenset],
    per_sample_f1s: list[float],
    rng: np.random.Generator,
) -> int:
    n_sub = len(indices)
    if n_sub == 1:
        return indices[0]

    if signal == "oracle":
        f1s = [per_sample_f1s[i] for i in indices]
        return indices[int(np.argmax(f1s))]

    if signal == "random":
        return int(rng.choice(indices))

    if signal == "logprob":
        lps = [logprobs[i] for i in indices]
        return indices[int(np.argmax(lps))]

    if signal == "SJ":
        scores = []
        for k in indices:
            others = [j for j in indices if j != k]
            scores.append(float(np.mean([sj_matrix[k][j] for j in others])))
        return indices[int(np.argmax(scores))]

    if signal == "FK":
        scores = []
        for k in indices:
            others = [j for j in indices if j != k]
            scores.append(float(np.mean([surface_matrix[k][j] for j in others])))
        return indices[int(np.argmax(scores))]

    if signal == "voting_conf":
        all_keys_count: Counter = Counter()
        for i in indices:
            for key in surface_keys[i]:
                all_keys_count[key] += 1
        scores = []
        for k in indices:
            keys_k = surface_keys[k]
            if not keys_k:
                scores.append(0.0)
            else:
                fracs = [all_keys_count[key] / n_sub for key in keys_k]
                scores.append(float(np.mean(fracs)))
        return indices[int(np.argmax(scores))]

    if signal == "EM":
        scores = []
        for k in indices:
            count = sum(1 for j in indices if j != k and surface_keys[k] == surface_keys[j])
            scores.append(count)
        return indices[int(np.argmax(scores))]

    raise ValueError(f"Unknown signal: {signal}")


# ── Main computation ───────────────────────────────────────────────

def run_selection_curves(
    instances: list[dict],
    subtask: str,
    max_n: int,
) -> dict:
    n_values = [v for v in [1, 2, 4, 8, 16] if v <= max_n]
    n_inst = len(instances)
    print(f"  {n_inst} instances, max_n={max_n}, n_values={n_values}")

    # ── Precompute ──
    print("  Precomputing pairwise matrices...")
    t0 = time.time()

    all_sj = []
    all_surf = []
    all_logprobs = []
    all_surf_keys = []
    all_f1s = []
    all_greedy_f1s = []

    for i, inst in enumerate(instances):
        if (i + 1) % 200 == 0:
            print(f"    {i+1}/{n_inst} ({time.time()-t0:.0f}s)")

        all_sj.append(precompute_pairwise_sj(inst, subtask))
        all_surf.append(precompute_pairwise_surface(inst, subtask))

        lps = []
        for s in inst["samples"]:
            lp = s.get("mean_logprob")
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            lps.append(lp)
        all_logprobs.append(lps)

        all_surf_keys.append(
            [frozenset(_extract_surface_keys(s, subtask)) for s in inst["samples"]]
        )
        all_f1s.append(precompute_per_sample_f1(inst, subtask))
        all_greedy_f1s.append(
            per_instance_f1(inst["greedy"], inst["gold"], subtask=subtask)
        )

    print(f"  Precomputation: {time.time()-t0:.1f}s")

    greedy_macro = float(np.mean(all_greedy_f1s))

    # ── Selection curves ──
    results: dict[int, dict[str, float]] = {}
    results_std: dict[int, dict[str, float]] = {}

    for n_val in n_values:
        t1 = time.time()
        results[n_val] = {}
        results_std[n_val] = {}

        if n_val == 1:
            for sig in SELECTION_SIGNALS:
                f1s = [all_f1s[i][0] for i in range(n_inst)]
                results[n_val][sig] = float(np.mean(f1s))
                results_std[n_val][sig] = 0.0
            results[n_val]["greedy"] = greedy_macro
            results_std[n_val]["greedy"] = 0.0

        elif n_val == max_n:
            rng = np.random.default_rng(SEED)
            for sig in SELECTION_SIGNALS:
                f1s = []
                for i in range(n_inst):
                    idx = list(range(max_n))
                    best = select_best_sample(
                        sig, idx, all_sj[i], all_surf[i],
                        all_logprobs[i], all_surf_keys[i], all_f1s[i], rng,
                    )
                    f1s.append(all_f1s[i][best])
                results[n_val][sig] = float(np.mean(f1s))
                results_std[n_val][sig] = 0.0
            results[n_val]["greedy"] = greedy_macro
            results_std[n_val]["greedy"] = 0.0

        else:
            for sig in SELECTION_SIGNALS:
                rep_means = []
                for rep in range(N_REPEATS):
                    rng = np.random.default_rng(SEED * 1000 + rep)
                    f1s = []
                    for i in range(n_inst):
                        idx = sorted(
                            rng.choice(max_n, size=n_val, replace=False).tolist()
                        )
                        best = select_best_sample(
                            sig, idx, all_sj[i], all_surf[i],
                            all_logprobs[i], all_surf_keys[i], all_f1s[i], rng,
                        )
                        f1s.append(all_f1s[i][best])
                    rep_means.append(float(np.mean(f1s)))
                results[n_val][sig] = float(np.mean(rep_means))
                results_std[n_val][sig] = float(np.std(rep_means))
            results[n_val]["greedy"] = greedy_macro
            results_std[n_val]["greedy"] = 0.0

        elapsed = time.time() - t1
        print(f"    N={n_val}: {elapsed:.1f}s  SJ={results[n_val]['SJ']:.4f}  "
              f"logprob={results[n_val]['logprob']:.4f}  oracle={results[n_val]['oracle']:.4f}")

    return {
        "n_values": n_values,
        "results": results,
        "results_std": results_std,
        "greedy_macro_f1": greedy_macro,
        "n_instances": n_inst,
    }


# ── Plotting ───────────────────────────────────────────────────────

def make_figure(all_data: dict[str, dict], fig_path: str):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import ScalarFormatter

    STYLES = {
        "SJ":          {"color": "#2066a8", "marker": "o", "ls": "-",  "lw": 2.0, "ms": 7,  "label": "Soft Jaccard (SJ)", "zorder": 10},
        "FK":          {"color": "#e08214", "marker": "s", "ls": "-",  "lw": 2.0, "ms": 6,  "label": "Fleiss' κ (FK)",    "zorder": 9},
        "logprob":     {"color": "#1a9641", "marker": "^", "ls": "-",  "lw": 2.0, "ms": 7,  "label": "Log-prob",          "zorder": 8},
        "voting_conf": {"color": "#d7191c", "marker": "D", "ls": "-",  "lw": 2.0, "ms": 6,  "label": "Voting Conf.",      "zorder": 7},
        "EM":          {"color": "#7b3294", "marker": "v", "ls": "-",  "lw": 1.8, "ms": 6,  "label": "Exact Match (EM)",  "zorder": 6},
        "random":      {"color": "#999999", "marker": "+", "ls": "--", "lw": 1.5, "ms": 7,  "label": "Random",            "zorder": 4},
        "oracle":      {"color": "#08519c", "marker": "*", "ls": "--", "lw": 1.5, "ms": 9,  "label": "Oracle",            "zorder": 5},
        "greedy":      {"color": "#636363", "marker": "",  "ls": ":",  "lw": 1.8, "ms": 0,  "label": "Greedy (T=0)",      "zorder": 3},
    }

    PLOT_ORDER = ["oracle", "SJ", "FK", "voting_conf", "logprob", "EM", "random", "greedy"]

    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.8), constrained_layout=True)

    dataset_order = ["scierc_ner", "scierc_re", "conll_ner"]

    for ax_idx, ds_key in enumerate(dataset_order):
        ax = axes[ax_idx]
        data = all_data[ds_key]
        n_vals = data["n_values"]
        results = data["results"]
        results_std = data["results_std"]

        for sig in PLOT_ORDER:
            st = STYLES[sig]
            ys = [results[n][sig] for n in n_vals]

            if sig == "greedy":
                ax.axhline(y=ys[0], color=st["color"], ls=st["ls"], lw=st["lw"],
                           label=st["label"], zorder=st["zorder"], alpha=0.7)
            else:
                stds = [results_std[n].get(sig, 0) for n in n_vals]
                has_err = any(s > 0 for s in stds)
                if has_err:
                    ys_arr = np.array(ys)
                    stds_arr = np.array(stds)
                    ax.fill_between(n_vals, ys_arr - stds_arr, ys_arr + stds_arr,
                                    color=st["color"], alpha=0.10, zorder=st["zorder"] - 1)
                ax.plot(n_vals, ys, color=st["color"], marker=st["marker"],
                        ls=st["ls"], lw=st["lw"], ms=st["ms"],
                        label=st["label"], zorder=st["zorder"],
                        markeredgecolor="white", markeredgewidth=0.6)

        ax.set_xscale("log", base=2)
        ax.set_xticks(n_vals)
        ax.xaxis.set_major_formatter(ScalarFormatter())
        ax.set_xlabel("N (number of samples)", fontsize=12)
        if ax_idx == 0:
            ax.set_ylabel("Macro F1", fontsize=12)
        ax.tick_params(labelsize=10)
        ax.grid(True, alpha=0.3, ls="--")

        ds_cfg = DATASETS[ds_key]
        ax.set_title(ds_cfg["title"], fontsize=13, fontweight="bold")

        y_vals_all = []
        for n in n_vals:
            y_vals_all.extend(results[n][sig] for sig in PLOT_ORDER)
        y_min = min(y_vals_all) - 0.02
        y_max = max(y_vals_all) + 0.02
        ax.set_ylim(y_min, y_max)

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=4, fontsize=10,
               bbox_to_anchor=(0.5, -0.12), frameon=True, edgecolor="#cccccc")

    os.makedirs(os.path.dirname(fig_path), exist_ok=True)
    fig.savefig(fig_path, dpi=300, bbox_inches="tight")
    png_path = fig_path.replace(".pdf", ".png")
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {fig_path}")
    print(f"  Saved: {png_path}")
    return fig_path, png_path


# ── Main ───────────────────────────────────────────────────────────

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(FIG_DIR, exist_ok=True)

    all_data = {}

    for ds_key, ds_cfg in DATASETS.items():
        print(f"\n{'='*60}")
        print(f"  Dataset: {ds_key} ({ds_cfg['subtask'].upper()})")
        print(f"{'='*60}")

        instances = load_data(ds_cfg["path"])
        if ds_cfg.get("filter_fn"):
            before = len(instances)
            instances = [inst for inst in instances if ds_cfg["filter_fn"](inst)]
            print(f"  Filtered: {before} → {len(instances)} (instances with gold labels)")

        data = run_selection_curves(instances, ds_cfg["subtask"], ds_cfg["max_n"])
        all_data[ds_key] = data

    # ── Generate figure ──
    print(f"\n{'='*60}")
    print("  Generating figure...")
    print(f"{'='*60}")
    fig_path = os.path.join(FIG_DIR, "fig_selection_curves.pdf")
    make_figure(all_data, fig_path)

    # ── Save metrics JSON ──
    metrics_out = {}
    for ds_key, data in all_data.items():
        metrics_out[ds_key] = {
            "n_instances": data["n_instances"],
            "greedy_macro_f1": data["greedy_macro_f1"],
            "n_values": data["n_values"],
            "results": {str(k): v for k, v in data["results"].items()},
            "results_std": {str(k): v for k, v in data["results_std"].items()},
        }
    metrics_path = os.path.join(OUTPUT_DIR, "exp010_metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics_out, f, indent=2)
    print(f"  Saved: {metrics_path}")

    # ── Print summary table ──
    print(f"\n{'='*60}")
    print("  SUMMARY")
    print(f"{'='*60}")
    for ds_key, data in all_data.items():
        print(f"\n  {ds_key} (n={data['n_instances']}):")
        n_vals = data["n_values"]
        print(f"  {'Signal':>15s}", end="")
        for n in n_vals:
            print(f"  N={n:>2d}", end="")
        print(f"  {'Δ(max-1)':>8s}")
        for sig in PLOT_ORDER:
            print(f"  {sig:>15s}", end="")
            for n in n_vals:
                print(f"  {data['results'][n][sig]:.4f}", end="")
            delta = data["results"][n_vals[-1]][sig] - data["results"][n_vals[0]][sig]
            print(f"  {delta:+.4f}")

    print("\nDone.")


PLOT_ORDER = ["oracle", "SJ", "FK", "voting_conf", "logprob", "EM", "random", "greedy"]

if __name__ == "__main__":
    main()

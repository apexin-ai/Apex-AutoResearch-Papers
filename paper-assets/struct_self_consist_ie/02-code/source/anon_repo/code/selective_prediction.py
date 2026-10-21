#!/usr/bin/env python3
"""
Confidence-Weighted Selective Prediction.

For each instance, compute 5 QE signals as instance-level confidence scores.
Sort by confidence, retain top-k% (coverage), compute mean F1 of retained set.
Output: precision-coverage curves + AUPRC for each dataset x signal.
"""

import json
import os
import sys
import time
from collections import Counter

import numpy as np

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    _ner_soft_jaccard_pair,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
    fleiss_kappa_surface,
)
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT_DIR = f"{BASE}/output/prescriptive_analysis"

DATASETS = {
    "SciERC_NER": {
        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "subtask": "ner",
        "gold_key": "entities",
    },
    "SciERC_RE": {
        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
        "subtask": "re",
        "gold_key": "relations",
    },
    "CoNLL_NER": {
        "path": f"{BASE}/output/exp_002_conll_n16_r1024/samples.jsonl",
        "subtask": "ner",
        "gold_key": "entities",
    },
    "FewNERD_NER": {
        "path": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
        "subtask": "ner",
        "gold_key": "entities",
    },
}

SIGNALS = ["SJ", "FK", "EM", "VC", "LP"]
COVERAGE_LEVELS = list(np.arange(0.05, 1.01, 0.05))


def load_data(path, gold_key):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if obj["gold"].get(gold_key, []):
                instances.append(obj)
    return instances


def compute_instance_sj(inst, subtask):
    samples = inst["samples"]
    N = len(samples)
    if N <= 1:
        return 1.0
    field = "entities" if subtask == "ner" else "relations"
    pair_fn = _ner_soft_jaccard_pair if subtask == "ner" else _re_soft_jaccard_pair
    total = 0.0
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            total += pair_fn(samples[i].get(field, []), samples[j].get(field, []))
            count += 1
    return total / count if count > 0 else 1.0


def compute_instance_fk(inst, subtask):
    return fleiss_kappa_surface(inst["samples"], subtask=subtask)


def compute_instance_em(inst, subtask):
    samples = inst["samples"]
    N = len(samples)
    if N <= 1:
        return 1.0
    key_sets = [frozenset(_extract_surface_keys(s, subtask)) for s in samples]
    match_count = 0
    total_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if key_sets[i] == key_sets[j]:
                match_count += 1
            total_pairs += 1
    return match_count / total_pairs if total_pairs > 0 else 1.0


def compute_instance_vc(inst, subtask):
    samples = inst["samples"]
    N = len(samples)
    greedy = inst.get("greedy", samples[0])
    greedy_keys = frozenset(_extract_surface_keys(greedy, subtask))
    if not greedy_keys:
        return 0.0
    all_keys_count = Counter()
    for s in samples:
        for key in _extract_surface_keys(s, subtask):
            all_keys_count[key] += 1
    fracs = [all_keys_count[key] / N for key in greedy_keys]
    return float(np.mean(fracs))


def compute_instance_lp(inst):
    greedy = inst.get("greedy", inst["samples"][0])
    lp = greedy.get("mean_logprob")
    if lp is None:
        cum = greedy.get("cumulative_logprob", -999)
        ntok = max(greedy.get("n_tokens", 1), 1)
        lp = cum / ntok
    return lp if np.isfinite(lp) else -999.0


def compute_precision_at_coverage(f1s, scores, coverages):
    n = len(f1s)
    order = np.argsort(-scores)
    sorted_f1 = f1s[order]
    results = []
    for cov in coverages:
        k = max(1, int(round(cov * n)))
        mean_f1 = float(np.mean(sorted_f1[:k]))
        results.append({"coverage": round(cov, 2), "f1": mean_f1, "n_retained": k})
    return results


def compute_auprc(curve_data, _=None):
    cov = np.array([r["coverage"] for r in curve_data])
    f1 = np.array([r["f1"] for r in curve_data])
    return float(np.trapz(f1, cov))


def random_baseline(f1s, coverages, n_repeats=200, seed=42):
    rng = np.random.RandomState(seed)
    n = len(f1s)
    results = []
    for cov in coverages:
        k = max(1, int(round(cov * n)))
        vals = []
        for _ in range(n_repeats):
            idx = rng.choice(n, k, replace=False)
            vals.append(float(np.mean(f1s[idx])))
        results.append({"coverage": round(cov, 2), "f1": float(np.mean(vals)), "n_retained": k})
    return results


def oracle_baseline(f1s, coverages):
    n = len(f1s)
    order = np.argsort(-f1s)
    sorted_f1 = f1s[order]
    results = []
    for cov in coverages:
        k = max(1, int(round(cov * n)))
        results.append({"coverage": round(cov, 2), "f1": float(np.mean(sorted_f1[:k])), "n_retained": k})
    return results


def analyze_dataset(name, cfg):
    print(f"\n{'='*60}")
    print(f"Dataset: {name}")
    print(f"{'='*60}")

    t0 = time.time()
    instances = load_data(cfg["path"], cfg["gold_key"])
    subtask = cfg["subtask"]
    n = len(instances)
    print(f"  Loaded {n} instances (gold-filtered)")

    greedy_f1s = np.zeros(n)
    signal_scores = {sig: np.zeros(n) for sig in SIGNALS}

    for i, inst in enumerate(instances):
        if (i + 1) % 500 == 0:
            print(f"  Processing {i+1}/{n} ({time.time()-t0:.0f}s)")

        greedy_f1s[i] = per_instance_f1(
            inst.get("greedy", inst["samples"][0]), inst["gold"], subtask=subtask
        )
        signal_scores["SJ"][i] = compute_instance_sj(inst, subtask)
        signal_scores["FK"][i] = compute_instance_fk(inst, subtask)
        signal_scores["EM"][i] = compute_instance_em(inst, subtask)
        signal_scores["VC"][i] = compute_instance_vc(inst, subtask)
        signal_scores["LP"][i] = compute_instance_lp(inst)

    elapsed = time.time() - t0
    print(f"  Computed all signals in {elapsed:.1f}s")

    coverages = COVERAGE_LEVELS
    result = {
        "dataset": name,
        "n_instances": n,
        "greedy_f1_mean": float(np.mean(greedy_f1s)),
    }

    # Random baseline
    rand_curve = random_baseline(greedy_f1s, coverages)
    rand_auprc = compute_auprc(rand_curve)
    result["random"] = {"curve": rand_curve, "auprc": rand_auprc}

    # Oracle baseline
    oracle_curve = oracle_baseline(greedy_f1s, coverages)
    oracle_auprc = compute_auprc(oracle_curve)
    result["oracle"] = {"curve": oracle_curve, "auprc": oracle_auprc}

    # Each signal
    for sig in SIGNALS:
        curve = compute_precision_at_coverage(greedy_f1s, signal_scores[sig], coverages)
        auprc = compute_auprc(curve)
        f1_80 = next(r["f1"] for r in curve if abs(r["coverage"] - 0.80) < 0.01)
        f1_90 = next(r["f1"] for r in curve if abs(r["coverage"] - 0.90) < 0.01)
        f1_100 = next(r["f1"] for r in curve if abs(r["coverage"] - 1.00) < 0.01)
        delta_80 = f1_80 - f1_100
        result[sig] = {
            "curve": curve,
            "auprc": auprc,
            "f1_80": f1_80,
            "f1_90": f1_90,
            "f1_100": f1_100,
            "delta_80": delta_80,
        }
        print(f"  {sig}: AUPRC={auprc:.4f}  F1@80%={f1_80:.4f}  F1@100%={f1_100:.4f}  delta@80%={delta_80:+.4f}")

    print(f"  Random AUPRC={rand_auprc:.4f}  Oracle AUPRC={oracle_auprc:.4f}")
    return result


def generate_latex_table(all_results):
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Selective Prediction: AUPRC and F1 at various coverage levels.}")
    lines.append(r"\label{tab:selective_prediction}")
    lines.append(r"\resizebox{\textwidth}{!}{")
    lines.append(r"\begin{tabular}{ll ccccc}")
    lines.append(r"\toprule")
    lines.append(r"Dataset & Signal & AUPRC & F1@80\% & F1@90\% & F1@100\% & $\Delta$@80\% \\")
    lines.append(r"\midrule")

    for res in all_results:
        ds = res["dataset"]
        first = True
        for sig in ["Random", "Oracle"] + SIGNALS:
            if sig in ("Random", "Oracle"):
                data = res[sig.lower()]
                f1_80 = next(r["f1"] for r in data["curve"] if abs(r["coverage"] - 0.80) < 0.01)
                f1_90 = next(r["f1"] for r in data["curve"] if abs(r["coverage"] - 0.90) < 0.01)
                f1_100 = next(r["f1"] for r in data["curve"] if abs(r["coverage"] - 1.00) < 0.01)
                delta_80 = f1_80 - f1_100
                row_data = {"auprc": data["auprc"], "f1_80": f1_80, "f1_90": f1_90, "f1_100": f1_100, "delta_80": delta_80}
            else:
                row_data = res[sig]

            ds_col = ds.replace("_", r"\_") if first else ""
            first = False

            best_auprc = max(res[s]["auprc"] for s in SIGNALS)
            auprc_str = f"\\textbf{{{row_data['auprc']:.4f}}}" if sig in SIGNALS and abs(row_data["auprc"] - best_auprc) < 1e-6 else f"{row_data['auprc']:.4f}"

            lines.append(
                f"  {ds_col} & {sig} & {auprc_str} & "
                f"{row_data['f1_80']:.4f} & {row_data['f1_90']:.4f} & "
                f"{row_data['f1_100']:.4f} & {row_data['delta_80']:+.4f} \\\\"
            )

        lines.append(r"\midrule")

    lines[-1] = r"\bottomrule"
    lines.append(r"\end{tabular}}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def plot_curves(all_results, out_path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 4, figsize=(20, 4.5), sharey=False)
    colors = {
        "SJ": "#1f77b4",
        "FK": "#ff7f0e",
        "EM": "#2ca02c",
        "VC": "#d62728",
        "LP": "#9467bd",
        "Random": "#aaaaaa",
        "Oracle": "#333333",
    }
    linestyles = {
        "SJ": "-",
        "FK": "-",
        "EM": "-",
        "VC": "-",
        "LP": "-",
        "Random": "--",
        "Oracle": ":",
    }

    for ax, res in zip(axes, all_results):
        ds = res["dataset"]

        # Random
        covs = [r["coverage"] for r in res["random"]["curve"]]
        f1s_r = [r["f1"] for r in res["random"]["curve"]]
        ax.plot(covs, f1s_r, color=colors["Random"], ls=linestyles["Random"],
                label="Random", linewidth=1.5)

        # Oracle
        covs = [r["coverage"] for r in res["oracle"]["curve"]]
        f1s_o = [r["f1"] for r in res["oracle"]["curve"]]
        ax.plot(covs, f1s_o, color=colors["Oracle"], ls=linestyles["Oracle"],
                label="Oracle", linewidth=1.5)

        # Signals
        for sig in SIGNALS:
            covs = [r["coverage"] for r in res[sig]["curve"]]
            f1s_s = [r["f1"] for r in res[sig]["curve"]]
            auprc = res[sig]["auprc"]
            ax.plot(covs, f1s_s, color=colors[sig], ls=linestyles[sig],
                    label=f"{sig} ({auprc:.3f})", linewidth=1.8)

        ax.set_title(ds.replace("_", " "), fontsize=12, fontweight="bold")
        ax.set_xlabel("Coverage", fontsize=11)
        ax.set_xlim(0.05, 1.0)
        ax.tick_params(labelsize=9)
        if ax == axes[0]:
            ax.set_ylabel("Mean F1 of Retained Instances", fontsize=11)
        ax.legend(fontsize=7.5, loc="lower left", framealpha=0.9)

    plt.tight_layout(pad=1.5)
    plt.savefig(out_path, bbox_inches="tight", dpi=150)
    plt.savefig(out_path.replace(".pdf", ".png"), bbox_inches="tight", dpi=150)
    print(f"\nFigure saved to {out_path}")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    all_results = []
    for name, cfg in DATASETS.items():
        res = analyze_dataset(name, cfg)
        all_results.append(res)

    # Save JSON
    json_path = f"{OUT_DIR}/selective_prediction.json"
    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {json_path}")

    # LaTeX table
    latex = generate_latex_table(all_results)
    tex_path = f"{OUT_DIR}/selective_prediction_table.tex"
    with open(tex_path, "w") as f:
        f.write(latex)
    print(f"LaTeX table saved to {tex_path}")
    print("\n" + latex)

    # Plot
    fig_path = f"{OUT_DIR}/fig_selective_prediction.pdf"
    plot_curves(all_results, fig_path)


if __name__ == "__main__":
    main()

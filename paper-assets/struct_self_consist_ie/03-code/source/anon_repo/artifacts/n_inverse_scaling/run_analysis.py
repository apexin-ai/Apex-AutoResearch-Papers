#!/usr/bin/env python3
"""Inverse scaling test: check if F1 decreases as N increases for construction methods.

For each dataset x model x method, sub-sample N=16 (or N=8) samples to N=2,4,6,8,(16),
compute entity-level micro F1, detect inverse scaling (F1 drop > 0.1pp),
and run paired bootstrap significance tests.
"""

import json
import math
import os
import sys
import time
import numpy as np
from collections import defaultdict, Counter

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUTPUT_DIR = f"{BASE}/artifacts/n_inverse_scaling"

CONFIGS = {
    "Qwen_SciERC": {
        "path": f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
        "model": "Qwen3-8B-FT", "dataset": "SciERC",
    },
    "Qwen_CoNLL": {
        "path": f"{BASE}/output/exp_002_conll_n16/samples.jsonl",
        "model": "Qwen3-8B-FT", "dataset": "CoNLL",
    },
    "Qwen_FewNERD": {
        "path": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
        "model": "Qwen3-8B-FT", "dataset": "FewNERD",
    },
    "LLaMA_SciERC": {
        "path": f"{BASE}/output/exp_007_llama_n16_r1024/samples.jsonl",
        "model": "LLaMA-3.1-8B-FT", "dataset": "SciERC",
    },
    "LLaMA_CoNLL": {
        "path": f"{BASE}/output/exp_017_llama_conll_n16/samples.jsonl",
        "model": "LLaMA-3.1-8B-FT", "dataset": "CoNLL",
    },
    "LLaMA_FewNERD": {
        "path": f"{BASE}/output/llama_fewnerd_s42/samples.jsonl",
        "model": "LLaMA-3.1-8B-FT", "dataset": "FewNERD",
    },
}

METHODS = ["majority_vote", "lp_weighted", "vc_weighted", "sj_weighted", "theta2n", "uniform"]

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}

def load_data(path, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances

def get_lp_weights(samples, inst):
    logprobs_list = inst.get("logprobs", None)
    lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and logprobs_list is not None and i < len(logprobs_list):
            lp = logprobs_list[i]
        if lp is None or not math.isfinite(lp):
            lp = -100.0
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    if total == 0:
        return [1.0 / len(samples)] * len(samples)
    return [w / total for w in ws]

def get_vc_weights(samples):
    N = len(samples)
    entity_counts = Counter()
    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += 1
                seen.add(key)
    weights = []
    for s in samples:
        ents = set()
        for e in s.get("entities", []):
            ents.add((e["start"], e["end"], e["type"]))
        if ents:
            w = sum(entity_counts[k] for k in ents) / (N * len(ents))
        else:
            w = 1.0 / N
        weights.append(w)
    total = sum(weights)
    if total == 0:
        return [1.0 / N] * N
    return [w / total for w in weights]

def get_sj_weights(samples):
    N = len(samples)
    sets = []
    for s in samples:
        es = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
        sets.append(es)
    weights = []
    for i in range(N):
        if N == 1:
            weights.append(1.0)
            continue
        total_j = 0.0
        for j in range(N):
            if j == i:
                continue
            a, b = sets[i], sets[j]
            if not a and not b:
                total_j += 1.0
            elif not a or not b:
                pass
            else:
                total_j += len(a & b) / len(a | b)
        weights.append(total_j / (N - 1))
    total = sum(weights)
    if total == 0:
        return [1.0 / N] * N
    return [w / total for w in weights]

def weighted_construction(samples, threshold, weights=None):
    entity_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        seen = set()
        for e in sample.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += w
                seen.add(key)
    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in entity_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed

def evaluate_instance(inst, n, method):
    samples = inst["samples"][:n]
    gold = entity_set(inst["gold"]["entities"])
    if method == "majority_vote":
        pred = weighted_construction(samples, threshold=0.5)
    elif method == "lp_weighted":
        ws = get_lp_weights(samples, inst)
        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
    elif method == "vc_weighted":
        ws = get_vc_weights(samples)
        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
    elif method == "sj_weighted":
        ws = get_sj_weights(samples)
        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
    elif method == "theta2n":
        pred = weighted_construction(samples, threshold=2.0/n)
    elif method == "uniform":
        pred = weighted_construction(samples, threshold=0.25)
    elif method == "greedy":
        pred = entity_set(inst["greedy"]["entities"])
    else:
        raise ValueError(f"Unknown: {method}")
    tp = len(pred & gold)
    fp = len(pred - gold)
    fn = len(gold - pred)
    return tp, fp, fn

def micro_f1_from_tuples(tuples):
    tp = sum(t[0] for t in tuples)
    fp = sum(t[1] for t in tuples)
    fn = sum(t[2] for t in tuples)
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)

def micro_prf_from_tuples(tuples):
    tp = sum(t[0] for t in tuples)
    fp = sum(t[1] for t in tuples)
    fn = sum(t[2] for t in tuples)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    f = 2 * p * r / (p + r)
    return p, r, f

def bootstrap_test(arr_n1, arr_n2, B=10000):
    n = len(arr_n1)
    assert n == len(arr_n2)
    a1 = np.array(arr_n1, dtype=np.int64)
    a2 = np.array(arr_n2, dtype=np.int64)
    s1 = a1.sum(axis=0)
    s2 = a2.sum(axis=0)
    def _f1(s):
        tp, fp, fn = s[0], s[1], s[2]
        if tp == 0: return 0.0
        p = tp / (tp + fp); r = tp / (tp + fn)
        return 2*p*r/(p+r)
    obs_diff = _f1(s2) - _f1(s1)
    rng = np.random.RandomState(42)
    diffs = np.empty(B)
    for b in range(B):
        idx = rng.randint(0, n, size=n)
        bs1 = a1[idx].sum(axis=0)
        bs2 = a2[idx].sum(axis=0)
        diffs[b] = _f1(bs2) - _f1(bs1)
    ci = (float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5)))
    p_value = float(np.mean(diffs >= 0))
    return {"obs_diff": float(obs_diff), "ci_95": ci, "p_value_inverse": p_value}

def compute_degeneracy(instances, n):
    n_degen = 0
    for inst in instances:
        samples = inst["samples"][:n]
        esets = [frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
                 for s in samples]
        if len(set(esets)) == 1:
            n_degen += 1
    return n_degen / len(instances)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    f1_by_n = {}
    inverse_summary = {}

    for cfg_name, cfg in CONFIGS.items():
        path = cfg["path"]
        if not os.path.exists(path):
            print(f"SKIP {cfg_name}: {path} not found", flush=True)
            continue

        print(f"\n{'='*70}", flush=True)
        print(f"  {cfg_name}  ({cfg['model']} / {cfg['dataset']})", flush=True)
        print(f"{'='*70}", flush=True)

        t0 = time.time()
        instances = load_data(path, gold_filter=True)
        max_n = len(instances[0]["samples"])
        print(f"  Loaded {len(instances)} instances, N_max={max_n}  ({time.time()-t0:.1f}s)", flush=True)

        n_vals = sorted(set(n for n in [2, 4, 6, 8, 16] if n <= max_n))

        greedy_tuples = [evaluate_instance(inst, max_n, "greedy") for inst in instances]
        greedy_f1 = micro_f1_from_tuples(greedy_tuples)
        print(f"  Greedy F1: {greedy_f1:.4f}", flush=True)

        precomputed = {}
        for method in METHODS:
            for n in n_vals:
                t1 = time.time()
                tuples = [evaluate_instance(inst, n, method) for inst in instances]
                f1 = micro_f1_from_tuples(tuples)
                p, r, _ = micro_prf_from_tuples(tuples)
                precomputed[(method, n)] = {"tuples": tuples, "f1": f1, "p": p, "r": r}
                elapsed = time.time() - t1
                if elapsed > 2:
                    print(f"    {method} N={n}: F1={f1:.4f} ({elapsed:.1f}s)", flush=True)

        config_result = {
            "model": cfg["model"], "dataset": cfg["dataset"],
            "n_instances": len(instances), "max_n": max_n,
            "greedy_f1": greedy_f1, "N_values": n_vals, "methods": {},
        }

        degen = {}
        for n in n_vals:
            degen[str(n)] = compute_degeneracy(instances, n)
        config_result["degeneracy_by_n"] = degen

        print(f"\n  {'Method':<18}", end="", flush=True)
        for n in n_vals:
            print(f"  N={n:>2}", end="", flush=True)
        print("  Behavior", flush=True)
        print(f"  {'-'*75}", flush=True)

        for method in METHODS:
            f1_dict = {}
            prf_dict = {}
            for n in n_vals:
                d = precomputed[(method, n)]
                f1_dict[str(n)] = d["f1"]
                prf_dict[str(n)] = {"P": d["p"], "R": d["r"], "F1": d["f1"]}

            f1_list = [f1_dict[str(n)] for n in n_vals]
            has_drop = any(f1_list[i] - f1_list[i+1] > 0.001 for i in range(len(f1_list)-1))
            is_plateau = all(abs(f1_list[i] - f1_list[i+1]) <= 0.001 for i in range(len(f1_list)-1))
            if has_drop:
                behavior = "inverse_scaling"
            elif is_plateau:
                behavior = "plateau"
            else:
                behavior = "monotonic_increasing"

            config_result["methods"][method] = {
                "f1_by_n": f1_dict, "prf_by_n": prf_dict, "behavior": behavior,
            }
            vals = "  ".join(f"{f1_dict[str(n)]:.4f}" for n in n_vals)
            marker = " <<<" if behavior == "inverse_scaling" else ""
            print(f"  {method:<18} {vals}  {behavior}{marker}", flush=True)

        print(f"  {'Degeneracy':<18}", end="", flush=True)
        print("  ".join(f"{degen[str(n)]:.3f}" for n in n_vals), flush=True)

        inverse_cases = []
        for method in METHODS:
            f1s = config_result["methods"][method]["f1_by_n"]
            for i in range(len(n_vals) - 1):
                n1, n2 = n_vals[i], n_vals[i+1]
                drop = f1s[str(n1)] - f1s[str(n2)]
                if drop > 0.001:
                    case = {"method": method, "n1": n1, "n2": n2,
                            "f1_n1": f1s[str(n1)], "f1_n2": f1s[str(n2)],
                            "drop_pp": drop * 100}
                    B = 5000 if len(instances) > 10000 else 10000
                    bt = bootstrap_test(
                        precomputed[(method, n1)]["tuples"],
                        precomputed[(method, n2)]["tuples"], B=B)
                    case["bootstrap"] = bt
                    case["significant"] = bt["ci_95"][1] < 0
                    inverse_cases.append(case)

        if inverse_cases:
            print(f"\n  ** {len(inverse_cases)} INVERSE SCALING TRANSITION(S) **", flush=True)
            n_sig = sum(1 for c in inverse_cases if c["significant"])
            print(f"  {n_sig} significant (95% CI entirely below 0)", flush=True)
            for c in inverse_cases:
                sig = "SIG" if c["significant"] else "ns"
                ci = c["bootstrap"]["ci_95"]
                print(f"    {c['method']:<18} N={c['n1']}->{c['n2']}: "
                      f"{c['f1_n1']:.4f}->{c['f1_n2']:.4f} (drop {c['drop_pp']:.2f}pp)  "
                      f"CI=[{ci[0]*100:+.2f},{ci[1]*100:+.2f}]pp  {sig}", flush=True)
        else:
            print(f"\n  No inverse scaling transitions detected.", flush=True)

        config_result["inverse_cases"] = inverse_cases
        f1_by_n[cfg_name] = config_result

        inverse_summary[cfg_name] = {
            "model": cfg["model"], "dataset": cfg["dataset"],
            "n_instances": len(instances), "max_n": max_n,
            "greedy_f1": greedy_f1,
            "method_behaviors": {m: config_result["methods"][m]["behavior"] for m in METHODS},
            "n_inverse_transitions": len(inverse_cases),
            "n_significant": sum(1 for c in inverse_cases if c["significant"]),
            "inverse_cases": inverse_cases,
            "degeneracy_by_n": degen,
        }
        print(f"  Total time: {time.time()-t0:.1f}s", flush=True)

    # save f1_by_n (strip tuples)
    save_f1 = {}
    for k, v in f1_by_n.items():
        sv = {kk: vv for kk, vv in v.items()}
        save_f1[k] = sv
    with open(os.path.join(OUTPUT_DIR, "f1_by_n.json"), "w") as f:
        json.dump(save_f1, f, indent=2)
    print(f"\nSaved f1_by_n.json", flush=True)

    with open(os.path.join(OUTPUT_DIR, "inverse_scaling_summary.json"), "w") as f:
        json.dump(inverse_summary, f, indent=2)
    print(f"Saved inverse_scaling_summary.json", flush=True)

    total_configs = len(inverse_summary)
    total_transitions = sum(s["n_inverse_transitions"] for s in inverse_summary.values())
    total_sig = sum(s["n_significant"] for s in inverse_summary.values())

    print(f"\n{'='*70}", flush=True)
    print(f"GLOBAL SUMMARY", flush=True)
    print(f"{'='*70}", flush=True)
    print(f"Configs analyzed: {total_configs}", flush=True)
    print(f"Total inverse scaling transitions: {total_transitions}", flush=True)
    print(f"Statistically significant: {total_sig}", flush=True)

    method_inverse = {m: 0 for m in METHODS}
    method_sig = {m: 0 for m in METHODS}
    for s in inverse_summary.values():
        for c in s["inverse_cases"]:
            method_inverse[c["method"]] += 1
            if c["significant"]:
                method_sig[c["method"]] += 1

    print(f"\nPer-method summary:", flush=True)
    print(f"  {'Method':<18} {'Inverse':>8} {'Signif':>8}", flush=True)
    for m in METHODS:
        print(f"  {m:<18} {method_inverse[m]:>8} {method_sig[m]:>8}", flush=True)

    # ---- plot ----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
        fig.suptitle("F1 vs N by Construction Method", fontsize=14, fontweight="bold")

        colors = {
            "majority_vote": "#e41a1c", "lp_weighted": "#377eb8",
            "vc_weighted": "#4daf4a", "sj_weighted": "#984ea3",
            "theta2n": "#ff7f00", "uniform": "#a65628",
        }
        mks = {
            "majority_vote": "o", "lp_weighted": "s",
            "vc_weighted": "D", "sj_weighted": "^",
            "theta2n": "v", "uniform": "P",
        }

        config_order = ["Qwen_SciERC", "Qwen_CoNLL", "Qwen_FewNERD",
                        "LLaMA_SciERC", "LLaMA_CoNLL", "LLaMA_FewNERD"]

        for idx, cfg_name in enumerate(config_order):
            ax = axes[idx // 3][idx % 3]
            if cfg_name not in f1_by_n:
                ax.set_title(f"{cfg_name} (no data)")
                continue

            data = f1_by_n[cfg_name]
            nvs = data["N_values"]

            ax.axhline(y=data["greedy_f1"], color="gray", linestyle="--",
                       linewidth=1, alpha=0.7, label="greedy")

            for method in METHODS:
                md = data["methods"][method]
                f1s = [md["f1_by_n"][str(n)] for n in nvs]
                is_inv = md["behavior"] == "inverse_scaling"
                lw = 2.5 if is_inv else 1.5
                ax.plot(nvs, f1s, color=colors[method], marker=mks[method],
                        linewidth=lw, markersize=6, label=method)

                if is_inv:
                    for i in range(len(nvs)-1):
                        if f1s[i] - f1s[i+1] > 0.001:
                            ax.annotate("", xy=(nvs[i+1], f1s[i+1]),
                                        xytext=(nvs[i], f1s[i]),
                                        arrowprops=dict(arrowstyle="->", color="red",
                                                       lw=2, alpha=0.6))

            ax.set_title(f"{data['model']} / {data['dataset']}", fontsize=11)
            ax.set_xlabel("N (samples)")
            ax.set_ylabel("Entity Micro F1")
            ax.set_xticks(nvs)
            ax.grid(True, alpha=0.3)

            all_f1s = [md["f1_by_n"][str(n)] for m, md in data["methods"].items() for n in nvs if str(n) in md["f1_by_n"]]
            y_min = min(min(all_f1s), data["greedy_f1"]) - 0.02
            y_max = max(max(all_f1s), data["greedy_f1"]) + 0.02
            ax.set_ylim(y_min, y_max)

        handles, labels = axes[0][0].get_legend_handles_labels()
        fig.legend(handles, labels, loc="lower center", ncol=7, fontsize=9,
                   bbox_to_anchor=(0.5, -0.02))
        plt.tight_layout(rect=[0, 0.04, 1, 0.96])
        fig_path = os.path.join(OUTPUT_DIR, "f1_vs_n_all_configs.png")
        plt.savefig(fig_path, dpi=150, bbox_inches="tight")
        print(f"\nSaved plot: {fig_path}", flush=True)
        plt.close()

        inv_configs = [k for k, v in inverse_summary.items() if v["n_inverse_transitions"] > 0]
        if inv_configs:
            n_inv = len(inv_configs)
            fig2, axes2 = plt.subplots(1, max(n_inv, 1), figsize=(7*max(n_inv,1), 5))
            if n_inv == 1:
                axes2 = [axes2]
            fig2.suptitle("Inverse Scaling Cases (F1 vs N)", fontsize=13, fontweight="bold")

            for i, cfg_name in enumerate(inv_configs):
                ax = axes2[i]
                data = f1_by_n[cfg_name]
                nvs = data["N_values"]
                ax.axhline(y=data["greedy_f1"], color="gray", linestyle="--",
                           linewidth=1, alpha=0.7, label="greedy")

                inv_methods = set(c["method"] for c in data["inverse_cases"])
                for method in METHODS:
                    md = data["methods"][method]
                    f1s = [md["f1_by_n"][str(n)] for n in nvs]
                    alpha = 1.0 if method in inv_methods else 0.3
                    lw = 2.5 if method in inv_methods else 1.0
                    ax.plot(nvs, f1s, color=colors[method], marker=mks[method],
                            linewidth=lw, markersize=7 if method in inv_methods else 4,
                            label=method, alpha=alpha)

                    if method in inv_methods:
                        for j in range(len(nvs)-1):
                            if f1s[j] - f1s[j+1] > 0.001:
                                sig_cases = [c for c in data["inverse_cases"]
                                            if c["method"] == method and c["n1"] == nvs[j]]
                                is_sig = any(c["significant"] for c in sig_cases)
                                txt = f"drop {(f1s[j]-f1s[j+1])*100:.1f}pp"
                                if is_sig:
                                    txt += "*"
                                mid_x = (nvs[j] + nvs[j+1]) / 2
                                mid_y = (f1s[j] + f1s[j+1]) / 2
                                ax.annotate(txt, xy=(mid_x, mid_y),
                                           fontsize=8, color="red", fontweight="bold",
                                           ha="center", va="bottom")

                ax.set_title(f"{data['model']} / {data['dataset']}", fontsize=11)
                ax.set_xlabel("N (samples)")
                ax.set_ylabel("Entity Micro F1")
                ax.set_xticks(nvs)
                ax.grid(True, alpha=0.3)
                ax.legend(fontsize=8, loc="best")

            plt.tight_layout()
            fig2_path = os.path.join(OUTPUT_DIR, "inverse_scaling_detail.png")
            plt.savefig(fig2_path, dpi=150, bbox_inches="tight")
            print(f"Saved detail plot: {fig2_path}", flush=True)
            plt.close()

    except Exception as e:
        print(f"Plotting error (non-fatal): {e}", flush=True)
        import traceback
        traceback.print_exc()

    # ---- analysis.md ----
    lines = ["# Inverse Scaling Analysis for Structured Self-Consistency\n\n"]
    lines.append(f"Date: {time.strftime('%Y-%m-%d')}\n\n")
    lines.append("## Question\n\n")
    lines.append("Does increasing the number of samples N ever *decrease* entity-level F1 ")
    lines.append("for any construction method? If so, which methods and under what conditions?\n\n")

    lines.append("## Setup\n\n")
    lines.append(f"- Configs: {total_configs} (2 models x 3 datasets)\n")
    lines.append(f"- Methods: {', '.join(METHODS)}\n")
    lines.append("- Threshold: majority_vote uses theta=0.5 (fixed); lp/vc/sj_weighted and theta2n use theta=2/N (adaptive); uniform uses theta=0.25 (fixed)\n")
    lines.append("- Metric: entity-level micro F1 (pooled TP/FP/FN)\n")
    lines.append("- Significance: paired bootstrap (B=5000-10000), 95% CI\n\n")

    lines.append("## Results\n\n")
    if total_transitions == 0:
        lines.append("**No inverse scaling detected in any configuration.**\n\n")
        lines.append("All methods show monotonically increasing or plateau behavior as N grows.\n\n")
    else:
        lines.append(f"**{total_transitions} inverse scaling transitions detected, {total_sig} statistically significant.**\n\n")
        lines.append("### Inverse Scaling Cases\n\n")
        lines.append("| Config | Method | N1->N2 | F1(N1) | F1(N2) | Drop | 95% CI | Sig? |\n")
        lines.append("|--------|--------|--------|--------|--------|------|--------|------|\n")
        for cfg_name, s in inverse_summary.items():
            for c in s["inverse_cases"]:
                ci = c["bootstrap"]["ci_95"]
                sig = "**YES**" if c["significant"] else "no"
                lines.append(
                    f"| {cfg_name} | {c['method']} | {c['n1']}->{c['n2']} | "
                    f"{c['f1_n1']:.4f} | {c['f1_n2']:.4f} | "
                    f"{c['drop_pp']:.2f}pp | [{ci[0]*100:+.2f},{ci[1]*100:+.2f}] | {sig} |\n"
                )

    lines.append("\n### Method Behavior Summary\n\n")
    lines.append("| Config | " + " | ".join(METHODS) + " |\n")
    lines.append("|--------" + "|--------" * len(METHODS) + "|\n")
    for cfg_name, s in inverse_summary.items():
        cells = []
        for m in METHODS:
            b = s["method_behaviors"][m]
            if b == "inverse_scaling":
                cells.append("**INVERSE**")
            elif b == "plateau":
                cells.append("plateau")
            else:
                cells.append("mono inc")
        lines.append(f"| {cfg_name} | " + " | ".join(cells) + " |\n")

    lines.append("\n### Degeneracy by N\n\n")
    ns_header = [2,4,6,8,16]
    lines.append("| Config |" + " | ".join(f"N={n}" for n in ns_header) + " |\n")
    lines.append("|--------" + "|------" * len(ns_header) + "|\n")
    for cfg_name, s in inverse_summary.items():
        cells = []
        for n in ns_header:
            d = s["degeneracy_by_n"].get(str(n), None)
            cells.append(f"{d:.1%}" if d is not None else "-")
        lines.append(f"| {cfg_name} | " + " | ".join(cells) + " |\n")

    lines.append("\n## Mechanism Analysis\n\n")
    if total_transitions > 0:
        inv_methods = set()
        for s in inverse_summary.values():
            for c in s["inverse_cases"]:
                inv_methods.add(c["method"])

        fixed_theta = inv_methods & {"majority_vote", "uniform"}
        adaptive_theta = inv_methods & {"lp_weighted", "vc_weighted", "sj_weighted", "theta2n"}

        if fixed_theta and not adaptive_theta:
            lines.append("Inverse scaling occurs **only in fixed-threshold methods** (")
            lines.append(", ".join(sorted(fixed_theta)))
            lines.append("). Adaptive-threshold methods (theta=2/N) are immune.\n\n")
            lines.append("**Mechanism**: With fixed theta, the effective vote requirement scales with N. ")
            lines.append("At theta=0.5, an entity needs >N/2 votes. As N grows, correct-but-variable entities ")
            lines.append("fail to reach this threshold, causing recall degradation that outweighs ")
            lines.append("the precision benefits of additional samples.\n\n")
        elif adaptive_theta and fixed_theta:
            lines.append("Inverse scaling occurs in both fixed and adaptive-threshold methods: ")
            lines.append(", ".join(sorted(inv_methods)))
            lines.append(".\n\n")
            lines.append("For fixed-theta methods, the mechanism is clear: rising vote requirements filter correct entities.\n")
            lines.append("For adaptive-theta methods, the mechanism may involve: weight distortion at intermediate N, ")
            lines.append("interaction between signal noise and N, or boundary effects in entity aggregation.\n\n")
        elif adaptive_theta:
            lines.append("Inverse scaling occurs in adaptive-threshold methods: ")
            lines.append(", ".join(sorted(adaptive_theta)))
            lines.append(". This suggests the issue is in the weighting mechanism, not the threshold.\n\n")
        else:
            lines.append("No clear pattern in affected methods.\n\n")

        # degeneracy correlation
        lines.append("### Degeneracy Correlation\n\n")
        for cfg_name, s in inverse_summary.items():
            if s["n_inverse_transitions"] > 0:
                lines.append(f"- **{cfg_name}**: degeneracy at N=2: {s['degeneracy_by_n'].get('2', 'N/A'):.1%}")
                max_n_key = str(max(int(k) for k in s['degeneracy_by_n'].keys()))
                lines.append(f", at N={max_n_key}: {s['degeneracy_by_n'][max_n_key]:.1%}\n")
    else:
        lines.append("No inverse scaling detected. The construction methods are robust to increasing N.\n\n")
        lines.append("This is expected for adaptive-threshold methods (theta=2/N): as N grows, ")
        lines.append("the threshold decreases, compensating for any dilution of correct-but-rare entities. ")
        lines.append("For fixed-threshold methods (theta=0.5, theta=0.25), the monotonic increase suggests ")
        lines.append("that additional samples consistently improve the precision-recall tradeoff.\n\n")

    lines.append("\n## Conclusion\n\n")
    if total_sig > 0:
        lines.append(f"We find {total_sig} statistically significant inverse scaling case(s). ")
        lines.append("This is a notable finding for structured self-consistency. ")
        lines.append("The finding has implications for practitioners choosing aggregation methods ")
        lines.append("and sample budgets.\n")
    elif total_transitions > 0:
        lines.append(f"We observe {total_transitions} inverse scaling transition(s), but none ")
        lines.append("are statistically significant. The drops are within noise range. ")
        lines.append("No strong claim of inverse scaling can be made.\n")
    else:
        lines.append("No inverse scaling is observed. Construction F1 monotonically increases ")
        lines.append("(or plateaus) with N across all tested configurations. ")
        lines.append("Structured self-consistency with entity-level construction is robust to sample budget.\n")

    with open(os.path.join(OUTPUT_DIR, "analysis.md"), "w") as f:
        f.writelines(lines)
    print(f"Saved analysis.md", flush=True)
    print("\nALL DONE", flush=True)

if __name__ == "__main__":
    main()

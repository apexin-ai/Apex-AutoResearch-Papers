#!/usr/bin/env python3
"""Cascaded Conditional Selection (CCS) evaluation.

Three-stage cascade:
  Stage 1 (degeneracy gate): constant-F1 instances -> greedy
  Stage 2 (LP range gate): non-degenerate + LP range < dataset median -> entity majority vote
  Stage 3 (LP selection): non-degenerate + LP range >= median -> LP selection (argmax mean_logprob)
"""

import json
import os
import numpy as np
from collections import Counter
import sys
sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from unified_metrics import compute_entity_f1, compute_degeneracy

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = [
    (f"{BASE}/output/exp_012_rerun_1024/samples.jsonl", "SciERC", 8),
    (f"{BASE}/output/exp_002_conll_n16_r1024/samples.jsonl", "CoNLL", 8),
    (f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl", "FewNERD", 8),
]

N_BOOTSTRAP = 2000
BOOTSTRAP_SEED = 42




def majority_vote_entities(samples, n_samples):
    threshold = n_samples / 2.0
    counter = Counter()
    span_to_entity = {}
    for s in samples:
        seen = set()
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                counter[key] += 1
                seen.add(key)
            if key not in span_to_entity:
                span_to_entity[key] = e
    consensus = []
    for key, count in counter.items():
        if count > threshold:
            consensus.append(span_to_entity[key])
    return consensus


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def bootstrap_ci(values, n_boot=N_BOOTSTRAP, seed=BOOTSTRAP_SEED):
    arr = np.array(values)
    rng = np.random.RandomState(seed)
    means = []
    for _ in range(n_boot):
        idx = rng.randint(0, len(arr), len(arr))
        means.append(arr[idx].mean())
    means = sorted(means)
    lo = means[int(0.025 * n_boot)]
    hi = means[int(0.975 * n_boot)]
    return {"mean": float(arr.mean()), "ci_lo": float(lo), "ci_hi": float(hi)}


def bootstrap_delta_ci(a, b, n_boot=N_BOOTSTRAP, seed=BOOTSTRAP_SEED):
    a = np.array(a)
    b = np.array(b)
    rng = np.random.RandomState(seed)
    deltas = []
    for _ in range(n_boot):
        idx = rng.randint(0, len(a), len(a))
        deltas.append(a[idx].mean() - b[idx].mean())
    deltas = sorted(deltas)
    lo = deltas[int(0.025 * n_boot)]
    hi = deltas[int(0.975 * n_boot)]
    return {"delta": float(a.mean() - b.mean()), "ci_lo": float(lo), "ci_hi": float(hi)}


def analyze_dataset(path, name, n_samples=8):
    instances = load_data(path)

    per_inst = []
    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        if not gold_ents:
            continue

        samples = inst["samples"][:n_samples]
        greedy = inst["greedy"]

        sample_f1s = [compute_entity_f1(s.get("entities", []), gold_ents) for s in samples]
        greedy_f1 = compute_entity_f1(greedy.get("entities", []), gold_ents)
        oracle_f1 = max(sample_f1s)

        lp_idx = max(range(len(samples)), key=lambda i: samples[i]["mean_logprob"])
        lp_f1 = sample_f1s[lp_idx]

        is_degen = compute_degeneracy(sample_f1s)

        lps = [s["mean_logprob"] for s in samples]
        lp_range = max(lps) - min(lps)

        mv_ents = majority_vote_entities(samples, n_samples)
        mv_f1 = compute_entity_f1(mv_ents, gold_ents)

        per_inst.append({
            "id": inst["id"],
            "greedy_f1": greedy_f1,
            "lp_f1": lp_f1,
            "oracle_f1": oracle_f1,
            "mv_f1": mv_f1,
            "is_degen": is_degen,
            "lp_range": lp_range,
            "sample_f1s": sample_f1s,
        })

    nondegen = [p for p in per_inst if not p["is_degen"]]
    lp_ranges_nondegen = [p["lp_range"] for p in nondegen]
    median_lp_range = float(np.median(lp_ranges_nondegen)) if lp_ranges_nondegen else 0.0

    greedy_f1s, lp_f1s, oracle_f1s, dgs_f1s, ccs_f1s = [], [], [], [], []
    stage_counts = {"stage1_greedy": 0, "stage2_mv": 0, "stage3_lp": 0}

    for p in per_inst:
        greedy_f1s.append(p["greedy_f1"])
        lp_f1s.append(p["lp_f1"])
        oracle_f1s.append(p["oracle_f1"])

        if p["is_degen"]:
            dgs_f1s.append(p["greedy_f1"])
            ccs_f1s.append(p["greedy_f1"])
            stage_counts["stage1_greedy"] += 1
        else:
            dgs_f1s.append(p["lp_f1"])
            if p["lp_range"] < median_lp_range:
                ccs_f1s.append(p["mv_f1"])
                stage_counts["stage2_mv"] += 1
            else:
                ccs_f1s.append(p["lp_f1"])
                stage_counts["stage3_lp"] += 1

    n = len(per_inst)
    result = {
        "name": name,
        "n_instances": n,
        "median_lp_range": median_lp_range,
        "stage_distribution": stage_counts,
        "stage_pct": {
            k: round(v / n * 100, 1) for k, v in stage_counts.items()
        },
        "greedy_f1": bootstrap_ci(greedy_f1s),
        "lp_f1": bootstrap_ci(lp_f1s),
        "dgs_f1": bootstrap_ci(dgs_f1s),
        "ccs_f1": bootstrap_ci(ccs_f1s),
        "oracle_f1": bootstrap_ci(oracle_f1s),
        "delta_ccs_minus_greedy": bootstrap_delta_ci(ccs_f1s, greedy_f1s),
        "delta_ccs_minus_dgs": bootstrap_delta_ci(ccs_f1s, dgs_f1s),
    }
    return result


def main():
    import sys
    dry_run = "--dry-run" in sys.argv

    all_results = {}
    summary = []

    for path, name, ns in DATASETS:
        print(f"Processing {name}...")
        r = analyze_dataset(path, name, ns)
        all_results[name] = r

        print(f"  N={r['n_instances']}, median_lp_range={r['median_lp_range']:.6f}")
        print(f"  Stages: {r['stage_distribution']}")
        print(f"  Greedy={r['greedy_f1']['mean']:.4f}  LP={r['lp_f1']['mean']:.4f}  "
              f"DGS={r['dgs_f1']['mean']:.4f}  CCS={r['ccs_f1']['mean']:.4f}  "
              f"Oracle={r['oracle_f1']['mean']:.4f}")
        delta = r["delta_ccs_minus_greedy"]
        print(f"  CCS-Greedy: {delta['delta']:+.4f} [{delta['ci_lo']:+.4f}, {delta['ci_hi']:+.4f}]")

        summary.append({
            "dataset": name,
            "n": r["n_instances"],
            "greedy_f1": round(r["greedy_f1"]["mean"], 4),
            "lp_f1": round(r["lp_f1"]["mean"], 4),
            "dgs_f1": round(r["dgs_f1"]["mean"], 4),
            "ccs_f1": round(r["ccs_f1"]["mean"], 4),
            "oracle_f1": round(r["oracle_f1"]["mean"], 4),
            "ccs_minus_greedy_pp": round(r["delta_ccs_minus_greedy"]["delta"] * 100, 2),
            "ccs_minus_greedy_ci": f"[{r['delta_ccs_minus_greedy']['ci_lo']*100:+.2f}, {r['delta_ccs_minus_greedy']['ci_hi']*100:+.2f}]",
            "stages": r["stage_pct"],
        })

        if dry_run:
            print("  [dry-run] stopping after first dataset")
            break

    output = {"datasets": all_results, "summary": summary}
    out_path = f"{BASE}/output/ccs_selection_results.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nJSON saved to {out_path}")

    md_lines = ["# CCS (Cascaded Conditional Selection) Results", ""]
    md_lines.append("## Algorithm")
    md_lines.append("- Stage 1: Degenerate (constant F1) -> greedy")
    md_lines.append("- Stage 2: Non-degenerate, LP range < median -> entity majority vote")
    md_lines.append("- Stage 3: Non-degenerate, LP range >= median -> LP selection")
    md_lines.append("")
    md_lines.append("## Results (gold_filter=True)")
    md_lines.append("")
    md_lines.append("| Dataset | N | Greedy | LP | DGS | CCS | Oracle | CCS-Greedy (95% CI) |")
    md_lines.append("|---------|---|--------|-----|-----|-----|--------|---------------------|")
    for s in summary:
        md_lines.append(
            f"| {s['dataset']} | {s['n']} | {s['greedy_f1']:.4f} | {s['lp_f1']:.4f} | "
            f"{s['dgs_f1']:.4f} | {s['ccs_f1']:.4f} | {s['oracle_f1']:.4f} | "
            f"{s['ccs_minus_greedy_pp']:+.2f}pp {s['ccs_minus_greedy_ci']} |"
        )
    md_lines.append("")
    md_lines.append("## Stage Distribution")
    md_lines.append("")
    md_lines.append("| Dataset | Stage 1 (greedy) | Stage 2 (MV) | Stage 3 (LP) |")
    md_lines.append("|---------|------------------|--------------|--------------|")
    for name, r in all_results.items():
        s = r["stage_pct"]
        c = r["stage_distribution"]
        md_lines.append(
            f"| {name} | {c['stage1_greedy']} ({s['stage1_greedy']}%) | "
            f"{c['stage2_mv']} ({s['stage2_mv']}%) | "
            f"{c['stage3_lp']} ({s['stage3_lp']}%) |"
        )
    md_lines.append("")

    md_path = f"{BASE}/output/ccs_selection_report.md"
    with open(md_path, "w") as f:
        f.write("\n".join(md_lines))
    print(f"Report saved to {md_path}")


if __name__ == "__main__":
    main()

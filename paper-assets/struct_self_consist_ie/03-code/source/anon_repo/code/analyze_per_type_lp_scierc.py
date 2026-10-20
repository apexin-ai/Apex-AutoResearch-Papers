#!/usr/bin/env python3
"""Per-entity-type LP selection analysis for SciERC (exp_012_rerun_1024)."""
import json, sys, argparse
import numpy as np
from collections import Counter
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1

def get_dominant_type(gold_entities):
    if not gold_entities:
        return None
    type_counts = Counter(e.get("type", "Unknown") for e in gold_entities)
    return type_counts.most_common(1)[0][0]

def compute_key_sets(samples):
    key_sets = []
    for s in samples:
        keys = frozenset((e.get("text",""), e.get("type","")) for e in s.get("entities", []))
        key_sets.append(keys)
    return key_sets

def main():
    input_dir = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024"
    data_path = f"{input_dir}/samples.jsonl"
    output_csv = f"{input_dir}/per_type_lp_analysis.csv"
    tex_path = f"{input_dir}/per_type_lp_table.tex"

    instances = []
    with open(data_path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    print(f"Total instances: {len(instances)}")

    # Filter gold-empty
    filtered = [inst for inst in instances if inst["gold"].get("entities")]
    print(f"After gold-filter: {len(filtered)}")

    # Group by dominant type
    type_groups = {}
    for inst in filtered:
        dtype = get_dominant_type(inst["gold"]["entities"])
        if dtype not in type_groups:
            type_groups[dtype] = []
        type_groups[dtype].append(inst)

    print(f"Entity types: {sorted(type_groups.keys())}")
    print(f"Counts: {[(k, len(v)) for k, v in sorted(type_groups.items(), key=lambda x: -len(x[1]))]}")

    # Per-type analysis
    results = []
    for etype, group in type_groups.items():
        n = len(group)
        greedy_f1s = np.zeros(n)
        oracle_f1s = np.zeros(n)
        lp_sel_f1s = np.zeros(n)
        is_degenerate = np.zeros(n, dtype=bool)
        lp_rho_per_inst = []

        for i, inst in enumerate(group):
            gold = inst["gold"]
            samples = inst["samples"]

            # Greedy F1
            greedy_f1s[i] = per_instance_f1(inst["greedy"], gold, subtask="ner")

            # Sample F1s and LPs
            sample_f1s = np.array([per_instance_f1(s, gold, subtask="ner") for s in samples])
            sample_lps = np.array([s.get("mean_logprob", float("nan")) for s in samples])

            oracle_f1s[i] = sample_f1s.max()

            # LP selection: pick sample with highest mean_logprob
            best_idx = np.nanargmax(sample_lps)
            lp_sel_f1s[i] = sample_f1s[best_idx]

            # Degeneracy
            key_sets = compute_key_sets(samples)
            is_degenerate[i] = len(set(key_sets)) == 1

            # Per-instance LP-F1 correlation
            if np.nanstd(sample_lps) > 1e-10 and np.std(sample_f1s) > 1e-10:
                rho, _ = spearmanr(sample_lps, sample_f1s)
                if not np.isnan(rho):
                    lp_rho_per_inst.append(rho)

        greedy_f1 = float(greedy_f1s.mean())
        oracle_f1 = float(oracle_f1s.mean())
        lp_sel_f1 = float(lp_sel_f1s.mean())
        degen_rate = float(is_degenerate.mean())
        lp_delta = lp_sel_f1 - greedy_f1
        headroom = oracle_f1 - greedy_f1
        lp_rho = float(np.mean(lp_rho_per_inst)) if lp_rho_per_inst else float("nan")

        results.append({
            "type": etype,
            "n_instances": n,
            "degeneracy_rate": degen_rate,
            "greedy_f1": greedy_f1,
            "lp_sel_f1": lp_sel_f1,
            "lp_delta_pp": lp_delta * 100,
            "lp_rho": lp_rho,
            "oracle_f1": oracle_f1,
            "headroom_pp": headroom * 100,
        })

    # Sort by n_instances descending
    results.sort(key=lambda x: -x["n_instances"])

    # Print table
    print("\n" + "="*110)
    print(f"{'Type':<22} {'N':>5} {'Degen%':>8} {'Greedy F1':>10} {'LP Sel F1':>10} {'Δ(pp)':>8} {'LP ρ':>8} {'Oracle F1':>10} {'Headroom':>10}")
    print("-"*110)
    for r in results:
        rho_str = f"{r['lp_rho']:.3f}" if not np.isnan(r['lp_rho']) else "  N/A"
        print(f"{r['type']:<22} {r['n_instances']:>5} {r['degeneracy_rate']*100:>7.1f}% {r['greedy_f1']:>10.4f} {r['lp_sel_f1']:>10.4f} {r['lp_delta_pp']:>+7.2f} {rho_str:>8} {r['oracle_f1']:>10.4f} {r['headroom_pp']:>9.2f}pp")
    print("="*110)

    # Overall (all filtered instances)
    all_greedy = np.array([per_instance_f1(inst["greedy"], inst["gold"], subtask="ner") for inst in filtered])
    all_lp_sel = np.zeros(len(filtered))
    all_oracle = np.zeros(len(filtered))
    all_degen = np.zeros(len(filtered), dtype=bool)
    for i, inst in enumerate(filtered):
        samples = inst["samples"]
        sample_f1s = np.array([per_instance_f1(s, inst["gold"], subtask="ner") for s in samples])
        sample_lps = np.array([s.get("mean_logprob", float("nan")) for s in samples])
        all_lp_sel[i] = sample_f1s[np.nanargmax(sample_lps)]
        all_oracle[i] = sample_f1s.max()
        key_sets = compute_key_sets(samples)
        all_degen[i] = len(set(key_sets)) == 1
    print(f"\n{'OVERALL':<22} {len(filtered):>5} {all_degen.mean()*100:>7.1f}% {all_greedy.mean():>10.4f} {all_lp_sel.mean():>10.4f} {(all_lp_sel.mean()-all_greedy.mean())*100:>+7.2f} {'':>8} {all_oracle.mean():>10.4f} {(all_oracle.mean()-all_greedy.mean())*100:>9.2f}pp")

    # CSV
    import csv
    with open(output_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["type","n_instances","degeneracy_rate","greedy_f1","lp_sel_f1","lp_delta_pp","lp_rho","oracle_f1","headroom_pp"])
        writer.writeheader()
        writer.writerows(results)
    print(f"\nCSV saved: {output_csv}")

    # LaTeX table
    max_delta_idx = max(range(len(results)), key=lambda i: results[i]["lp_delta_pp"])
    with open(tex_path, "w") as f:
        f.write("\\begin{table}[t]\n")
        f.write("\\centering\n")
        f.write("\\caption{Per-entity-type LP selection analysis on SciERC.}\n")
        f.write("\\label{tab:per_type_lp_scierc}\n")
        f.write("\\begin{tabular}{lrrrrrrr}\n")
        f.write("\\toprule\n")
        f.write("Entity Type & N & Degen.\\% & Greedy & LP Sel & $\\Delta$ (pp) & LP $\\rho$ & Oracle \\\\\n")
        f.write("\\midrule\n")
        for i, r in enumerate(results):
            delta_str = f"{r['lp_delta_pp']:+.2f}"
            if i == max_delta_idx:
                delta_str = "\\textbf{" + delta_str + "}"
            rho_str = f"{r['lp_rho']:.3f}" if not np.isnan(r['lp_rho']) else "---"
            type_name = r['type'].replace("OtherScientificTerm", "OtherSciTerm")
            f.write(f"{type_name} & {r['n_instances']} & {r['degeneracy_rate']*100:.1f} & {r['greedy_f1']:.4f} & {r['lp_sel_f1']:.4f} & {delta_str} & {rho_str} & {r['oracle_f1']:.4f} \\\\\n")
        f.write("\\midrule\n")
        f.write(f"Overall & {len(filtered)} & {all_degen.mean()*100:.1f} & {all_greedy.mean():.4f} & {all_lp_sel.mean():.4f} & {(all_lp_sel.mean()-all_greedy.mean())*100:+.2f} & --- & {all_oracle.mean():.4f} \\\\\n")
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")
        f.write("\\end{table}\n")
    print(f"LaTeX saved: {tex_path}")

    # Causal analysis
    print("\n===== Correlation Analysis: Degeneracy vs LP Delta =====")
    degen_rates = np.array([r["degeneracy_rate"] for r in results])
    lp_deltas = np.array([r["lp_delta_pp"] for r in results])
    headrooms = np.array([r["headroom_pp"] for r in results])

    if len(results) >= 4:
        rho_dd, p_dd = spearmanr(degen_rates, lp_deltas)
        rho_dh, p_dh = spearmanr(degen_rates, headrooms)
        rho_hd, p_hd = spearmanr(headrooms, lp_deltas)
        print(f"Spearman(degeneracy, lp_delta):  ρ={rho_dd:.3f}, p={p_dd:.4f}")
        print(f"Spearman(degeneracy, headroom):  ρ={rho_dh:.3f}, p={p_dh:.4f}")
        print(f"Spearman(headroom, lp_delta):    ρ={rho_hd:.3f}, p={p_hd:.4f}")
    else:
        print("Too few types for correlation analysis.")

if __name__ == "__main__":
    main()

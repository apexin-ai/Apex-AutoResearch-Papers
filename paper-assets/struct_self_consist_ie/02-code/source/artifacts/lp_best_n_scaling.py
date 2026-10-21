"""Compute LP-best F1 vs Greedy F1 for N-scaling analysis (micro-average)."""
import json
import os
import sys

DATA_ROOT = "/root/autodl-tmp/struct_self_consist_ie/output"

CONFIGS = [
    ("SciERC", 8, "scierc_mf4v2_seed42", 42),
    ("SciERC", 16, "exp_001_seed42_v2", 42),
    ("SciERC", 32, "scierc_n32_s42", 42),
    ("SciERC", 64, "scierc_n64_seed42", 42),
    ("CoNLL", 8, "conll_mf4v2_seed123", 123),
    ("CoNLL", 16, "conll_n16_s456", 456),
    ("CoNLL", 32, "conll_n32_s42", 42),
    ("CoNLL", 64, "conll_n64_seed42", 42),
    ("FewNERD", 8, "fewnerd_mf4v2_seed42_v3", 42),
    ("FewNERD", 16, "fewnerd_n16_s42", 42),
]


def extract_entities(output_dict):
    return frozenset(
        (e["text"], e["type"], e["start"], e["end"])
        for e in output_dict.get("entities", [])
    )


def compute_micro_f1(results):
    total_tp = sum(r[0] for r in results)
    total_pred = sum(r[1] for r in results)
    total_gold = sum(r[2] for r in results)
    p = total_tp / total_pred if total_pred > 0 else 0
    r = total_tp / total_gold if total_gold > 0 else 0
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0
    return f1, p, r, total_tp, total_pred, total_gold


def analyze_file(filepath, N_expected):
    with open(filepath) as f:
        instances = [json.loads(line) for line in f]

    lp_best_results = []
    greedy_results = []
    n_gold_nonempty = 0

    for inst in instances:
        gold_ents = extract_entities(inst["gold"])
        if len(gold_ents) == 0:
            continue
        n_gold_nonempty += 1

        samples = inst["samples"]
        n_actual = min(len(samples), N_expected)

        mean_lps = [s["mean_logprob"] for s in samples[:n_actual]]
        best_idx = max(range(n_actual), key=lambda i: mean_lps[i])

        pred_lp = extract_entities(samples[best_idx])
        tp_lp = len(pred_lp & gold_ents)
        lp_best_results.append((tp_lp, len(pred_lp), len(gold_ents)))

        pred_greedy = extract_entities(samples[0])
        tp_greedy = len(pred_greedy & gold_ents)
        greedy_results.append((tp_greedy, len(pred_greedy), len(gold_ents)))

    lp_f1, lp_p, lp_r, _, _, _ = compute_micro_f1(lp_best_results)
    greedy_f1, gr_p, gr_r, _, _, _ = compute_micro_f1(greedy_results)

    return {
        "lp_best_f1": lp_f1,
        "greedy_f1": greedy_f1,
        "delta_pp": (lp_f1 - greedy_f1) * 100,
        "n_instances": n_gold_nonempty,
        "lp_p": lp_p,
        "lp_r": lp_r,
    }


def main():
    header = f"{'Dataset':<10} {'N':>4} {'LP-best F1':>11} {'Greedy F1':>10} {'LP d (pp)':>10} {'instances':>10} {'seed':>5}"
    sep = "-" * 70
    print(header)
    print(sep)

    results_lines = []
    for dataset, N, dirname, seed in CONFIGS:
        filepath = os.path.join(DATA_ROOT, dirname, "samples.jsonl")
        if not os.path.exists(filepath):
            line = f"{dataset:<10} {N:>4} {'MISSING':>11}"
            print(line)
            continue
        sys.stderr.write(f"Processing {dataset} N={N} ...\n")
        sys.stderr.flush()
        r = analyze_file(filepath, N)
        line = f"{dataset:<10} {N:>4} {r['lp_best_f1']*100:>10.2f}% {r['greedy_f1']*100:>9.2f}% {r['delta_pp']:>+9.2f} {r['n_instances']:>10} {seed:>5}"
        print(line)
        results_lines.append(line)

    out_path = os.path.join(DATA_ROOT, "lp_best_n_scaling_results.txt")
    with open(out_path, "w") as f:
        f.write(header + "\n")
        f.write(sep + "\n")
        for line in results_lines:
            f.write(line + "\n")
        f.write("\nNotes:\n")
        f.write("- CoNLL N=8 uses seed123 (seed42 not available)\n")
        f.write("- CoNLL N=16 uses seed456 (seed42 not available)\n")
        f.write("- FewNERD N=32 not available\n")
        f.write("- Entity matching: 4-tuple (text, type, start, end)\n")
        f.write("- F1: micro-average over gold-nonempty instances\n")
        f.write("- LP-best: sample with highest mean_logprob\n")
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()

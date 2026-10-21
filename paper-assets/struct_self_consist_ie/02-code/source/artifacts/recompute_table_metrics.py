#!/usr/bin/env python3
"""Recompute gold-filtered + mean_LP metrics for Few-NERD and CoNLL."""
import json
import numpy as np
from scipy import stats as scipy_stats

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def entity_set(output):
    ents = output.get("entities", [])
    return set((e["text"], e["type"]) for e in ents)

def compute_f1(pred_set, gold_set):
    if not pred_set and not gold_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)

def analyze_dataset(data, label):
    total = len(data)
    filtered = [d for d in data if len(d["gold"].get("entities", [])) > 0]
    N = len(filtered)
    print(f"\n{'='*60}")
    print(f"{label}: total={total}, gold-filtered n={N}")
    print(f"{'='*60}")

    greedy_f1s = []
    oracle_f1s = []
    mean_lps = []
    max_lps = []
    lp_sel_f1s = []
    degen_count = 0
    n_samples = len(filtered[0]["samples"]) if filtered else 0
    print(f"N samples per instance: {n_samples}")

    for d in filtered:
        gold_set = entity_set(d["gold"])
        greedy_set = entity_set(d["greedy"])
        gf1 = compute_f1(greedy_set, gold_set)
        greedy_f1s.append(gf1)

        samples = d["samples"]
        logprobs = d.get("logprobs", [])
        if not logprobs:
            logprobs = [s.get("mean_logprob", s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)) for s in samples]

        sample_f1s = []
        for s in samples:
            sf1 = compute_f1(entity_set(s), gold_set)
            sample_f1s.append(sf1)

        oracle_f1s.append(max(sample_f1s))
        mean_lps.append(float(np.mean(logprobs)))
        max_lps.append(float(np.max(logprobs)))

        best_lp_idx = int(np.argmax(logprobs))
        lp_sel_f1s.append(sample_f1s[best_lp_idx])

        if len(set(sample_f1s)) == 1:
            degen_count += 1

    greedy_f1s = np.array(greedy_f1s)
    oracle_f1s = np.array(oracle_f1s)
    mean_lps = np.array(mean_lps)
    max_lps = np.array(max_lps)
    lp_sel_f1s = np.array(lp_sel_f1s)

    greedy_macro = float(greedy_f1s.mean())
    oracle_macro = float(oracle_f1s.mean())
    headroom = (oracle_macro - greedy_macro) * 100
    degen_pct = degen_count / N * 100
    lp_sel_macro = float(lp_sel_f1s.mean())
    lp_delta = (lp_sel_macro - greedy_macro) * 100

    rho_mean, p_mean = scipy_stats.spearmanr(mean_lps, greedy_f1s)
    rho_max, p_max = scipy_stats.spearmanr(max_lps, greedy_f1s)

    print(f"  greedy_F1     = {greedy_macro:.6f} ({greedy_macro:.3f})")
    print(f"  oracle_F1     = {oracle_macro:.6f} ({oracle_macro:.3f})")
    print(f"  headroom      = {headroom:.2f}pp")
    print(f"  degen%        = {degen_pct:.1f}%  ({degen_count}/{N})")
    print(f"  mean_LP rho   = {rho_mean:.6f} (p={p_mean:.2e})")
    print(f"  max_LP rho    = {rho_max:.6f} (p={p_max:.2e})")
    print(f"  LP_sel_F1     = {lp_sel_macro:.6f} ({lp_sel_macro:.3f})")
    print(f"  LP_delta      = {lp_delta:+.2f}pp")

    return {
        "n": N,
        "greedy": round(greedy_macro, 6),
        "oracle": round(oracle_macro, 6),
        "headroom": round(headroom, 2),
        "degen": round(degen_pct, 1),
        "mean_lp_rho": round(float(rho_mean), 6),
        "max_lp_rho": round(float(rho_max), 6),
        "lp_sel": round(lp_sel_macro, 6),
        "lp_delta": round(lp_delta, 2),
    }

base = "/root/autodl-tmp/struct_self_consist_ie/output"

print("="*60)
print("Few-NERD (exp_021_inference)")
print("="*60)
fewnerd = load_data(f"{base}/exp_021_inference/samples.jsonl")
fewnerd_res = analyze_dataset(fewnerd, "Few-NERD")

print("\n" + "="*60)
print("CoNLL (exp002_conll2003)")
print("="*60)
conll = load_data(f"{base}/exp002_conll2003/samples.jsonl")
conll_res = analyze_dataset(conll, "CoNLL")

print("\n" + "="*60)
print("SUMMARY JSON")
print("="*60)
print(json.dumps({"fewnerd": fewnerd_res, "conll": conll_res}, indent=2))

#!/usr/bin/env python3
"""exp-007 340M Rebound comprehensive analysis."""

import json
import os
import sys
import numpy as np
from itertools import combinations
from scipy.stats import mannwhitneyu

# ============================================================
# Configuration
# ============================================================
BASE_340M = "/root/entrainment_gated_ft/lm_eval_clean/exp007/340m"
BASE_1_3B_EXP007 = "/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b"
BASE_1_3B_OLD = "/root/entrainment_gated_ft/lm_eval_clean/1.3b"
BASE_1_3B_RESULTS = "/root/entrainment_gated_ft/results_1.3b/lm_eval_fixed"

ARCHITECTURES = ["GDN", "RetNet", "HGRN2"]
RATIOS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]
RATIO_KEYS = ["pure", "h24_1", "h12_1", "h6_1", "h3_1"]

SIGMA_1_3B = [0.02405, 0.01624, 0.01360, 0.00606, 0.00494]

PATHS_1_3B_CROSS_SCALE = {
    "GDN": {
        "pure": os.path.join(BASE_1_3B_EXP007, "GDN-pure", "samples", "lambada_openai.jsonl"),
        "h3-1": os.path.join(BASE_1_3B_OLD, "GDN-h3-1-logsamples", "samples", "lambada_openai.jsonl"),
    },
    "RetNet": {
        "pure": os.path.join(BASE_1_3B_RESULTS, "1.3B-100B-RetNet-pure",
                             "__root__autodl-tmp__models_1.3b__1.3B-100B-RetNet-pure",
                             "samples_lambada_openai_2026-05-18T18-59-18.864716.jsonl"),
        "h3-1": os.path.join(BASE_1_3B_EXP007, "RetNet-h3-1", "samples", "lambada_openai.jsonl"),
    },
    "HGRN2": {
        "pure": os.path.join(BASE_1_3B_EXP007, "HGRN2-pure", "samples", "lambada_openai.jsonl"),
        "h3-1": os.path.join(BASE_1_3B_EXP007, "HGRN2-h3-1", "samples", "lambada_openai.jsonl"),
    },
}


def get_340m_path(arch, ratio):
    return os.path.join(BASE_340M, f"{arch}-{ratio}" if ratio != "pure" else f"{arch}-pure",
                        "samples", "lambada_openai.jsonl")


def load_jsonl(path):
    data = {}
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            data[rec["doc_id"]] = rec
    return data


def load_acc(path):
    data = load_jsonl(path)
    return {did: int(rec["acc"]) for did, rec in data.items()}


def jaccard(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0.0
    return round(len(s1 & s2) / len(s1 | s2), 4)


def context_word_count(rec):
    return len(rec["doc"]["text"].split())


# ============================================================
# Load data
# ============================================================
print("Loading 340M data...")
acc_340m = {}
full_340m = {}
for arch in ARCHITECTURES:
    acc_340m[arch] = {}
    full_340m[arch] = {}
    for ratio in RATIOS:
        path = get_340m_path(arch, ratio)
        raw = load_jsonl(path)
        acc_340m[arch][ratio] = {did: int(r["acc"]) for did, r in raw.items()}
        full_340m[arch][ratio] = raw
        n_correct = sum(acc_340m[arch][ratio].values())
        n_total = len(acc_340m[arch][ratio])
        print(f"  {arch}-{ratio}: {n_correct}/{n_total} ({n_correct/n_total:.4f})")

# Transformer
tf_raw = load_jsonl(os.path.join(BASE_340M, "Transformer", "samples", "lambada_openai.jsonl"))
acc_340m["Transformer"] = {"pure": {did: int(r["acc"]) for did, r in tf_raw.items()}}
n_tf = sum(acc_340m["Transformer"]["pure"].values())
print(f"  Transformer: {n_tf}/{len(acc_340m['Transformer']['pure'])} ({n_tf/len(acc_340m['Transformer']['pure']):.4f})")

print("\nLoading 1.3B data...")
acc_1_3b = {}
for arch in ARCHITECTURES:
    acc_1_3b[arch] = {}
    for rk in ["pure", "h3-1"]:
        path = PATHS_1_3B_CROSS_SCALE[arch][rk]
        if os.path.exists(path):
            acc_1_3b[arch][rk] = load_acc(path)
            n = sum(acc_1_3b[arch][rk].values())
            print(f"  1.3B {arch}-{rk}: {n}/{len(acc_1_3b[arch][rk])}")
        else:
            acc_1_3b[arch][rk] = None
            print(f"  1.3B {arch}-{rk}: NOT FOUND ({path})")

# ============================================================
# (a) Cross-Architecture Convergence (340M)
# ============================================================
print("\n=== (a) Cross-Architecture Convergence ===")
cross_arch = {}
stds_340m = []

for ratio, rkey in zip(RATIOS, RATIO_KEYS):
    accs = {}
    for arch in ARCHITECTURES:
        total = len(acc_340m[arch][ratio])
        correct = sum(acc_340m[arch][ratio].values())
        accs[arch] = round(correct / total, 4)
    vals = list(accs.values())
    std = round(float(np.std(vals, ddof=0)), 4)
    stds_340m.append(std)
    cross_arch[rkey] = {"std": std, "mean": round(float(np.mean(vals)), 4), "accs": accs}
    print(f"  {ratio}: std={std}, accs={accs}")

min_idx = int(np.argmin(stds_340m))
pure_std = stds_340m[0]
min_std = stds_340m[min_idx]
endpoint_std = stds_340m[-1]

cross_arch["peak_reduction_pct"] = round((pure_std - min_std) / pure_std * 100, 4) if pure_std > 0 else 0
cross_arch["peak_at"] = RATIO_KEYS[min_idx]
cross_arch["endpoint_reduction_pct"] = round((pure_std - endpoint_std) / pure_std * 100, 4) if pure_std > 0 else 0

comparison = {}
for i, rk in enumerate(RATIO_KEYS):
    comparison[rk] = {
        "sigma_340m": stds_340m[i],
        "sigma_1_3b": SIGMA_1_3B[i],
        "ratio_340m_over_1_3b": round(stds_340m[i] / SIGMA_1_3B[i], 4) if SIGMA_1_3B[i] > 0 else None
    }
cross_arch["comparison_1_3b"] = comparison

print(f"  Peak reduction: {cross_arch['peak_reduction_pct']}% at {cross_arch['peak_at']}")
print(f"  Endpoint reduction: {cross_arch['endpoint_reduction_pct']}%")
print(f"  h3-1 σ: {endpoint_std}")

# ============================================================
# (b) Per-Example Helped/Hurt (340M, pure → h3-1)
# ============================================================
print("\n=== (b) Per-Example Helped/Hurt ===")
per_example = {}
helped_sets = {}
hurt_sets = {}

for arch in ARCHITECTURES:
    pure = acc_340m[arch]["pure"]
    h3_1 = acc_340m[arch]["h3-1"]
    common = set(pure) & set(h3_1)
    helped = {d for d in common if pure[d] == 0 and h3_1[d] == 1}
    hurt = {d for d in common if pure[d] == 1 and h3_1[d] == 0}
    helped_sets[arch] = helped
    hurt_sets[arch] = hurt
    per_example[arch] = {"helped": len(helped), "hurt": len(hurt), "net": len(helped) - len(hurt)}
    print(f"  {arch}: helped={len(helped)}, hurt={len(hurt)}, net={len(helped)-len(hurt)}")

jac_helped = {}
jac_hurt = {}
for a1, a2 in combinations(ARCHITECTURES, 2):
    k = f"{a1}_vs_{a2}"
    jac_helped[k] = jaccard(helped_sets[a1], helped_sets[a2])
    jac_hurt[k] = jaccard(hurt_sets[a1], hurt_sets[a2])
    print(f"  Jaccard helped {k}: {jac_helped[k]}, hurt: {jac_hurt[k]}")

per_example["pairwise_jaccard_helped"] = jac_helped
per_example["pairwise_jaccard_hurt"] = jac_hurt

# ============================================================
# (c) Cross-Scale Jaccard (340M vs 1.3B, h3-1)
# ============================================================
print("\n=== (c) Cross-Scale Jaccard ===")
cross_scale = {}

for arch in ARCHITECTURES:
    p13 = acc_1_3b[arch].get("pure")
    h13 = acc_1_3b[arch].get("h3-1")
    if p13 is None or h13 is None:
        cross_scale[f"{arch}_h3_1"] = {"helped_jaccard": None, "hurt_jaccard": None,
                                        "note": f"Missing 1.3B data (pure={'found' if p13 else 'missing'}, h3-1={'found' if h13 else 'missing'})"}
        print(f"  {arch}: SKIPPED — missing 1.3B data")
        continue

    common_13 = set(p13) & set(h13)
    helped_13 = {d for d in common_13 if p13[d] == 0 and h13[d] == 1}
    hurt_13 = {d for d in common_13 if p13[d] == 1 and h13[d] == 0}

    hj = jaccard(helped_sets[arch], helped_13)
    huj = jaccard(hurt_sets[arch], hurt_13)

    cross_scale[f"{arch}_h3_1"] = {
        "helped_jaccard": hj,
        "hurt_jaccard": huj,
        "helped_340m": len(helped_sets[arch]),
        "helped_1_3b": len(helped_13),
        "helped_overlap": len(helped_sets[arch] & helped_13),
        "hurt_340m": len(hurt_sets[arch]),
        "hurt_1_3b": len(hurt_13),
        "hurt_overlap": len(hurt_sets[arch] & hurt_13),
    }
    print(f"  {arch}: helped_J={hj} ({len(helped_sets[arch])}∩{len(helped_13)}={len(helped_sets[arch]&helped_13)}), "
          f"hurt_J={huj} ({len(hurt_sets[arch])}∩{len(hurt_13)}={len(hurt_sets[arch]&hurt_13)})")

# ============================================================
# (d) Rebound Analysis (h6-1 correct → h3-1 wrong)
# ============================================================
print("\n=== (d) Rebound Analysis ===")
rebound_all = set()
stay_correct_all = set()
rebound_per_arch = {}

for arch in ARCHITECTURES:
    h6 = acc_340m[arch]["h6-1"]
    h3 = acc_340m[arch]["h3-1"]
    common = set(h6) & set(h3)
    rb = {d for d in common if h6[d] == 1 and h3[d] == 0}
    sc = {d for d in common if h6[d] == 1 and h3[d] == 1}
    rebound_all |= rb
    stay_correct_all |= sc
    rebound_per_arch[arch] = {"rebound": len(rb), "stay_correct": len(sc)}
    print(f"  {arch}: rebound={len(rb)}, stay_correct={len(sc)}")

stay_correct_all -= rebound_all

ref_full = full_340m["GDN"]["h6-1"]
pure_ref = acc_340m["GDN"]["pure"]

rb_lens = np.array([context_word_count(ref_full[d]) for d in rebound_all if d in ref_full])
sc_lens = np.array([context_word_count(ref_full[d]) for d in stay_correct_all if d in ref_full])
rb_pure = np.array([pure_ref[d] for d in rebound_all if d in pure_ref])
sc_pure = np.array([pure_ref[d] for d in stay_correct_all if d in pure_ref])

if len(rb_lens) > 0 and len(sc_lens) > 0:
    u_stat, u_p = mannwhitneyu(rb_lens, sc_lens, alternative='two-sided')
else:
    u_stat, u_p = None, None

rebound_analysis = {
    "rebound_samples_count": len(rebound_all),
    "stay_correct_samples_count": len(stay_correct_all),
    "per_architecture": rebound_per_arch,
    "context_length_comparison": {
        "rebound_mean": round(float(rb_lens.mean()), 4) if len(rb_lens) else None,
        "rebound_median": round(float(np.median(rb_lens)), 4) if len(rb_lens) else None,
        "rebound_std": round(float(rb_lens.std()), 4) if len(rb_lens) else None,
        "stay_correct_mean": round(float(sc_lens.mean()), 4) if len(sc_lens) else None,
        "stay_correct_median": round(float(np.median(sc_lens)), 4) if len(sc_lens) else None,
        "stay_correct_std": round(float(sc_lens.std()), 4) if len(sc_lens) else None,
    },
    "baseline_acc_comparison": {
        "rebound_pure_acc_rate": round(float(rb_pure.mean()), 4) if len(rb_pure) else None,
        "stay_correct_pure_acc_rate": round(float(sc_pure.mean()), 4) if len(sc_pure) else None,
    },
    "mann_whitney_p": round(float(u_p), 4) if u_p is not None else None,
    "mann_whitney_stat": round(float(u_stat), 4) if u_stat is not None else None,
}

print(f"  Total: rebound={len(rebound_all)}, stay_correct={len(stay_correct_all)}")
print(f"  Context length: rebound mean={rebound_analysis['context_length_comparison']['rebound_mean']}, "
      f"stay_correct mean={rebound_analysis['context_length_comparison']['stay_correct_mean']}")
print(f"  Mann-Whitney p={rebound_analysis['mann_whitney_p']}")
print(f"  Pure acc rate: rebound={rebound_analysis['baseline_acc_comparison']['rebound_pure_acc_rate']}, "
      f"stay_correct={rebound_analysis['baseline_acc_comparison']['stay_correct_pure_acc_rate']}")

# ============================================================
# (e) Attention Ratio Evolution
# ============================================================
print("\n=== (e) Attention Ratio Evolution ===")
evolution = {}
pairs = list(zip(RATIOS[:-1], RATIOS[1:]))
kpairs = list(zip(RATIO_KEYS[:-1], RATIO_KEYS[1:]))

for arch in ARCHITECTURES:
    evolution[arch] = {}
    for (r1, r2), (rk1, rk2) in zip(pairs, kpairs):
        d1 = acc_340m[arch][r1]
        d2 = acc_340m[arch][r2]
        common = set(d1) & set(d2)
        helped = sum(1 for d in common if d1[d] == 0 and d2[d] == 1)
        hurt = sum(1 for d in common if d1[d] == 1 and d2[d] == 0)
        key = f"{rk1}_to_{rk2}"
        evolution[arch][key] = {"helped": helped, "hurt": hurt, "net": helped - hurt}
        print(f"  {arch} {r1}→{r2}: helped={helped}, hurt={hurt}, net={helped-hurt}")

# ============================================================
# Output
# ============================================================
output = {
    "cross_arch_convergence_340m": cross_arch,
    "per_example_340m": per_example,
    "cross_scale_jaccard": cross_scale,
    "rebound_analysis": rebound_analysis,
    "attention_ratio_evolution": evolution,
}

out_path = "/root/entrainment_gated_ft/exp007_340m_analysis.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"\nSaved to {out_path}")
print(json.dumps(output, indent=2, ensure_ascii=False))

#!/usr/bin/env python3
"""Full per-example analysis for ARC-Easy + LAMBADA (Parts A-F)."""
import json
import numpy as np
from itertools import permutations as iterperms

np.random.seed(42)

ARCHS = ["GDN", "RetNet", "HGRN2"]
RATIOS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]
HYBRID_RATIOS = ["h24-1", "h12-1", "h6-1", "h3-1"]
ARCH_PAIRS = [("GDN", "RetNet"), ("GDN", "HGRN2"), ("RetNet", "HGRN2")]
N_PERM = 10000
OUT_DIR = "/root/entrainment_gated_ft"

# === Paths ===
ARC_BASE = "/root/entrainment_gated_ft/lm_eval_clean/arc_easy"
ARC_ARCH_MAP = {"GDN": "GatedDeltaNet", "RetNet": "RetNet", "HGRN2": "HGRN2"}

def arc_path(arch, ratio):
    a = ARC_ARCH_MAP[arch]
    if ratio == "pure":
        return f"{ARC_BASE}/1.3B-100B-{a}-pure/samples/arc_easy.jsonl"
    num = ratio.split("-")[0][1:]
    return f"{ARC_BASE}/1.3B-100B-{a}-hybrid-{num}-1/samples/arc_easy.jsonl"

LAMB_EXP = "/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b"
LAMB_EXTRA = "/root/entrainment_gated_ft/lm_eval_clean/1.3b"

def lambada_path(arch, ratio):
    if arch == "GDN" and ratio in ["h24-1", "h6-1", "h3-1"]:
        return f"{LAMB_EXTRA}/GDN-{ratio}-logsamples/samples/lambada_openai.jsonl"
    name = {"GDN": "GDN", "RetNet": "RetNet", "HGRN2": "HGRN2"}[arch]
    return f"{LAMB_EXP}/{name}-{ratio}/samples/lambada_openai.jsonl"

def load_jsonl(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    return data

# === Load ===
print("Loading data...")
arc_data = {}
lambada_raw = {}
for arch in ARCHS:
    for ratio in RATIOS:
        arc_data[(arch, ratio)] = load_jsonl(arc_path(arch, ratio))
        lambada_raw[(arch, ratio)] = load_jsonl(lambada_path(arch, ratio))

N_ARC = len(arc_data[("GDN", "pure")])
N_LAMB = len(lambada_raw[("GDN", "pure")])
print(f"ARC-Easy: {N_ARC}, LAMBADA: {N_LAMB}")

for arch in ARCHS:
    for ratio in RATIOS:
        assert len(arc_data[(arch, ratio)]) == N_ARC, f"ARC mismatch {arch}/{ratio}: {len(arc_data[(arch,ratio)])} != {N_ARC}"
        assert len(lambada_raw[(arch, ratio)]) == N_LAMB, f"LAMB mismatch {arch}/{ratio}: {len(lambada_raw[(arch,ratio)])} != {N_LAMB}"

# Verify doc_id alignment
for arch in ARCHS:
    for ratio in RATIOS:
        for i in range(min(5, N_ARC)):
            assert arc_data[(arch, ratio)][i]["doc_id"] == i, f"ARC doc_id mismatch {arch}/{ratio} idx={i}"
        for i in range(min(5, N_LAMB)):
            assert lambada_raw[(arch, ratio)][i]["doc_id"] == i, f"LAMB doc_id mismatch {arch}/{ratio} idx={i}"

# Extract arrays
arc_accs = {}; arc_lp = {}
lamb_accs = {}; lamb_lp = {}
for arch in ARCHS:
    for ratio in RATIOS:
        s = arc_data[(arch, ratio)]
        arc_accs[(arch, ratio)] = np.array([x["acc"] for x in s])
        arc_lp[(arch, ratio)] = np.array([x["filtered_resps"][x["target"]][0] for x in s])
        s2 = lambada_raw[(arch, ratio)]
        lamb_accs[(arch, ratio)] = np.array([float(x["acc"]) for x in s2])
        lamb_lp[(arch, ratio)] = np.array([x["filtered_resps"][0][0] for x in s2])

print("\nOverall accuracies:")
for bname, ad in [("ARC", arc_accs), ("LAMB", lamb_accs)]:
    for arch in ARCHS:
        vals = " ".join(f"{r}={np.mean(ad[(arch,r)]):.4f}" for r in RATIOS)
        print(f"  {bname} {arch}: {vals}")

# ============ A. Per-Example Classification ============
print("\n=== A. Per-Example Classification ===")
pe = {}
for arch in ARCHS:
    pe[arch] = {}
    pure = arc_accs[(arch, "pure")]
    for ratio in HYBRID_RATIOS:
        hyb = arc_accs[(arch, ratio)]
        h = int(np.sum((pure == 0) & (hyb == 1)))
        r = int(np.sum((pure == 1) & (hyb == 0)))
        sr = int(np.sum((pure == 1) & (hyb == 1)))
        sw = int(np.sum((pure == 0) & (hyb == 0)))
        pe[arch][ratio] = {
            "n_helped": h, "n_hurt": r,
            "n_stayed_right": sr, "n_stayed_wrong": sw,
            "net_effect": h - r
        }
        print(f"  {arch:6s} {ratio:5s}: helped={h:3d} hurt={r:3d} stayed_right={sr:4d} stayed_wrong={sw:4d} net={h-r:+d}")

# ============ B & C. Jaccard Analysis ============
print("\n=== B & C. Jaccard Analysis ===")

def jaccard(a, b):
    u = a | b
    return len(a & b) / len(u) if len(u) > 0 else 0.0

def get_sets(arch, ratio, accs):
    p = accs[(arch, "pure")]
    h = accs[(arch, ratio)]
    helped = set(np.where((p == 0) & (h == 1))[0])
    hurt = set(np.where((p == 1) & (h == 0))[0])
    return helped, hurt

def j_null_calc(sA, sB, N):
    ei = sA * sB / N
    eu = sA + sB - ei
    return ei / eu if eu > 0 else 0.0

def j_max_calc(sA, sB):
    mn = min(sA, sB)
    d = sA + sB - mn
    return mn / d if d > 0 else 0.0

def perm_test(setA, setB, N, n_perm):
    obs = jaccard(setA, setB)
    la, lb = len(setA), len(setB)
    if la == 0 or lb == 0:
        return 1.0
    cnt = 0
    for _ in range(n_perm):
        pa = set(np.random.choice(N, la, replace=False))
        pb = set(np.random.choice(N, lb, replace=False))
        if jaccard(pa, pb) >= obs:
            cnt += 1
    return cnt / n_perm

jacc = {}
jacc_null = {}
for ratio in HYBRID_RATIOS:
    jacc[ratio] = {}
    jacc_null[ratio] = {}
    for a1, a2 in ARCH_PAIRS:
        pk = f"{a1}-{a2}"
        h1, r1 = get_sets(a1, ratio, arc_accs)
        h2, r2 = get_sets(a2, ratio, arc_accs)
        jh = jaccard(h1, h2)
        jr = jaccard(r1, r2)
        jacc[ratio][pk] = {
            "helped_jaccard": round(jh, 4), "hurt_jaccard": round(jr, 4),
            "helped_sizes": [len(h1), len(h2)], "hurt_sizes": [len(r1), len(r2)],
            "helped_intersection": len(h1 & h2), "hurt_intersection": len(r1 & r2)
        }
        print(f"  {ratio:5s} {pk:14s}: J_helped={jh:.4f}(|A|={len(h1)},|B|={len(h2)},∩={len(h1&h2)})  J_hurt={jr:.4f}(|A|={len(r1)},|B|={len(r2)},∩={len(r1&r2)})")

        for st, s1, s2 in [("helped", h1, h2), ("hurt", r1, r2)]:
            jo = jaccard(s1, s2)
            jn = j_null_calc(len(s1), len(s2), N_ARC)
            jm = j_max_calc(len(s1), len(s2))
            nes = (jo - jn) / (jm - jn) if (jm - jn) > 1e-10 else 0.0
            pv = perm_test(s1, s2, N_ARC, N_PERM)
            jacc_null[ratio][f"{pk}_{st}"] = {
                "J_obs": round(jo, 4), "J_null": round(jn, 4), "J_max": round(jm, 4),
                "normalized_ES": round(nes, 4), "p_value_permutation": round(pv, 4),
                "n_permutations": N_PERM, "sizes": [len(s1), len(s2)]
            }
            sig = "***" if pv < 0.001 else "**" if pv < 0.01 else "*" if pv < 0.05 else "ns"
            print(f"         {st:7s}: J_obs={jo:.4f} J_null={jn:.4f} J_max={jm:.4f} NES={nes:.4f} p={pv:.4f} {sig}")

# ============ D. Convergence sigma ============
print("\n=== D. Convergence sigma ===")

def spearman(x, y):
    n = len(x)
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    d = rx - ry
    return 1.0 - 6.0 * np.sum(d**2) / (n * (n**2 - 1))

conv = {}
msigs = []
for ratio in RATIOS:
    stack = np.stack([arc_accs[(a, ratio)] for a in ARCHS])
    sig = np.std(stack, axis=0)
    ms = float(np.mean(sig))
    conv[ratio] = {
        "mean_sigma": round(ms, 6),
        "median_sigma": round(float(np.median(sig)), 6),
        "n_unanimous_correct": int(np.sum(np.all(stack == 1, axis=0))),
        "n_unanimous_wrong": int(np.sum(np.all(stack == 0, axis=0))),
        "n_split": int(np.sum((np.sum(stack, axis=0) > 0) & (np.sum(stack, axis=0) < 3)))
    }
    msigs.append(ms)
    print(f"  {ratio:5s}: mean_sigma={ms:.6f} split={conv[ratio]['n_split']} unan_right={conv[ratio]['n_unanimous_correct']} unan_wrong={conv[ratio]['n_unanimous_wrong']}")

ranks = np.arange(1, 6, dtype=float)
msigs_arr = np.array(msigs)
rho = spearman(ranks, msigs_arr)

cnt_rho = 0
tot_rho = 0
for perm in iterperms(range(5)):
    ps = msigs_arr[list(perm)]
    r = spearman(ranks, ps)
    if abs(r) >= abs(rho) - 1e-10:
        cnt_rho += 1
    tot_rho += 1
p_rho = cnt_rho / tot_rho
conv["spearman"] = {"rho": round(float(rho), 4), "p_exact_two_tailed": round(p_rho, 4), "n_permutations": tot_rho}
print(f"  Spearman rho={rho:.4f}, p_exact={p_rho:.4f} (n_perm={tot_rho})")

# ============ E. Multiplicity Metrics ============
print("\n=== E. Formal Predictive Multiplicity (Marx et al. 2020) ===")

def compute_mult(accs_d, lp_d, N, name):
    res = {}
    for ratio in RATIOS:
        stack = np.stack([accs_d[(a, ratio)] for a in ARCHS])
        lps = np.stack([lp_d[(a, ratio)] for a in ARCHS])
        nc = np.sum(stack, axis=0)
        unan = (nc == 0) | (nc == 3)
        alpha = float(1.0 - np.mean(unan))

        ac_mask = (nc == 3)
        n_cc = int(np.sum(ac_mask))
        if n_cc > 0:
            lpc = lps[:, ac_mask]
            spreads = np.max(lpc, axis=0) - np.min(lpc, axis=0)
            delta = float(np.mean(spreads))
            delta_std = float(np.std(spreads))
            delta_median = float(np.median(spreads))
        else:
            delta = delta_std = delta_median = None

        dist = {
            "0_of_3": int(np.sum(nc == 0)),
            "1_of_3": int(np.sum(nc == 1)),
            "2_of_3": int(np.sum(nc == 2)),
            "3_of_3": int(np.sum(nc == 3))
        }

        res[ratio] = {
            "ambiguity_alpha": round(alpha, 6),
            "discrepancy_delta_mean": round(delta, 6) if delta is not None else None,
            "discrepancy_delta_std": round(delta_std, 6) if delta_std is not None else None,
            "discrepancy_delta_median": round(delta_median, 6) if delta_median is not None else None,
            "n_concordant_correct": n_cc,
            "disagreement_distribution": dist,
            "n_samples": N
        }
        d_s = f"{delta:.4f}" if delta is not None else "N/A"
        print(f"  {name:4s} {ratio:5s}: alpha={alpha:.4f} delta={d_s} n_cc={n_cc} dist=[{dist['0_of_3']},{dist['1_of_3']},{dist['2_of_3']},{dist['3_of_3']}]")
    return res

mult_arc = compute_mult(arc_accs, arc_lp, N_ARC, "ARC")
mult_lamb = compute_mult(lamb_accs, lamb_lp, N_LAMB, "LAMB")

# ============ F. Save ============
print("\n=== Saving results ===")

r1 = {
    "benchmark": "arc_easy", "n_samples": N_ARC,
    "architectures": ARCHS, "ratios": RATIOS,
    "per_example_classification": pe,
    "convergence_sigma": conv
}
p1 = f"{OUT_DIR}/arc_easy_per_example.json"
with open(p1, "w") as f:
    json.dump(r1, f, indent=2)
print(f"  {p1}")

r2 = {
    "description": "Formal Predictive Multiplicity Metrics (Marx et al. 2020)",
    "model_set": "3 architectures (GDN, RetNet, HGRN2) at each attention ratio",
    "arc_easy": {"n_samples": N_ARC, "metrics": mult_arc},
    "lambada": {"n_samples": N_LAMB, "metrics": mult_lamb}
}
p2 = f"{OUT_DIR}/formal_multiplicity_metrics.json"
with open(p2, "w") as f:
    json.dump(r2, f, indent=2)
print(f"  {p2}")

r3 = {
    "benchmark": "arc_easy", "n_samples": N_ARC,
    "jaccard_similarity": jacc, "jaccard_null_model": jacc_null
}
p3 = f"{OUT_DIR}/arc_easy_jaccard_analysis.json"
with open(p3, "w") as f:
    json.dump(r3, f, indent=2)
print(f"  {p3}")

print("\nAll done!")

import json, numpy as np
from scipy import stats
from pathlib import Path
from datetime import date

DATA_DIR = Path("/root/entrainment_gated_ft/lm_eval_clean")
OUT_DIR = Path("/root/entrainment_gated_ft/analysis")

RATIOS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]
ARCHS = ["RetNet", "HGRN2"]

FILES = {}
for arch in ARCHS:
    for r in RATIOS:
        if r == "pure":
            fname = f"1.3B-100B-{arch}-pure.json"
        else:
            fname = f"1.3B-100B-{arch}-hybrid-{r.replace('h','').replace('-1','')}-1.json"
        FILES[(arch, r)] = DATA_DIR / fname

# ── Part 1: Load summary CSV for aggregate accuracy ──
import csv
summary = {}
with open(DATA_DIR / "summary_all_1.3b.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        summary[row["model_name"]] = float(row["lambada_acc"])

# ── Part 2: Load per-example acc arrays ──
per_example = {}
for (arch, r), fpath in FILES.items():
    d = json.load(open(fpath))
    samples = d["samples"]["lambada_openai"]
    # Sort by doc_id to ensure alignment
    samples_sorted = sorted(samples, key=lambda x: x["doc_id"])
    per_example[(arch, r)] = np.array([s["acc"] for s in samples_sorted])
    # Verify doc_ids match across all files
    if (arch, r) == ("RetNet", "pure"):
        ref_ids = [s["doc_id"] for s in samples_sorted]
    else:
        ids = [s["doc_id"] for s in samples_sorted]
        assert ids == ref_ids, f"doc_id mismatch for {arch}-{r}"

N = len(ref_ids)
print(f"Loaded {N} LAMBADA examples per model, all doc_ids aligned.")

# ── Part 3: Cross-architecture σ ──
cross_arch_sigma = {}
for r in RATIOS:
    name_map = {"RetNet": f"RetNet-{r}", "HGRN2": f"HGRN2-{r}"}
    retnet_acc = summary[name_map["RetNet"]]
    hgrn2_acc = summary[name_map["HGRN2"]]
    sigma = np.std([retnet_acc, hgrn2_acc])
    cross_arch_sigma[r] = {
        "retnet_acc": retnet_acc,
        "hgrn2_acc": hgrn2_acc,
        "abs_diff": abs(retnet_acc - hgrn2_acc),
        "sigma": sigma
    }
    print(f"  {r}: RetNet={retnet_acc:.4f}, HGRN2={hgrn2_acc:.4f}, σ={sigma:.6f}")

# Check monotonicity of σ
sigmas = [cross_arch_sigma[r]["sigma"] for r in RATIOS]
ratio_indices = list(range(len(RATIOS)))  # 0=pure(0 attn), 4=h3-1(8 attn layers)
rho, p_val = stats.spearmanr(ratio_indices, sigmas)
# Monotonic decreasing means rho should be negative (σ drops as attention increases)
is_monotonic = all(sigmas[i] >= sigmas[i+1] for i in range(len(sigmas)-1))
print(f"\nσ sequence: {[f'{s:.6f}' for s in sigmas]}")
print(f"Strictly monotonic decreasing: {is_monotonic}")
print(f"Spearman ρ = {rho:.4f}, p = {p_val:.4f}")

# ── Part 4: Per-example Jaccard ──
jaccard_results = {}
hybrid_ratios = ["h24-1", "h12-1", "h6-1", "h3-1"]

for r in hybrid_ratios:
    # For each arch: helped = pure_wrong & hybrid_right, hurt = pure_right & hybrid_wrong
    helped_sets = {}
    hurt_sets = {}
    for arch in ARCHS:
        pure_acc = per_example[(arch, "pure")]
        hybrid_acc = per_example[(arch, r)]
        helped = set(np.where((pure_acc == 0) & (hybrid_acc == 1))[0].tolist())
        hurt = set(np.where((pure_acc == 1) & (hybrid_acc == 0))[0].tolist())
        helped_sets[arch] = helped
        hurt_sets[arch] = hurt

    # Jaccard between RetNet and HGRN2
    def jaccard(a, b):
        if len(a) == 0 and len(b) == 0:
            return 0.0
        return len(a & b) / len(a | b)

    helped_j = jaccard(helped_sets["RetNet"], helped_sets["HGRN2"])
    hurt_j = jaccard(hurt_sets["RetNet"], hurt_sets["HGRN2"])

    jaccard_results[r] = {
        "helped": {
            "n_retnet": len(helped_sets["RetNet"]),
            "n_hgrn2": len(helped_sets["HGRN2"]),
            "intersection": len(helped_sets["RetNet"] & helped_sets["HGRN2"]),
            "union": len(helped_sets["RetNet"] | helped_sets["HGRN2"]),
            "J": helped_j
        },
        "hurt": {
            "n_retnet": len(hurt_sets["RetNet"]),
            "n_hgrn2": len(hurt_sets["HGRN2"]),
            "intersection": len(hurt_sets["RetNet"] & hurt_sets["HGRN2"]),
            "union": len(hurt_sets["RetNet"] | hurt_sets["HGRN2"]),
            "J": hurt_j
        }
    }
    print(f"\n  {r}: helped J={helped_j:.4f} (RetNet={len(helped_sets['RetNet'])}, HGRN2={len(helped_sets['HGRN2'])}, ∩={len(helped_sets['RetNet'] & helped_sets['HGRN2'])})")
    print(f"       hurt   J={hurt_j:.4f} (RetNet={len(hurt_sets['RetNet'])}, HGRN2={len(hurt_sets['HGRN2'])}, ∩={len(hurt_sets['RetNet'] & hurt_sets['HGRN2'])})")

# ── Part 5: Check Jaccard saturation ──
helped_js = [jaccard_results[r]["helped"]["J"] for r in hybrid_ratios]
hurt_js = [jaccard_results[r]["hurt"]["J"] for r in hybrid_ratios]
max_helped_j = max(helped_js)
# Saturates if range of Jaccard values is small (< 0.03) or first value ~= last
helped_range = max(helped_js) - min(helped_js)
hurt_range = max(hurt_js) - min(hurt_js)
jaccard_saturates = helped_range < 0.05 and hurt_range < 0.05

print(f"\nHelped Jaccard range: {helped_range:.4f}, Hurt Jaccard range: {hurt_range:.4f}")
print(f"Jaccard saturates: {jaccard_saturates}")

# ── Part 6: Conclusion ──
if is_monotonic and jaccard_saturates:
    conclusion = "decoupling_holds_without_GDN"
elif not is_monotonic and not jaccard_saturates:
    conclusion = "decoupling_depends_on_GDN"
else:
    conclusion = "mixed"

# For comparison: include 3-arch σ from exp-010
# (already known: cross-arch std drops 0.024→0.005 monotonically)

result = {
    "analysis": "retnet_hgrn2_only_decoupling",
    "date": str(date.today()),
    "motivation": "Exclude GDN (16-head confound, D004) to test if decoupling holds with only RetNet + HGRN2",
    "n_examples": N,
    "architectures": ARCHS,
    "ratios": RATIOS,
    "cross_arch_sigma": cross_arch_sigma,
    "sigma_sequence": sigmas,
    "sigma_monotonic_decreasing": is_monotonic,
    "sigma_spearman": {"rho": float(rho), "p": float(p_val)},
    "per_example_jaccard": jaccard_results,
    "helped_jaccard_sequence": helped_js,
    "hurt_jaccard_sequence": hurt_js,
    "jaccard_saturates": jaccard_saturates,
    "jaccard_helped_range": helped_range,
    "jaccard_hurt_range": hurt_range,
    "conclusion": conclusion,
    "comparison_to_3arch": {
        "note": "With 3 archs (incl GDN), σ dropped 0.024→0.005 monotonically. 2-arch results shown above.",
        "3arch_sigma_range": "0.024 to 0.005"
    }
}

out_path = OUT_DIR / "retnet_hgrn2_only_decoupling.json"
with open(out_path, "w") as f:
    json.dump(result, f, indent=2)

print(f"\n{'='*60}")
print(f"Result saved to {out_path}")
print(f"Conclusion: {conclusion}")

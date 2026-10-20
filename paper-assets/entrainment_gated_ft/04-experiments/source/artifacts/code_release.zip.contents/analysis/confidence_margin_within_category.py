"""Within-category confidence margin analysis: eliminates definitional confound.

Key insight on margin semantics:
- margin = abs(target_token_loglikelihood)
- For pure-CORRECT: higher margin = lower probability = less confident correct = closer to boundary
- For pure-WRONG: lower margin = higher probability for target = almost correct = closer to boundary
- The "closer to boundary" direction is OPPOSITE for correct vs wrong samples.
"""
import json, os
import numpy as np
from scipy import stats

BASE = "/root/entrainment_gated_ft/lm_eval_clean/exp007/1.3b"

MODELS = {
    "GDN":    {"pure": "GDN-pure",    "hybrid": "GDN-h12-1"},
    "RetNet": {"pure": "RetNet-pure", "hybrid": "RetNet-h3-1"},
    "HGRN2":  {"pure": "HGRN2-pure",  "hybrid": "HGRN2-h3-1"},
}

def load_samples(subdir):
    path = os.path.join(BASE, subdir, "samples", "lambada_openai.jsonl")
    samples = []
    with open(path) as f:
        for line in f:
            samples.append(json.loads(line.strip()))
    return samples

def extract(samples):
    logliks, accs, doc_ids = [], [], []
    for s in samples:
        fr = s["filtered_resps"]
        ll = fr[0][0] if isinstance(fr[0], (list, tuple)) else fr[0]
        logliks.append(float(ll))
        accs.append(int(s["acc"]))
        doc_ids.append(s["doc_id"])
    return np.array(logliks), np.array(accs), np.array(doc_ids)

def cohens_d(x, y):
    nx, ny = len(x), len(y)
    if nx < 2 or ny < 2:
        return 0.0
    pooled_std = np.sqrt(((nx-1)*np.var(x, ddof=1) + (ny-1)*np.var(y, ddof=1)) / (nx+ny-2))
    return float((np.mean(x) - np.mean(y)) / pooled_std) if pooled_std > 0 else 0.0

def margin_stats(arr):
    return {
        "mean": round(float(np.mean(arr)), 4),
        "median": round(float(np.median(arr)), 4),
        "std": round(float(np.std(arr, ddof=1)), 4),
        "q25": round(float(np.percentile(arr, 25)), 4),
        "q75": round(float(np.percentile(arr, 75)), 4),
    }

def run_test(group_a, group_b, label_a, label_b):
    na, nb = len(group_a), len(group_b)
    if na < 2 or nb < 2:
        return {
            f"{label_a}_n": int(na), f"{label_b}_n": int(nb),
            "skipped": True, "reason": "insufficient samples",
        }
    U, p = stats.mannwhitneyu(group_a, group_b, alternative='two-sided')
    r_rb = 1 - (2*U) / (na * nb)
    d = cohens_d(group_a, group_b)
    mean_a, mean_b = np.mean(group_a), np.mean(group_b)
    if p < 0.05:
        direction = f"{label_a}_lower" if mean_a < mean_b else f"{label_b}_lower"
    else:
        direction = "no_diff"
    return {
        f"{label_a}_n": int(na),
        f"{label_b}_n": int(nb),
        f"{label_a}_margin": margin_stats(group_a),
        f"{label_b}_margin": margin_stats(group_b),
        "U": round(float(U), 1),
        "p": float(p),
        "r_rb": round(float(r_rb), 4),
        "cohens_d": round(float(d), 4),
        "direction": direction,
    }

results = {}

for arch, dirs in MODELS.items():
    pure_ll, pure_acc, pure_ids = extract(load_samples(dirs["pure"]))
    hyb_ll, hyb_acc, hyb_ids = extract(load_samples(dirs["hybrid"]))
    assert np.array_equal(pure_ids, hyb_ids), f"doc_id mismatch for {arch}"

    pure_margin = np.abs(pure_ll)

    helped       = (pure_acc == 0) & (hyb_acc == 1)
    hurt         = (pure_acc == 1) & (hyb_acc == 0)
    stayed_right = (pure_acc == 1) & (hyb_acc == 1)
    stayed_wrong = (pure_acc == 0) & (hyb_acc == 0)

    print(f"\n{'='*60}")
    print(f"{arch}: helped={helped.sum()}, hurt={hurt.sum()}, "
          f"stayed_right={stayed_right.sum()}, stayed_wrong={stayed_wrong.sum()}")

    # Control 1: within pure-correct (hurt vs stayed_right)
    # For correct samples: higher abs(loglik) = lower probability = less confident = closer to boundary
    # Expected: hurt has HIGHER margin (less confident correct → vulnerable to attention flipping)
    c1 = run_test(pure_margin[hurt], pure_margin[stayed_right], "hurt", "stayed_right")
    if not c1.get("skipped"):
        c1_dir = c1["direction"]
        # For pure-correct: "hurt has higher margin" = "stayed_right_lower" = expected
        if c1_dir == "stayed_right_lower":
            c1["hypothesis_supported"] = True
            c1["interpretation"] = (
                "Hurt samples had higher abs(loglik) = lower target probability = less confident correct. "
                "Supports hypothesis: weakly-correct answers are vulnerable to attention flipping."
            )
        elif c1_dir == "hurt_lower":
            c1["hypothesis_supported"] = False
            c1["interpretation"] = (
                "Hurt samples had lower abs(loglik) = higher target probability = more confident correct. "
                "Contradicts hypothesis: confidently-correct answers were more likely to be flipped."
            )
        else:
            c1["hypothesis_supported"] = False
            c1["interpretation"] = "No significant difference in confidence within pure-correct."
    print(f"  C1 (pure-correct): dir={c1.get('direction')}, p={c1.get('p','N/A'):.2e}, d={c1.get('cohens_d','N/A')}, supported={c1.get('hypothesis_supported')}")

    # Control 2: within pure-wrong (helped vs stayed_wrong)
    # For wrong samples: lower abs(loglik) = higher target probability = near-miss = closer to boundary
    # Expected: helped has LOWER margin (near-miss wrong → rescuable by attention)
    c2 = run_test(pure_margin[helped], pure_margin[stayed_wrong], "helped", "stayed_wrong")
    if not c2.get("skipped"):
        c2_dir = c2["direction"]
        if c2_dir == "helped_lower":
            c2["hypothesis_supported"] = True
            c2["interpretation"] = (
                "Helped samples had lower abs(loglik) = higher target probability = near-miss wrong. "
                "Supports hypothesis: near-miss wrong answers are rescuable by attention."
            )
        elif c2_dir == "stayed_wrong_lower":
            c2["hypothesis_supported"] = False
            c2["interpretation"] = (
                "Stayed-wrong had lower abs(loglik) — the most uncertain wrong answers were NOT helped."
            )
        else:
            c2["hypothesis_supported"] = False
            c2["interpretation"] = "No significant difference in confidence within pure-wrong."
    print(f"  C2 (pure-wrong): dir={c2.get('direction')}, p={c2.get('p','N/A'):.2e}, d={c2.get('cohens_d','N/A')}, supported={c2.get('hypothesis_supported')}")

    results[arch] = {
        "hybrid_config": dirs["hybrid"],
        "control_1_pure_correct": c1,
        "control_2_pure_wrong": c2,
    }

# Cross-arch summary
c1_supported = [r["control_1_pure_correct"].get("hypothesis_supported", False) for r in results.values()]
c2_supported = [r["control_2_pure_wrong"].get("hypothesis_supported", False) for r in results.values()]

if all(c1_supported) and all(c2_supported):
    conclusion = "within_category_significant"
    summary = (
        "Both controls significant across all 3 architectures with expected directions. "
        "C1: hurt samples were less confident correct (higher |loglik|) than stayed-right — "
        "weakly-correct answers are vulnerable to attention flipping. "
        "C2: helped samples were near-miss wrong (lower |loglik|) vs stayed-wrong — "
        "near-miss wrong answers are rescuable by attention. "
        "Confidence margin genuinely predicts per-example attention effect, "
        "NOT a definitional artifact of the across-category comparison."
    )
elif not any(c1_supported) and not any(c2_supported):
    conclusion = "within_category_null"
    summary = ("Neither control supported in any architecture. "
               "Original across-category effect was entirely definitional artifact.")
else:
    conclusion = "mixed"
    parts = []
    for arch, r in results.items():
        c1s = r["control_1_pure_correct"].get("hypothesis_supported", False)
        c2s = r["control_2_pure_wrong"].get("hypothesis_supported", False)
        parts.append(f"{arch}: C1={'yes' if c1s else 'no'}, C2={'yes' if c2s else 'no'}")
    summary = "Mixed: " + "; ".join(parts)

output = {
    "analysis": "confidence_margin_within_category",
    "date": "2026-05-20",
    "purpose": "rebuttal_reserve_corrected",
    "motivation": (
        "Original across-category analysis (helped vs hurt) has definitional confound: "
        "helped = pure-wrong (naturally high |loglik|), hurt = pure-right (naturally lower |loglik|). "
        "Within-category controls eliminate this confound by comparing only within pure-correct "
        "or only within pure-wrong."
    ),
    "method": {
        "confidence_proxy": "abs(target_token_loglikelihood) from pure model",
        "margin_semantics": {
            "pure_correct": "higher |loglik| = lower probability = less confident correct = closer to boundary",
            "pure_wrong": "lower |loglik| = higher probability for target = near-miss = closer to boundary",
        },
        "control_1": "Within pure-correct: hurt (pure-right, hybrid-wrong) vs stayed-right (pure-right, hybrid-right)",
        "control_2": "Within pure-wrong: helped (pure-wrong, hybrid-right) vs stayed-wrong (pure-wrong, hybrid-wrong)",
        "hypotheses": {
            "C1": "hurt has higher |loglik| than stayed-right (less confident correct → vulnerable)",
            "C2": "helped has lower |loglik| than stayed-wrong (near-miss wrong → rescuable)",
        },
        "tests": ["Mann-Whitney U (two-sided)", "Cohen's d (pooled std)", "rank-biserial r_rb"],
        "note": "GDN uses h12-1 (1.3B h3-1 unavailable); RetNet/HGRN2 use h3-1",
    },
    "per_architecture": results,
    "cross_arch_summary": summary,
    "conclusion": conclusion,
}

out_path = "/root/entrainment_gated_ft/analysis/confidence_margin_within_category.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved: {out_path}")
print(f"Conclusion: {conclusion}")
print(summary)

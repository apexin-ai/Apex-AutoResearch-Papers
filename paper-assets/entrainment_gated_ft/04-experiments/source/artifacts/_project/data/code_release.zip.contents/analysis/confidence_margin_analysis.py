"""Confidence Margin Analysis: helped/hurt samples vs decision boundary proximity."""
import json, os, sys
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

results = {}

for arch, dirs in MODELS.items():
    print(f"\n{'='*60}")
    print(f"{arch}: pure={dirs['pure']}  hybrid={dirs['hybrid']}")
    print(f"{'='*60}")

    pure_ll, pure_acc, pure_ids = extract(load_samples(dirs["pure"]))
    hyb_ll, hyb_acc, hyb_ids = extract(load_samples(dirs["hybrid"]))

    # align by doc_id
    assert np.array_equal(pure_ids, hyb_ids), f"doc_id mismatch for {arch}"
    n = len(pure_ids)

    # confidence margin = abs(loglikelihood) on pure model
    # lower = closer to decision boundary
    pure_margin = np.abs(pure_ll)

    helped = (pure_acc == 0) & (hyb_acc == 1)
    hurt   = (pure_acc == 1) & (hyb_acc == 0)
    same   = pure_acc == hyb_acc

    helped_m = pure_margin[helped]
    hurt_m   = pure_margin[hurt]

    print(f"N={n}, helped={helped.sum()}, hurt={hurt.sum()}, same={same.sum()}")
    print(f"Helped margin: mean={helped_m.mean():.4f}, med={np.median(helped_m):.4f}, "
          f"q25={np.percentile(helped_m,25):.4f}, q75={np.percentile(helped_m,75):.4f}")
    print(f"Hurt   margin: mean={hurt_m.mean():.4f}, med={np.median(hurt_m):.4f}, "
          f"q25={np.percentile(hurt_m,25):.4f}, q75={np.percentile(hurt_m,75):.4f}")

    # Mann-Whitney U
    U, p = stats.mannwhitneyu(helped_m, hurt_m, alternative='two-sided')
    n1, n2 = len(helped_m), len(hurt_m)
    r_rb = 1 - (2*U) / (n1 * n2)
    print(f"Mann-Whitney U={U:.1f}, p={p:.6f}, r_rb={r_rb:.4f}")

    # KS test
    ks_stat, ks_p = stats.ks_2samp(helped_m, hurt_m)
    print(f"KS test: D={ks_stat:.4f}, p={ks_p:.6f}")

    # Borderline analysis: proportion in low-confidence bins
    thresholds = [1.0, 2.0, 3.0]
    borderline_rates = {}
    for t in thresholds:
        h_rate = (helped_m < t).mean() if len(helped_m) > 0 else 0
        u_rate = (hurt_m < t).mean() if len(hurt_m) > 0 else 0
        borderline_rates[f"<{t}"] = {"helped": float(h_rate), "hurt": float(u_rate)}
        print(f"  margin<{t}: helped={h_rate:.3f}, hurt={u_rate:.3f}")

    # Cohen's d
    pooled_std = np.sqrt((helped_m.std()**2 + hurt_m.std()**2) / 2)
    d = (helped_m.mean() - hurt_m.mean()) / pooled_std if pooled_std > 0 else 0

    if p < 0.05 and helped_m.mean() < hurt_m.mean():
        interp = "helped_lower_confidence"
    elif p < 0.05 and hurt_m.mean() < helped_m.mean():
        interp = "hurt_lower_confidence"
    else:
        interp = "no_significant_difference"

    results[arch] = {
        "hybrid_config": dirs["hybrid"],
        "n_total": int(n),
        "n_helped": int(n1),
        "n_hurt": int(n2),
        "n_same": int(same.sum()),
        "helped_margin": {
            "mean": round(float(helped_m.mean()), 4),
            "median": round(float(np.median(helped_m)), 4),
            "std": round(float(helped_m.std()), 4),
            "q25": round(float(np.percentile(helped_m, 25)), 4),
            "q75": round(float(np.percentile(helped_m, 75)), 4),
        },
        "hurt_margin": {
            "mean": round(float(hurt_m.mean()), 4),
            "median": round(float(np.median(hurt_m)), 4),
            "std": round(float(hurt_m.std()), 4),
            "q25": round(float(np.percentile(hurt_m, 25)), 4),
            "q75": round(float(np.percentile(hurt_m, 75)), 4),
        },
        "mann_whitney": {"U": round(float(U), 1), "p": float(p), "r_rb": round(float(r_rb), 4)},
        "ks_test": {"D": round(float(ks_stat), 4), "p": float(ks_p)},
        "cohens_d": round(float(d), 4),
        "borderline_rates": borderline_rates,
        "interpretation": interp,
    }

# cross-arch narrative
interps = [r["interpretation"] for r in results.values()]
if all(i == "no_significant_difference" for i in interps):
    narrative = "opaque_reinforced"
    narrative_text = ("Confidence margin shows no significant difference between helped/hurt "
                      "across all architectures. The borderline hypothesis is NOT supported. "
                      "This reinforces the 'opaque' narrative: attention's per-example effect "
                      "cannot be predicted from the pure model's confidence.")
elif any(i == "helped_lower_confidence" for i in interps):
    narrative = "borderline_hypothesis_partial"
    narrative_text = ("Some architectures show helped samples had lower pure-model confidence, "
                      "partially supporting the borderline hypothesis.")
else:
    narrative = "mixed"
    narrative_text = "Mixed or unexpected pattern."

output = {
    "analysis": "confidence_margin",
    "date": "2026-05-20",
    "purpose": "rebuttal_reserve",
    "method": {
        "confidence_proxy": "abs(target_token_loglikelihood) from pure model",
        "interpretation": "lower value = closer to decision boundary",
        "comparison": "helped (pure wrong, hybrid right) vs hurt (pure right, hybrid wrong)",
        "tests": ["Mann-Whitney U (two-sided)", "KS two-sample", "Cohen's d"],
        "note": "GDN uses h12-1 (h3-1 unavailable at 1.3B); RetNet/HGRN2 use h3-1"
    },
    "per_architecture": results,
    "cross_arch_narrative": narrative,
    "narrative_text": narrative_text,
}

out_path = "/root/entrainment_gated_ft/analysis/confidence_margin_analysis.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved: {out_path}")
print(f"\nNarrative: {narrative}")
print(narrative_text)

import json
from itertools import combinations
from pathlib import Path

BASE = Path("/root/entrainment_gated_ft/lm_eval_clean")
RATIOS = ["h24-1", "h12-1", "h6-1", "h3-1"]

# Map (arch, config) -> path to lambada_openai.jsonl
PATHS = {}
# exp007/1.3b has most models
for d in (BASE / "exp007" / "1.3b").iterdir():
    if d.is_dir():
        jsonl = d / "samples" / "lambada_openai.jsonl"
        if jsonl.exists():
            name = d.name  # e.g. GDN-pure, RetNet-h3-1
            PATHS[name] = jsonl
# 1.3b/ has extra GDN logsamples
for d in (BASE / "1.3b").iterdir():
    if d.is_dir():
        jsonl = d / "samples" / "lambada_openai.jsonl"
        if jsonl.exists():
            name = d.name.replace("-logsamples", "")
            if name not in PATHS:
                PATHS[name] = jsonl

ARCH_MAP = {
    "GatedDeltaNet": {"pure": "GDN-pure", "h24-1": "GDN-h24-1", "h12-1": "GDN-h12-1", "h6-1": "GDN-h6-1", "h3-1": "GDN-h3-1"},
    "RetNet": {"pure": "RetNet-pure", "h24-1": "RetNet-h24-1", "h12-1": "RetNet-h12-1", "h6-1": "RetNet-h6-1", "h3-1": "RetNet-h3-1"},
    "HGRN2": {"pure": "HGRN2-pure", "h24-1": "HGRN2-h24-1", "h12-1": "HGRN2-h12-1", "h6-1": "HGRN2-h6-1", "h3-1": "HGRN2-h3-1"},
}

def load_correct_set(path):
    correct = set()
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            if row["acc"] == 1:
                correct.add(row["doc_id"])
    return correct

def jaccard(a, b):
    union = a | b
    if len(union) == 0:
        return float('nan')
    return len(a & b) / len(union)

print("Available paths:", sorted(PATHS.keys()))

results = {}
all_helped_j = []
all_hurt_j = []

for arch, name_map in ARCH_MAP.items():
    print(f"\n=== {arch} ===")
    # Check all paths exist
    missing = [k for k, v in name_map.items() if v not in PATHS]
    if missing:
        print(f"  MISSING: {missing}")
        continue

    pure_correct = load_correct_set(PATHS[name_map["pure"]])
    print(f"  pure correct: {len(pure_correct)}/5153")

    # Compute helped/hurt for each ratio
    helped = {}
    hurt = {}
    for r in RATIOS:
        r_correct = load_correct_set(PATHS[name_map[r]])
        helped[r] = r_correct - pure_correct
        hurt[r] = pure_correct - r_correct
        print(f"  {r}: correct={len(r_correct)}, helped={len(helped[r])}, hurt={len(hurt[r])}")

    # Pairwise Jaccard
    helped_jaccard = {}
    hurt_jaccard = {}
    for r1, r2 in combinations(RATIOS, 2):
        key = f"{r1}_vs_{r2}"
        hj = jaccard(helped[r1], helped[r2])
        huj = jaccard(hurt[r1], hurt[r2])
        helped_jaccard[key] = round(hj, 4)
        hurt_jaccard[key] = round(huj, 4)
        all_helped_j.append(hj)
        all_hurt_j.append(huj)
        print(f"  J_helped({r1},{r2})={hj:.4f}  J_hurt({r1},{r2})={huj:.4f}")

    results[arch] = {
        "helped_jaccard": helped_jaccard,
        "hurt_jaccard": hurt_jaccard,
        "helped_counts": {r: len(helped[r]) for r in RATIOS},
        "hurt_counts": {r: len(hurt[r]) for r in RATIOS},
        "pure_correct_count": len(pure_correct),
    }

import math
valid_hj = [x for x in all_helped_j if not math.isnan(x)]
valid_huj = [x for x in all_hurt_j if not math.isnan(x)]
mean_hj = sum(valid_hj) / len(valid_hj) if valid_hj else float('nan')
mean_huj = sum(valid_huj) / len(valid_huj) if valid_huj else float('nan')

# Interpretation
if mean_hj > 0.4:
    interp = f"Within-architecture helped/hurt sets are moderately to highly stable (mean helped J={mean_hj:.3f}, mean hurt J={mean_huj:.3f}). Different attention ratios help/hurt largely the same examples."
elif mean_hj > 0.2:
    interp = f"Within-architecture helped/hurt sets show moderate overlap (mean helped J={mean_hj:.3f}, mean hurt J={mean_huj:.3f}). There is a shared core but also ratio-specific effects."
else:
    interp = f"Within-architecture helped/hurt sets are unstable (mean helped J={mean_hj:.3f}, mean hurt J={mean_huj:.3f}). Even within one architecture, different attention ratios help/hurt different examples."

results["summary"] = {
    "mean_within_arch_helped_J": round(mean_hj, 4),
    "mean_within_arch_hurt_J": round(mean_huj, 4),
    "interpretation": interp,
}

out_path = "/root/entrainment_gated_ft/analysis/within_arch_stability.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {out_path}")
print(f"\nSummary: mean_helped_J={mean_hj:.4f}, mean_hurt_J={mean_huj:.4f}")
print(interp)

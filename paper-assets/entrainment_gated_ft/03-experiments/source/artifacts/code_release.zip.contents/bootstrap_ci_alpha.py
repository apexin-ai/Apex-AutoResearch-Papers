import numpy as np
import json
from pathlib import Path

np.random.seed(42)
N_BOOTSTRAP = 10000
BASE = Path("/root/entrainment_gated_ft/lm_eval_clean")

ARCHS = ["GatedDeltaNet", "RetNet", "HGRN2"]
RATIOS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]

BENCHMARKS = {
    "PIQA": {"dir": "piqa", "file": "piqa.jsonl", "metric": "acc"},
    "HellaSwag": {"dir": "hellaswag", "file": "hellaswag.jsonl", "metric": "acc_norm"},
    "ARC-Easy": {"dir": "arc_easy", "file": "arc_easy.jsonl", "metric": "acc"},
    "LAMBADA": {"dir": None, "file": "lambada_openai.jsonl", "metric": "acc"},
}

def ratio_to_dir_suffix(ratio):
    """h24-1 -> hybrid-24-1, pure -> pure"""
    if ratio == "pure":
        return "pure"
    return "hybrid-" + ratio[1:]  # strip leading 'h'

def get_sample_path(bench_key, arch, ratio):
    info = BENCHMARKS[bench_key]
    if bench_key != "LAMBADA":
        config = ratio_to_dir_suffix(ratio)
        return BASE / info["dir"] / f"1.3B-100B-{arch}-{config}" / "samples" / info["file"]
    else:
        short = {"GatedDeltaNet": "GDN", "RetNet": "RetNet", "HGRN2": "HGRN2"}[arch]
        config = "pure" if ratio == "pure" else ratio
        if arch == "GatedDeltaNet" and ratio in ("h3-1", "h6-1", "h24-1"):
            return BASE / "1.3b" / f"{short}-{config}-logsamples" / "samples" / info["file"]
        else:
            return BASE / "exp007" / "1.3b" / f"{short}-{config}" / "samples" / info["file"]

def load_per_example(path, metric):
    results = {}
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            doc_id = rec["doc_id"]
            results[doc_id] = int(rec[metric])
    return results

def bootstrap_alpha(disagreements, n_boot=N_BOOTSTRAP):
    n = len(disagreements)
    alphas = np.zeros(n_boot)
    for i in range(n_boot):
        idx = np.random.randint(0, n, size=n)
        alphas[i] = disagreements[idx].mean()
    return {
        "alpha_hat": float(disagreements.mean()),
        "ci_lower": float(np.percentile(alphas, 2.5)),
        "ci_upper": float(np.percentile(alphas, 97.5)),
        "ci_width": float(np.percentile(alphas, 97.5) - np.percentile(alphas, 2.5)),
        "se": float(alphas.std()),
    }

results = {}
for bench_key in BENCHMARKS:
    results[bench_key] = {}
    for ratio in RATIOS:
        arch_preds = {}
        for arch in ARCHS:
            path = get_sample_path(bench_key, arch, ratio)
            if not path.exists():
                print(f"MISSING: {path}")
                continue
            arch_preds[arch] = load_per_example(path, BENCHMARKS[bench_key]["metric"])

        if len(arch_preds) < 3:
            print(f"Skipping {bench_key}/{ratio}: only {len(arch_preds)} archs")
            continue

        common_ids = sorted(set.intersection(*[set(v.keys()) for v in arch_preds.values()]))
        n_samples = len(common_ids)

        preds = np.array([[arch_preds[a][did] for did in common_ids] for a in ARCHS])
        disagree = (preds.min(axis=0) != preds.max(axis=0)).astype(np.int32)

        ci = bootstrap_alpha(disagree)
        ci["n_samples"] = n_samples
        results[bench_key][ratio] = ci
        print(f"{bench_key:12s} {ratio:6s}: α={ci['alpha_hat']:.4f} [{ci['ci_lower']:.4f}, {ci['ci_upper']:.4f}] (n={n_samples})")

output = {
    "analysis": "bootstrap_ci_alpha",
    "n_bootstrap": N_BOOTSTRAP,
    "seed": 42,
    "results": results,
}

out_path = "/tmp/bootstrap_ci_alpha.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {out_path}")

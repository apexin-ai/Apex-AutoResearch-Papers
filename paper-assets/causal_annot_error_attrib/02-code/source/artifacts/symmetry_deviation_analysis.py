"""Frobenius distance to symmetry for empirical LLM confusion matrices."""

import json
import numpy as np
from pathlib import Path

DATA_FILES = [
    "plan011_frontier_cms.json",
    "plan011_new_cms.json",
    "plan011_new_cms_round2.json",
    "plan011_new_cms_vast_qwen3_zs.json",
]

def load_all_matrices():
    base = Path(__file__).parent
    matrices = {}
    for fname in DATA_FILES:
        p = base / fname
        if not p.exists():
            print(f"SKIP (not found): {fname}")
            continue
        with open(p) as f:
            data = json.load(f)
        for config_name, entry in data.items():
            C = np.array(entry["confusion_matrix_normalized"])
            matrices[config_name] = C
    return matrices


def analyze(matrices):
    per_matrix = {}
    d_rels = []

    for name, C in sorted(matrices.items()):
        K = C.shape[0]
        C_sym = (C + C.T) / 2
        d_F = float(np.linalg.norm(C - C_sym, "fro"))
        d_rel = float(d_F / np.linalg.norm(C, "fro"))
        diag_mean = float(np.mean(np.diag(C)))
        d_rels.append(d_rel)
        per_matrix[name] = {
            "K": K,
            "d_F": round(d_F, 6),
            "d_rel": round(d_rel, 6),
            "diag_mean": round(diag_mean, 4),
            "C": C.tolist(),
        }

    d_rels = np.array(d_rels)
    diag_means = [v["diag_mean"] for v in per_matrix.values()]

    summary = {
        "d_rel_min": round(float(np.min(d_rels)), 6),
        "d_rel_median": round(float(np.median(d_rels)), 6),
        "d_rel_mean": round(float(np.mean(d_rels)), 6),
        "d_rel_max": round(float(np.max(d_rels)), 6),
        "n_near_symmetric_005": int(np.sum(d_rels < 0.05)),
        "n_near_symmetric_010": int(np.sum(d_rels < 0.10)),
        "diag_mean_range": [round(min(diag_means), 4), round(max(diag_means), 4)],
    }

    return {
        "description": "Frobenius distance to symmetry for empirical LLM confusion matrices",
        "n_matrices": len(matrices),
        "summary": summary,
        "per_matrix": per_matrix,
    }


if __name__ == "__main__":
    matrices = load_all_matrices()
    result = analyze(matrices)

    out_path = Path(__file__).parent / "symmetry_deviation_results.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    s = result["summary"]
    print(f"n_matrices: {result['n_matrices']}")
    print(f"d_rel: min={s['d_rel_min']:.4f}  median={s['d_rel_median']:.4f}  mean={s['d_rel_mean']:.4f}  max={s['d_rel_max']:.4f}")
    print(f"near-symmetric (<5%): {s['n_near_symmetric_005']}/{result['n_matrices']}")
    print(f"near-symmetric (<10%): {s['n_near_symmetric_010']}/{result['n_matrices']}")
    print(f"diag_mean range: [{s['diag_mean_range'][0]:.4f}, {s['diag_mean_range'][1]:.4f}]")
    print()
    for name, v in sorted(result["per_matrix"].items()):
        print(f"  {name:45s}  K={v['K']:2d}  d_rel={v['d_rel']:.4f}  diag={v['diag_mean']:.4f}")

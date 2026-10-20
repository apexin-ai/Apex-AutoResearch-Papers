"""Compute Gwet's AC1 inter-coder agreement coefficient."""

import json
import numpy as np
from pathlib import Path

DATA_DIR = Path(__file__).parent


def compute_ac1(matrix):
    """Compute Gwet's AC1 from a confusion matrix (rows=coder1, cols=coder2)."""
    matrix = np.array(matrix, dtype=float)
    N = matrix.sum()
    q = matrix.shape[0]

    P_o = np.trace(matrix) / N

    row_marginals = matrix.sum(axis=1)
    col_marginals = matrix.sum(axis=0)
    pi_k = (row_marginals + col_marginals) / (2 * N)

    P_e = (2.0 / (q * (q - 1))) * np.sum(pi_k * (1 - pi_k))

    ac1 = (P_o - P_e) / (1 - P_e)
    return ac1, P_o, P_e, pi_k


def bootstrap_ac1_ci(matrix, n_boot=10000, alpha=0.05, seed=42):
    """Bootstrap CI for AC1 by resampling cell pairs from the confusion matrix."""
    matrix = np.array(matrix, dtype=float)
    N = int(matrix.sum())
    q = matrix.shape[0]
    rng = np.random.default_rng(seed)

    pairs = []
    for i in range(q):
        for j in range(q):
            count = int(matrix[i, j])
            pairs.extend([(i, j)] * count)
    pairs = np.array(pairs)

    ac1_samples = []
    for _ in range(n_boot):
        idx = rng.choice(N, size=N, replace=True)
        boot_pairs = pairs[idx]
        boot_matrix = np.zeros((q, q), dtype=float)
        for r, c in boot_pairs:
            boot_matrix[r, c] += 1

        boot_P_o = np.trace(boot_matrix) / N
        boot_row = boot_matrix.sum(axis=1)
        boot_col = boot_matrix.sum(axis=0)
        boot_pi = (boot_row + boot_col) / (2 * N)
        boot_P_e = (2.0 / (q * (q - 1))) * np.sum(boot_pi * (1 - boot_pi))

        if boot_P_e < 1.0:
            ac1_samples.append((boot_P_o - boot_P_e) / (1 - boot_P_e))
        else:
            ac1_samples.append(1.0)

    ac1_samples = np.array(ac1_samples)
    lower = float(np.percentile(ac1_samples, 100 * alpha / 2))
    upper = float(np.percentile(ac1_samples, 100 * (1 - alpha / 2)))
    return lower, upper


def interpret_ac1(ac1):
    if ac1 >= 0.81:
        return "almost perfect"
    elif ac1 >= 0.61:
        return "substantial"
    elif ac1 >= 0.41:
        return "moderate"
    elif ac1 >= 0.21:
        return "fair"
    elif ac1 >= 0.0:
        return "slight"
    else:
        return "poor"


def main():
    with open(DATA_DIR / "merged_agreement.json") as f:
        data = json.load(f)

    matrix = data["confusion_matrix_merged"]["matrix"]
    labels = data["confusion_matrix_merged"]["labels"]
    N = data["n_traces"]

    ac1, P_o, P_e, pi_k = compute_ac1(matrix)
    ci_lower, ci_upper = bootstrap_ac1_ci(matrix)

    print(f"=== Overall Gwet's AC1 ===")
    print(f"N = {N}, q = {len(labels)}")
    print(f"P_o (observed agreement) = {P_o:.4f}")
    print(f"P_e (AC1 chance agreement) = {P_e:.4f}")
    print(f"AC1 = {ac1:.4f}")
    print(f"95% CI = [{ci_lower:.4f}, {ci_upper:.4f}]")
    print(f"Cohen's κ = {data['merged_kappa']}")
    print(f"Category marginals (π_k): {dict(zip(labels, [round(float(p), 4) for p in pi_k]))}")
    print()

    prevalence_note = (
        f"AC1 ({ac1:.3f}) vs κ ({data['merged_kappa']:.3f}): "
        f"the {ac1 - data['merged_kappa']:.3f} gap confirms prevalence paradox — "
        f"'inappropriate_action' dominates at π={pi_k[labels.index('inappropriate_action')]:.2f}, "
        f"inflating κ's chance agreement and depressing κ."
    )
    print(prevalence_note)

    per_type = {}
    for atype, info in data["per_type_merged_kappa"].items():
        entry = {
            "n": info["n"],
            "percent_agreement": info["percent_agreement"],
            "kappa": info["kappa"],
            "ac1_note": "per-type confusion matrices unavailable; AC1 requires full category×category matrix"
        }
        per_type[atype] = entry

    results = {
        "overall_ac1": round(float(ac1), 4),
        "overall_ac1_ci_95": [round(ci_lower, 4), round(ci_upper, 4)],
        "overall_kappa_comparison": data["merged_kappa"],
        "overall_percent_agreement": data["merged_percent_agreement"],
        "P_o": round(float(P_o), 4),
        "P_e_ac1": round(float(P_e), 4),
        "category_marginals_pi": {lab: round(float(p), 4) for lab, p in zip(labels, pi_k)},
        "interpretation": interpret_ac1(ac1),
        "prevalence_paradox": prevalence_note,
        "per_type": per_type,
        "target_met": float(ac1) >= 0.70,
        "note": "AC1 is more robust to prevalence imbalance than Cohen's κ"
    }

    out_path = DATA_DIR / "gwet_ac1_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to {out_path}")
    print(f"Target (AC1 ≥ 0.70): {'✅ MET' if results['target_met'] else '❌ NOT MET'}")


if __name__ == "__main__":
    main()

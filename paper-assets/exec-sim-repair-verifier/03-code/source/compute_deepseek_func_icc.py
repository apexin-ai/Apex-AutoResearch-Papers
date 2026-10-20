#!/usr/bin/env python3
"""Compute inter-seed ICC(3,1) for DeepSeek function-level CLS."""
import json, sys, os
import numpy as np

def load_predictions(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

def icc_3_1(matrix):
    """ICC(3,1) two-way mixed, single measures.
    matrix: (n_subjects, k_raters) array of 0/1 values.
    """
    n, k = matrix.shape
    if n < 2 or k < 2:
        return float('nan'), float('nan'), float('nan')

    grand_mean = matrix.mean()
    row_means = matrix.mean(axis=1)
    col_means = matrix.mean(axis=0)

    SS_total = ((matrix - grand_mean) ** 2).sum()
    SS_rows = k * ((row_means - grand_mean) ** 2).sum()
    SS_cols = n * ((col_means - grand_mean) ** 2).sum()
    SS_error = SS_total - SS_rows - SS_cols

    MS_rows = SS_rows / (n - 1)
    MS_error = SS_error / ((n - 1) * (k - 1))

    # ICC(3,1)
    denom = MS_rows + (k - 1) * MS_error
    if denom == 0:
        icc = 0.0
    else:
        icc = (MS_rows - MS_error) / denom

    # 95% CI using F distribution
    if MS_error == 0:
        return icc, float('nan'), float('nan')

    F_val = MS_rows / MS_error
    from scipy.stats import f as f_dist
    df1 = n - 1
    df2 = (n - 1) * (k - 1)

    F_L = F_val / f_dist.ppf(0.975, df1, df2)
    F_U = F_val / f_dist.ppf(0.025, df1, df2)

    icc_lo = (F_L - 1) / (F_L + k - 1)
    icc_hi = (F_U - 1) / (F_U + k - 1)

    return icc, icc_lo, icc_hi


def main():
    s42_path = sys.argv[1]
    s123_path = sys.argv[2]

    preds_s42 = load_predictions(s42_path)
    preds_s123 = load_predictions(s123_path)

    assert len(preds_s42) == len(preds_s123), \
        f"Mismatch: {len(preds_s42)} vs {len(preds_s123)}"

    n = len(preds_s42)
    matrix = np.zeros((n, 2), dtype=float)
    for i in range(n):
        matrix[i, 0] = preds_s42[i]['correct']
        matrix[i, 1] = preds_s123[i]['correct']

    icc, lo, hi = icc_3_1(matrix)

    agree = (matrix[:, 0] == matrix[:, 1]).sum()
    both_correct = ((matrix[:, 0] == 1) & (matrix[:, 1] == 1)).sum()
    both_wrong = ((matrix[:, 0] == 0) & (matrix[:, 1] == 0)).sum()

    acc_s42 = matrix[:, 0].mean()
    acc_s123 = matrix[:, 1].mean()

    print(f"n_test_cases = {n}")
    print(f"acc_s42  = {acc_s42:.4f}")
    print(f"acc_s123 = {acc_s123:.4f}")
    print(f"agreement = {agree}/{n} ({agree/n*100:.1f}%)")
    print(f"both_correct = {both_correct}")
    print(f"both_wrong = {both_wrong}")
    print(f"ICC(3,1) = {icc:.4f}")
    print(f"95% CI = [{lo:.4f}, {hi:.4f}]")

    result = {
        "model": "DeepSeek-Coder-6.7B",
        "granularity": "function-level",
        "n_test_cases": n,
        "n_seeds": 2,
        "seeds": [42, 123],
        "acc_s42": round(acc_s42, 4),
        "acc_s123": round(acc_s123, 4),
        "agreement": agree,
        "agreement_pct": round(agree / n * 100, 2),
        "both_correct": int(both_correct),
        "both_wrong": int(both_wrong),
        "icc_3_1": round(icc, 4),
        "icc_95ci_lo": round(lo, 4),
        "icc_95ci_hi": round(hi, 4),
    }

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "artifacts", "deepseek_func_icc_result.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == '__main__':
    main()

"""TOST Power Analysis + Bayesian Equivalence Testing.

Tests whether cross-lingual asymmetry in the conflict task is equivalent
to the baseline XNLI asymmetry.
"""

import argparse
import json
import numpy as np
from scipy import stats


def tost_power(observed_diff, se_diff, margin, alpha=0.05):
    z_alpha = stats.norm.ppf(1 - alpha)
    z1 = (observed_diff + margin) / se_diff - z_alpha
    z2 = (margin - observed_diff) / se_diff - z_alpha
    power = stats.norm.cdf(z1) * stats.norm.cdf(z2)

    z_lower = (observed_diff + margin) / se_diff
    z_upper = (margin - observed_diff) / se_diff
    p_lower = 1 - stats.norm.cdf(z_lower)
    p_upper = 1 - stats.norm.cdf(z_upper)
    tost_p = max(p_lower, p_upper)

    return {
        'observed_diff': observed_diff,
        'se_diff': round(se_diff, 4),
        'margin': margin,
        'power': round(float(max(0, power)), 4),
        'tost_p_value': round(float(tost_p), 4),
        'tost_reject': bool(tost_p < alpha),
    }


def bayesian_equivalence(observed_diff, se_diff, prior_scale=5.0):
    ll_h0 = stats.norm.logpdf(observed_diff, 0, se_diff)
    se_h1 = np.sqrt(se_diff**2 + prior_scale**2)
    ll_h1 = stats.norm.logpdf(observed_diff, 0, se_h1)
    bf01 = np.exp(ll_h0 - ll_h1)

    if bf01 > 10:
        interpretation = 'strong evidence for equivalence'
    elif bf01 > 3:
        interpretation = 'moderate evidence for equivalence'
    elif bf01 > 1:
        interpretation = 'anecdotal evidence for equivalence'
    elif bf01 > 1/3:
        interpretation = 'anecdotal evidence against equivalence'
    elif bf01 > 1/10:
        interpretation = 'moderate evidence against equivalence'
    else:
        interpretation = 'strong evidence against equivalence'

    return {
        'observed_diff': observed_diff,
        'BF01': round(float(bf01), 4),
        'log10_BF01': round(float(np.log10(bf01)), 4),
        'interpretation': interpretation,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True,
                        help='JSON: [{"model": "...", "conflict_se": ..., "xnli_se": ..., "conflict_asym": ..., "xnli_asym": ...}]')
    parser.add_argument("--output", type=str, default="results/tost_bayesian_equivalence.json")
    args = parser.parse_args()

    models = json.loads(args.input)
    all_results = {}

    print("=" * 60)
    print("TOST Power Analysis")
    print("=" * 60)

    for entry in models:
        model = entry["model"]
        diff = entry["conflict_asym"] - entry["xnli_asym"]
        se_diff = np.sqrt(entry["conflict_se"]**2 + entry["xnli_se"]**2)

        for margin in [2, 5, 10]:
            key = f'{model}_margin{margin}'
            r = tost_power(diff, se_diff, margin)
            all_results[f'tost_{key}'] = r
            print(f"  {model} (margin={margin}pp): power={r['power']:.4f}, "
                  f"TOST p={r['tost_p_value']:.4f}")

    print()
    print("=" * 60)
    print("Bayesian Equivalence Testing")
    print("=" * 60)

    for entry in models:
        model = entry["model"]
        diff = entry["conflict_asym"] - entry["xnli_asym"]
        se_diff = np.sqrt(entry["conflict_se"]**2 + entry["xnli_se"]**2)

        for prior_scale in [3, 5, 10]:
            key = f'{model}_prior{prior_scale}'
            r = bayesian_equivalence(diff, se_diff, prior_scale)
            all_results[f'bayesian_{key}'] = r
            print(f"  {model} (prior={prior_scale}pp): BF01={r['BF01']:.4f} -> {r['interpretation']}")

    from pathlib import Path
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved to {args.output}")


if __name__ == '__main__':
    main()

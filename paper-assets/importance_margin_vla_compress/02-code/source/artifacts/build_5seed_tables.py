#!/usr/bin/env python3
"""Build final 5-seed summary tables from registry.yaml.

Strategy: s42-s43 use hardcoded values verified against ROADMAP 2-seed table
and decision logs. s44-s46 extracted from registry with comprehensive metric
key scanning. All values in percentage format.
"""

import yaml
import math
import re

REGISTRY_PATH = "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/registry.yaml"

SEEDS = [42, 43, 44, 45, 46]
METHODS = ["l2norm", "random", "attn"]
K_VALUES = [0.95, 0.9, 0.85, 0.75, 0.7, 0.5]

# Verified s42-s43 values (cross-checked against ROADMAP 2-seed table)
VERIFIED = {
    # L2norm s42 (all strict)
    ("l2norm", 0.95, 42): 86.2,
    ("l2norm", 0.9, 42): 80.0,
    ("l2norm", 0.85, 42): 77.6,
    ("l2norm", 0.75, 42): 70.8,   # D299
    ("l2norm", 0.7, 42): 63.2,
    ("l2norm", 0.5, 42): 49.2,
    # L2norm s43 (all strict)
    ("l2norm", 0.95, 43): 85.8,
    ("l2norm", 0.9, 43): 81.2,
    ("l2norm", 0.85, 43): 78.6,
    ("l2norm", 0.75, 43): 73.2,   # D299
    ("l2norm", 0.7, 43): 65.4,    # w41 strict, matches 2-seed mean=64.3
    ("l2norm", 0.5, 43): 52.8,

    # Random s42 (all strict)
    ("random", 0.95, 42): 60.6,
    ("random", 0.9, 42): 34.2,    # D292, strict_v2 (conclusion=negative but valid)
    ("random", 0.85, 42): 44.0,   # strict_w27
    ("random", 0.75, 42): 63.0,
    ("random", 0.7, 42): 66.0,    # strict_v2 cqa1
    ("random", 0.5, 42): 49.8,    # D297
    # Random s43 (all strict)
    ("random", 0.95, 43): 60.8,
    ("random", 0.9, 43): 35.0,    # D292 override, w41 strict
    ("random", 0.85, 43): 47.2,   # strict_w27, ROADMAP server log truth
    ("random", 0.75, 43): 60.6,   # strict_w41
    ("random", 0.7, 43): 64.4,    # strict_w38
    ("random", 0.5, 43): 51.4,    # D297

    # Attn s42 (prefer w41 strict, matches 2-seed verified table)
    ("attn", 0.95, 42): 78.4,     # strict_w41_v2
    ("attn", 0.9, 42): 64.0,      # strict, SR_libero_10=64
    ("attn", 0.85, 42): 50.0,     # strict, SR_libero_10=50
    ("attn", 0.75, 42): 49.8,     # strict_w41 (NOT cqa1=52.4, matches 2-seed mean=50.9)
    ("attn", 0.7, 42): 53.6,      # strict_w41 (NOT cqa1=50.8, matches 2-seed mean=53.7)
    ("attn", 0.5, 42): 52.0,      # strict_w41, D296
    # Attn s43 (all strict)
    ("attn", 0.95, 43): 77.2,     # strict_w41
    ("attn", 0.9, 43): 62.8,      # strict_cqa1, overall_success_rate=62.8
    ("attn", 0.85, 43): 52.4,     # strict_w41
    ("attn", 0.75, 43): 52.0,     # ROADMAP override, cqa1
    ("attn", 0.7, 43): 53.8,      # strict_w41
    ("attn", 0.5, 43): 48.8,      # strict_w38, D296
}

# Additional verified s44 from decision logs
VERIFIED_S44 = {
    ("l2norm", 0.95, 44): 86.8,   # D295
    ("l2norm", 0.9, 44): 80.4,    # D294
    ("l2norm", 0.75, 44): 67.4,   # D299
    ("random", 0.9, 44): 31.8,    # D292
    ("random", 0.5, 44): 50.2,    # D297
    ("attn", 0.5, 44): 48.8,      # D296
    ("l2norm", 0.5, 45): 51.2,    # 500-base: 256/500=51.2% (registry has 490-base 52.2%, T9 timeout 40/50 eps)
}

ALL_METRIC_KEYS = [
    "success_rate", "SR", "overall_sr", "sr",
    "avg_success_rate", "SR_libero_10", "overall_success_rate",
]

def _try_extract_from_dict(metrics):
    """Try extracting SR from a metrics dict."""
    if not isinstance(metrics, dict):
        return None
    for key in ALL_METRIC_KEYS:
        val = metrics.get(key)
        if val is not None:
            try:
                v = float(val)
                return v * 100 if 0 < v <= 1 else v
            except (ValueError, TypeError):
                continue
    return None

def extract_sr(exp):
    if not isinstance(exp, dict):
        return None
    # Try top-level metrics first
    metrics = exp.get("metrics")
    if metrics is not None:
        if isinstance(metrics, (int, float)):
            v = float(metrics)
            return v * 100 if 0 < v <= 1 else v
        if isinstance(metrics, str):
            try:
                v = float(metrics)
                return v * 100 if 0 < v <= 1 else v
            except (ValueError, TypeError):
                pass
        result = _try_extract_from_dict(metrics)
        if result is not None:
            return result
    # Fallback: metrics nested inside spec (structural anomaly in some entries)
    spec = exp.get("spec", {})
    if isinstance(spec, dict):
        spec_metrics = spec.get("metrics")
        if spec_metrics is not None:
            result = _try_extract_from_dict(spec_metrics)
            if result is not None:
                return result
    return None

def extract_seed(exp_id):
    m = re.search(r'seed(\d+)', exp_id)
    return int(m.group(1)) if m else None

def extract_method(exp_id):
    if '_l2norm_' in exp_id:
        return 'l2norm'
    elif '_random_' in exp_id:
        return 'random'
    elif '_attn_' in exp_id or '_attention_' in exp_id:
        return 'attn'
    return None

def extract_k(exp_id):
    m = re.search(r'_k0?(\d+)_', exp_id)
    if not m:
        return None
    digits = m.group(1)
    k_map = {
        '95': 0.95, '9': 0.9, '85': 0.85, '75': 0.75,
        '7': 0.7, '5': 0.5, '05': 0.05, '50': 0.5, '70': 0.7,
    }
    if digits.startswith('0') and digits not in k_map:
        return float('0.' + digits)
    return k_map.get(digits)

def score_experiment(exp_id, exp, method):
    """Score an experiment for selection priority."""
    s = 0
    if '_strict' in exp_id:
        s += 1000
    conclusion = exp.get('conclusion', '')
    if conclusion == 'success':
        s += 100
    elif conclusion == 'negative':
        s += 50
    if method == 'attn':
        spec = exp.get('spec', {})
        server = spec.get('server', '') if isinstance(spec, dict) else ''
        if 'w27' not in server and '27271' not in server:
            s += 200
    # Prefer later versions
    for suffix in ['_v4', '_v3', '_v2']:
        if suffix in exp_id:
            s += 10
            break
    return s

def sample_std(values):
    n = len(values)
    if n < 2:
        return 0.0
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / (n - 1)
    return math.sqrt(variance)

def main():
    with open(REGISTRY_PATH, 'r') as f:
        registry = yaml.safe_load(f)
    experiments = registry.get("experiments", {})

    # Start with verified hardcoded values
    data = {m: {k: {} for k in K_VALUES} for m in METHODS}
    sources = {m: {k: {} for k in K_VALUES} for m in METHODS}

    for key, val in {**VERIFIED, **VERIFIED_S44}.items():
        method, k, seed = key
        data[method][k][seed] = val
        sources[method][k][seed] = "verified"

    # Extract s44-s46 from registry (s44 only fills gaps not covered by VERIFIED_S44)
    # Collect candidates grouped by (method, k, seed)
    candidates = {}
    for exp_id, exp in experiments.items():
        if not isinstance(exp, dict):
            continue
        if not exp_id.startswith("eval_pi05_"):
            continue
        if '_long_' not in exp_id:
            continue
        status = exp.get("status")
        conclusion = exp.get("conclusion")
        if status != "DONE":
            continue
        if conclusion not in ("success", "negative"):
            continue

        seed = extract_seed(exp_id)
        method = extract_method(exp_id)
        k = extract_k(exp_id)

        if seed is None or method is None or k is None:
            continue
        if seed not in [44, 45, 46] or method not in METHODS or k not in K_VALUES:
            continue

        sr = extract_sr(exp)
        if sr is None:
            continue

        cell = (method, k, seed)
        if cell in data[method][k] and sources[method][k].get(seed) == "verified":
            continue  # already have verified value

        score = score_experiment(exp_id, exp, method)
        if cell not in candidates or score > candidates[cell][0]:
            candidates[cell] = (score, sr, exp_id)

    # Fill in from candidates
    for (method, k, seed), (score, sr, exp_id) in candidates.items():
        if seed not in data[method][k]:
            data[method][k][seed] = sr
            sources[method][k][seed] = exp_id

    # Print combined table
    print("=" * 110)
    print("π0.5 LIBERO-Long FINAL SUMMARY (sample std, n-1)")
    print("=" * 110)
    header = "| k    | L2norm mean±std  | n | Random mean±std  | n | Attn mean±std    | n | Margin L2-Rand |"
    print(header)
    print("|------|-----------------|---|-----------------|---|-----------------|---|--------------| ")

    for k in K_VALUES:
        cells = {}
        for method in METHODS:
            vals = [data[method][k][s] for s in SEEDS if s in data[method][k]]
            n = len(vals)
            if vals:
                mean = sum(vals) / n
                std = sample_std(vals)
                tag = f"({n}s)" if n < 5 else ""
                cells[method] = (f"{mean:.1f}±{std:.1f}{tag}", n, mean)
            else:
                cells[method] = ("N/A", 0, None)

        l2_str, l2_n, l2_mean = cells["l2norm"]
        rnd_str, rnd_n, rnd_mean = cells["random"]
        attn_str, attn_n, _ = cells["attn"]

        if l2_mean is not None and rnd_mean is not None:
            margin = l2_mean - rnd_mean
            margin_str = f"{margin:+.1f}pp"
        else:
            margin_str = "N/A"

        print(f"| {k:<4} | {l2_str:<15} | {l2_n} | {rnd_str:<15} | {rnd_n} | {attn_str:<15} | {attn_n} | {margin_str:<12} |")

    # Per-seed detail
    for method in METHODS:
        print(f"\n{method} per-seed:")
        for k in K_VALUES:
            parts = []
            for s in SEEDS:
                v = data[method][k].get(s)
                src = sources[method][k].get(s, "")
                if v is not None:
                    marker = "✓" if src == "verified" else ""
                    parts.append(f"s{s}={v:.1f}{marker}")
                else:
                    parts.append(f"s{s}=?")
            print(f"  k={k}: {', '.join(parts)}")

    # Missing data
    print(f"\n{'='*110}")
    print("MISSING DATA")
    print("=" * 110)
    any_missing = False
    for method in METHODS:
        for k in K_VALUES:
            missing = [s for s in SEEDS if s not in data[method][k]]
            if missing:
                print(f"  {method} k={k}: seeds {missing}")
                any_missing = True
    if not any_missing:
        print("  None — all cells have data")

    # Data cleaning report
    print(f"\n{'='*110}")
    print("DATA CLEANING REPORT")
    print("=" * 110)
    print("1. Attn k=0.75 seed43: cqa1=52.0% (override, w27 doesn't support attention)")
    print("2. Attn k=0.75 seed42: strict_w41=49.8% (NOT w27, verified against 2-seed table)")
    print("   Alt: strict_cqa1=52.4% exists but 2-seed table used w41 value")
    print("3. Random k=0.9 seed43: w41_strict=35.0% (D292 override, not old cqa1_v2=32.4%)")
    print("4. Random k=0.85 seed43: strict_w27=47.2% (server log truth, not mixed per-task)")
    print("5. Attn k=0.7 seed42: strict_w41=53.6% (NOT cqa1=50.8, matches 2-seed=53.7±0.1)")
    print("6. All metrics unified to percentage format")
    print(f"\nVerified cells (s42-s43 hardcoded): {len(VERIFIED) + len(VERIFIED_S44)}")
    print(f"Registry-extracted cells: {sum(1 for m in METHODS for k in K_VALUES for s in SEEDS if sources[m][k].get(s) not in (None, 'verified'))}")

if __name__ == "__main__":
    main()

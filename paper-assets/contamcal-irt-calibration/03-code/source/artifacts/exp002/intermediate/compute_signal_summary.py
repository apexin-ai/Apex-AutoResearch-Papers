"""
Compute signal AUC (d005 vs d000) and Cohen's d (d100 vs d000) for 1.5B and 3B models.

For each scale (1.5B, 3B), for each benchmark (MMLU, GSM8K, ARC), for each signal:
  S1 = embedding_similarity (key: s1_embedding)
  S2 = min_k_plus_plus (key: s2_minkpp)
  S4 = self_critique (key: s4_selfcritique)

Output: signal_summary_15B_3B.json
"""

import json
import os
import sys
from pathlib import Path

import numpy as np

SIGNAL_DIR = Path("/root/autodl-tmp/exp002/signals")
OUTPUT_FILE = SIGNAL_DIR / "signal_summary_15B_3B.json"

BENCHMARKS = ["mmlu", "gsm8k", "arc"]
SIGNAL_MAP = {
    "S1": {"key": "s1_embedding", "file_prefix": "signal_embedding_", "alt_keys": ["embedding_similarity"]},
    "S2": {"key": "s2_minkpp", "file_prefix": "signal_minkpp_", "alt_keys": ["min_k_plus_plus"]},
    "S4": {"key": "s4_selfcritique", "file_prefix": "signal_selfcritique_", "alt_keys": ["self_critique"]},
}

# C006 blacklist — NEVER use these directories
BLACKLISTED_DIRS = {
    "Qwen2.5-3B_d000_s42",
    "Qwen2.5-3B_d000_v2_s42",
    "Qwen2.5-3B_d005_s42",
    "Qwen2.5-3B_d025_s42",
    "Qwen2.5-3B_d100_s42",
}


def compute_auc(neg_scores, pos_scores):
    labels = [0] * len(neg_scores) + [1] * len(pos_scores)
    scores = list(neg_scores) + list(pos_scores)
    pairs = sorted(zip(scores, labels), reverse=True)
    tp, fp = 0, 0
    tp_total = sum(labels)
    fp_total = len(labels) - tp_total
    auc = 0.0
    for s, l in pairs:
        if l == 1:
            tp += 1
        else:
            fp += 1
            auc += tp
    return auc / (tp_total * fp_total) if tp_total * fp_total > 0 else 0.5


def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    m1, m2 = np.mean(group1), np.mean(group2)
    s1, s2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    sp = np.sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    return float((m2 - m1) / sp) if sp > 0 else 0.0


def find_signal_dir(scale: str, dosage: str) -> Path | None:
    """Find the best matching directory for a given scale and dosage.

    For 1.5B: prefer _v3 if exists, else latest alpha=32 version.
    For 3B: ONLY use alpha=32 versions (_v3, _a32, etc). Never blacklisted.
    """
    prefix = f"Qwen2.5-{scale}"
    dosage_tag = f"d{dosage:>03s}" if len(dosage) < 3 else f"d{dosage}"

    if not SIGNAL_DIR.exists():
        return None

    candidates = []
    for d in SIGNAL_DIR.iterdir():
        if not d.is_dir():
            continue
        name = d.name
        if name in BLACKLISTED_DIRS:
            continue
        if not name.startswith(prefix):
            continue
        # Must contain the dosage tag
        parts = name.replace(prefix + "_", "")
        if not parts.startswith(dosage_tag):
            continue
        candidates.append(d)

    if not candidates:
        return None

    # Priority: _v3 > _a32 > plain (for 3B, plain is blacklisted anyway)
    for suffix_priority in ["_v3_", "_a32_"]:
        for c in candidates:
            if suffix_priority in c.name:
                return c

    # If only one candidate and it's not blacklisted, use it
    if len(candidates) == 1:
        return candidates[0]

    # Return the one with the longest name (likely most specific version)
    return max(candidates, key=lambda p: len(p.name))


def load_signal_scores(signal_dir: Path, signal_info: dict, benchmark: str) -> list[float] | None:
    """Load signal scores for a given benchmark from a signal directory."""
    # Try individual signal file first
    bench_name = benchmark
    # Handle arc -> arc_challenge mapping
    file_candidates = [
        signal_dir / f"{signal_info['file_prefix']}{bench_name}.json",
        signal_dir / f"{signal_info['file_prefix']}arc_challenge.json" if bench_name == "arc" else None,
    ]

    key = signal_info["key"]
    alt_keys = signal_info["alt_keys"]

    for fpath in file_candidates:
        if fpath is None:
            continue
        if fpath.exists():
            with open(fpath) as f:
                data = json.load(f)
            scores = extract_scores(data, key, alt_keys)
            if scores is not None:
                return scores

    # Try merged signal file
    merged_candidates = [
        signal_dir / f"signals_merged_{bench_name}.json",
        signal_dir / f"signals_merged_arc_challenge.json" if bench_name == "arc" else None,
    ]
    for fpath in merged_candidates:
        if fpath is None:
            continue
        if fpath.exists():
            with open(fpath) as f:
                data = json.load(f)
            scores = extract_scores(data, key, alt_keys)
            if scores is not None:
                return scores

    return None


def extract_scores(data: list[dict], primary_key: str, alt_keys: list[str]) -> list[float] | None:
    """Extract numeric scores from records, trying primary then alt keys."""
    if not isinstance(data, list) or len(data) == 0:
        return None

    # Try primary key
    if primary_key in data[0]:
        scores = [r[primary_key] for r in data if r.get(primary_key) is not None]
        return scores if scores else None

    # Try alt keys
    for ak in alt_keys:
        if ak in data[0]:
            scores = [r[ak] for r in data if r.get(ak) is not None]
            return scores if scores else None

    return None


def main():
    print(f"Signal directory: {SIGNAL_DIR}")
    print(f"Exists: {SIGNAL_DIR.exists()}")

    if not SIGNAL_DIR.exists():
        print("ERROR: Signal directory does not exist!")
        sys.exit(1)

    # List all directories
    all_dirs = sorted([d.name for d in SIGNAL_DIR.iterdir() if d.is_dir()])
    print(f"\nAll signal directories ({len(all_dirs)}):")
    for d in all_dirs:
        tag = " [BLACKLISTED]" if d in BLACKLISTED_DIRS else ""
        print(f"  {d}{tag}")

    results = {}
    missing = []

    for scale in ["1.5B", "3B"]:
        print(f"\n{'='*60}")
        print(f"Processing scale: {scale}")
        print(f"{'='*60}")

        # Find directories
        d000_dir = find_signal_dir(scale, "000")
        d005_dir = find_signal_dir(scale, "005")
        d100_dir = find_signal_dir(scale, "100")

        print(f"  d000 dir: {d000_dir}")
        print(f"  d005 dir: {d005_dir}")
        print(f"  d100 dir: {d100_dir}")

        scale_results = {
            "auc_d005": {"S1": {}, "S2": {}, "S4": {}},
            "cohens_d_d100": {"S1": {}, "S2": {}, "S4": {}},
            "directories_used": {
                "d000": str(d000_dir) if d000_dir else None,
                "d005": str(d005_dir) if d005_dir else None,
                "d100": str(d100_dir) if d100_dir else None,
            },
        }

        for sig_name, sig_info in SIGNAL_MAP.items():
            for bench in BENCHMARKS:
                bench_upper = bench.upper()

                # Load d000 scores
                if d000_dir:
                    d000_scores = load_signal_scores(d000_dir, sig_info, bench)
                else:
                    d000_scores = None

                # AUC: d005 vs d000
                if d005_dir and d000_scores:
                    d005_scores = load_signal_scores(d005_dir, sig_info, bench)
                    if d005_scores and d000_scores:
                        auc = compute_auc(d000_scores, d005_scores)
                        scale_results["auc_d005"][sig_name][bench_upper] = round(auc, 4)
                        print(f"  AUC {sig_name} {bench_upper}: {auc:.4f} (n_neg={len(d000_scores)}, n_pos={len(d005_scores)})")
                    else:
                        missing.append(f"{scale}/{sig_name}/AUC_{bench_upper}")
                        print(f"  MISSING: {scale}/{sig_name}/AUC_{bench_upper}")
                else:
                    missing.append(f"{scale}/{sig_name}/AUC_{bench_upper}")
                    if not d005_dir:
                        print(f"  MISSING d005 dir for {scale}")
                    elif not d000_scores:
                        print(f"  MISSING d000 {sig_name} {bench_upper} scores")

                # Cohen's d: d100 vs d000
                if d100_dir and d000_scores:
                    d100_scores = load_signal_scores(d100_dir, sig_info, bench)
                    if d100_scores and d000_scores:
                        cd = cohens_d(d000_scores, d100_scores)
                        scale_results["cohens_d_d100"][sig_name][bench_upper] = round(cd, 4)
                        print(f"  Cohen's d {sig_name} {bench_upper}: {cd:.4f}")
                    else:
                        missing.append(f"{scale}/{sig_name}/CohenD_{bench_upper}")
                        print(f"  MISSING: {scale}/{sig_name}/CohenD_{bench_upper}")
                else:
                    missing.append(f"{scale}/{sig_name}/CohenD_{bench_upper}")

        results[scale] = scale_results

    results["missing"] = missing

    # Verify with sklearn if available
    try:
        from sklearn.metrics import roc_auc_score
        print("\n\n--- sklearn verification ---")
        for scale in ["1.5B", "3B"]:
            d000_dir = find_signal_dir(scale, "000")
            d005_dir = find_signal_dir(scale, "005")
            if not d000_dir or not d005_dir:
                continue
            for sig_name, sig_info in SIGNAL_MAP.items():
                for bench in BENCHMARKS:
                    d000_scores = load_signal_scores(d000_dir, sig_info, bench)
                    d005_scores = load_signal_scores(d005_dir, sig_info, bench)
                    if d000_scores and d005_scores:
                        labels = [0] * len(d000_scores) + [1] * len(d005_scores)
                        scores = d000_scores + d005_scores
                        sk_auc = roc_auc_score(labels, scores)
                        my_auc = results[scale]["auc_d005"][sig_name].get(bench.upper())
                        diff = abs(sk_auc - my_auc) if my_auc else float("nan")
                        print(f"  {scale} {sig_name} {bench}: sklearn={sk_auc:.4f} manual={my_auc} diff={diff:.6f}")
    except ImportError:
        print("\nsklearn not available, skipping verification")

    # Save results
    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n\nResults saved to: {OUTPUT_FILE}")
    print("\n" + "=" * 60)
    print("FULL RESULTS:")
    print("=" * 60)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()

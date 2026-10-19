"""TrajGuard-style Mahalanobis distance baseline for commitment detection.

Input: Pre-extracted hidden states (.pt files)
Output: Per-trace Mahalanobis distances + crossing detection metrics

Approach:
- Build reference distribution from safe traces (final_judgment=0.5)
- For each jailbreak trace step, compute MD from reference
- Detect commitment: MD > threshold for K consecutive steps
"""

import sys
import json
import time
from pathlib import Path
from typing import List, Dict, Optional, Tuple

import numpy as np
import torch
from sklearn.decomposition import PCA
from sklearn.covariance import LedoitWolf

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.config import (
    HIDDEN_STATES_DIR, LAYERS, HIDDEN_DIM, DETECTION_WINDOW, SEED
)
from src.data_loader import prepare_dataset, split_data

LAYER_14_IDX = 2  # LAYERS=[12..24], index 2 = layer 14
PCA_DIMS = [32, 64, 128, 256]
THRESHOLD_PERCENTILES = [90, 95, 99]
OUTPUT_DIR = Path("DATA_DIR/artifacts/exp_005_trajguard")


def load_trace_hidden_states(trace_id: str, layer_idx: int = LAYER_14_IDX) -> Optional[np.ndarray]:
    pt_path = HIDDEN_STATES_DIR / f"{trace_id}.pt"
    if not pt_path.exists():
        return None
    data = torch.load(pt_path, map_location="cpu", weights_only=False)
    hs = data["hidden_states"][:, layer_idx, :]  # [num_sentences, 4096]
    return hs.float().numpy()


def collect_safe_hidden_states(safe_traces: List[Dict]) -> np.ndarray:
    all_steps = []
    for trace in safe_traces:
        hs = load_trace_hidden_states(trace["trace_id"])
        if hs is not None:
            all_steps.append(hs)
    return np.concatenate(all_steps, axis=0)  # [N_safe_steps, 4096]


def first_crossing_point_md(
    md_sequence: np.ndarray,
    threshold: float,
    consecutive_k: int = DETECTION_WINDOW,
) -> Optional[int]:
    n = len(md_sequence)
    if n < consecutive_k:
        return None
    for i in range(n - consecutive_k + 1):
        if all(md_sequence[i:i + consecutive_k] > threshold):
            return i
    return None


def compute_mahalanobis_pca(
    X_ref: np.ndarray, X_query: np.ndarray, n_components: int
) -> Tuple[np.ndarray, object]:
    pca = PCA(n_components=n_components, random_state=SEED)
    X_ref_pca = pca.fit_transform(X_ref)

    mean = X_ref_pca.mean(axis=0)
    cov = np.cov(X_ref_pca, rowvar=False)
    cov_inv = np.linalg.inv(cov + 1e-6 * np.eye(n_components))

    X_query_pca = pca.transform(X_query)
    diff = X_query_pca - mean
    md = np.sqrt(np.sum(diff @ cov_inv * diff, axis=1))
    return md, pca


def compute_mahalanobis_ledoitwolf(
    X_ref: np.ndarray, X_query: np.ndarray
) -> np.ndarray:
    lw = LedoitWolf()
    lw.fit(X_ref)
    mean = lw.location_
    precision = lw.precision_  # inverse covariance

    diff = X_query - mean
    md = np.sqrt(np.sum(diff @ precision * diff, axis=1))
    return md


def evaluate_config(
    jailbreak_traces: List[Dict],
    safe_val_md: np.ndarray,
    compute_md_fn,
    config_name: str,
) -> List[Dict]:
    results = []
    for pctl in THRESHOLD_PERCENTILES:
        threshold = float(np.percentile(safe_val_md, pctl))

        per_trace = []
        detected_count = 0
        lead_times = []

        for trace in jailbreak_traces:
            hs = load_trace_hidden_states(trace["trace_id"])
            if hs is None:
                continue
            md_seq = compute_md_fn(hs)
            fcp = first_crossing_point_md(md_seq, threshold)
            cp = trace["commitment_point"]

            lead = None
            if fcp is not None:
                detected_count += 1
                lead = cp - fcp
                lead_times.append(lead)

            per_trace.append({
                "trace_id": trace["trace_id"],
                "commitment_point": cp,
                "first_crossing": fcp,
                "lead_time": lead,
                "num_steps": len(md_seq),
                "md_mean": float(md_seq.mean()),
                "md_max": float(md_seq.max()),
            })

        n_traces = len(per_trace)
        crossing_rate = detected_count / n_traces if n_traces > 0 else 0.0

        results.append({
            "config": config_name,
            "threshold_percentile": pctl,
            "threshold_value": threshold,
            "crossing_rate": crossing_rate,
            "lead_time_mean": float(np.mean(lead_times)) if lead_times else None,
            "lead_time_median": float(np.median(lead_times)) if lead_times else None,
            "n_traces": n_traces,
            "n_detected": detected_count,
            "per_trace": per_trace,
        })
    return results


def main():
    t0 = time.time()
    print("Loading dataset...")
    dataset = prepare_dataset()
    safe_traces = dataset["safe"]
    jailbreak_traces = dataset["jailbreak_with_commitment"]

    safe_train, safe_val, safe_test = split_data(safe_traces)
    jb_train, jb_val, jb_test = split_data(jailbreak_traces)

    print(f"Safe: {len(safe_traces)} (train={len(safe_train)}, val={len(safe_val)}, test={len(safe_test)})")
    print(f"Jailbreak: {len(jailbreak_traces)} (train={len(jb_train)}, val={len(jb_val)}, test={len(jb_test)})")

    # Build reference from safe train traces
    print("Collecting safe train hidden states (layer 14)...")
    X_safe_train = collect_safe_hidden_states(safe_train)
    print(f"  Safe train steps: {X_safe_train.shape[0]} x {X_safe_train.shape[1]}")

    # Collect safe val hidden states for threshold calibration
    print("Collecting safe val hidden states...")
    X_safe_val = collect_safe_hidden_states(safe_val)
    print(f"  Safe val steps: {X_safe_val.shape[0]}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    all_configs = []

    # PCA-based methods
    for n_comp in PCA_DIMS:
        print(f"\n--- PCA dims={n_comp} ---")
        pca = PCA(n_components=n_comp, random_state=SEED)
        X_train_pca = pca.fit_transform(X_safe_train)

        mean_pca = X_train_pca.mean(axis=0)
        cov_pca = np.cov(X_train_pca, rowvar=False)
        cov_inv = np.linalg.inv(cov_pca + 1e-6 * np.eye(n_comp))

        def _md_pca(hs, _pca=pca, _mean=mean_pca, _cov_inv=cov_inv):
            X_pca = _pca.transform(hs)
            diff = X_pca - _mean
            return np.sqrt(np.sum(diff @ _cov_inv * diff, axis=1))

        # Compute safe val MD for threshold
        safe_val_md = _md_pca(X_safe_val)
        print(f"  Safe val MD: mean={safe_val_md.mean():.2f}, p90={np.percentile(safe_val_md, 90):.2f}, p95={np.percentile(safe_val_md, 95):.2f}, p99={np.percentile(safe_val_md, 99):.2f}")

        configs = evaluate_config(jb_test, safe_val_md, _md_pca, f"pca_{n_comp}")
        for c in configs:
            print(f"  pctl={c['threshold_percentile']}: crossing_rate={c['crossing_rate']:.3f}, lead_mean={c['lead_time_mean']}")
        all_configs.extend(configs)

    # LedoitWolf shrinkage
    print("\n--- LedoitWolf (full 4096-d) ---")
    lw = LedoitWolf()
    lw.fit(X_safe_train)
    lw_mean = lw.location_
    lw_precision = lw.precision_

    def _md_lw(hs, _mean=lw_mean, _prec=lw_precision):
        diff = hs - _mean
        return np.sqrt(np.sum(diff @ _prec * diff, axis=1))

    safe_val_md_lw = _md_lw(X_safe_val)
    print(f"  Safe val MD: mean={safe_val_md_lw.mean():.2f}, p90={np.percentile(safe_val_md_lw, 90):.2f}, p95={np.percentile(safe_val_md_lw, 95):.2f}, p99={np.percentile(safe_val_md_lw, 99):.2f}")

    configs_lw = evaluate_config(jb_test, safe_val_md_lw, _md_lw, "ledoitwolf_4096")
    for c in configs_lw:
        print(f"  pctl={c['threshold_percentile']}: crossing_rate={c['crossing_rate']:.3f}, lead_mean={c['lead_time_mean']}")
    all_configs.extend(configs_lw)

    # Save results
    result = {
        "method": "trajguard_mahalanobis",
        "layer": 14,
        "layer_idx": LAYER_14_IDX,
        "detection_window": DETECTION_WINDOW,
        "n_safe_train_steps": int(X_safe_train.shape[0]),
        "n_jb_test_traces": len(jb_test),
        "configs": all_configs,
    }

    output_path = OUTPUT_DIR / "results.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nResults saved to {output_path}")

    # Summary table
    print("\n" + "=" * 80)
    print("SUMMARY: TrajGuard Mahalanobis Distance Baseline")
    print("=" * 80)
    print(f"{'Config':<20} {'Pctl':<6} {'Threshold':<10} {'CrossRate':<12} {'LeadMean':<12} {'LeadMed':<10}")
    print("-" * 80)
    for c in all_configs:
        lead_m = f"{c['lead_time_mean']:.1f}" if c['lead_time_mean'] is not None else "N/A"
        lead_med = f"{c['lead_time_median']:.1f}" if c['lead_time_median'] is not None else "N/A"
        print(f"{c['config']:<20} {c['threshold_percentile']:<6} {c['threshold_value']:<10.2f} {c['crossing_rate']:<12.3f} {lead_m:<12} {lead_med:<10}")

    # Comparison with existing methods
    print("\n" + "=" * 80)
    print("COMPARISON WITH EXISTING METHODS")
    print("=" * 80)
    print(f"{'Method':<35} {'CrossRate':<12} {'LeadMean':<12}")
    print("-" * 60)
    print(f"{'Static LR L14':<35} {'46.5%':<12} {'-2.0':<12}")
    print(f"{'Temporal LR W=15':<35} {'76.7%':<12} {'-1.1':<12}")
    print(f"{'GRU multi-7L h=256':<35} {'76.7%':<12} {'+4.7':<12}")
    print("-" * 60)

    # Find best TrajGuard config
    best = max(all_configs, key=lambda c: (c['crossing_rate'], c['lead_time_mean'] or -999))
    lead_str = f"{best['lead_time_mean']:.1f}" if best['lead_time_mean'] is not None else "N/A"
    print(f"{'TrajGuard best (' + best['config'] + ' p' + str(best['threshold_percentile']) + ')':<35} {best['crossing_rate']:.1%}{'':<5} {lead_str:<12}")

    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.1f}s")


if __name__ == "__main__":
    main()

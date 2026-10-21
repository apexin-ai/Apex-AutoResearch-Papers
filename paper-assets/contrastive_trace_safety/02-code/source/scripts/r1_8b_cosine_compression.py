#!/usr/bin/env python3
"""R1-8B cosine compression analysis — geometric layer characterization.

Computes step-to-step cosine distance at each layer across all AdvBench traces.
R1-8B: 32 layers, 4096 hidden dim.

Input:  artifacts/hidden_states_advbench_r1_8b/*.pt (shape: n_steps × 32 × 4096)
Output: artifacts/r1_8b_cosine_compression_results.json
"""

import json, sys, time
import numpy as np
import torch
from pathlib import Path

sys.stdout.reconfigure(line_buffering=True)

BASE = Path("/root/autodl-tmp/contrastive_trace_safety")
HS_DIR = BASE / "artifacts" / "hidden_states_advbench_r1_8b"
RESULTS_FILE = BASE / "artifacts" / "r1_8b_cosine_compression_results.json"

N_LAYERS = 32
SHALLOW_RANGE = (0, 5)
DEEP_RANGE = (24, 31)  # Adjusted for 32-layer model


def cosine_distance(a, b):
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a < 1e-8 or norm_b < 1e-8:
        return 1.0
    return 1.0 - dot / (norm_a * norm_b)


def main():
    print(f"{'='*60}")
    print("R1-8B Cosine Compression Analysis")
    print(f"{'='*60}")

    pt_files = sorted(HS_DIR.glob("advbench_*.pt"))
    print(f"  Found {len(pt_files)} trace files")

    if len(pt_files) == 0:
        print("  ERROR: No trace files found")
        sys.exit(1)

    layer_cos_dists = [[] for _ in range(N_LAYERS)]
    traces_used = 0
    pairs_total = 0
    t_start = time.time()

    for fi, pt_path in enumerate(pt_files):
        d = torch.load(pt_path, map_location="cpu", weights_only=False)
        hs = d["hidden_states"]

        if isinstance(hs, torch.Tensor):
            hs = hs.float().numpy()

        n_steps = hs.shape[0]
        if n_steps < 2:
            continue

        traces_used += 1

        for layer_idx in range(N_LAYERS):
            for t in range(n_steps - 1):
                cd = cosine_distance(hs[t, layer_idx, :], hs[t + 1, layer_idx, :])
                layer_cos_dists[layer_idx].append(cd)
                pairs_total += 1

        if (fi + 1) % 100 == 0 or fi < 5:
            elapsed = time.time() - t_start
            print(f"  [{fi+1}/{len(pt_files)}] {traces_used} traces, "
                  f"{pairs_total} pairs, {elapsed:.1f}s")

    print(f"\n  Processed {traces_used} traces, {pairs_total} step-pairs")

    layer_stats = []
    for l in range(N_LAYERS):
        dists = layer_cos_dists[l]
        if len(dists) == 0:
            layer_stats.append({"layer": l, "mean": None, "std": None, "n": 0})
            continue
        arr = np.array(dists)
        layer_stats.append({
            "layer": l,
            "mean": round(float(arr.mean()), 6),
            "std": round(float(arr.std()), 6),
            "median": round(float(np.median(arr)), 6),
            "n": len(dists),
        })

    shallow_means = [s["mean"] for s in layer_stats
                     if s["mean"] is not None
                     and SHALLOW_RANGE[0] <= s["layer"] <= SHALLOW_RANGE[1]]
    deep_means = [s["mean"] for s in layer_stats
                  if s["mean"] is not None
                  and DEEP_RANGE[0] <= s["layer"] <= DEEP_RANGE[1]]

    shallow_avg = float(np.mean(shallow_means)) if shallow_means else None
    deep_avg = float(np.mean(deep_means)) if deep_means else None
    ratio = shallow_avg / deep_avg if (shallow_avg and deep_avg and deep_avg > 1e-8) else None

    print(f"\n{'='*70}")
    print("COSINE COMPRESSION RESULTS:")
    print(f"{'='*70}")
    print(f"\n  Layer | Mean Cos Dist | Std")
    print(f"  ------|---------------|------")
    for s in layer_stats:
        if s["mean"] is not None:
            marker = ""
            if SHALLOW_RANGE[0] <= s["layer"] <= SHALLOW_RANGE[1]:
                marker = " <- shallow"
            elif DEEP_RANGE[0] <= s["layer"] <= DEEP_RANGE[1]:
                marker = " <- deep"
            print(f"  L{s['layer']:2d}   | {s['mean']:.6f}      | {s['std']:.6f}{marker}")

    print(f"\n  Shallow (L{SHALLOW_RANGE[0]}-L{SHALLOW_RANGE[1]}) mean: {shallow_avg:.6f}")
    print(f"  Deep (L{DEEP_RANGE[0]}-L{DEEP_RANGE[1]}) mean:    {deep_avg:.6f}")
    print(f"  Ratio (shallow/deep): {ratio:.4f}")

    if ratio is not None and ratio < 1.0:
        print(f"  -> SHALLOW COMPRESSION CONFIRMED (ratio < 1)")
        print(f"    Shallow layers show {(1-ratio)*100:.1f}% less step-to-step variation than deep layers")
    else:
        print(f"  -> No shallow compression (ratio >= 1)")

    elapsed = time.time() - t_start

    output = {
        "experiment": "r1_8b_cosine_compression",
        "model": "deepseek-r1-distill-llama-8b",
        "n_traces": traces_used,
        "n_step_pairs": pairs_total,
        "n_layers": N_LAYERS,
        "shallow_range": f"L{SHALLOW_RANGE[0]}-L{SHALLOW_RANGE[1]}",
        "deep_range": f"L{DEEP_RANGE[0]}-L{DEEP_RANGE[1]}",
        "shallow_mean_cosine_dist": round(shallow_avg, 6) if shallow_avg else None,
        "deep_mean_cosine_dist": round(deep_avg, 6) if deep_avg else None,
        "shallow_deep_ratio": round(ratio, 4) if ratio else None,
        "compression_confirmed": ratio is not None and ratio < 1.0,
        "compression_magnitude_pct": round((1 - ratio) * 100, 1) if ratio and ratio < 1 else 0,
        "per_layer": layer_stats,
        "runtime_seconds": round(elapsed, 1),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }

    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_FILE, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n  Saved: {RESULTS_FILE} ({elapsed:.0f}s)")


if __name__ == "__main__":
    main()

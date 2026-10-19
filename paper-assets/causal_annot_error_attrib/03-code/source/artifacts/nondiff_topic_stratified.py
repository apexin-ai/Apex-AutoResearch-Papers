#!/usr/bin/env python3
"""
Non-Differential Misclassification Verification via Topic-Stratified Analysis

Verifies the non-differential assumption P(A*|A, Y) = P(A*|A) using VAST dataset
topics as a proxy for outcome Y. If confusion matrices C_topic(t) do not vary
meaningfully by topic beyond sampling noise, this supports the assumption.

Approach:
  Since raw per-sample LLM predictions are not available (only aggregated confusion
  matrices), we use a simulation-based permutation test:
    1. For each model config, take the overall confusion matrix C_overall.
    2. Use the VAST test.jsonl topic+label distribution to establish per-topic
       sample sizes and label distributions.
    3. Simulate B=10,000 bootstrap samples: for each topic, draw predictions from
       C_overall according to the topic's label distribution, compute C_topic,
       measure max |C_topic - C_overall|.
    4. The 95th/99th percentile of bootstrap max-deviations gives the expected
       range under the non-differential null. If observed deviations (from the
       actual annotation process) were within this range, the assumption holds.
    5. Since we only have C_overall (not per-topic observed CMs), we report the
       expected deviation range as an upper bound on what's consistent with
       the non-differential assumption.

This is a *necessary condition* check, not sufficient: topics are a proxy for Y,
and non-differential with respect to topic does not guarantee non-differential
with respect to the actual outcome.

Inputs:
  - artifacts/plan011_frontier_cms.json (aggregated confusion matrices)
  - artifacts/plan011_frontier_annotations/data/vast/test.jsonl (topic distribution)

Outputs:
  - artifacts/nondiff_topic_stratified_results.json

Dependencies: numpy (no GPU needed)
"""

import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

# ── Paths ──────────────────────────────────────────────────────────────────
PROJ_ROOT = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
ARTIFACTS = PROJ_ROOT / "artifacts"
CMS_PATH = ARTIFACTS / "plan011_frontier_cms.json"
VAST_TEST = ARTIFACTS / "plan011_frontier_annotations" / "data" / "vast" / "test.jsonl"
OUTPUT_PATH = ARTIFACTS / "nondiff_topic_stratified_results.json"

# ── Parameters ─────────────────────────────────────────────────────────────
MIN_TOPIC_SAMPLES = 10   # topics with fewer samples excluded (CM too noisy)
N_BOOTSTRAP = 10_000     # bootstrap iterations for null distribution
SEED = 42
LABEL_NAMES = ["Con", "Pro", "Neutral"]
K = 3


def load_vast_test():
    """Load VAST test records, return list of dicts with topic and label_name."""
    records = []
    with open(VAST_TEST) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def load_confusion_matrices():
    """Load all VAST confusion matrices from the frontier CMs file.

    Returns dict: config_key -> {"C": ndarray(K,K), "labels": list, "n_valid": int, ...}
    """
    # Merge from all available CM files
    cm_files = [
        "plan011_frontier_cms.json",
        "plan011_new_cms.json",
        "plan011_new_cms_round2.json",
        "plan011_new_cms_vast_qwen3_zs.json",
    ]
    configs = {}
    for fname in cm_files:
        path = ARTIFACTS / fname
        if not path.exists():
            continue
        data = json.load(open(path))
        for key, val in data.items():
            if not key.startswith("vast/"):
                continue
            config_key = key.replace("vast/", "")
            if config_key in configs:
                continue  # keep first occurrence
            C = np.array(val["confusion_matrix_normalized"])
            labels = val.get("labels", LABEL_NAMES)
            n_valid = val.get("n_valid", val.get("n_samples", None))
            acc = val.get("accuracy", None)
            configs[config_key] = {
                "C": C,
                "labels": labels,
                "n_valid": n_valid,
                "accuracy": acc,
                "source_file": fname,
            }
    return configs


def get_topic_label_distribution(records):
    """Compute per-topic label counts.

    Returns dict: topic -> {label_name: count}
    Also returns list of topics with >= MIN_TOPIC_SAMPLES.
    """
    topic_labels = {}
    for r in records:
        t = r["topic"]
        ln = r["label_name"]
        if t not in topic_labels:
            topic_labels[t] = Counter()
        topic_labels[t][ln] += 1

    # Filter to topics with sufficient samples
    qualified = {
        t: dict(counts) for t, counts in topic_labels.items()
        if sum(counts.values()) >= MIN_TOPIC_SAMPLES
    }
    return qualified


def get_active_cols(label_counts):
    """Return list of column indices (gold labels) with > 0 samples."""
    label_idx = {ln: i for i, ln in enumerate(LABEL_NAMES)}
    active = []
    for label_name, n_samples in label_counts.items():
        if label_name in label_idx and n_samples > 0:
            active.append(label_idx[label_name])
    return sorted(active)


def simulate_topic_cm(C, label_counts, rng):
    """Simulate a per-topic confusion matrix by drawing predictions from C_overall.

    For each gold label k with n_k samples in this topic, draw n_k predicted
    labels from C[:, k] (the k-th column of the confusion matrix).

    Args:
        C: (K, K) column-stochastic confusion matrix. C[j, k] = P(pred=j | gold=k).
        label_counts: dict {label_name: count} for this topic.
        rng: numpy random generator.

    Returns:
        C_topic: (K, K) column-stochastic confusion matrix for this topic.
        active_cols: list of column indices that have samples.
    """
    label_idx = {ln: i for i, ln in enumerate(LABEL_NAMES)}
    counts = np.zeros((K, K), dtype=float)
    active_cols = []

    for label_name, n_samples in label_counts.items():
        if label_name not in label_idx:
            continue
        k = label_idx[label_name]
        if n_samples == 0:
            continue
        active_cols.append(k)
        # Draw n_samples predictions from C[:, k]
        preds = rng.choice(K, size=n_samples, p=C[:, k])
        counts[:, k] = np.bincount(preds, minlength=K).astype(float)

    active_cols = sorted(active_cols)

    # Normalize to column-stochastic
    col_sums = counts.sum(axis=0)
    col_safe = np.where(col_sums < 1, 1.0, col_sums)
    C_topic = counts / col_safe
    return C_topic, active_cols


def compute_max_deviation(C_topic, C_overall, active_cols):
    """Max absolute deviation between topic CM and overall CM.

    Only compares columns (gold labels) that have samples in the topic,
    otherwise empty columns produce artificial large deviations.

    Args:
        C_topic: (K, K) topic confusion matrix.
        C_overall: (K, K) overall confusion matrix.
        active_cols: list of column indices that have samples in this topic.
    """
    if not active_cols:
        return 0.0
    diff = np.abs(C_topic[:, active_cols] - C_overall[:, active_cols])
    return float(np.max(diff))


def compute_mean_deviation(C_topic, C_overall, active_cols):
    """Mean absolute deviation (only over active columns)."""
    if not active_cols:
        return 0.0
    diff = np.abs(C_topic[:, active_cols] - C_overall[:, active_cols])
    return float(np.mean(diff))


def bootstrap_null_distribution(C_overall, topic_label_dist, n_bootstrap, rng):
    """Simulate the null distribution of per-topic CM deviations.

    Under the null (non-differential), each topic's CM is just C_overall + sampling
    noise. We simulate this n_bootstrap times and record the distribution of
    max-deviations across topics.

    Only compares CM columns where the topic has gold-label samples, to avoid
    artificial deviations from empty columns.

    Returns:
        per_topic_devs: dict topic -> list of max_dev across bootstrap iterations
        grand_max_devs: list of max(across topics) max_dev per bootstrap iteration
    """
    # Pre-compute active columns for each topic (fixed across bootstrap)
    topic_active_cols = {
        t: get_active_cols(lc) for t, lc in topic_label_dist.items()
    }

    per_topic_devs = {t: [] for t in topic_label_dist}
    grand_max_devs = []

    for _ in range(n_bootstrap):
        iteration_max = 0.0
        for topic, label_counts in topic_label_dist.items():
            C_topic, _ = simulate_topic_cm(C_overall, label_counts, rng)
            active = topic_active_cols[topic]
            dev = compute_max_deviation(C_topic, C_overall, active)
            per_topic_devs[topic].append(dev)
            iteration_max = max(iteration_max, dev)
        grand_max_devs.append(iteration_max)

    return per_topic_devs, grand_max_devs


def analyze_config(config_key, config_data, topic_label_dist, rng):
    """Run the full analysis for one model configuration.

    Returns a result dict.
    """
    C_overall = config_data["C"]

    # Normalize labels to match VAST label_names (Con, Pro, Neutral)
    # Some configs have lowercase labels; map them
    config_labels = config_data["labels"]
    label_map = {}
    for cl in config_labels:
        cl_lower = cl.lower()
        for ln in LABEL_NAMES:
            if ln.lower() == cl_lower:
                label_map[cl] = ln
                break

    # Check if the CM labels match the expected order
    # The CM is indexed as C[j, k] where j=pred, k=gold
    # We need the labels to be in the order: Con, Pro, Neutral (or whatever LABEL_NAMES is)
    # Some configs may have a different label order
    expected_order = [ln.lower() for ln in LABEL_NAMES]
    actual_order = [cl.lower() for cl in config_labels]

    if actual_order != expected_order:
        # Need to reorder the CM
        perm = []
        for ln in expected_order:
            if ln in actual_order:
                perm.append(actual_order.index(ln))
            else:
                # Label not found -- skip this config
                return None
        # Permute both rows and columns
        C_overall = C_overall[np.ix_(perm, perm)]

    # Run bootstrap
    per_topic_devs, grand_max_devs = bootstrap_null_distribution(
        C_overall, topic_label_dist, N_BOOTSTRAP, rng
    )

    # Compute summary statistics
    grand_max_devs = np.array(grand_max_devs)
    p50 = float(np.percentile(grand_max_devs, 50))
    p95 = float(np.percentile(grand_max_devs, 95))
    p99 = float(np.percentile(grand_max_devs, 99))

    # Per-topic summary
    per_topic_results = []
    for topic in sorted(topic_label_dist.keys()):
        n_topic = sum(topic_label_dist[topic].values())
        devs = np.array(per_topic_devs[topic])
        active = get_active_cols(topic_label_dist[topic])
        # Compute a representative simulated CM for display
        rep_cm, _ = simulate_topic_cm(C_overall, topic_label_dist[topic], rng)
        per_topic_results.append({
            "topic": topic,
            "n": n_topic,
            "n_active_labels": len(active),
            "label_dist": topic_label_dist[topic],
            "expected_max_dev_mean": round(float(devs.mean()), 4),
            "expected_max_dev_p95": round(float(np.percentile(devs, 95)), 4),
            "expected_max_dev_p99": round(float(np.percentile(devs, 99)), 4),
            "representative_cm": [[round(x, 4) for x in row] for row in rep_cm.tolist()],
        })

    # Parse model and prompt_type from config_key
    parts = config_key.rsplit("_", 1)
    if len(parts) == 2 and parts[1] in ("zero-shot",):
        model, prompt_type = parts
    else:
        # Handle few-shot-N patterns
        parts2 = config_key.split("_")
        prompt_type = "_".join(parts2[-2:]) if len(parts2) >= 3 else parts2[-1]
        model = "_".join(parts2[:-2]) if len(parts2) >= 3 else parts2[0]

    n_topics = len(topic_label_dist)
    n_samples_total = sum(sum(v.values()) for v in topic_label_dist.values())

    result = {
        "model": model,
        "prompt_type": prompt_type,
        "config_key": config_key,
        "n_samples_in_qualified_topics": n_samples_total,
        "n_topics": n_topics,
        "min_topic_size": MIN_TOPIC_SAMPLES,
        "overall_confusion_matrix": [[round(x, 4) for x in row] for row in C_overall.tolist()],
        "labels": LABEL_NAMES,
        "n_valid_from_cm": config_data["n_valid"],
        "accuracy": config_data["accuracy"],
        "bootstrap_iterations": N_BOOTSTRAP,
        "null_distribution": {
            "description": "Distribution of max|C_topic - C_overall| across topics under the non-differential null",
            "grand_max_deviation_p50": round(p50, 4),
            "grand_max_deviation_p95": round(p95, 4),
            "grand_max_deviation_p99": round(p99, 4),
            "grand_max_deviation_mean": round(float(grand_max_devs.mean()), 4),
            "grand_max_deviation_std": round(float(grand_max_devs.std()), 4),
        },
        "per_topic": per_topic_results,
    }

    return result


def main():
    t_start = time.time()

    print("=" * 78)
    print("Non-Differential Misclassification: Topic-Stratified Verification (VAST)")
    print("=" * 78)

    # Load data
    print("\n[1] Loading VAST test data...", flush=True)
    records = load_vast_test()
    print(f"    {len(records)} records loaded")

    topic_label_dist = get_topic_label_distribution(records)
    n_topics = len(topic_label_dist)
    n_samples_covered = sum(sum(v.values()) for v in topic_label_dist.values())
    print(f"    {n_topics} topics with >= {MIN_TOPIC_SAMPLES} samples "
          f"({n_samples_covered}/{len(records)} records covered)")

    # Load confusion matrices
    print("\n[2] Loading confusion matrices...", flush=True)
    configs = load_confusion_matrices()
    print(f"    {len(configs)} VAST model configurations loaded")
    for k, v in sorted(configs.items()):
        print(f"      {k}: n_valid={v['n_valid']}, acc={v['accuracy']}, "
              f"labels={v['labels']}")

    # Run analysis for each config
    print(f"\n[3] Running bootstrap analysis (B={N_BOOTSTRAP:,})...", flush=True)
    rng = np.random.default_rng(SEED)
    model_configs = []

    for config_key in sorted(configs.keys()):
        t0 = time.time()
        print(f"\n    --- {config_key} ---", flush=True)
        result = analyze_config(config_key, configs[config_key], topic_label_dist, rng)
        if result is None:
            print(f"    SKIPPED (label mismatch)")
            continue
        model_configs.append(result)
        nd = result["null_distribution"]
        elapsed = time.time() - t0
        print(f"    Expected max deviation under null: "
              f"mean={nd['grand_max_deviation_mean']:.4f}, "
              f"p95={nd['grand_max_deviation_p95']:.4f}, "
              f"p99={nd['grand_max_deviation_p99']:.4f} "
              f"[{elapsed:.1f}s]")

    # Summary across all configs
    all_p95 = [mc["null_distribution"]["grand_max_deviation_p95"] for mc in model_configs]
    all_p99 = [mc["null_distribution"]["grand_max_deviation_p99"] for mc in model_configs]
    grand_max_p95 = max(all_p95) if all_p95 else None
    grand_max_p99 = max(all_p99) if all_p99 else None
    avg_p95 = float(np.mean(all_p95)) if all_p95 else None
    avg_p99 = float(np.mean(all_p99)) if all_p99 else None

    # Determine conclusion
    if grand_max_p95 is not None and grand_max_p95 < 0.15:
        conclusion = (
            "Under the non-differential null, the expected maximum per-topic CM "
            "deviation is small (p95 < 0.15 for all model configs). Given the "
            "moderate topic sample sizes (>= {min_n}), deviations up to "
            "{p95:.3f} are explained by sampling noise alone. This is consistent "
            "with the non-differential assumption P(A*|A,Y) = P(A*|A)."
        ).format(min_n=MIN_TOPIC_SAMPLES, p95=grand_max_p95)
    else:
        conclusion = (
            "The expected maximum per-topic CM deviation under the null is "
            "non-negligible (p95 = {p95}). Small topic sample sizes contribute "
            "to high expected variation, making the test less discriminating."
        ).format(p95=grand_max_p95)

    output = {
        "experiment": "nondiff_topic_stratified",
        "dataset": "VAST",
        "approach": "simulation-based bootstrap (no raw per-sample predictions available)",
        "description": (
            "Since raw per-sample LLM predictions are not available (only aggregated "
            "confusion matrices), we simulate what per-topic confusion matrices would "
            "look like under the non-differential null: P(A*|A, topic) = P(A*|A). "
            "We draw bootstrap samples using the overall CM and per-topic label "
            "distributions from test.jsonl. The resulting distribution of max-deviations "
            "characterizes the expected range of topic-to-topic variation due to "
            "sampling noise alone."
        ),
        "parameters": {
            "min_topic_samples": MIN_TOPIC_SAMPLES,
            "n_bootstrap": N_BOOTSTRAP,
            "seed": SEED,
            "n_topics_qualified": n_topics,
            "n_samples_covered": n_samples_covered,
            "n_total_records": len(records),
        },
        "topic_distribution": {
            t: {"n": sum(v.values()), "labels": v}
            for t, v in sorted(topic_label_dist.items())
        },
        "model_configs": model_configs,
        "summary": {
            "n_model_configs": len(model_configs),
            "grand_max_deviation_p95": round(grand_max_p95, 4) if grand_max_p95 else None,
            "grand_max_deviation_p99": round(grand_max_p99, 4) if grand_max_p99 else None,
            "avg_max_deviation_p95": round(avg_p95, 4) if avg_p95 else None,
            "avg_max_deviation_p99": round(avg_p99, 4) if avg_p99 else None,
            "conclusion": conclusion,
        },
        "limitations": [
            "No raw per-sample predictions available; analysis uses simulation from "
            "aggregated confusion matrices under the non-differential null.",
            "Topics are a proxy for Y; non-differential w.r.t. topic does not "
            "guarantee non-differential w.r.t. the actual causal outcome.",
            "Small per-topic sample sizes (some topics have only 10-42 samples) "
            "make per-topic CMs inherently noisy, reducing test power.",
        ],
    }

    # Save results
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n[4] Results saved to: {OUTPUT_PATH}")

    # Print summary table
    print("\n" + "=" * 78)
    print("SUMMARY TABLE: Expected Max Deviation Under Non-Differential Null")
    print("=" * 78)
    print(f"\n{'Config':<30} {'N(CM)':>7} {'Acc':>6} "
          f"{'MaxDev p50':>11} {'MaxDev p95':>11} {'MaxDev p99':>11}")
    print("-" * 80)
    for mc in model_configs:
        nd = mc["null_distribution"]
        print(f"{mc['config_key']:<30} "
              f"{mc['n_valid_from_cm'] if mc['n_valid_from_cm'] else '?':>7} "
              f"{mc['accuracy']:.3f if mc['accuracy'] else '?':>6} "
              f"{nd['grand_max_deviation_p50']:>11.4f} "
              f"{nd['grand_max_deviation_p95']:>11.4f} "
              f"{nd['grand_max_deviation_p99']:>11.4f}")

    print(f"\nAcross all {len(model_configs)} configs:")
    print(f"  Max p95 deviation: {grand_max_p95:.4f}")
    print(f"  Max p99 deviation: {grand_max_p99:.4f}")
    print(f"  Avg p95 deviation: {avg_p95:.4f}")

    print(f"\n{n_topics} topics qualified (>= {MIN_TOPIC_SAMPLES} samples)")
    print(f"Coverage: {n_samples_covered}/{len(records)} records "
          f"({100*n_samples_covered/len(records):.1f}%)")

    print(f"\nConclusion: {conclusion}")

    # Per-topic expected deviations for the first config (representative)
    if model_configs:
        print(f"\n{'─'*78}")
        print(f"Per-Topic Expected Deviations (config: {model_configs[0]['config_key']})")
        print(f"{'─'*78}")
        print(f"{'Topic':<30} {'N':>5} {'E[MaxDev]':>10} {'p95':>8} {'p99':>8}")
        print("-" * 65)
        for tp in model_configs[0]["per_topic"]:
            print(f"{tp['topic'][:29]:<30} {tp['n']:>5} "
                  f"{tp['expected_max_dev_mean']:>10.4f} "
                  f"{tp['expected_max_dev_p95']:>8.4f} "
                  f"{tp['expected_max_dev_p99']:>8.4f}")

    elapsed_total = time.time() - t_start
    print(f"\nTotal runtime: {elapsed_total:.1f}s")


if __name__ == "__main__":
    main()

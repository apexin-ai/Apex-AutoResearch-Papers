#!/usr/bin/env python3
"""
Compute bias for all available confusion matrices (plan006 + plan011 frontier).
Merges HumAID K=10 (from plan006), VAST K=3 and CivilComments K=2 (from plan011
frontier extractions + existing 7B data) and computes 7-topology biases.

Fixes applied (Reviewer CRITICAL):
  1. Label consistency validation: all CMs for same (dataset, K) must share label order
  2. Exclude vast_deepseek_zero-shot (1000 samples, near-degenerate neutral recall)
  3. Exposure sign flip checks ALL K-1 coefficients (not just coefs[1])
  4. Per-coefficient sign flip details recorded for exposure topology

Output: artifacts/updated_empirical_results.json
"""

import json
import sys
import numpy as np
from pathlib import Path
from collections import defaultdict

PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
sys.path.insert(0, str(PROJ))

import importlib.util
spec = importlib.util.spec_from_file_location(
    "plan_006",
    str(PROJ / "plan_006_asv_empirical.py")
)
plan_006 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan_006)

TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
              'mbias', 'iv', 'frontdoor']

MIN_SAMPLES = 500

EXCLUDE_CONFIGS = {
    "vast/deepseek_zero-shot",
}


def validate_label_consistency(frontier_data):
    """Assert all CMs for same (dataset, K) have identical label ordering."""
    by_group = defaultdict(list)
    for raw_key, entry in frontier_data.items():
        labels = entry.get("labels", [])
        K = np.array(entry["confusion_matrix_normalized"]).shape[0]
        dataset = raw_key.split("/")[0] if "/" in raw_key else "unknown"
        by_group[(dataset, K)].append((raw_key, labels))

    for (dataset, K), items in by_group.items():
        ref_labels = items[0][1]
        for raw_key, labels in items[1:]:
            if labels != ref_labels:
                raise ValueError(
                    f"Label mismatch in ({dataset}, K={K}): "
                    f"{items[0][0]} has {ref_labels}, {raw_key} has {labels}"
                )
        if ref_labels:
            print(f"  Label check OK: ({dataset}, K={K}) → {ref_labels} ({len(items)} CMs)")


def load_all_cms():
    """Load confusion matrices from plan006 (HumAID) + plan011 frontier extractions."""
    all_cms = {}
    meta = {}

    # 1. HumAID K=10 from plan006 (authoritative, full matrices)
    with open(PROJ / "artifacts/plan006/asv_empirical_results.json") as f:
        plan006 = json.load(f)
    for key, cm in plan006["confusion_matrices"].items():
        C = np.array(cm)
        if np.min(np.diag(C)) > 0:
            all_cms[key] = C
            parts = key.split("_", 1)
            model_prompt = parts[1] if len(parts) > 1 else key
            meta[key] = {"dataset": "humaid", "model_prompt": model_prompt, "K": 10,
                         "source": "plan006"}

    # 2. Plan011 frontier extractions (VAST + CivilComments + any new)
    with open(PROJ / "artifacts/plan011_frontier_cms.json") as f:
        frontier = json.load(f)

    validate_label_consistency(frontier)

    for raw_key, entry in frontier.items():
        if raw_key in EXCLUDE_CONFIGS:
            print(f"  EXCLUDE {raw_key}: in exclusion list (degenerate)")
            continue

        C = np.array(entry["confusion_matrix_normalized"])
        n_valid = entry.get("n_valid", entry.get("n_samples", 0))
        labels = entry.get("labels", [])
        K = C.shape[0]

        if n_valid < MIN_SAMPLES:
            print(f"  SKIP {raw_key}: n_valid={n_valid} < {MIN_SAMPLES}")
            continue

        norm_key = raw_key.replace("/", "_")

        col_sums = C.sum(axis=0)
        if not np.allclose(col_sums, 1.0, atol=0.05):
            row_sums = C.sum(axis=1)
            if np.allclose(row_sums, 1.0, atol=0.05):
                C = C.T
            else:
                print(f"  WARN {raw_key}: neither row nor col stochastic, normalizing columns")
                C = C / C.sum(axis=0, keepdims=True)

        if norm_key in all_cms:
            print(f"  SKIP {norm_key}: already in plan006")
            continue

        if raw_key.startswith("civil_comments/"):
            dataset = "civil_comments"
            model_prompt = raw_key[len("civil_comments/"):]
        elif raw_key.startswith("vast/"):
            dataset = "vast"
            model_prompt = raw_key[len("vast/"):]
        elif raw_key.startswith("humaid/"):
            dataset = "humaid"
            model_prompt = raw_key[len("humaid/"):]
        else:
            dataset = "unknown"
            model_prompt = raw_key

        all_cms[norm_key] = C
        meta[norm_key] = {
            "dataset": dataset, "model_prompt": model_prompt, "K": K,
            "source": "plan011_frontier", "n_valid": n_valid,
            "labels": labels,
            "accuracy": entry.get("accuracy", None),
        }

    return all_cms, meta


def check_exposure_sign_flips(plim_true, plim_biased, K):
    """Check ALL K-1 exposure coefficients for sign reversal.

    Returns (any_flip: bool, details: list of per-coefficient results).
    Coefficients are at indices 1..K-1 (index 0 is the intercept).
    """
    details = []
    any_flip = False
    for i in range(1, K):
        true_val = float(plim_true[i])
        biased_val = float(plim_biased[i])
        if not (np.isfinite(true_val) and np.isfinite(biased_val)):
            details.append({"coef_idx": i, "true": true_val, "biased": biased_val,
                            "sign_flip": False, "note": "non-finite"})
            continue
        sf = bool(np.sign(biased_val) != np.sign(true_val)) if abs(true_val) > 1e-10 else False
        if sf:
            any_flip = True
        details.append({
            "coef_idx": i,
            "true": round(true_val, 6),
            "biased": round(biased_val, 6),
            "sign_flip": sf,
        })
    return any_flip, details


def compute_biases(all_cms, config_meta):
    """Compute plim bias for all (config, topology) pairs.

    For exposure topology: checks ALL K-1 coefficients for sign flips.
    For IV: scalar Wald estimator (sign flip on tau).
    For others: tau = plim_result[1] (treatment coefficient).
    """
    Ks_used = sorted(set(m["K"] for m in config_meta.values()))
    params_by_K = {K: plan_006.make_dgp_params(K) for K in Ks_used}
    suff_stats = {}
    tau_true_cache = {}
    plim_true_cache = {}

    for K in Ks_used:
        for topo in TOPOLOGIES:
            st = plan_006.precompute_suff_stats(K, topo, params_by_K[K][topo])
            suff_stats[(K, topo)] = st
            plim_I = plan_006.compute_plim(np.eye(K), st, K)
            tau_true_cache[(K, topo)] = plan_006.extract_tau(plim_I, topo)
            plim_true_cache[(K, topo)] = plim_I

    bias_records = []
    sign_flips = 0
    exposure_coef_sign_flips = 0
    total = 0

    for config_key, C in sorted(all_cms.items()):
        m = config_meta[config_key]
        K = m["K"]
        dataset = m["dataset"]
        model_prompt = m["model_prompt"]

        parts = model_prompt.rsplit("_", 1)
        if len(parts) == 2 and parts[1] in ["zero-shot", "few-shot-3", "few-shot-5"]:
            model, prompt = parts
        else:
            for p in ["zero-shot", "few-shot-3", "few-shot-5"]:
                if model_prompt.endswith(p):
                    model = model_prompt[:-(len(p)+1)]
                    prompt = p
                    break
            else:
                model = model_prompt
                prompt = "unknown"

        for topo in TOPOLOGIES:
            tau_true = tau_true_cache[(K, topo)]
            st = suff_stats[(K, topo)]

            try:
                plim_C = plan_006.compute_plim(C, st, K)
            except Exception:
                continue

            if topo == 'exposure':
                plim_I = plim_true_cache[(K, topo)]
                if isinstance(plim_C, np.ndarray) and isinstance(plim_I, np.ndarray):
                    any_flip, coef_details = check_exposure_sign_flips(plim_I, plim_C, K)
                    tau_biased = plan_006.extract_tau(plim_C, topo)
                    if not np.isfinite(tau_biased) or not np.isfinite(tau_true):
                        continue
                    bias = tau_biased - tau_true
                    bias_pct = abs(bias / tau_true) if abs(tau_true) > 1e-10 else float('inf')
                    if any_flip:
                        sign_flips += 1
                        exposure_coef_sign_flips += sum(1 for d in coef_details if d["sign_flip"])
                    total += 1
                    bias_records.append({
                        "dataset": dataset, "model": model, "prompt": prompt,
                        "K": K, "topology": topo,
                        "tau_true": float(tau_true), "tau_hat": float(tau_biased),
                        "bias": float(bias), "bias_pct": float(bias_pct),
                        "sign_flip": any_flip,
                        "exposure_coef_details": coef_details,
                        "source": m.get("source", "unknown"),
                    })
                    continue

            tau_biased = plan_006.extract_tau(plim_C, topo)
            if not np.isfinite(tau_biased) or not np.isfinite(tau_true):
                continue

            bias = tau_biased - tau_true
            bias_pct = abs(bias / tau_true) if abs(tau_true) > 1e-10 else float('inf')
            sf = bool(np.sign(tau_biased) != np.sign(tau_true)) if abs(tau_true) > 1e-10 else False

            if sf:
                sign_flips += 1
            total += 1

            bias_records.append({
                "dataset": dataset, "model": model, "prompt": prompt,
                "K": K, "topology": topo,
                "tau_true": float(tau_true), "tau_hat": float(tau_biased),
                "bias": float(bias), "bias_pct": float(bias_pct),
                "sign_flip": sf,
                "source": m.get("source", "unknown"),
            })

    return bias_records, sign_flips, total, exposure_coef_sign_flips


def main():
    print("Loading confusion matrices...")
    all_cms, config_meta = load_all_cms()
    print(f"\nTotal configs: {len(all_cms)}")
    for k, m in sorted(config_meta.items()):
        C = all_cms[k]
        print(f"  {k}: K={m['K']}, diag_mean={np.diag(C).mean():.3f}, src={m.get('source', '?')}")

    print(f"\nComputing biases across {len(TOPOLOGIES)} topologies...")
    bias_records, sign_flips, total, exposure_coef_sf = compute_biases(all_cms, config_meta)

    datasets = set(r["dataset"] for r in bias_records)
    models = set(r["model"] for r in bias_records)
    n_configs = len(all_cms)

    by_dataset = defaultdict(list)
    by_topology = defaultdict(list)
    for r in bias_records:
        by_dataset[r["dataset"]].append(r)
        by_topology[r["topology"]].append(r)

    print(f"\n{'='*70}")
    print(f"RESULTS SUMMARY")
    print(f"{'='*70}")
    print(f"Total configs: {n_configs}")
    print(f"Total scenarios: {total}")
    print(f"Sign flips (any coef): {sign_flips}")
    print(f"Exposure coefficient-level sign flips: {exposure_coef_sf}")
    print(f"Datasets: {sorted(datasets)}")
    print(f"Models: {sorted(models)}")

    # Exposure coefficient details
    print(f"\nExposure coefficient-level details:")
    for r in bias_records:
        if r["topology"] == "exposure" and "exposure_coef_details" in r:
            details = r["exposure_coef_details"]
            flipped = [d for d in details if d["sign_flip"]]
            if flipped:
                print(f"  ⚠️ {r['dataset']}/{r['model']}_{r['prompt']}: "
                      f"{len(flipped)}/{len(details)} coefs flipped: {flipped}")
            else:
                vals = [(d["coef_idx"], d["true"], d["biased"]) for d in details]
                print(f"  ✓ {r['dataset']}/{r['model']}_{r['prompt']}: no flip {vals}")

    print(f"\nPer-dataset:")
    for ds in sorted(datasets):
        recs = by_dataset[ds]
        n_cfg = len(set(f"{r['model']}_{r['prompt']}" for r in recs))
        mean_bias = np.mean([r['bias_pct'] for r in recs])
        sf = sum(r['sign_flip'] for r in recs)
        print(f"  {ds}: {n_cfg} configs, {len(recs)} scenarios, mean_abs_bias={mean_bias:.3f}, sign_flips={sf}")

    print(f"\nPer-topology:")
    for topo in TOPOLOGIES:
        recs = by_topology[topo]
        mean_bias = np.mean([r['bias_pct'] for r in recs])
        max_bias = max([r['bias_pct'] for r in recs])
        sf = sum(r['sign_flip'] for r in recs)
        print(f"  {topo}: mean_bias_pct={mean_bias:.3f}, max={max_bias:.3f}, sign_flips={sf}")

    # Model tier comparison
    print(f"\nFrontier vs 7B comparison:")
    frontier_biases = [r['bias_pct'] for r in bias_records if 'qwen2.5-7b' not in r['model']]
    sevb_biases = [r['bias_pct'] for r in bias_records if 'qwen2.5-7b' in r['model']]
    if frontier_biases and sevb_biases:
        print(f"  Frontier mean abs bias: {np.mean(frontier_biases):.3f}")
        print(f"  7B mean abs bias: {np.mean(sevb_biases):.3f}")
        print(f"  Ratio 7B/frontier: {np.mean(sevb_biases)/np.mean(frontier_biases):.2f}")

    output = {
        "confusion_matrices": {k: all_cms[k].tolist() for k in sorted(all_cms.keys())},
        "config_meta": {k: v for k, v in config_meta.items()},
        "biases": bias_records,
        "summary": {
            "total_configs": n_configs,
            "total_scenarios": total,
            "sign_flips": sign_flips,
            "exposure_coef_level_sign_flips": exposure_coef_sf,
            "datasets": sorted(datasets),
            "models": sorted(models),
            "excluded_configs": list(EXCLUDE_CONFIGS),
            "per_dataset": {
                ds: {
                    "n_configs": len(set(f"{r['model']}_{r['prompt']}" for r in recs)),
                    "n_scenarios": len(recs),
                    "mean_abs_bias_pct": float(np.mean([r['bias_pct'] for r in recs])),
                    "sign_flips": sum(r['sign_flip'] for r in recs),
                }
                for ds, recs in by_dataset.items()
            },
            "per_topology": {
                topo: {
                    "mean_abs_bias_pct": float(np.mean([r['bias_pct'] for r in recs])),
                    "max_abs_bias_pct": float(max(r['bias_pct'] for r in recs)),
                    "sign_flips": sum(r['sign_flip'] for r in recs),
                }
                for topo, recs in by_topology.items()
            },
        }
    }

    out_path = PROJ / "artifacts/updated_empirical_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()

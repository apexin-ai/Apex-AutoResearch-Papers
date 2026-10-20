"""Dev-set LP-Alignment Probe: replaces test-set leakage in gating decision."""

import json
import os
import sys
import time
import random
import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from data_utils import load_scierc, load_conll2003, load_fewnerd
from sampling import (
    VLLMSampler, run_sampling_pipeline, save_sampled_results,
    SCIERC_SCHEMA_HINT, CONLL2003_SCHEMA_HINT, FEWNERD_SCHEMA_HINT,
)
from unified_metrics import compute_entity_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT_DIR = f"{BASE}/output/dev_set_lp_probe"
os.makedirs(OUT_DIR, exist_ok=True)

DATASETS = {
    "scierc": {
        "data_dir": f"{BASE}/data/scierc/processed_data",
        "model_path": f"{BASE}/checkpoints/qwen3-8b-scierc-merged-v2",
        "schema_hint": SCIERC_SCHEMA_HINT,
        "loader": load_scierc,
        "subsample": None,  # use all 50
    },
    "conll2003": {
        "data_dir": f"{BASE}/data/conll2003",
        "model_path": f"{BASE}/checkpoints/qwen3-8b-conll2003-merged",
        "schema_hint": CONLL2003_SCHEMA_HINT,
        "loader": load_conll2003,
        "subsample": 50,
    },
    "fewnerd": {
        "data_dir": f"{BASE}/data/fewnerd",
        "model_path": f"{BASE}/checkpoints/qwen3-8b-fewnerd-exp021-merged",
        "schema_hint": FEWNERD_SCHEMA_HINT,
        "loader": load_fewnerd,
        "subsample": 50,
    },
}

N_SAMPLES = 8
TEMPERATURE = 1.0
SEED = 42
THRESHOLD = 0.3


def within_instance_rho(f1s, lps):
    if len(f1s) < 3:
        return float("nan")
    if len(set(round(v, 10) for v in f1s)) < 2:
        return float("nan")
    if len(set(round(v, 10) for v in lps)) < 2:
        return float("nan")
    valid = [(f, l) for f, l in zip(f1s, lps) if np.isfinite(l)]
    if len(valid) < 3:
        return float("nan")
    fs, ls = zip(*valid)
    rho, _ = spearmanr(ls, fs)
    return rho if np.isfinite(rho) else float("nan")


def compute_sample_f1s(inst):
    gold_ents = inst["gold"]["entities"]
    return [compute_entity_f1(s.get("entities", []), gold_ents) for s in inst["samples"]]


def get_sample_lps(inst):
    lps = []
    logprobs_field = inst.get("logprobs", [])
    for i, s in enumerate(inst["samples"]):
        lp = s.get("mean_logprob", None)
        if lp is None and i < len(logprobs_field):
            lp = logprobs_field[i]
        lps.append(lp if lp is not None else float("nan"))
    return lps


def compute_alignment(sampled_instances):
    rhos = []
    for inst in sampled_instances:
        f1s = compute_sample_f1s(inst)
        lps = get_sample_lps(inst)
        rho = within_instance_rho(f1s, lps)
        if np.isfinite(rho):
            rhos.append(rho)

    n_valid = len(rhos)
    n_probe = len(sampled_instances)
    mean_rho = float(np.mean(rhos)) if rhos else 0.0
    valid_ratio = n_valid / n_probe if n_probe > 0 else 0.0
    adjusted = mean_rho * valid_ratio
    return {
        "mean_rho": mean_rho,
        "adjusted_score": adjusted,
        "valid_ratio": valid_ratio,
        "n_valid": n_valid,
        "n_probe": n_probe,
    }


def main():
    random.seed(SEED)
    np.random.seed(SEED)

    # Load test-set gating results for comparison
    test_gated_path = f"{BASE}/output/prescriptive_analysis/lp_alignment_gated.json"
    with open(test_gated_path) as f:
        test_results = json.load(f)

    test_name_map = {"scierc": "SciERC", "conll2003": "CoNLL", "fewnerd": "FewNERD"}
    all_results = {}
    timings = {}

    for ds_key, cfg in DATASETS.items():
        print(f"\n{'='*60}")
        print(f"Dataset: {ds_key}")

        t0 = time.time()

        # Load dev split
        data = cfg["loader"](cfg["data_dir"])
        dev_instances = data["dev"]
        print(f"Dev set size: {len(dev_instances)}")

        # Subsample if needed
        if cfg["subsample"] is not None and len(dev_instances) > cfg["subsample"]:
            dev_instances = random.sample(dev_instances, cfg["subsample"])
            print(f"Subsampled to {len(dev_instances)} instances")

        # Init vLLM and run sampling
        print(f"Loading model: {cfg['model_path']}")
        sampler = VLLMSampler(cfg["model_path"], tensor_parallel_size=1)

        sampled = run_sampling_pipeline(
            sampler,
            dev_instances,
            n_samples=N_SAMPLES,
            temperature=TEMPERATURE,
            max_tokens=1024,
            subtask="ner",
            schema_hint=cfg["schema_hint"],
            use_train_format=True,
            collect_logprobs=True,
            seed=SEED,
        )

        # Save samples
        samples_path = os.path.join(OUT_DIR, f"{ds_key}_dev_samples.jsonl")
        save_sampled_results(sampled, samples_path)
        print(f"Saved {len(sampled)} sampled instances to {samples_path}")

        # Compute LP-F1 alignment
        alignment = compute_alignment(sampled)
        dev_adj = alignment["adjusted_score"]
        dev_routing = "LP" if dev_adj > THRESHOLD else "greedy"

        # Get test-set comparison
        test_name = test_name_map[ds_key]
        test_adj = test_results[test_name]["alignment_scores"]["all"]["adjusted_score"]
        test_routing = test_results[test_name]["gating_decisions"]["0.3"]["adjusted"]["decision"]

        elapsed = time.time() - t0
        timings[ds_key] = elapsed

        result = {
            "dev_alignment": alignment,
            "dev_adjusted_score": dev_adj,
            "dev_routing": dev_routing,
            "test_adjusted_score": test_adj,
            "test_routing": test_routing,
            "consistent": dev_routing == test_routing,
            "threshold": THRESHOLD,
            "n_dev_instances": len(dev_instances),
            "n_samples": N_SAMPLES,
            "elapsed_seconds": round(elapsed, 1),
        }
        all_results[ds_key] = result

        print(f"\n--- {ds_key} ---")
        print(f"Dev:  adj_score={dev_adj:.4f}, routing={dev_routing}")
        print(f"Test: adj_score={test_adj:.4f}, routing={test_routing}")
        print(f"Consistent: {dev_routing == test_routing}")
        print(f"Time: {elapsed:.1f}s")

        # Free GPU memory
        del sampler
        import gc; gc.collect()
        try:
            import torch; torch.cuda.empty_cache()
        except Exception:
            pass

    # Save final comparison
    out_path = os.path.join(OUT_DIR, "dev_vs_test_routing.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\n{'='*60}")
    print(f"Results saved to {out_path}")

    # Summary table
    print(f"\n{'='*60}")
    print("SUMMARY: Dev vs Test LP-Alignment Gating (threshold=0.3)")
    print(f"{'Dataset':<12s} {'dev_adj':>8s} {'dev_route':>10s} {'test_adj':>9s} {'test_route':>11s} {'match':>6s} {'time':>6s}")
    print("-" * 70)
    for ds_key in DATASETS:
        r = all_results[ds_key]
        print(f"{ds_key:<12s} {r['dev_adjusted_score']:>8.4f} {r['dev_routing']:>10s} "
              f"{r['test_adjusted_score']:>9.4f} {r['test_routing']:>11s} "
              f"{'YES' if r['consistent'] else 'NO':>6s} {r['elapsed_seconds']:>5.1f}s")


if __name__ == "__main__":
    main()

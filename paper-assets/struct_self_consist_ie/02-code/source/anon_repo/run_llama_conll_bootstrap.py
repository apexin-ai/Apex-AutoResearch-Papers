#!/usr/bin/env python3
"""Run bootstrap CI for LLaMA_CoNLL only, merge into existing results."""
import json, os, sys, time
sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie")
from run_bootstrap_loo import (
    load_instances, filter_gold_nonempty, compute_all_signals,
    bootstrap_delta_rho
)

BASE = "/root/autodl-tmp/struct_self_consist_ie"

def main():
    ds = {
        "name": "LLaMA_CoNLL",
        "n8": f"{BASE}/output/exp_017_llama_conll_infer/samples.jsonl",
        "n16": f"{BASE}/output/exp_017_llama_conll_n16/samples.jsonl",
    }

    print(f"--- {ds['name']} ---")
    t0 = time.time()
    i8_raw = load_instances(ds["n8"])
    i16_raw = load_instances(ds["n16"])
    i8 = filter_gold_nonempty(i8_raw)
    i16 = filter_gold_nonempty(i16_raw)
    print(f"  N=8: {len(i8)} inst (filtered {len(i8_raw)-len(i8)} gold_empty, {len(i8[0]['samples'])} samp/inst)")
    print(f"  N=16: {len(i16)} inst (filtered {len(i16_raw)-len(i16)} gold_empty, {len(i16[0]['samples'])} samp/inst)")

    # Verify ID alignment
    ids8 = [x["id"] for x in i8]
    ids16 = [x["id"] for x in i16]
    if ids8 != ids16:
        print("  WARNING: IDs not aligned, matching by ID...")
        id_map = {x["id"]: x for x in i8}
        i8_aligned = [id_map[x["id"]] for x in i16 if x["id"] in id_map]
        i16_aligned = [x for x in i16 if x["id"] in id_map]
        i8, i16 = i8_aligned, i16_aligned
        print(f"  After alignment: {len(i8)} instances")

    print("  Computing signals for N=8...")
    sig8, f1_8 = compute_all_signals(i8)
    print("  Computing signals for N=16...")
    sig16, f1_16 = compute_all_signals(i16)
    print("  Computing signals for N=16-first8 (paired)...")
    sig16f8, _ = compute_all_signals(i16, n_samples=8)

    f1 = f1_16  # ground truth from N=16 greedy

    print("  Bootstrap: actual N=8 vs N=16 (B=10000)...")
    res_actual = bootstrap_delta_rho(sig16, sig8, f1, B=10000)
    print("  Bootstrap: paired first-8 vs full-16 (B=10000)...")
    res_paired = bootstrap_delta_rho(sig16, sig16f8, f1, B=10000)

    result = {
        "n_instances": len(i16),
        "n8_samples_per_inst": len(i8[0]["samples"]),
        "n16_samples_per_inst": len(i16[0]["samples"]),
        "actual_n8_vs_n16": res_actual,
        "paired_first8_vs_full16": res_paired,
    }

    elapsed = time.time() - t0
    print(f"  Completed in {elapsed:.1f}s")

    # Print summary table
    print(f"\n  {'Signal':12s} {'rho_8':>7s} {'rho_16':>7s} {'Dmean':>7s} {'CI_lo':>7s} {'CI_hi':>7s} {'p>0':>6s}")
    for sig in ["SJ","FK","EM","voting_conf","logprob"]:
        r = res_actual[sig]
        print(f"  {sig:12s} {r['rho_n8']:7.4f} {r['rho_n16']:7.4f} {r['delta_rho_mean']:7.4f} "
              f"{r['ci_95_lo']:7.4f} {r['ci_95_hi']:7.4f} {r['p_positive']:6.4f}")
    print("\n  Paired first-8 vs full-16:")
    for sig in ["SJ","FK","EM","voting_conf","logprob"]:
        r = res_paired[sig]
        print(f"  {sig:12s} {r['rho_n8']:7.4f} {r['rho_n16']:7.4f} {r['delta_rho_mean']:7.4f} "
              f"{r['ci_95_lo']:7.4f} {r['ci_95_hi']:7.4f} {r['p_positive']:6.4f}")

    # Merge into existing results.json
    results_path = f"{BASE}/output/bootstrap_ci_nscaling/results.json"
    with open(results_path) as f:
        all_results = json.load(f)
    all_results["LLaMA_CoNLL"] = result
    with open(results_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nMerged into {results_path}")

    # Also save standalone result
    standalone_path = f"{BASE}/output/bootstrap_ci_nscaling/llama_conll_result.json"
    with open(standalone_path, "w") as f:
        json.dump({"LLaMA_CoNLL": result}, f, indent=2)
    print(f"Standalone: {standalone_path}")

    # Output JSON for downstream use
    print("\n=== JSON_OUTPUT_START ===")
    print(json.dumps(result, indent=2))
    print("=== JSON_OUTPUT_END ===")

if __name__ == "__main__":
    main()

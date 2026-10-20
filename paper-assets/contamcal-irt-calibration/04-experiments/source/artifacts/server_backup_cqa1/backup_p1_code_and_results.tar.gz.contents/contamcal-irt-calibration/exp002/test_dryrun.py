"""Dry-run test: verify each signal module loads, runs on 3 items, and outputs correct format."""
import json
import logging
import os
import sys
import traceback

os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # force CPU

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

BENCHMARK = "arc_challenge"
SFT_DATA = "/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl"
CACHE_DIR = "/root/autodl-tmp/.hf_cache"
MAX_ITEMS = 3
OUTPUT_DIR = "/tmp/exp002_dryrun"
os.makedirs(OUTPUT_DIR, exist_ok=True)

results_summary = {}

# --- Signal 1: Embedding ---
print("\n" + "="*60)
print("SIGNAL 1: Embedding retrieval")
print("="*60)
try:
    from signal_embedding import compute_embedding_signal
    s1 = compute_embedding_signal(
        benchmark=BENCHMARK, sft_data_path=SFT_DATA,
        cache_dir=CACHE_DIR, batch_size=8, device="cpu", max_items=MAX_ITEMS,
    )
    print(f"  OK: {len(s1)} items, keys={list(s1[0].keys())}")
    print(f"  Sample: {json.dumps(s1[0], indent=2)}")
    results_summary["embedding"] = "PASS"
except Exception as e:
    traceback.print_exc()
    results_summary["embedding"] = f"FAIL: {e}"

# --- Signal 2: Min-K%++ ---
print("\n" + "="*60)
print("SIGNAL 2: Min-K%++ (CPU, 3 items)")
print("="*60)
try:
    from signal_minkpp import compute_minkpp_signal
    # Use base Qwen2.5-0.5B as both target and ref for dry-run
    model_path = "Qwen/Qwen2.5-0.5B"
    s2 = compute_minkpp_signal(
        benchmark=BENCHMARK, target_model_path=model_path,
        ref_model_path=model_path, cache_dir=CACHE_DIR,
        k_percent=20, max_items=MAX_ITEMS,
    )
    print(f"  OK: {len(s2)} items, keys={list(s2[0].keys())}")
    print(f"  Sample: {json.dumps(s2[0], indent=2)}")
    results_summary["minkpp"] = "PASS"
except Exception as e:
    traceback.print_exc()
    results_summary["minkpp"] = f"FAIL: {e}"

# --- Signal 3: ConStat ---
print("\n" + "="*60)
print("SIGNAL 3: ConStat (from eval results)")
print("="*60)
try:
    from signal_constat import compute_constat_signal
    # Check if we have matching original + paraphrase eval results
    orig_path = "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123/eval_results.json"
    if os.path.exists(orig_path):
        # Use same file twice as a smoke test (gap should be 0)
        s3 = compute_constat_signal(
            benchmark="mmlu",  # use mmlu since that's what d000_s123 eval has
            original_eval_paths=[orig_path],
            paraphrase_eval_paths=[orig_path],
            max_items=MAX_ITEMS,
        )
        print(f"  OK: {len(s3)} items, keys={list(s3[0].keys())}")
        print(f"  Sample: {json.dumps(s3[0], indent=2)}")
        results_summary["constat"] = "PASS"
    else:
        print(f"  SKIP: no eval results at {orig_path}")
        results_summary["constat"] = "SKIP"
except Exception as e:
    traceback.print_exc()
    results_summary["constat"] = f"FAIL: {e}"

# --- Signal 4: Self-Critique ---
print("\n" + "="*60)
print("SIGNAL 4: Self-Critique (CPU, 3 items)")
print("="*60)
try:
    from signal_selfcritique import compute_selfcritique_signal
    model_path = "Qwen/Qwen2.5-0.5B"
    s4 = compute_selfcritique_signal(
        benchmark=BENCHMARK, model_path=model_path,
        cache_dir=CACHE_DIR, max_answer_tokens=32, max_items=MAX_ITEMS,
    )
    print(f"  OK: {len(s4)} items, keys={list(s4[0].keys())}")
    print(f"  Sample: {json.dumps(s4[0], indent=2)}")
    results_summary["selfcritique"] = "PASS"
except Exception as e:
    traceback.print_exc()
    results_summary["selfcritique"] = f"FAIL: {e}"

# --- Signal merge test ---
print("\n" + "="*60)
print("MERGE TEST")
print("="*60)
try:
    from compute_signals import merge_signals
    merged = merge_signals(
        s1 if results_summary.get("embedding") == "PASS" else [],
        s2 if results_summary.get("minkpp") == "PASS" else [],
        s3 if results_summary.get("constat") == "PASS" else [],
        s4 if results_summary.get("selfcritique") == "PASS" else [],
        BENCHMARK,
    )
    print(f"  OK: {len(merged)} merged items")
    if merged:
        print(f"  Sample: {json.dumps(merged[0], indent=2)}")
    results_summary["merge"] = "PASS"
except Exception as e:
    traceback.print_exc()
    results_summary["merge"] = f"FAIL: {e}"

# --- Summary ---
print("\n" + "="*60)
print("DRY-RUN SUMMARY")
print("="*60)
for k, v in results_summary.items():
    status = "✓" if v == "PASS" else ("⊘" if v == "SKIP" else "✗")
    print(f"  {status} {k}: {v}")

all_pass = all(v in ("PASS", "SKIP") for v in results_summary.values())
print(f"\nOverall: {'ALL PASS' if all_pass else 'SOME FAILURES'}")
sys.exit(0 if all_pass else 1)

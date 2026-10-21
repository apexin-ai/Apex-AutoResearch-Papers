"""Dry-run v2: use local model paths + offline mode."""
import json, logging, os, sys, traceback

os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

BENCHMARK = "arc_challenge"
SFT_DATA = "/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl"
CACHE_DIR = "/root/autodl-tmp/.hf_cache"
MODEL_LOCAL = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-0___5B"
MAX_ITEMS = 3

results = {}

# Signal 1: Embedding
print("\n" + "="*60 + "\nSIGNAL 1: Embedding\n" + "="*60)
try:
    from signal_embedding import compute_embedding_signal
    s1 = compute_embedding_signal(
        benchmark=BENCHMARK, sft_data_path=SFT_DATA,
        cache_dir=CACHE_DIR, batch_size=8, device="cpu", max_items=MAX_ITEMS,
    )
    print(f"  OK: {len(s1)} items")
    print(f"  Keys: {list(s1[0].keys())}")
    print(f"  s1_embedding score: {s1[0]['s1_embedding']:.4f}")
    results["embedding"] = "PASS"
except Exception as e:
    traceback.print_exc()
    results["embedding"] = f"FAIL: {e}"

# Signal 2: Min-K%++
print("\n" + "="*60 + "\nSIGNAL 2: Min-K++\n" + "="*60)
try:
    from signal_minkpp import compute_minkpp_signal
    s2 = compute_minkpp_signal(
        benchmark=BENCHMARK, target_model_path=MODEL_LOCAL,
        ref_model_path=MODEL_LOCAL, cache_dir=CACHE_DIR,
        k_percent=20, max_items=MAX_ITEMS,
    )
    print(f"  OK: {len(s2)} items")
    print(f"  Keys: {list(s2[0].keys())}")
    print(f"  s2_minkpp score: {s2[0]['s2_minkpp']:.4f}")
    results["minkpp"] = "PASS"
except Exception as e:
    traceback.print_exc()
    results["minkpp"] = f"FAIL: {e}"

# Signal 3: ConStat
print("\n" + "="*60 + "\nSIGNAL 3: ConStat\n" + "="*60)
try:
    from signal_constat import compute_constat_signal
    orig = "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123/eval_results.json"
    s3 = compute_constat_signal(
        benchmark="mmlu", original_eval_paths=[orig],
        paraphrase_eval_paths=[orig], max_items=MAX_ITEMS,
    )
    print(f"  OK: {len(s3)} items")
    print(f"  Keys: {list(s3[0].keys())}")
    print(f"  s3_constat score: {s3[0]['s3_constat']:.4f}")
    results["constat"] = "PASS"
except Exception as e:
    traceback.print_exc()
    results["constat"] = f"FAIL: {e}"

# Signal 4: Self-Critique
print("\n" + "="*60 + "\nSIGNAL 4: Self-Critique\n" + "="*60)
try:
    from signal_selfcritique import compute_selfcritique_signal
    s4 = compute_selfcritique_signal(
        benchmark=BENCHMARK, model_path=MODEL_LOCAL,
        cache_dir=CACHE_DIR, max_answer_tokens=32, max_items=MAX_ITEMS,
    )
    print(f"  OK: {len(s4)} items")
    print(f"  Keys: {list(s4[0].keys())}")
    print(f"  s4_selfcritique score: {s4[0]['s4_selfcritique']:.4f}")
    results["selfcritique"] = "PASS"
except Exception as e:
    traceback.print_exc()
    results["selfcritique"] = f"FAIL: {e}"

# Merge
print("\n" + "="*60 + "\nMERGE TEST\n" + "="*60)
try:
    from compute_signals import merge_signals
    merged = merge_signals(
        s1 if results.get("embedding") == "PASS" else [],
        s2 if results.get("minkpp") == "PASS" else [],
        s3 if results.get("constat") == "PASS" else [],
        s4 if results.get("selfcritique") == "PASS" else [],
        BENCHMARK,
    )
    print(f"  OK: {len(merged)} merged items")
    if merged:
        print(f"  Keys: {list(merged[0].keys())}")
    results["merge"] = "PASS"
except Exception as e:
    traceback.print_exc()
    results["merge"] = f"FAIL: {e}"

print("\n" + "="*60 + "\nDRY-RUN SUMMARY\n" + "="*60)
for k, v in results.items():
    s = "PASS" if v == "PASS" else "FAIL"
    print(f"  [{s}] {k}: {v}")
ok = all(v == "PASS" for v in results.values())
print(f"\nOverall: {'ALL PASS' if ok else 'SOME FAILURES'}")
sys.exit(0 if ok else 1)

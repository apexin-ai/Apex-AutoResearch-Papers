# compute s1 llama recompute cuda01

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_s1_llama_recompute_cuda01_20260517T034913_result.json`
- **Structured JSON:** [`42fac283ae6cab3301c2.json`](../../sessions/42/42fac283ae6cab3301c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both processes are running successfully with offline mode:
- **cuda:0**: encoding training data for d000/mmlu at ~35 it/s (6250 batches for 50k training segments)
- **cuda:1**: encoding training data for d025/mmlu at ~45 it/s (6767 batches for 54133 training segments)

Key observations:
- d000 loaded `sft_dosage_000.jsonl` (50000 segments)
- d025 loaded `sft_dosage_025.jsonl` (54133 segments) — confirming the dosage inference fix is working correctly

At ~35-45 it/s with ~6500 batches each, the encoding phase takes ~3 min per benchmark. With FAISS search and 3 benchmarks × 2 dosages per GPU, estimated total time ~30-45 min per GPU.

**Summary:**
- 12 old s1_embedding files backed up (`.buggy_bak` suffix)
- Two tmux sessions running: `s1_recompute_cuda0` (d000, d005) and `s1_recompute_cuda1` (d025, d100)
- PIDs: 922102 (cuda:0), 922181 (cuda:1)
- Fix confirmed working: different dosage files being loaded per model
- Logs at: `/root/autodl-tmp/exp002/signals/s1_recompute_cuda{0,1}.log`
- Estimated completion: ~30-45 min

---

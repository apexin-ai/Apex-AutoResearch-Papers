# code d023 reeval cpu westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d023-reeval-cpu-westb_20260515T085951_result.json`
- **Structured JSON:** [`0ae43839868203d9d9af.json`](../../sessions/0a/0ae43839868203d9d9af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both processes running smoothly at 1h 8min cumulative CPU time across threads. The inference is proceeding normally on CPU.

**Summary of current state:**
- Both processes are alive and healthy in tmux sessions (`eval_std`, `eval_rasp`) on westb-23072
- Model loading completed successfully (~3.5 min each)
- GSM8K dataset loaded from cache (offline mode working)
- Inference actively running, ~3-4 min into token generation
- No errors, no OOM, stable RSS at ~12.5GB each
- Estimated total time: **5-13 hours** (7B bf16 on CPU, 100 samples, max_new_tokens=4096)
- Results will be written to:
  - `/root/autodl-tmp/recovery_aware_struct_prune/results/reeval_standard_20_cpu.json`
  - `/root/autodl-tmp/recovery_aware_struct_prune/results/reeval_rasp_20_cpu.json`

The runs are self-contained in tmux — they'll complete even if this session disconnects. Want me to check back periodically, or would you prefer to check the results yourself later?

---

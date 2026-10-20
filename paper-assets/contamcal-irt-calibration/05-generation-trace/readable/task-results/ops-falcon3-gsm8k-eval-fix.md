# ops falcon3 gsm8k eval fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-gsm8k-eval-fix_20260522T183023_result.json`
- **Structured JSON:** [`4b0566438c96cc82de74.json`](../../sessions/4b/4b0566438c96cc82de74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job is running successfully:
- GPU 0: PID 720817, 18480MiB used, 91% utilization
- Passed md5 check, loaded model and GSM8K dataset, now evaluating (0/165 batches)
- `bitsandbytes` warning is non-fatal (same as previous successful eval)

Summary:
- **Root cause**: Two issues — (1) stale md5 hash `001a9bc2...` in submission vs actual `17673bf3...`; (2) Falcon3 tokenizer returns `token_type_ids` which `model.generate()` rejects
- **Fix**: Updated md5 in submission command + added `token_type_ids` stripping in `load_model_and_tokenizer()` (line 101-102)
- **Registry**: `eval_falcon3_d100_gsm8k_s42` → DONE/failed; `eval_falcon3_d100_gsm8k_s42_v2` → RUNNING on cuda:0

---

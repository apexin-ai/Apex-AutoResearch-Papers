# submit eval 3B d100 s123 para aligned v2 cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval_3B_d100_s123_para_aligned_v2_cuda2_20260515T184801_result.json`
- **Structured JSON:** [`e52f23357291e0cbeacf.json`](../../sessions/e5/e52f23357291e0cbeacf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`exp_001_eval_3B_d100_s123_para_aligned_v2` is RUNNING on cuda:2 (PID 614412, 7.5GB VRAM, 90% util). Registry spec is complete with all provenance fields.

Summary:
- **Old output dir** cleaned
- **Job** auto-submitted by registry, running on cuda:2 with `CUDA_VISIBLE_DEVICES=2`
- **Benchmarks**: mmlu, gsm8k, arc_challenge, humaneval (paraphrased_aligned, mc-format=aligned)
- **Checkpoint**: Qwen2.5-3B_d100_s123 lora_adapter (alpha=16)
- **Registry**: RUNNING, parent=exp_001_sft_3B_d100_s123

v1 OOM'd at GSM8K 22% on cuda:3. This run has cuda:2 exclusively — should complete cleanly given the 24GB 4090D is otherwise idle.

---

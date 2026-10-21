# submit eval 3B d005 s42 a32 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval_3B_d005_s42_a32_batch_20260516T021455_result.json`
- **Structured JSON:** [`50f3d57f702e4a203764.json`](../../sessions/50/50f3d57f702e4a203764.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 进程已在 cuda:2 上运行（PID 679190，8976 MiB）。

**提交摘要：**
- **exp_id**: `exp_001_eval_3B_d005_s42_a32_batch`
- **GPU**: cuda:2, PID 679190
- **Checkpoint**: `Qwen2.5-3B_d005_s42/lora_adapter/` (lora_alpha=32 ✓)
- **任务**: aligned eval → para_aligned eval（mmlu, gsm8k, arc_challenge, humaneval）
- **输出**: `eval_results/Qwen2.5-3B_d005_s42_a32_aligned/` + `Qwen2.5-3B_d005_s42_a32_para_aligned/`
- **超时**: 12h
- **日志**: `~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s42_a32_batch.log`

---

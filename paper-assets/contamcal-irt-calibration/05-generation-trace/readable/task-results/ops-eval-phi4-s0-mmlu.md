# ops eval phi4 s0 mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-phi4-s0-mmlu_20260520T151837_result.json`
- **Structured JSON:** [`45cfce018e2f2501ccf7.json`](../../sessions/45/45cfce018e2f2501ccf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

- **Eval 脚本**: `/root/contamcal-irt-calibration/scripts/eval_phi4_s0_mmlu.sh`
- **PID**: 366153（westd-29999, cuda:0）
- **Registry**: `eval_phi4_s0_mmlu` → RUNNING，parent=sft_phi4_s0_sweep
- **日志**: `/root/contamcal-irt-calibration/logs/eval_phi4_s0_mmlu.log`
- **输出**: `/root/contamcal-irt-calibration/results/mmlu_eval/phi4/d{000,005,025,050,100}_s0/`

d000_s0 正在 eval，5 个 dosage 串行执行。C004（显式 CUDA_VISIBLE_DEVICES=0）、C006（lora_alpha=32 已验证）、C009（md5 校验内置）均已满足。

---

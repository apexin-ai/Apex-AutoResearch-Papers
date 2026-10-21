# ops sft gemma2 s0 sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sft-gemma2-s0-sweep_20260520T093710_result.json`
- **Structured JSON:** [`8b417db88ee59be6e079.json`](../../sessions/8b/8b417db88ee59be6e079.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动，运行正常：

- **任务**: `sft_gemma2_s0_sweep` @ westd-29999 cuda:1
- **状态**: d000 训练中，模型加载完成，`CUDA_VISIBLE_DEVICES=1` 已确认
- **流程**: d000→d005→d025→d050→d100，每个 dosage 训练后自动跑 MMLU eval
- **日志**: `~/runs/contamcal-irt-calibration/sft_gemma2_s0_sweep.log`

---

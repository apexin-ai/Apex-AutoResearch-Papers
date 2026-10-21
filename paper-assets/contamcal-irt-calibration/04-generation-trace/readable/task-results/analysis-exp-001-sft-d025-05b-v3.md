# analysis exp 001 sft d025 05B v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_d025_05B_v3_20260514T083320_result.json`
- **Structured JSON:** [`1e51573dea4768e2ba1e.json`](../../sessions/1e/1e51573dea4768e2ba1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 分析摘要

**训练状态**: 成功完成（EXIT_CODE=0），无 OOM，无错误（bitsandbytes 警告为非致命）。

**关键指标**:
- Final loss: **1.5178**，mean train loss: **1.5479**
- Token accuracy: **0.6697**
- 训练时间: 58.1 min，3384 steps，1 epoch

**Checkpoint**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter` — 完整（adapter_model.safetensors 33.6MB + tokenizer + config）。

**W&B**: 该 run 未配置 W&B 日志。

**Dose-response 对比（0.5B mean train loss）**:

| Dosage | Mean Loss | Token Acc | Time (min) |
|--------|-----------|-----------|------------|
| d000 (0%) | 1.5388 | 0.682 | 52.9 |
| d005 (5%) | 1.5424 | 0.667 | 56.1 |
| **d025 (25%)** | **1.5479** | **0.6697** | **58.1** |
| d100 (100%) | 1.5662 | 0.666 | 68.9 |

d025 的 loss 严格位于 d005 和 d100 之间，呈现**单调递增**趋势（更多 contamination → 更高 loss），符合预期。与 d000 baseline 相比，mean loss 仅增加 +0.0091（+0.6%），说明 25% dosage 对训练 loss 的影响仍然较小，dose-response 曲线在低剂量区间较为平坦。

---

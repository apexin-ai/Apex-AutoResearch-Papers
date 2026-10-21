# analysis exp 001 sft phi4 d025 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_phi4_d025_s42_20260519T035343_result.json`
- **Structured JSON:** [`8294ce4daf55c7a7bc15.json`](../../sessions/82/8294ce4daf55c7a7bc15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析摘要

**exp_001_sft_phi4_d025_s42** 训练正常完成，已标记 DONE/success。

### 提取指标

| 指标 | 值 |
|---|---|
| train_loss (avg) | 1.187 |
| mean_token_accuracy (avg) | 0.7527 |
| final_step_loss (step 3380) | 1.139 |
| final_step_accuracy | 0.7329 |
| total_steps | 3384 |
| train_runtime | 7956s (2h13m) |
| W&B | 无 |
| checkpoint | 完整 (adapter_model.safetensors 213MB, lora_alpha=32 confirmed) |

### Dose-response 对比

| dosage | train_loss | acc |
|---|---|---|
| d000 (0%) | 1.183 | 0.7287 |
| d005 (5%) | 1.185 | 0.7302 |
| d025 (25%) | 1.187 | 0.7527 |

**趋势**：train_loss 三个 dosage 几乎持平（1.183→1.187），差异 <0.004，符合 null finding 预期。mean_token_accuracy d025 略高于 d000/d005（+0.02），可能因为 25% contamination 数据中 benchmark items 格式更规律、更易拟合，但需要后续 eval 阶段在 held-out benchmark 上验证这是否转化为实际性能差异。

---

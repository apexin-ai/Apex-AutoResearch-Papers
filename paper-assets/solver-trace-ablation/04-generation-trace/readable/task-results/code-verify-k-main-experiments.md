# code verify K main experiments

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-K-main-experiments_20260516T031829_result.json`
- **Structured JSON:** [`891ce8ff0b853208f5f6.json`](../../sessions/89/891ce8ff0b853208f5f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

## K 值验证结果

**所有 config 文件统一配置 `num_generations: 8`**（代码默认值是 4，但 config 覆盖为 8）。

**prove_rate 粒度验证**（所有有 reward_log 的实验）：

| 实验 | prove_rate 粒度 | batch×K |
|------|----------------|---------|
| plan001_exec_only_s43_1000_r2 | 1/8 | 8 |
| plan001_exec_only_s44_1000_r2 | 1/8 | 8 |
| plan002_additive_b01_s42_1000 | 1/8 | 8 |
| plan002_additive_b01_s43_r2 | 1/8 | 8 |
| plan018_additive_random_b01_s42_1000 | 1/8 | 8 |
| plan018_additive_random_b01_s42_1000_r3 | 1/8 | 8 |
| plan018_additive_random_b01_s43_r3 | 1/8 | 8 |
| plan018_additive_random_b01_s44_r2 | 1/8 | 8 |
| exp1_isr_b03_s42_1000 | 1/8 | 8 |
| exp1_isr_b03_s44_r2 | 1/8 | 8 |
| exp1_random_b03_s43_r4 | 1/8 | 8 |
| exp1_random_b03_s44_r2 | 1/8 | 8 |

**没有 reward_log 的实验**：plan001_s42_r2、plan002_b01_s42、plan018_s42、所有 plan009 SFT（SFT 不用 GRPO，无 reward_log 正常）、exp1_isr_b03_s43、exp1_random_b03_s42/s43。

**粒度解释**：prove_rate = proved / step_buf["total"]，`step_buf["total"]` 在 TRL 1.1.0 中 = `per_device_train_batch_size(4) × gradient_accumulation_steps(2) = 8` 个样本/step = 1 个 prompt × K=8 生成。所有 prove_rate 值严格是 1/8 整数倍，零异常。

**结论：所有主实验 K=8，完全一致。** 论文报告 K=8 无误。

---

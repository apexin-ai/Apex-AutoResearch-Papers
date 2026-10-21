# diag rasp grpo checkpoint check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_rasp-grpo-checkpoint-check_20260515T223312_result.json`
- **Structured JSON:** [`e908492a82d27e0db335.json`](../../sessions/e9/e908492a82d27e0db335.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RASP GRPO Checkpoint Survey (westb)

| Version | Output Dir | 内容 | Checkpoints | 训练步数(推测) | Has Peak Checkpoint? |
|---------|-----------|------|-------------|---------------|---------------------|
| v2 | `grpo_stage2_rasp_20_v2` | completions (step 10-30) | **0** | ~30 steps | **NO** |
| v3 | `grpo_stage2_rasp_20_v3` | 空目录 | **0** | 未知 | **NO** |
| v4 | `grpo_stage2_rasp_20_v4` | completions (空) | **0** | 未知 | **NO** |
| v5 | `grpo_stage2_rasp_20_v5` | completions (step 10-90) | **0** | ~90 steps | **NO** |
| v6 | `grpo_stage2_rasp_20_v6` | completions (空) | **0** | 未知 | **NO** |
| v7 | `grpo_rasp_20_v7` | 空目录 | **0** | 未知 | **NO** |
| v7 | `grpo_stage2_rasp_20_v7` | 空目录 | **0** | 未知 | **NO** |
| v8 | `grpo_rasp_20_v8` | completions (step 10-20) | **0** | ~20-30 steps | **NO** |

**Standard GRPO v8**: `grpo_stage2_standard_20_v8/checkpoint-50` — 12GB, 完整 checkpoint，save_steps=50, max_steps=100, reward 在 step 40 达到 0.096 后 step 50 跌回 0.037。

### 结论

**RASP GRPO 全版本（v2-v8）没有任何 checkpoint 保存在磁盘上。**

原因：
- 所有版本 `save_steps` 默认 100-200，而 RASP GRPO 大多在 step 30 之前就 collapse/被 kill
- v5 跑到了 ~90 steps 但 save_steps 也是 100，差 10 步就能保存
- v8 `save_steps=50`，但在 step ~28-30 被 kill，未达到保存阈值
- 即使有 `save_total_limit`，从未触发过保存

**只有 completions parquet 文件留存，没有模型权重。** 这是论文核心对比的致命缺口——无法从 checkpoint 恢复 peak 性能模型。

**需要用 `save_steps=5` 重跑** 才能捕获 collapse 前 peak 附近的 checkpoint。

---

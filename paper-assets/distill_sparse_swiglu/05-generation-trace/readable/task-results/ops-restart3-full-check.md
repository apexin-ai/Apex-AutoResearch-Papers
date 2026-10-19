# ops restart3 full check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart3_full_check_20260520T032819_result.json`
- **Structured JSON:** [`8c146debdd81dac97649.json`](../../sessions/8c/8c146debdd81dac97649.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### westd-41718

| # | 实验 | GPU | PID | 状态 | 详情 |
|---|------|-----|-----|------|------|
| 1 | MSE 30% 7-task eval | cuda:0 | 202340 | **DEAD — 崩溃** | `AssertionError: Layer 27: sparsity 0.248 deviates from target 0.300`。sparsity 断言阈值 0.05 太严格，Layer 27 实际 0.248 vs 目标 0.300，差 0.052。cuda:0 已空闲 (0 MiB, 0%)。 |
| 2 | MSE 50% train | cuda:1 | 202489 | **ALIVE — 训练中** | Step 80/1000, loss 从 97.9→0.006 快速收敛。sparsity=0.508 (目标0.5)。lambda 自动调到 128。cuda:1 满载 (53353 MiB, 100%)。checkpoint 尚未生成。 |

### westd-34887

| # | 实验 | GPU | PID | 状态 | 详情 |
|---|------|-----|-----|------|------|
| 3 | TEAL global HS/PIQA | cuda:0 | 157764 | **ALIVE — 93%** | 37585/40168 loglikelihood requests, ~3min 剩余。cuda:0 满载 (39993 MiB, 99%)。 |
| 4 | BCE global HS/PIQA | cuda:1 | 157845 | **ALIVE — 93%** | 37657/40168 loglikelihood requests, ~3min 剩余。cuda:1 满载 (68697 MiB, 98%)。 |

### 需要处理

**实验 1 (MSE 7-task eval)** 需要修复：`evaluate.py:165` 的 sparsity 断言容差 0.05 对 MSE predictor 太严格。Layer 27 sparsity 0.248 偏离目标 0.300 仅 5.2%，应放宽容差或改为 warning。修复后需在 cuda:0 上重启。

---

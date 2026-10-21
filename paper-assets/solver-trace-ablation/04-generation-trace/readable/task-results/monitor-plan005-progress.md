# monitor plan005 progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_plan005_progress_20260513T235317_result.json`
- **Structured JSON:** [`a8b32f72a0b0771fb49c.json`](../../sessions/a8/a8b32f72a0b0771fb49c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan005-sta-low-s42 训练状态

| 项目 | 值 |
|------|-----|
| **进度** | **498/500 步** — 即将完成 |
| **进程** | PID 85790 存活，已运行 1h11m |
| **预计完成** | ~20 秒内（~8.5s/step） |
| **Checkpoints** | checkpoint-400, checkpoint-450 已保存 |

### 关键指标趋势

| 指标 | 初始 (step 1-5) | 最新 (step 494-498) | Baseline |
|------|-----------------|---------------------|----------|
| prove_rate | 0.125 - 0.375 | **0.75 - 1.0** | 0.12 |
| reward_mean | 0.12 - 0.37 | **0.70 - 0.91** | — |
| isr_mean | 0.10 - 0.28 | 0.09 - 0.28 | 0.064 |
| parse_rate | 1.0 | 1.0 | — |
| loss | 0.03 - 0.07 | -0.08 - 0.11 | — |

### 判断

- **训练正常**，无异常。prove_rate 从 baseline 0.12 大幅提升到 0.75-1.0。
- ISR 提升幅度不大（0.064 → 0.09-0.28 波动），符合 STA weight=0.1 低权重的预期。
- loss 偶有负值属于 GRPO 正常现象。
- 总耗时 ~71 分钟/500 步，与 plan001-r2（62 分钟）量级一致。

---

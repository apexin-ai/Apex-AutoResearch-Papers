# diag exp002 clipped ratio

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp002-clipped-ratio_20260518T174410_result.json`
- **Structured JSON:** [`5aaeabf7fd1d1c0913a5.json`](../../sessions/5a/5aaeabf7fd1d1c0913a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### exp-002 (`exp002_v2.log`)

`completions/clipped_ratio` 指标存在，共 10 个 step 的记录：

| 指标 | 值 |
|------|------|
| **mean** | **0.8031** |
| min | 0.7438 |
| max | 0.8500 |

逐 step 值：0.775, 0.775, 0.844, 0.744, 0.806, 0.775, 0.850, 0.819, 0.831, 0.813

### exp-003 (`exp003_v2.log`)

日志中 **没有 `clipped_ratio` 指标**。exp-003 使用的是自定义 `dcgrpo_trainer`，日志只记录 reward 相关指标（`reward/r3_mean`, `reward/combined_mean`），没有 completion length/truncation 统计。

### 结论

exp-002 的 clipped_ratio 均值 ~80%，与 exp-014 dry-run 的 84% 处于同一水平。**这是共同问题（max_completion_length=256 对当前任务普遍偏短），不是 exp-014 特有的。** 两个实验的截断率差异在正常波动范围内。

---

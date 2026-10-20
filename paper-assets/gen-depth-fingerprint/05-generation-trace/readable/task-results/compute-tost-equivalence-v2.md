# compute tost equivalence v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_tost-equivalence-v2_20260518T123445_result.json`
- **Structured JSON:** [`aadfd62a8ea01a788115.json`](../../sessions/aa/aadfd62a8ea01a788115.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都完成了。

---

## 任务 A: TOST 等价性检验结果

数据：`features_8gen.csv`，37058 行，gen-1: 7896，gen-2+: 21199，等价性边界 |d| < 0.10

| Feature | Group | d_obs | p_TOST | Equivalent? |
|---|---|---|---|---|
| entropy_min | near-stationary | -0.0157 | 8.18e-11 | **YES** |
| entropy_max | near-stationary | +0.0622 | 2.07e-03 | **YES** |
| tail_decay | near-stationary | +0.0873 | 1.68e-01 | NO |
| entropy_std | intermediate | +0.4571 | 1.00e+00 | NO |
| hapax_ratio | drifting | +0.7346 | 1.00e+00 | NO |
| ttr | drifting | +0.8142 | 1.00e+00 | NO |
| entropy_mean | drifting | +1.0544 | 1.00e+00 | NO |

**解读：**
- `entropy_min` 和 `entropy_max` 通过等价性检验（p < 0.05），确认其 gen-1 vs gen-2+ 差异在 |d| < 0.10 以内，是真正的 near-stationary。
- `tail_decay` 虽然 d=0.087 在边界附近，但 p=0.168 未通过（样本量不足以在此边界下确认等价）。
- drifting 特征（entropy_mean, ttr, hapax_ratio）的 d 值都远大于 0.10，符合预期。

JSON 已保存至 `/root/gen-depth-fingerprint/results/tost_equivalence.json`。

## 任务 B: tmux 清理

所有 tmux sessions 已清除，服务器上无残留 session。

---

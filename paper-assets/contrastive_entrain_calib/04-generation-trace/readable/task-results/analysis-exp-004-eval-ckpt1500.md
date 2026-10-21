# analysis exp 004 eval ckpt1500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-004-eval-ckpt1500_20260520T154443_result.json`
- **Structured JSON:** [`b08d6abccec97e297db6.json`](../../sessions/b0/b08d6abccec97e297db6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

### 真实 Metrics（已从 log + summary 双重确认）

| 指标 | 值 |
|------|-----|
| **ToF** | 0.0939 |
| **NoF** | 0.8895 |
| **SYCONScore** | **0.1699** |
| n_valid | 181 |
| n_invalid | 181 |
| n_total | 362 |
| eval_time | 1741s |

### 对比分析

- **vs vanilla baseline**: 0.1699 vs 0.1335 = **+27.3%** → conclusion = **success**
- **vs ckpt-1000** (0.2048): 低于 ckpt-1000，下降 17.0%
- **vs ckpt-2000** (0.2550): 低于 ckpt-2000，下降 33.4%

**注意**：ckpt-1500 的 SYCONScore 与 ckpt-500 (0.1699) 完全一致——这不是自动填充错误，而是真实评估结果。ACT 训练轨迹在 ckpt-500→1500 之间出现了平台期，随后在 ckpt-1000→2000 区间上升。

完整轨迹：500(0.1699) → **1000(0.2048)** → **1500(0.1699)** → 2000(0.2550) → 2500(0.2389) → 3000(0.2058)

这个非单调模式值得关注——ckpt-1500 是一个明显的 dip。

### Registry 更新

- metrics: 已更新（含完整 eval metadata）
- conclusion: success（已存在，未改动）
- checkpoint_path: 已更新
- log_path: 已更新

---

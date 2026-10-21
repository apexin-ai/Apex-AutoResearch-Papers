# analysis exp 034 dual critic cheetah

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_034_dual_critic_cheetah_20260521T121500_result.json`
- **Structured JSON:** [`7c09e7c1141b5fbbde81.json`](../../sessions/7c/7c09e7c1141b5fbbde81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_034 分析完成。

## 结果摘要

**结论：NEGATIVE** — dual-critic 未能预防 Cheetah Run 的 CIVO。

### 关键指标
| 指标 | 值 |
|------|-----|
| 最终 eval_return | **97.5**（baseline ~650-700，差距 85%）|
| 峰值 eval_return | 315.7（45K step，CIVO 前）|
| 最大 NVE | **1.753**（55K step，CIVO 触发）|
| CIVO 触发次数 | 2 次（55K: 1.75, 105K: 1.59）|
| v1 vs v2 最大差异 | 0.004（几乎无分化）|

### 核心发现

1. **CIVO 在 55K 和 105K 两次触发**（NVE > 1.5x），eval 从峰值 315.7 崩溃到 27.2
2. **双 critic 完全没有分化**（v1 ≈ v2 始终差异 < 0.005），min 算子等于无效
3. **与 Walker 形成鲜明对比**：Walker dual-critic 完全预防 CIVO（NVE ≤ 1.1, eval 787.7），Cheetah 失败
4. **推测原因**：Cheetah 的 value overestimation 来源于 world model 复合误差，而非 critic 自身的分歧——两个 critic 在相同的 imagined trajectories 上训练，自然收敛到相同的（高估的）值

### 产出
- 分析报告：`artifacts/exp_034/report/report_exp_034_analysis.md`
- Registry 已更新：exp_034 → DONE (negative)

---

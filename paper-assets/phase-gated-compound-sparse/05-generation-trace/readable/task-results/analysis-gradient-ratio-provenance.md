# analysis gradient ratio provenance

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient-ratio-provenance_20260514T072731_result.json`
- **Structured JSON:** [`6165ffbebec8ebb7518c.json`](../../sessions/61/6165ffbebec8ebb7518c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。核心发现：

**问题 1：** "47-104×" 由 Reviewer agent 用 `low_mean/high_mean` 计算（s015 因负值替换为 median ratio 69×），Director 直接采纳进 D028，未注明公式混用。

**问题 2：** s020=5.90 根因——Worker 2 存的是 `low_mean - high_mean`（**差值**），不是比值。同一字段名 `gradient_paired_aggregate` 在 s015/s025 存 median ratio，在 s020/s030 存 mean difference。

**问题 3：** s025=222.35 根因——使用 `low_median/high_median`，high_median=0.032 极小导致 ratio 膨胀。D028 的 85× 用的是 mean ratio（high_mean=0.303 大 10 倍）。

**问题 4 推荐：**
- **主指标**：segment median difference → 0.39, 1.48, 7.16, 14.59（单调、无除法、完全可复现）
- **补充**：Cohen's d → 0.60, 0.72, 0.95, 1.12（标准效应量，审稿人熟知）
- **弃用所有 ratio 指标**：high-phase II 中 29-49% 样本 < 0.01，ratio 本质不稳定

报告已注册为 artifact `gradient_ratio_provenance_report`。

---

# check mvp pilot 004 completion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mvp_pilot_004_completion_20260514T090432_result.json`
- **Structured JSON:** [`15de7814d9818dd7eec3.json`](../../sessions/15/15de7814d9818dd7eec3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_pilot_004 结果报告

**Verdict: FAIL**

---

### NER

| 指标 | 值 |
|------|-----|
| Greedy F1 | 0.6671 |
| Oracle F1 | 0.7756 |
| Headroom | +0.1085 |
| Fleiss κ mean | 0.4048 |
| Soft Jaccard mean | 0.7008 |
| Sample F1 mean/std | 0.6084 / 0.3174 |
| Sample F1=0 (%) | 12.19% |
| Gold-empty filtered | 22 |
| All-samples-F1=0 filtered | 21 |

| 相关性 | ρ | p-value | n |
|--------|------|---------|-----|
| Full ρ(κ,F1) | +0.2590 | 1.475e-09 | 529 |
| Full ρ(SJ,F1) | **+0.3825** | 7.075e-20 | 529 |
| Cond ρ(κ,F1) | +0.2352 | 8.162e-08 | 508 |
| Cond ρ(SJ,F1) | **+0.3762** | 1.602e-18 | 508 |

- SJ > κ (full): **YES** (delta=+0.1235)
- SJ > κ (cond): **YES** (delta=+0.1410)

---

### RE

| 指标 | 值 |
|------|-----|
| Greedy F1 | 0.4208 |
| Oracle F1 | 0.5882 |
| Headroom | +0.1674 |
| Fleiss κ mean | 0.2996 |
| Soft Jaccard mean | 0.6114 |
| Sample F1 mean/std | 0.3612 / 0.3830 |
| Sample F1=0 (%) | **44.30%** |
| Gold-empty filtered | 154 |
| All-samples-F1=0 filtered | 84 |

| 相关性 | ρ | p-value | n |
|--------|------|---------|-----|
| Full ρ(κ,F1) | +0.2782 | 1.724e-08 | 397 |
| Full ρ(SJ,F1) | +0.2441 | 8.550e-07 | 397 |
| Cond ρ(κ,F1) | +0.3067 | 3.052e-08 | 313 |
| Cond ρ(SJ,F1) | +0.3161 | 1.080e-08 | 313 |

- SJ > κ (full): **NO** (delta=-0.0341)
- SJ > κ (cond): YES (delta=+0.0094, 几乎无差异)

---

### 失败原因分析

1. **RE full ρ(SJ,F1) = 0.2441，远低于 0.40 阈值**——Gate 1 关键条件未通过
2. **RE 中 SJ 未胜过 κ（full）**——κ 反而更高（0.2782 vs 0.2441）
3. **RE 44.3% 样本 F1=0**——极高的零分比例严重稀释相关性信号
4. RE conditional 下 SJ 仅微弱胜出 κ（+0.0094），无实际意义

NER 方面结果积极（SJ 一致性优势明显），但 RE 拖累了整体 verdict。核心问题是 RE 质量仍太低——近半数实例的采样结果全为零分。

Registry 已更新为 ANALYZING，cron 已删除。

---

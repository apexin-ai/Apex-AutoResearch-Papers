# analysis d120 recalc 17855 alpha sweep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d120_recalc_17855_alpha_sweep_20260520T054131_result.json`
- **Structured JSON:** [`5753e8764ff0f19687dd.json`](../../sessions/57/5753e8764ff0f19687dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D120 alpha_sweep 全量重算完成。

**执行结果**：22 个 fp32 目录，17 个成功，5 个因代数不足跳过。

**核心发现**：

| α 区间 | thresh_onset | PermG_fwd | K≥3 |
|--------|-------------|-----------|-----|
| 0.05–0.45 | **0/8**（全灭） | 0/8（除 a010_s43: 3/8） | 0-4/8 |
| 0.50 | **0-6/8**（seed 不稳定） | 6/8（4个 seed 一致） | 1-5/8 |
| 0.60–0.75 | **0/8**（全灭） | 0-6/8 | 0-6/8 |

**D105 true 3σ 的 threshold_onset 极其保守**——22 个实验中仅 a010_s43（2/8）、a050_s42（4/8）、a050_s43（6/8）有显著性。downstream 指标在多数实验中无法突破 full-series std 的 3σ 阈值。K≥3 共识在 α≥0.50 主要由 PermG + diff_xcorr + naive_xcorr 三法驱动，threshold_onset 和 TY 几乎不贡献。

报告已注册：`artifacts/d120_alpha_sweep_recalc/report.md`

---

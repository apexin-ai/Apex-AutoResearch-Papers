# analysis alpha sweep a030 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a030_s42_fp32_20260519T203048_result.json`
- **Structured JSON:** [`277b4d7a8da4b5f9a274.json`](../../sessions/27/277b4d7a8da4b5f9a274.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

**α=0.30 确认在 blind zone，PermG=0/8。**

| 指标 | 值 |
|------|-----|
| PermG fwd | **0/8** |
| PermG rev | 0/8 |
| K≥3 | 6/8 |
| K≥4 | 3/8 |
| naive_xcorr | 8/8 |
| diff_xcorr | 4/8 |
| threshold_onset | 8/8 |

尽管 drift 显著（entropy -17%，d1/d2/d3 -37~50%，mauve -26%），PermG 在 T=11 下无法检测。PermG raw p-values 范围 0.053–0.128，全部 BH FDR 不显著。

TY Granger 5/8 显著但 4/5 有 d_max=2, df_resid=1（per C003 不可用作证据）。

**Onset boundary 更新**：α=0.25/0.30/0.35/0.40 均 PermG=0/8，α=0.50 PermG=6/8 → onset ∈ (0.40, 0.50]。

Registry 已更新为 DONE/success，报告已注册。

---

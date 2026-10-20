# analysis c4 a075 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_a075_s42_fp32_20260519T182301_result.json`
- **Structured JSON:** [`cd2f06fff7ac74ecff86.json`](../../sessions/cd/cd2f06fff7ac74ecff86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**c4_a075_s42_fp32 — SUCCESS**

| 指标 | 结果 |
|------|------|
| PermG_fwd | **8/8** (parent WikiText: 6/8, ↑2) |
| PermG_rev | 0/8 (完美非对称) |
| K≥4 (3σ) | **8/8** (parent: 6/8, ↑2) |
| K≥3 (3σ) | 8/8 |
| threshold_onset (3σ) | 8/8 |
| naive_xcorr | 8/8 |
| diff_xcorr | 8/8 |
| TY_granger | 6/8 (distinct_1 pairs miss, d_max=1 df_resid=4) |

关键 drift: entropy -35.32%, ece +2809%, ppl +2152%, mauve -42.26%

C4 跨域验证比 WikiText parent 信号更强。Registry 已更新为 DONE/success，报告已注册。

---

# analysis a060 v4 d120 canonical

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a060_v4_d120_canonical_20260520T115048_result.json`
- **Structured JSON:** [`7e84d8e3a7c853a34994.json`](../../sessions/7e/7e84d8e3a7c853a34994.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D120 分析完成。

**alpha_sweep_a060_s42_fp32_v4 → negative**

| Method | Fwd | Rev |
|--------|-----|-----|
| PermG (FDR) | 0/8 | 0/8 |
| TY Granger | 0/8 | — |
| diff_xcorr (FDR) | 6/8 | 6/8 |
| naive_xcorr | 2/8 | — |
| threshold_onset_3sigma | 0/8 | — |
| **K≥3** | **0/8** | |
| **K≥4** | **0/8** | |

Registry 已更新至 DONE(negative)，报告已注册。α=0.60 T=10 的 non-monotonic sync dip 确认——PermG 全军覆没，仅 diff_xcorr 有单方法信号（6/8），不足以形成共识。可作为 T=20 对比基线。

---

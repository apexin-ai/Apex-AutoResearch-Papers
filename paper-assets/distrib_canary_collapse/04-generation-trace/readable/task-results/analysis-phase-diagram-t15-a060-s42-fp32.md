# analysis phase diagram t15 a060 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase_diagram_t15_a060_s42_fp32_20260521T183727_result.json`
- **Structured JSON:** [`26e1b59dd31e4947d8b4.json`](../../sessions/26/26e1b59dd31e4947d8b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## T=15 α=0.60 s42 fp32 — Sync-Dip 持续确认

| 指标 | 值 |
|------|-----|
| **PermG_fwd** | **0/8** |
| PermG_rev | 0/8 |
| diff_xcorr_fdr_fwd | 6/8 |
| threshold_onset_3sigma | 4/8 |
| TY_granger | 4/8 |
| robust_pairs (≥3/5) | 3/8 |

**漂移**：token_entropy -25.5%, ece +1582%, distinct_2 -39.8%, mauve -12.5%

**关键结论**：α=0.60 的 sync-dip 从 T=10 贯穿到 T=15 再到 T=20，是连续现象而非边界效应。尽管 α=0.60 远超 α_c(15)≈0.304，collapse 确实在发生（distinct_2 跌了 40%），但指标同步移动导致 PermG 无法建立时间先后关系。其他方法（diff_xcorr 6/8, threshold 4/8, TY 4/8）仍能检测到退化信号。

Artifact 已注册，registry 已更新为 DONE/success。

---

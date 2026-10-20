# analysis tost equivalence

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost_equivalence_20260515T050401_result.json`
- **Structured JSON:** [`51fef24ce41f67cef9c8.json`](../../sessions/51/51fef24ce41f67cef9c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `tost_equivalence.json`。

### 解读

**NER (n=529):**
- **δ=0.02 (严格)**: SJ 和 LP 确认等价——差异确实 <2%
- **δ=0.03**: SJ, EM, LP, VC 四个信号确认等价；FK 的 mean_Δ=-0.018 偏大，未通过
- **δ=0.05 (宽松)**: 全部 5 个信号确认等价

**RE (n=397):**
- RE 的 per-instance 方差更大（std~0.23-0.25 vs NER 的 0.16-0.22），等价更难确认
- **δ=0.02**: 没有信号能确认等价
- **δ=0.03**: 仅 LP (mean_Δ=-0.009) 确认等价
- **δ=0.05**: SJ, FK, LP 确认等价；EM (mean_Δ=-0.032) 和 VC (mean_Δ=-0.045) 未通过——VC 实际上在 RE 上有系统性负向偏移，不仅"不优于 greedy"，反而有害

**论文可用的 claim**: 在 δ=0.05 的等价边界下，NER 所有 5 个信号的 selection F1 与 greedy F1 统计等价（TOST p<0.05）；在 δ=0.03 下 NER 有 4/5 信号等价。RE 上 LP 是最稳健的信号（δ=0.03 即确认等价），但 EM 和 VC 在 RE 上系统性低于 greedy，即使 δ=0.05 也无法确认等价。

---

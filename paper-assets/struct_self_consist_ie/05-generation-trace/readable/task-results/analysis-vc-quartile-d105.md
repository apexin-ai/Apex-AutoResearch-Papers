# analysis vc quartile d105

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vc_quartile_d105_20260516T045336_result.json`
- **Structured JSON:** [`2dc08769a6300d1e9057.json`](../../sessions/2d/2dc08769a6300d1e9057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。产出：
- `artifacts/vc_quartile_analysis/results.json` — 完整数值结果
- `artifacts/vc_quartile_analysis/report.md` — 可读报告

**核心结论：VC 分层不能解决 LP 压缩问题。**

- **SciERC NER Q4** (mean VC=0.92): LP delta = **-0.004**，无恢复
- **SciERC RE Q4** (mean VC=0.89): LP delta = **+0.040**，唯一正向信号，LP 捕获了 28% 的 oracle headroom
- **CoNLL NER Q3/Q4** (VC=1.0): 退化情况，50% 实例所有 sample 完全一致，无选择空间
- LP delta 在 NER 上跨 quartile 非单调（+0.016, -0.006, +0.020, -0.004），与 VC 无系统性关系
- 所有信号（SJ/FK/EM）在多数 quartile 也表现为 delta ≤ 0，与 LP 一致

---

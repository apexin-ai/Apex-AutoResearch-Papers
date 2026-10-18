# analysis r1 statistical supplements

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r1_statistical_supplements_20260521T155122_result.json`
- **Structured JSON:** [`7c30e304427a4a63852d.json`](../../sessions/7c/7c30e304427a4a63852d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项分析完成。结果摘要：

### N3.2 Partial Correlation
- **FewRel** (N=204): zero-order r=−0.570 → partial r=**−0.537** (p<.0001), VIF=1.18。BCS 与 degree centrality 相关性仅 0.39，partial correlation 几乎不变，BCS 效应独立于 degree centrality。
- **DocRED** (N=110): zero-order r=−0.760 → partial r=**−0.348** (p=.0002), VIF=50.9。BCS 与 degree centrality 近共线 (r=0.99)，但 partial r 仍高度显著。

### W2 DocRED Range-Matched MDE
- MDE at 80% power = **5.47pp**，observed interaction = 0.93pp，power = 7.6%
- 样本不足以区分 true null 与 small (<5.5pp) interaction

### W3 NER Null Power
- Few-NERD BCS SD = 0.027，仅为 FewRel 的 **19.4%**
- FewRel 的 r=−0.570 在 NERD 的 BCS range 下衰减至 r=−0.111，低于 min detectable r = 0.132
- Power at attenuated effect = 65.1%
- 结论：NER BCS-null 归因于 BCS variance 不足，而非 BCS-accuracy 关系不存在

输出文件：
- `artifacts/r1_statistical_supplements.json`
- `artifacts/r1_statistical_supplements.md`

---

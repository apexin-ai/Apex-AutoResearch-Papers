# analysis data strategy ablation s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_data_strategy_ablation_s43_20260520T092916_result.json`
- **Structured JSON:** [`eb7644d52b032e0c6a2f.json`](../../sessions/eb/eb7644d52b032e0c6a2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**s43 accumulate 完全复现 s42 结果**：
- PermG FDR = **0/8**，K>=3 = **0/8**（replace 基线 6/8）
- entropy drift 仅 -2.83%（replace: -15.81%），ece drift +67.8%（replace: +679.56%）
- distinct_1 drift -28.4% 与 replace (-29%) 几乎一致 — 多样性退化仍发生，但 canary 信号被稀释导致 lead-lag 不可检测
- 两个种子一致，accumulate 对 lead-lag 的抑制效应是 **seed-robust** 的

报告已注册：`art_20260520_737e7d`

---

# analysis benchmark statistics

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_benchmark-statistics_20260520T041506_result.json`
- **Structured JSON:** [`df9e1a09c94748620d29.json`](../../sessions/df/df9e1a09c94748620d29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

统计分析已写入 memory.md「全 Benchmark 统计摘要」段。核心结论：

| Benchmark | Δ (pp) | p-value | 判定 |
|-----------|--------|---------|------|
| **Object** | +6.9 | <0.001 | Strong |
| **Spatial** | +4.2 | <0.001 | Moderate |
| **Long (OOD)** | +3.4 | 0.016 | Moderate |
| **Goal (OOD)** | -1.4 | 0.579 | Neutral |

方法排序：CRM norm01 > norm02 K=10 > norm02 K=5 > Adaptive-K > Argmin ≈ VLA-only。分析脚本保存在 `artifacts/statistical_analysis.py`。

---

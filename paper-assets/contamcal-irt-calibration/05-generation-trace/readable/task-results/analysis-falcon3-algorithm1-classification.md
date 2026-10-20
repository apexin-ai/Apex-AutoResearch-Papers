# analysis falcon3 algorithm1 classification

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_falcon3-algorithm1-classification_20260522T131404_result.json`
- **Structured JSON:** [`955b651bae638854c603.json`](../../sessions/95/955b651bae638854c603.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分类结果：

| Benchmark | Pattern | Δ(d100−d000) | Confidence |
|-----------|---------|--------------|------------|
| **MMLU 5-shot** | **Benefit** | +4.19 pp | 1.000 |
| **ARC 25-shot** | **Benefit-sat** | +4.01 pp | 0.601 |

**MMLU**: 单调递增，无饱和，全 7 家族中正向 delta 最大（超过 Gemma-2 的 +3.76pp）。

**ARC**: 正向但饱和——前半段增益 +3.24pp，后半段仅 +0.77pp（ratio=0.238 < 0.3 阈值）。中间 d025→d050 有 −1.53pp 回落，但非 V-recovery（整体 delta 仍为正）。

**跨家族定位**: Falcon3 归入 Benefit 聚类（与 Gemma-2 并列），区别于 Benefit-sat 组（OLMo-2、LLaMA-3.1）和负向组（Qwen-14B U-collapse、Qwen-7B V-recovery）。

产出已注册: `artifacts/falcon3_algorithm1_classification.md`

---

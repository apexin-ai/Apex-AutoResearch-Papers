# analysis exp007 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp007_bootstrap_ci_20260513T033359_result.json`
- **Structured JSON:** [`1977391a1442df5fdd92.json`](../../sessions/19/1977391a1442df5fdd92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### Bootstrap 95% CI + Permutation Test

| Experiment | Pair | AUC | 95% CI | p-value |
|---|---|---|---|---|
| **Qwen rewrite** | 0v1 | 0.9956 | [0.9946, 0.9965] | <0.002 |
| | 1v2 | 0.6955 | [0.6859, 0.7041] | <0.002 |
| | 2v3 | 0.5893 | [0.5795, 0.5991] | <0.002 |
| | 3v4 | 0.5435 | [0.5333, 0.5551] | <0.002 |
| | 4v5 | 0.5340 | [0.5238, 0.5448] | <0.002 |
| **Pythia** | 0v1 | 0.9932 | [0.9921, 0.9943] | <0.002 |
| | 1v2 | 0.6539 | [0.6454, 0.6630] | <0.002 |
| | 2v3 | 0.5514 | [0.5417, 0.5628] | <0.002 |
| | 3v4 | 0.5152 | [0.5041, 0.5260] | 0.006 |
| | 4v5 | 0.5136 | [0.5021, 0.5249] | 0.008 |
| **OLMo** | 0v1 | 0.9970 | [0.9964, 0.9975] | <0.002 |
| | 1v2 | 0.6145 | [0.6045, 0.6247] | <0.002 |
| | 2v3 | 0.5496 | [0.5399, 0.5596] | <0.002 |
| | 3v4 | 0.5091 | [0.4973, 0.5200] | 0.064 |
| | 4v5 | 0.5045 | [0.4932, 0.5150] | 0.232 |

### 关键检查

**OLMo 1v2 CI lower = 0.6045 > 0.60 — K\* claim ROBUST。** CI 完全在 0.60 阈值之上。

方法：复用原始 pipeline 的 GroupKFold(5) + LGBMClassifier 计算 OOF predictions，然后对 OOF predictions 做 doc_id 级 bootstrap resampling（1000x）和 label permutation test（500x）。所有 AUC 值与 registry metrics 吻合。

额外发现：
- OLMo 3v4 (p=0.064) 和 4v5 (p=0.232) 不显著，CI 跨 0.5 — 确认 depth 3+ 已饱和
- Pythia 3v4/4v5 虽然 p<0.01，但 CI 非常窄地高于 0.5，实际效应可忽略
- 所有 CI 宽度约 0.02，统计精度足够

---

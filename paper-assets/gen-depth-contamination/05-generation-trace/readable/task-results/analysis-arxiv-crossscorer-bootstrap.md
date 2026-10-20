# analysis arXiv crossscorer bootstrap

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_arXiv_crossscorer_bootstrap_20260518T034111_result.json`
- **Structured JSON:** [`8eb7167a16c7296af1fb.json`](../../sessions/8e/8eb7167a16c7296af1fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。核心结论：

**2v3 pair 关键结果（theta=0.60）：**

| Generator | AUC | 95% CI | K* (CI-based) |
|-----------|-----|--------|---------------|
| Qwen-7B | 0.5986 | [0.5835, **0.6133**] | 2 (CI upper > 0.60, lower < 0.60) |
| Qwen-1.5B | 0.6316 | [**0.6165**, 0.6464] | **3** (CI lower > 0.60) |
| LLaMA-8B | 0.6202 | [**0.6054**, 0.6355] | **3** (CI lower > 0.60) |
| Mistral-7B | 0.6075 | [0.5930, **0.6220**] | 2 (CI upper > 0.60, lower < 0.60) |

- Qwen-7B: CI 横跨阈值，57% bootstrap samples 落在 theta 以下，K* 保守取 2
- Qwen-1.5B / LLaMA-8B: CI lower 都 > 0.60，K*=3 有统计支撑
- Mistral-7B: CI 也横跨阈值（p(AUC<=0.60)=15.6%），K* 保守取 2
- 所有 permutation tests 均 p < 0.001，确认真实可分性

---

# analysis arXiv crossscorer full results

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_arXiv_crossscorer_full_results_20260518T030420_result.json`
- **Structured JSON:** [`edd2dfd75524957e8588.json`](../../sessions/ed/edd2dfd75524957e8588.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/arXiv_crossscorer_summary/full_results.md`。

核心发现：
- **Qwen-7B K\*=2**，其余三个模型 K\*=3（Qwen-7B 的 2v3 AUC=0.5989 刚好低于 0.60 阈值）
- 所有模型 0v1 AUC 在 0.96-0.98，1v2 在 0.81-0.84，到 3v4 已接近随机（0.52-0.55）
- LLaMA-8B 的 1v2 AUC 最高（0.8433），Qwen-1.5B 的 2v3 AUC 最高（0.6317）
- Top feature importance 跨模型高度一致：freq_entropy 稳居第一，surp_std、surp_d1_skew 紧随其后
- 结果文件中没有 bootstrap CI，只有 5-fold CV 的 per-fold 值和 population std

---

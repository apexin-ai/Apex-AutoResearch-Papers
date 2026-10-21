# ssh collect pythia topk50 results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_pythia_topk50_results_20260514T201806_result.json`
- **Structured JSON:** [`d379ed6ab6da2163e29a.json`](../../sessions/d3/d379ed6ab6da2163e29a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册。核心结论：

## Pythia Top-k k=50 结果总结

| 指标 | Top-k k=50 | Baseline (Nucleus) | Δ |
|------|-----------|-------------------|---|
| 4-class RF acc | **69.63%** | 78.2% | **-8.57pp** |
| AUC d1v2 | 0.7518 | 0.8607 | -0.1089 |
| AUC d2v3 | 0.6918 | 0.8005 | -0.1087 |
| 3-class acc | 59.20% | — | — |
| 3-class filtered acc | 61.33% | — | — |

**结论: Partial Success (weaker signal)**

Top-k k=50 是目前所有 5 个完成 cell 中表现最差的。深度信号仍可检测（远高于 chance），但显著弱于 nucleus 和 temp09。核心原因是 top-k 截断概率分布尾部，限制输出多样性，使递归生成文本更快趋于同质化，d2 vs d3 AUC 仅 0.6918。

Feature importance 排序稳定（var_surprisal、p90_ppl、mean_ppl），code contamination 模式一致。Filtered 结果略优于 unfiltered，确认 contamination 引入噪声。

3×3 矩阵 5/9 完成，GPT-2 XL temp09 正在运行中。

---

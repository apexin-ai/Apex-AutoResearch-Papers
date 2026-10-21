# analysis bonferroni alpha check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bonferroni-alpha-check_20260522T172835_result.json`
- **Structured JSON:** [`86627a7b5a70cbfa1619.json`](../../sessions/86/86627a7b5a70cbfa1619.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## Llama-3.1-8B-Instruct (n=136)

| 文件 | Layer | Position | Probe Acc | Alpha 数量 | Alphas |
|------|-------|----------|-----------|-----------|--------|
| `steering_results_L13_last.json` | 13 | last | 0.761 | **10** | [-20, -10, -5, -2, -1, 1, 2, 5, 10, 20] |
| `steering_results_L13_all.json` | 13 | all | 0.761 | **6** | [-20, -10, -5, 5, 10, 20] |
| `steering_results_L18_last.json` | 18 | last | 0.739 | **10** | [-20, -10, -5, -2, -1, 1, 2, 5, 10, 20] |
| `steering_results_L28_all.json` | 28 | all | 0.776 | **6** | [-20, -10, -5, 5, 10, 20] |
| `steering_results.json` | 28 | last | 0.776 | **10** | [-20, -10, -5, -2, -1, 1, 2, 5, 10, 20] |

## Gemma-2-9B-IT (n=158)

| 文件 | Layer | Position | Probe Acc | Alpha 数量 | Alphas |
|------|-------|----------|-----------|-----------|--------|
| `steering_results_gemma_L17.json` | 17 | last | 0.753 | **6** | [-20, -10, -5, 5, 10, 20] |
| `steering_results_gemma_L21.json` | 21 | last | 0.763 | **6** | [-20, -10, -5, 5, 10, 20] |

规律：`position=last` 的实验用了完整 10 个 alpha（含 ±1, ±2），`position=all` 和 Gemma 实验只用了 6 个（跳过了小 alpha）。

---

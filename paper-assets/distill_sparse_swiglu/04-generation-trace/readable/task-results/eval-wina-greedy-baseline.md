# eval wina greedy baseline

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_wina_greedy_baseline_20260515T185653_result.json`
- **Structured JSON:** [`36108450e6441f432e6e.json`](../../sessions/36/36108450e6441f432e6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总 training-free baselines 全景：

| Method | Strategy | PPL (50% sparsity) |
|--------|----------|-------------------|
| Dense | — | 6.12 |
| **WINA greedy** | **per-layer allocation** | **2,126** |
| TEAL greedy | per-layer allocation | 50,035 |
| Vanilla TEAL | global top-K | 66,036 |
| R-Sparse | global top-K | 74,929 |
| WINA (global) | global top-K | 82,567 |

WINA greedy 是表现最好的 training-free baseline（PPL 2126），比 global top-K 变体好 1-2 个数量级，这得益于贪心分配将 sparsity 预算集中在早期层（低 error 层 90% 剪枝）、保留后期层完整。但仍是 Dense PPL 的 347 倍，确认 **training-free 方法在 50% SwiGLU sparsity 下全面失败**，Claim 1 无懈可击。

---

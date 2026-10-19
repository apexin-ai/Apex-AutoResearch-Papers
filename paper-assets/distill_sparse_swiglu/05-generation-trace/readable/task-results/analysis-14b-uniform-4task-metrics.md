# analysis 14b uniform 4task metrics

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_14b_uniform_4task_metrics_20260518T015654_result.json`
- **Structured JSON:** [`0850b0158a65c04cf45d.json`](../../sessions/08/0850b0158a65c04cf45d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已更新为 DONE。

**结果汇总：**

| Metric | KL+uniform | TEAL+uniform | 对比：KL global_topk | 对比：TEAL global_topk |
|--------|-----------|-------------|---------------------|----------------------|
| WikiText-2 PPL | **7.63** | 8.01 | 7.62 | 8.76 |
| ARC-C | 54.44% | 55.29% | — | — |
| WinoGrande | 72.45% | 69.85% | — | — |
| MMLU | 64.49% | 66.34% | 63.72% | 71.83% |

**关键发现：**
- **KL+uniform MMLU = 64.49%**，仅比 global_topk (63.72%) 提高 0.77pp，远低于 70% 阈值 → **negative**，确认 MMLU gap 是 KL objective 固有的，与 allocation 策略无关
- **TEAL+uniform MMLU = 66.34%**，比 TEAL global_topk (71.83%) 下降 5.49pp → uniform allocation 对 TEAL 反而有害，说明 TEAL 的 global_topk 分配本身是有效的
- PPL 方面两种 allocation 差异很小（KL: 7.63 vs 7.62, TEAL: 8.01 vs 8.76），PPL 对 allocation 不敏感

---

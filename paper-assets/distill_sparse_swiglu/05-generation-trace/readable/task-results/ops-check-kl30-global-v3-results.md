# ops check kl30 global v3 results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-kl30-global-v3-results_20260518T230950_result.json`
- **Structured JSON:** [`b8dc6bec6d60534d9b7d.json`](../../sessions/b8/b8dc6bec6d60534d9b7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，结果如下：

## Global Eval 结果 (TEAL global_topk, 30% sparsity, LLaMA-3.1-8B)

| Metric | s123 | s456 |
|---|---|---|
| **WikiText-2 PPL** | 8.9748 | **8.9332** |
| **ARC-C (acc_norm)** | 0.4531 | **0.4633** |
| **WinoGrande** | 0.6930 | **0.7111** |
| **MMLU** | 0.3807 | **0.4382** |
| **GSM8K** | 0.0758 | 0.0758 |

s456 在所有指标上优于或持平 s123，MMLU 差异最大（+5.75pp）。

**GPU 状态**: 两块 GPU 均空闲（0% utilization, 0 MiB used）。

**HellaSwag/PIQA 支持**: `benchmark_eval.py` 已包含 `hellaswag` (10-shot) 和 `piqa` (0-shot) 配置，可直接使用。

---

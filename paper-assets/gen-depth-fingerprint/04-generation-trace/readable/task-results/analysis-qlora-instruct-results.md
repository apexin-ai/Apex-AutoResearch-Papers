# analysis qlora instruct results

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qlora_instruct_results_20260519T094959_result.json`
- **Structured JSON:** [`8d41c096f248cace3558.json`](../../sessions/8d/8d41c096f248cace3558.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部完成。汇总如下：

## OLMo-2-0425-1B-Instruct (instruct)
| Metric | Value |
|---|---|
| macro_f1_5class | **0.5976** ± 0.0046 |
| macro_f1_3class | **0.8881** ± 0.0071 |
| binary_f1 (gen1 vs gen2+) | **0.8363** ± 0.0096 |
| per_class_5class | d0=0.990, d1=0.766, d2=0.433, d3=0.343, d4=0.455 |
| n_samples | 4429 |
| runtime | 1689.7s |

## OLMo-2-1B (base)
| Metric | Value |
|---|---|
| macro_f1_5class | **0.5398** ± 0.0150 |
| macro_f1_3class | **0.8588** ± 0.0036 |
| binary_f1 (gen1 vs gen2+) | **0.7925** ± 0.0097 |
| per_class_5class | d0=0.992, d1=0.700, d2=0.366, d3=0.222, d4=0.419 |
| n_samples | 2379 |
| runtime | 911.7s |

## Qwen3-1.7B-Instruct (instruct)
| Metric | Value |
|---|---|
| macro_f1_5class | **0.5514** ± 0.0031 |
| macro_f1_3class | **0.9066** ± 0.0082 |
| binary_f1 (gen1 vs gen2+) | **0.8672** ± 0.0137 |
| per_class_5class | d0=0.986, d1=0.800, d2=0.408, d3=0.155, d4=0.408 |
| n_samples | 4963 |
| runtime | 1880.5s |

## Qwen3-1.7B (base)
| Metric | Value |
|---|---|
| macro_f1_5class | **0.5544** ± 0.0068 |
| macro_f1_3class | **0.9040** ± 0.0094 |
| binary_f1 (gen1 vs gen2+) | **0.8597** ± 0.0123 |
| per_class_5class | d0=0.995, d1=0.798, d2=0.354, d3=0.271, d4=0.354 |
| n_samples | 2291 |
| runtime | 880.9s |

所有 4 个 JSON 完整内容已在上方工具输出中返回，无截断。

---

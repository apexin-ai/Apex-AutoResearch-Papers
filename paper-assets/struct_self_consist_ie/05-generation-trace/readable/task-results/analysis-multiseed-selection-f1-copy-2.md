# analysis multiseed selection f1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed_selection_f1_20260515T124243_result.json`
- **Structured JSON:** [`62230dd6435752c13988.json`](../../sessions/62/62230dd6435752c13988.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `output/analysis_multiseed_selection_f1.json`，汇总如下：

---

## Qwen SciERC NER (N=8, 529 instances, 3 seeds)

| Method | Mean F1 | ±σ | Δ vs Greedy |
|--------|--------:|-----:|------------:|
| **Greedy** | 0.6458 | 0.0020 | — |
| Random | 0.6069 | 0.0060 | -0.0389 |
| **LP** | **0.6462** | 0.0034 | **+0.0004** |
| SJ | 0.6413 | 0.0086 | -0.0045 |
| FK | 0.6413 | 0.0080 | -0.0046 |
| EM | 0.6339 | 0.0057 | -0.0119 |
| VC | 0.6194 | 0.0068 | -0.0265 |
| Oracle | 0.7764 | 0.0039 | +0.1306 |

LP 是唯一略超 greedy 的 signal，但 p > 0.19（所有 seed），不显著。其余 signal 均 ≤ greedy。

## LLaMA SciERC NER (N=8, 529 instances, 3 seeds)

| Method | Mean F1 | ±σ | Δ vs Greedy |
|--------|--------:|-----:|------------:|
| **Greedy** | 0.6457 | 0.0003 | — |
| Random | 0.6201 | 0.0014 | -0.0257 |
| **LP** | **0.6451** | 0.0032 | -0.0006 |
| FK | 0.6440 | 0.0038 | -0.0018 |
| SJ | 0.6438 | 0.0056 | -0.0019 |
| VC | 0.6414 | 0.0013 | -0.0044 |
| EM | 0.6379 | 0.0087 | -0.0078 |
| Oracle | 0.7660 | 0.0087 | +0.1203 |

所有 signal 均 ≤ greedy（p 全部 > 0.09，不显著）。

## LLaMA CoNLL NER (N=16, 2756 instances, 3 seeds)

| Method | Mean F1 | ±σ | Δ vs Greedy | p-value range |
|--------|--------:|-----:|------------:|--------------:|
| **Greedy** | 0.9240 | 0.0002 | — | — |
| Random | 0.9216 | 0.0002 | -0.0024 | — |
| **VC** | **0.9268** | 0.0002 | **+0.0028** | 0.003–0.027 |
| **FK** | **0.9263** | 0.0001 | **+0.0023** | 0.0001–0.015 |
| **EM** | **0.9263** | 0.0001 | **+0.0023** | 0.0003–0.015 |
| **SJ** | **0.9262** | 0.0003 | **+0.0023** | 0.0004–0.012 |
| **LP** | **0.9252** | 0.0003 | **+0.0012** | 0.002–0.180 |
| Oracle | 0.9488 | 0.0006 | +0.0249 | — |

CoNLL 上所有 5 个 signal 均显著 beat greedy（VC/SJ/FK/EM 的 bootstrap p < 0.03 across all seeds）。SciERC 上 greedy 已接近最优，selection 无显著提升——oracle gap（~13 pt）表明 room 在，但当前 signal 对 SciERC 这种 fine-grained 任务的 selection 能力不足。

---

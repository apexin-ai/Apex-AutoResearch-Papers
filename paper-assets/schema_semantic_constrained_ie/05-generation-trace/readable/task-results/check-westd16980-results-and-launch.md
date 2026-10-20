# check westd16980 results and launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd16980-results-and-launch_20260522T180006_result.json`
- **Structured JSON:** [`87b7ca0e6a8ee9a63f91.json`](../../sessions/87/87b7ca0e6a8ee9a63f91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 已完成实验结果

**1. eval_70b_lora_scierc_beam4_s1** → **success**

| 指标 | 值 |
|------|-----|
| R-F1 | 44.81 (P=39.45, R=51.85) |
| E-F1 | 64.89 (P=62.29, R=67.72) |
| DR | 0% |
| RV | 0% |
| ET | 0% |
| CF | 1 |
| Parse fail | 0% |

对比 greedy S1 (R-F1=44.53): beam4 提升 +0.28pp，DR 保持 0%。

**2. entity_order_ablation_qwen_scierc** → **negative** (不是 order-invariant)

| 指标 | Shuffled | Original | Delta |
|------|----------|----------|-------|
| R-F1 | 43.77 | ~47.15 | **-3.38pp** |
| E-F1 | 67.05 | — | — |
| DR | 0% | ~0.09% | — |
| CF | 21 | ~0 | +21 |

R-F1 下降 3.38pp 远超 0.5pp 阈值，CF violations 从 ~0 增到 21。实体类型顺序对 constrained decoding 有显著影响。

### 新实验启动状态

| 实验 | GPU | PID | 显存占用 | 状态 |
|------|-----|-----|----------|------|
| eval_70b_lora_scierc_semantic_only | cuda:0 | 971668 | ~40GB/98GB | RUNNING, 推理中 |
| eval_70b_lora_scierc_full_s2 | cuda:1 | 972139 | ~40GB/98GB | RUNNING, 推理中 |

---

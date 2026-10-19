# ops gpu check and submit teal

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-and-submit-teal_20260516T113831_result.json`
- **Structured JSON:** [`70e60ea9098201aae50d.json`](../../sessions/70/70e60ea9098201aae50d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 已完成实验结果

| 指标 | bench_kl30_global (30% sparsity) | bench_kl50_global (50% sparsity) |
|------|---:|---:|
| wikitext2_ppl | **8.9768** | **11.7933** |
| arc_challenge_acc_norm | 0.3968 | 0.3285 |
| winogrande_acc | 0.7017 | 0.6346 |
| mmlu_acc | 0.2527 | 0.2789 |
| gsm8k_exact_match | 0.0879 | 0.0129 |

两个实验均正常完成（EXIT_CODE=0），runtime ~2h each。

### 2. 已提交新实验

| 实验 | GPU | PID | 模式 |
|------|-----|-----|------|
| **bench_teal30** | cuda:0 | 227692 | teal_vanilla, sparsity=0.3 |
| **bench_teal50** | cuda:1 | 227770 | teal_vanilla, sparsity=0.5 |

预计 ~2h 完成。

---

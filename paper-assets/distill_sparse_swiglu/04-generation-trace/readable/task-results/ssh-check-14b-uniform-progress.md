# ssh check 14b uniform progress

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_14b_uniform_progress_20260518T013307_result.json`
- **Structured JSON:** [`56bb828e631a69624a4b.json`](../../sessions/56/56bb828e631a69624a4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已完成。结果汇总：

| Metric | KL Uniform (30%) | TEAL Uniform (30%) |
|---|---|---|
| WikiText-2 PPL | **7.63** | 8.01 |
| ARC-c (acc_norm) | 54.4% | **55.3%** |
| WinoGrande (acc) | **72.5%** | 69.9% |
| MMLU (acc) | 64.5% | **66.3%** |

KL uniform PPL 更优（7.63 vs 8.01），但下游任务 MMLU 仍落后 TEAL uniform 1.8 个百分点（64.5 vs 66.3），ARC-c 也略低。WinoGrande 上 KL 反而领先 2.6 个百分点。

这与之前非 uniform 分配的趋势一致：KL 蒸馏在 PPL 上占优但 MMLU 存在 gap，说明这是 KL 目标本身的特性，不是分配策略导致的。

---

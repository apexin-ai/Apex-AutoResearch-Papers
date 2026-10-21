# eval d014 v7 2 bypass acis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d014-v7_2-bypass-acis_20260515T221856_result.json`
- **Structured JSON:** [`5a95fed912255a063bd8.json`](../../sessions/5a/5a95fed912255a063bd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both JSON files ready. Here are the results:

## Bypass-ACIS Evaluation Results

### Clean condition (eps=0, no pruning) — G3 diagnostic

| Model | bypass-ACIS clean action_loss | baseline clean action_loss | G3 ratio |
|---|---|---|---|
| **v7.2 (IMM)** | 0.00780 | 0.00408 | **1.91x** |
| **baseline** | 0.00408 | 0.00408 | 1.00x |

### Full condition breakdown

| Condition | v7.2 bypass-ACIS | baseline bypass-ACIS | Ratio |
|---|---|---|---|
| eps0.0_pruneFalse | 0.00780 | 0.00408 | 1.91x |
| eps0.0_pruneTrue | 0.02850 | 0.11897 | 0.24x |
| eps0.01_pruneFalse | 0.00793 | 0.00458 | 1.73x |
| eps0.01_pruneTrue | 0.02847 | 0.11898 | 0.24x |
| eps0.02_pruneFalse | 0.00963 | 0.00558 | 1.73x |
| eps0.02_pruneTrue | 0.03076 | 0.12176 | 0.25x |
| eps0.05_pruneFalse | 0.02294 | 0.01804 | 1.27x |
| eps0.05_pruneTrue | 0.04175 | 0.13948 | 0.30x |

### 结论

**bypass G3 = 1.91 >> 1.10 → IMM 训练损坏了模型权重，需要 gradient isolation。**

即使完全绕过 ACIS 打分和 token selection，仅使用 IMM 训练后的 policy 权重（含 LoRA），action_loss 仍然是 baseline 的 1.91 倍。这说明退化不是 selection 机制的 overhead，而是 ACIS/LoRA 的梯度回传污染了 VLM backbone 权重。

附注：pruneTrue 条件下 v7.2 反而远好于 baseline（0.24-0.30x），因为 IMM 的 LoRA 微调提供了对随机 pruning 的某种鲁棒性，但这不改变 clean 条件下权重已受损的事实。

---

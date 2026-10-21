# ssh status eval 41312 batch

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_status_eval_41312_batch_20260518T003704_result.json`
- **Structured JSON:** [`628c8295a8a05db70968.json`](../../sessions/62/628c8295a8a05db70968.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 eval 完成。汇总报告：

---

## 实验状态报告

### 1. 实验状态

| 实验 | 状态 | Train Loss | Runtime |
|------|------|-----------|---------|
| ess_only_seed456_r2 | **Completed** | 5.998 | 7611s (~2.1h) |
| ess_only_seed123_r2 | **Completed** | 6.860 | 8674s (~2.4h) |
| random_reweight_seed456 | **Completed** | 6.657 | 10739s (~3.0h) |
| grid_b0_2_seed42 | **Running** | — | step 2427/6103 (40%), ETA ~2h09m |

### 2. Eval Perplexity（eval_holdout.jsonl, 5000 docs, 4.08M tokens）

| 实验 | Loss | PPL |
|------|------|-----|
| ess_only_seed123 | 2.8747 | **17.72** |
| ess_only_seed456 | 2.8770 | 17.76 |
| random_reweight_seed456 | 2.8779 | 17.78 |

三者 PPL 非常接近（17.72–17.78），差异不到 0.4%。

### 3. GPU 使用

| GPU | 显存 | 利用率 | 任务 |
|-----|------|--------|------|
| 0 | 46539/97887 MiB | 100% | grid_b0_2_seed42 训练中 |
| 1 | 0 MiB | 0% | 空闲 |
| 2 | 0 MiB | 0% | 空闲（eval 刚完成） |
| 3 | 0 MiB | 0% | 空闲（eval 刚完成） |

### 4. 关键观察

grid_b0_2_seed42 预计还需 ~2 小时完成，完成后可在 GPU 1-3 任一卡上 eval。

---

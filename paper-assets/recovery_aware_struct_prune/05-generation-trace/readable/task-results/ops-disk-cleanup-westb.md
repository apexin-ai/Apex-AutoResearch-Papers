# ops disk cleanup westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_westb_20260518T110324_result.json`
- **Structured JSON:** [`3dde307abb1b332b8feb.json`](../../sessions/3d/3dde307abb1b332b8feb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。`grpo_cka_only_20/checkpoint-100` 完好（含 optimizer.pt）。

## 汇报

| 项目 | 数值 |
|---|---|
| **清理前可用** | 1.9G (100%) |
| **清理后可用** | **23G (92%)** |
| **释放空间** | ~21G |

### 清理内容

| 目标 | 释放 |
|---|---|
| `pruned_rasp_30/` | ~11G |
| `pruned_standard_30/` | ~11G |
| `wandb/` (根分区) | ~122M |
| `__pycache__` | 微量 |

`sft_rasp_30/` 和 `sft_standard_30/` 不存在，无需处理。

### 当前最大目录 (Top 5)

| 目录 | 大小 |
|---|---|
| `grpo_cka_only_20/` | 38G (含 checkpoint-100 27G + model 12G) |
| `sft_rasp_rlvr_20/` | 12G |
| `sft_random_20/` | 12G |
| `sft_gradient_20/` | 12G |
| `sft_cka_only_20/` | 12G |

当前共 15 个 ~11-12G 的模型目录 + 1 个 38G 的 GRPO 目录，占 ~228G。如需进一步释放空间，需要判断哪些 20%/25% 实验模型可以清理。

---

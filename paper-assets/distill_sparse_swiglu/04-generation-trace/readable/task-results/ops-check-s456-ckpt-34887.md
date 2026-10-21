# ops check s456 ckpt 34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_s456_ckpt_34887_20260520T000510_result.json`
- **Structured JSON:** [`207a46d37a18640bc33b.json`](../../sessions/20/207a46d37a18640bc33b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 checkpoint 都存在：

| Checkpoint | 状态 | 大小 | 时间 |
|---|---|---|---|
| `kl_sparsity30_s456/predictor_kl_normalized.pt` | **FOUND** | 145 MB | May 18 21:54 |
| `kl_sparsity30_s123/predictor_kl_normalized.pt` | **FOUND** | 145 MB | May 18 21:54 |

s456 目录下只有 `predictor_kl_normalized.pt` 一个文件（无其他中间 checkpoint）。

---

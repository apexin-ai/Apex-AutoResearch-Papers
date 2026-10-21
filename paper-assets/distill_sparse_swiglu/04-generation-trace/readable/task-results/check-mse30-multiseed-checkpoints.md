# check mse30 multiseed checkpoints

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mse30_multiseed_checkpoints_20260522T092442_result.json`
- **Structured JSON:** [`ca4af9a797ca06ab40bd.json`](../../sessions/ca/ca4af9a797ca06ab40bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 checkpoint 都存在且完整：

| 文件 | 大小 | 时间 |
|------|------|------|
| `mse30_s123/predictor_mse.pt` | 144.9 MB | May 21 09:39 |
| `mse30_s456/predictor_mse.pt` | 144.9 MB | May 21 09:39 |

两个文件大小完全一致（151,964,963 bytes），与预期的 predictor 模型大小匹配。

checkpoints 目录下 mse 相关目录共 4 个：
- `mse30_s42`
- `mse30_s123`
- `mse30_s456`
- `mse50_s42`

---

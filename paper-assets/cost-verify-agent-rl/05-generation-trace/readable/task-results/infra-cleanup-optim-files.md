# infra cleanup optim files

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cleanup-optim-files_20260517T120614_result.json`
- **Structured JSON:** [`fd81ac34e691ef8cb3b1.json`](../../sessions/fd/fd81ac34e691ef8cb3b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

| 指标 | 值 |
|------|------|
| 删除前可用 | 33G (87% used) |
| 删除后可用 | 59G (77% used) |
| 释放空间 | **~26G** |

两个 checkpoint 保留的文件确认一致：
- `model_world_size_2_rank_0.pt` (3.8G)
- `model_world_size_2_rank_1.pt` (3.8G)
- `huggingface/` 目录
- `fsdp_config.json`

---

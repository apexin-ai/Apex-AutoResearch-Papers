# ssh westd root partition cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_root_partition_cleanup_20260520T224427_result.json`
- **Structured JSON:** [`788b55f4653e0d5effbd.json`](../../sessions/78/788b55f4653e0d5effbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**清理内容：**
| 项目 | 释放空间 | 操作 |
|------|---------|------|
| `grpo_standard_15_seed123_v3` | ~13G | 移至数据盘 |
| `grpo_standard_15_seed456_v3` | ~13G | 移至数据盘 |
| `.cache/pip` | 94M | 删除 |
| `.cache/huggingface` | 347M | 删除 |
| 空 v2 目录 + `__pycache__` | 微量 | 删除 |

**清理后状态：**
- 根分区：5.0G used / **26G free** (17%) — 远超 5G 目标
- 数据盘：557G used / 63G free (90%)
- GPU 0/1 上的 eval 进程未受影响（它们加载的模型在数据盘）

---

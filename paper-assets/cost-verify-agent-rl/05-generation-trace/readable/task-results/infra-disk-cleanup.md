# infra disk cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-cleanup_20260514T124551_result.json`
- **Structured JSON:** [`3e62f296481c3e1171b6.json`](../../sessions/3e/3e62f296481c3e1171b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理结果汇报：

**无需清理。** 任务中列出的 5 个失败实验 checkpoint（exp012, exp013b, exp013c, exp013d, exp013e）已不存在，之前已被删除。

**当前磁盘状态：**
- `/root/autodl-tmp` 总计 250G，已用 113G，**可用 138GB**（45%）
- 远超 50GB 的空间需求

**现存目录：**
| 目录 | 大小 | 状态 |
|------|------|------|
| checkpoints/exp008_sft | 23G | 保护 |
| checkpoints/exp013f | 62G | 保护 |
| checkpoints/qwen3_sft_final | ~small | 新增 |
| alfworld/ | 2.2G | 保护 |
| models/ | 3.8G | — |
| ray_tmp/ | 42M | 可忽略 |
| tmp/ | 53M | 可忽略 |

磁盘空间充足，无需额外操作。

---

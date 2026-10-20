# ssh westd p0 disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_p0_disk_cleanup_20260521T033936_result.json`
- **Structured JSON:** [`393f1be80dfff14244ac.json`](../../sessions/39/393f1be80dfff14244ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westb-23072 没有找到任何 `optimizer.pt` 文件，无需清理。

## 磁盘状态对比

| 服务器 | 清理前 | 清理后 | 变化 |
|--------|--------|--------|------|
| **westd-29022** | 610G/619G (99%) | 610G/619G (99%) | optimizer.pt 可能已不存在或体积很小，释放空间不明显 |
| **westb-23072** | 227G/250G (91%) | 227G/250G (91%) | 无 optimizer.pt 文件，无需清理 |

westd-29022 仍然 99%，那两个 optimizer.pt 可能之前已被删除。westd 磁盘压力仍然很大，如需进一步清理需要排查其他大文件。

---

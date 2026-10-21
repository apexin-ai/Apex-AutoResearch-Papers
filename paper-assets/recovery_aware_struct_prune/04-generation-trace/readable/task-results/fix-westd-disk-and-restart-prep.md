# fix westd disk and restart prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd_disk_and_restart_prep_20260516T140141_result.json`
- **Structured JSON:** [`ff8a47eee083b2421163.json`](../../sessions/ff/ff8a47eee083b2421163.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成，全部验证通过：

| 指标 | 清理前 | 清理后 | 状态 |
|------|--------|--------|------|
| 根分区可用 | 25G | 25G | >= 10G ✅ |
| 数据盘可用 | **2.2M (100%)** | **483G (36%)** | >= 50G ✅ |
| wandb 符号链接 | 无 | → `/root/autodl-tmp/recovery_aware_struct_prune/wandb` | ✅ |
| GRPO 崩溃输出 | 486G (4个目录) | 已删除 | ✅ |

数据盘释放约 **482G**，从 100% 满恢复到 36% 使用。

---

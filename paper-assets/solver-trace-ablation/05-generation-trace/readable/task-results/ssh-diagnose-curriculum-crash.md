# ssh diagnose curriculum crash

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-curriculum-crash_20260516T145431_result.json`
- **Structured JSON:** [`7ce6d933f52e2274feb5.json`](../../sessions/7c/7ce6d933f52e2274feb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。诊断总结：

## 诊断结果

**根因：数据盘 `/root/autodl-tmp` 250G/250G 100% 满**，两个实验在 checkpoint 保存时 `SafetensorError: No space left on device (os error 28)` 崩溃。

| 实验 | 崩溃位置 | Phase 2 触发？ | Checkpoint 可用？ |
|------|----------|---------------|-------------------|
| `t02-s42` | step 50/500 | 未到（warmup=100） | 不可用（shard 1/4 仅 12KB） |
| `t02-s43` | step 100/500 | 刚触发（step 91 出现 `gate_pass=1.0`） | 不可用（同上） |

**附：`gated-isr-t03-s43`** 旧实验日志尾部同为磁盘满崩溃（step 100），registry 已是 DONE/failed，未修改。

**两张 GPU 当前空闲（0MiB），tmux 无 session，进程已清除干净。**

重跑前需要先清理 `/root/autodl-tmp` 腾出空间——当前根分区有 21G 余量但数据盘完全满。

---

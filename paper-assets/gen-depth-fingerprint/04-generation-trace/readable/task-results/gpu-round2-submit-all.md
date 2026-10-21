# gpu round2 submit all

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_round2-submit-all_20260514T215413_result.json`
- **Structured JSON:** [`7c96a531d9aacd3ec0c8.json`](../../sessions/7c/7c96a531d9aacd3ec0c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

0.6b 进程仍在运行（tmux session 丢失但进程存活为孤儿进程，不影响执行）。4 卡全部在跑。

## 状态汇报

| 任务 | GPU | tmux session | PID | 状态 |
|------|-----|-------------|-----|------|
| Qwen3-1.7B shard 0 | cuda:0 | plan-002-qwen17b-r2-s0 | 120612 | **新提交** - resume 跳过 154 seeds，从 155/498 继续 |
| Qwen3-1.7B shard 1 | cuda:1 | plan-002-qwen17b-r2-s1 | 120689 | **新提交** - resume 跳过 143 seeds |
| Qwen3-0.6B shard 0 | cuda:2 | *(session丢失，进程在跑)* | 117855 | 运行中，782+ 行已写入 |
| Qwen3-0.6B shard 1 | cuda:3 | *(session丢失，进程在跑)* | 118126 | 运行中，727+ 行已写入 |

**关键修复**：发现 1.7B 旧进程在写入**已删除的文件**（inode 被 `rm` 删除但 fd 仍打开），从 `/proc/PID/fd/` 恢复了 shard0=699 行(154 seeds)、shard1=669 行(143 seeds)，杀旧进程后重新提交，resume 逻辑自动跳过已完成 seeds。

---

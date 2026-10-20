# verify seed0 running

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_seed0_running_20260514T004644_result.json`
- **Structured JSON:** [`fccacbaa568b56019748.json`](../../sessions/fc/fccacbaa568b56019748.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

| 检查项 | 状态 |
|--------|------|
| **PID 122208** | **运行中**，已运行 ~2m50s，bash wrapper 正常 |
| **子进程** | PID 122212 (timeout 86400) 正常运行，launch_seed0.sh 已启动 |
| **日志** | 正在进行数据预处理——Map tokenization 进度 ~42% (752k/1.8M)，尚未开始训练 |
| **GPU** | cuda:0 (RTX PRO 6000 Black, 96GB) 空闲，**GPU-Util 0%，无进程占用**——因为当前仍在 CPU 上做 tokenization，尚未加载模型 |
| **旧 PID 122711** | 已死（`exit code 1`），旧 session 已清理 |

一切正常。训练管线刚启动不到 3 分钟，正在 tokenize wikitext-103（~42% 完成），预计再过 2-3 分钟 tokenization 结束后会加载模型到 GPU 并开始训练。

---

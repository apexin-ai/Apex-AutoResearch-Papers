# ssh urgent kill timeout

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-kill-timeout_20260520T212728_result.json`
- **Structured JSON:** [`6a00da2414e06f7f3ebc.json`](../../sessions/6a/6a00da2414e06f7f3ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**情况不妙。** `kill 886277 886351` 返回 exit 0（两个 timeout 进程确实存在并被杀了），但训练 PID 886278 和 886352 也不存在了——`timeout` 收到 SIGTERM 后把信号转发给了子进程组。

当前服务器上存活的训练进程是**不同的 PID**：

| PID | 任务 | 启动时间 | GPU |
|-----|------|---------|-----|
| **949112** | `train_unified.py --seed 456` (deepseek-cwm-repo-s456-v2) | May20 | GPU 1 (20GB/32GB, 99%) |
| **978461** | `eval_repo_cwm.py` s123_v2 eval | May20 | GPU 0 |
| 990708-990711 | DataLoader workers of 949112 | 02:24 today | — |

**GPU 状态**：
- GPU 0: 100% util, 0 MiB（eval 进程可能刚释放）
- GPU 1: 99%, 20253 MiB（s456_v2 训练活跃）
- GPU 2: 86%, 30651 MiB
- GPU 3: 100%, 0 MiB

原始 PID 886278/886352 的 Qwen 训练已经不在了。被杀的 886277/886351 很可能就是这两个训练的 timeout wrapper，信号级联导致训练一起被终止了。`timeout` 默认 kill 整个进程组（`--foreground` 才不会）。

需要确认：这两个 Qwen 训练是否需要重新启动？还是说它们实际上已经在之前完成、被替换为当前的 DeepSeek 训练了？

---

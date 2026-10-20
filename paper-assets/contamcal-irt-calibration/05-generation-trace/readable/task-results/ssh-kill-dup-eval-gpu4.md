# ssh kill dup eval gpu4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-dup-eval-gpu4_20260513T214930_result.json`
- **Structured JSON:** [`c5f88c96e926792601ec.json`](../../sessions/c5/c5f88c96e926792601ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 tmux 日志。评估仍在运行中（输出目录为空，进程活跃）。

**结果汇总：**

| 项目 | 状态 |
|------|------|
| PID 221677 | **已 kill** |
| PID 221376 | **正常运行中**，已运行 ~19 分钟，状态 Rl |
| GPU 4 显存 | 5829 MiB（kill 前两个进程共占，现在只剩一个，显存已释放一半） |
| 输出目录 | 空，尚无结果文件，无冲突 |
| 评估结果 | **尚未完成**，进程仍在跑 mmlu/gsm8k/arc_challenge/humaneval 四个 benchmark |

评估还需要一些时间才能出结果。需要我稍后轮询检查完成状态吗？

---

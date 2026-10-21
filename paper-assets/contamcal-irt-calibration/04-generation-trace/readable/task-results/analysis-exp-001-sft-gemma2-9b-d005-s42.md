# analysis exp 001 sft gemma2 9b d005 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_gemma2_9b_d005_s42_20260518T232616_result.json`
- **Structured JSON:** [`b5de04ba2f9db01a597b.json`](../../sessions/b5/b5de04ba2f9db01a597b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：FAILED**

服务器上不存在任何 Gemma-2-9B 相关的文件、目录、进程或日志。具体情况：

- `/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d005_s42/` — 不存在
- 日志文件 — 不存在
- 全盘搜索 — 无任何 gemma 相关文件或目录
- 无活跃进程或 tmux session

训练从未在此服务器（cqa1-21977）上产出任何输出。可能的原因：
1. 训练在启动阶段就失败了（OOM、import error 等），未创建 output dir
2. 训练实际运行在另一台服务器上
3. 任务从未真正提交

GPU 状态：cuda:0 占用 22928/24564 MiB（有其他任务），仅 1 张 GPU 可见。

需要确认：这个任务是在哪台服务器、哪个 GPU 上提交的？

---

# diagnose w38 cuda0 pid363197

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w38_cuda0_pid363197_20260528T080804_result.json`
- **Structured JSON:** [`864d55adba77f71070ce.json`](../../sessions/86/864d55adba77f71070ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

**PID 363197 身份确认：**
- **实验**: `eval_pi05_random_k075_long_seed46_strict_w38` — π0.5 Random k=0.75, Long suite (libero_10), seed 46
- **命令**: `python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.75 --suite libero_10 --n_episodes 50 --seed 46 --gpu 0`
- **父进程 PID 363188**: submit_training_job 的 wrapper bash 进程，正常的 agent-ml 部署结构

**运行状态：**
- 启动时间: 2026-05-28 15:47 (约 20 分钟前)
- 当前进度: Task 0 完成 (82%), Task 1 进行中 (ep 10, 40%)
- GPU 显存占用: 10705 MiB
- 有 6h timeout 保护

**结论：合法进程，应保留。** 这是通过 submit_training_job 正常部署的 π0.5 实验，正在正常推进中。不是残留进程。

---

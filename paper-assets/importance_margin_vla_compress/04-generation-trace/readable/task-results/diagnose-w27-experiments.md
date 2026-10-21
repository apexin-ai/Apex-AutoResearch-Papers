# diagnose w27 experiments

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w27_experiments_20260528T015249_result.json`
- **Structured JSON:** [`338300b5e08ef6b29d90.json`](../../sessions/33/338300b5e08ef6b29d90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行，GPU 活跃。汇总：

### 实验 1: `eval_pi05_l2norm_k075_long_seed45_strict_w27`
- **状态**: RUNNING，正在执行 Task 7（T7），已完成 T0-T6
- **进度**: 7/10 tasks done，运行 ~1h44m
- **已完成任务成绩**: T0=82%, T1=84%, T2=78%, T3=64%, T4=54%, T5=80%, T6=48%
- **当前累计**: 245/350 = 70.0%
- **实际日志路径**: `/root/autodl-tmp/importance_margin_vla_compress/logs/l2norm_k075_s45.log`

### 实验 2: `eval_pi05_random_k085_long_seed45_strict_w27`
- **状态**: RUNNING，正在执行 Task 6（T6），已完成 T0-T5
- **进度**: 6/10 tasks done，运行 ~1h44m
- **已完成任务成绩**: T0=52%, T1=54%, T2=52%, T3=72%, T4=6%, T5=38%
- **当前累计**: 137/300 = 45.7%
- **实际日志路径**: `/root/autodl-tmp/importance_margin_vla_compress/logs/random_k085_s45.log`

两个进程各占 ~10.6GB GPU 显存，分别在不同 GPU 上运行。GPU 并非 idle，registry 状态 RUNNING 正确，无需更新。预计还需 ~40-50 分钟完成剩余 tasks。

---

# monitor westd val sweep diagnosis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-val-sweep-diagnosis_20260515T172009_result.json`
- **Structured JSON:** [`203ace1dab9a408009bd.json`](../../sessions/20/203ace1dab9a408009bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. cls8b-s42-resume-val-sweep (PID 388791, GPU 0) — 已死

| 项目 | 详情 |
|------|------|
| **进程** | 不存在，GPU 0 空闲（0MiB, 0%） |
| **退出码** | 1，退出时间 2026-05-16 00:03:21 CST |
| **最后日志** | 评估 checkpoint-1800 到 560/9335 (6.0%)，running_acc=87.7%，时间 22:16:22 |
| **结果保存** | 无。输出目录为空 |

**死亡原因**：日志无 Traceback/Error/OOM 信息，直接中断。最后日志行到退出文件时间戳间隔 ~1h47m。最可能是评估 seq_length=8192 时触发了 CUDA OOM（8B 模型 + 8192 seq 在单卡 32GB 上紧张），进程被 kill 但 stderr 未写入日志文件。

**修复方案**：GPU 0 现在空闲，可直接重启。建议修改脚本跳过已完成的 step（CSV 已有 1800 的 seq2048 结果），从 step 1800 seq8192 开始。若 OOM 复现，降 batch_size 到 4 或降 max_seq_length 到 4096。

---

### 2. CWM 8B training (PID 266816, GPU 2) — 运行中

| 项目 | 详情 |
|------|------|
| **运行时长** | 23h36m |
| **GPU** | GPU 2, 30733MiB/32607MiB, **98% util** |
| **最新 checkpoint** | step 5100 (May 16 00:50) |
| **保存速度** | ~40 min / 100 steps |

Checkpoint 历史：400 → 4800 → 4900 → 5000 → 5100（中间的被清理了）。

---

### 3. CLS 8B s42 resume training (PID 295794, GPU 1) — 运行中

| 项目 | 详情 |
|------|------|
| **运行时长** | 19h32m |
| **GPU** | GPU 1, 27313MiB/32607MiB, **48% util** |
| **最新 checkpoint** | step 6200 (May 16 01:07) |
| **保存速度** | ~41 min / 200 steps |

已保存 28 个 checkpoints（800 → 6200），全部保留。

---

### 4. CWM 8B ckpt-400 test eval (PID 381618, GPU 3) — 运行中

| 项目 | 详情 |
|------|------|
| **运行时长** | 2h42m |
| **GPU** | GPU 3, 22527MiB/32607MiB, **87% util** |
| **进度** | 1760/9784 (18.0%) |
| **速度** | ~10.9 samples/min |
| **ETA** | ~12.3 小时（约 May 16 13:30 完成） |

---

### GPU 概览

| GPU | 状态 | 显存 | 利用率 | 任务 |
|-----|------|------|--------|------|
| 0 | **空闲** | 0/32GB | 0% | val-sweep 已死 |
| 1 | 运行 | 27.3/32GB | 48% | CLS 8B s42 训练 |
| 2 | 运行 | 30.7/32GB | 98% | CWM 8B 训练 |
| 3 | 运行 | 22.5/32GB | 87% | CWM 8B ckpt400 eval |

---

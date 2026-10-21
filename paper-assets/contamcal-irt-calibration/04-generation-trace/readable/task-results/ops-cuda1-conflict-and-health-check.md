# ops cuda1 conflict and health check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda1-conflict-and-health-check_20260515T175815_result.json`
- **Structured JSON:** [`d52880a296e2223d4438.json`](../../sessions/d5/d52880a296e2223d4438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 601354 已 kill，cuda:4 VRAM 从 23540 → 13877 MiB，恢复正常。

---

## GPU 健康检查报告

### 1. 各 GPU 进程状态

| GPU | VRAM | Util | 任务 | 进度 | 预计剩余 |
|-----|------|------|------|------|---------|
| cuda:0 | 17975/24564 | 4% | SFT 3B d100 s123 a32 v2 | 1220/4159 = **29%** | ~3h20m |
| cuda:1 | 13341/24564 | 19% | SFT 3B d100 s42 a32 v2 | 1265/4159 = **30%** | ~3h10m |
| cuda:2 | 8985/24564 | 82% | eval 3B d005 s123 aligned | GSM8K 1239/1319=94% | ~1-1.5h (还有 arc+humaneval) |
| cuda:3 | 13583/24564 | 67% | eval 3B d025 s123 aligned | HumanEval 106/164=**65%** | **~7-8min** (最后一个 benchmark) |
| cuda:4 | 13877/24564 | 50% | SFT 3B d000 v3 | 834/3125 = **27%** | ~2h50m |
| cuda:5 | 17649/24564 | 5% | SFT 3B d025 v3 s42 | 1504/3384 = **44%** | ~2h07m |

### 2. cuda:1 冲突 → 虚警

PID 593740（bash wrapper）和 PID 593745（python 子进程）是同一任务的父子进程。GPU 上只有 593745 占用 13332 MiB。**无冲突。**

### 3. cuda:4 真实冲突 → 已解决

- **保留**: PID 597179 — SFT d000 v3（13868 MiB，已跑 1h07m）
- **已 kill**: PID 601354 — compute_signals d005 s42 MMLU（9658 MiB，跑了 37min）
- 原因：compute_signals 是后提交的较低优先级任务，违反 C001/C003 约束
- VRAM 从 23540 → 13877 MiB，利用率从 100% → 50%

### 4. eval 完成时间估算

- **cuda:3 (d025 s123)**: HumanEval 是最后一个 benchmark，剩 58 items × ~8s ≈ **~8min 内完成**
- **cuda:2 (d005 s123)**: GSM8K 剩 80 items (~10min)，之后还有 arc_challenge + humaneval ≈ **~1-1.5h**

### 5. SFT 训练进度

| 任务 | Step | Loss | Epoch | 速度 |
|------|------|------|-------|------|
| d100 s123 (cuda:0) | 1220/4159 | ~1.18 | 0.29 | ~4.0s/it |
| d100 s42 (cuda:1) | 1265/4159 | ~1.15 | 0.28 | ~3.95s/it |
| d000 v3 (cuda:4) | 834/3125 | ~1.14 | 0.26 | ~4.6s/it |
| d025 v3 (cuda:5) | 1504/3384 | ~1.12 | 0.35 | ~4.1s/it |

### 6. 异常

- **cuda:4 冲突已修复**。compute_signals d005 s42 需要重新提交到空闲 GPU
- **cuda:5 无标准 log 文件**（~/runs/ 下没有），进度通过 output-dir 的 train.log 获取。该进程不是通过 agent-ml wrapper 启动的
- cuda:3 eval 即将完成，完成后该 GPU 可用于新任务

---

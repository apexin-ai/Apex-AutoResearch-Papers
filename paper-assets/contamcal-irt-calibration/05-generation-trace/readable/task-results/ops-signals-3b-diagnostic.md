# ops signals 3B diagnostic

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_signals-3B-diagnostic_20260515T195644_result.json`
- **Structured JSON:** [`6af9768ac08b21ca1a21.json`](../../sessions/6a/6af9768ac08b21ca1a21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是结构化诊断报告。

---

## 1. 进程存活状态

| PID | 状态 | 运行时间 | GPU (实际) | 命令 | 来源 |
|-----|------|----------|-----------|------|------|
| 617201 | **ALIVE** | 1h 00m | GPU 3 (CUDA_VISIBLE_DEVICES=3) | `run_batch.py --model-size 3B --gpu 0` (全部 dosage) | 未知来源，非 v4/v5 框架 |
| 617202 | ALIVE (子进程) | ~1h | GPU 3 (7526 MiB) | `compute_signals.py d000_s42/mmlu` | 617201 子进程 |
| 622557 | **ALIVE** | 16m | GPU 4 (CUDA_VISIBLE_DEVICES=4) | `run_batch.py --model-size 3B --gpu 0 --only d100` | 未知来源 |
| 622558 | ALIVE (子进程) | ~16m | GPU 4 (6882 MiB) | `compute_signals.py d100_s42/mmlu` | 622557 子进程 |
| 622855 | **ALIVE** | 15m | GPU 2 (CUDA_VISIBLE_DEVICES=2) | `run_batch.py --model-size 3B --gpu 0 --only d005 d025` | 未知来源 |
| 622856 | ALIVE (子进程) | ~15m | GPU 2 (6882 MiB) | `compute_signals.py d005_s42/mmlu` | 622855 子进程 |
| 623826 | **ALIVE** | 13m | GPU 4 (CUDA_VISIBLE_DEVICES=4) | `run_batch.py --model-size 3B --gpu 0 --only d025 d100` | **v5** (tmux wrapper) |
| 623837 | ALIVE (子进程) | ~13m | GPU 4 (7946 MiB) | `compute_signals.py d025_s42/mmlu` | v5 子进程 |
| 623480 | **ALIVE** | 13m | GPU 2 (CUDA_VISIBLE_DEVICES=2) | `evaluate.py gsm8k d005_s123` | exp_001 eval 任务 |
| 623491 | ALIVE (子进程) | ~13m | GPU 2 (6788 MiB) | `evaluate.py --benchmarks gsm8k` | 623480 子进程 |

**v4 日志文件** `/root/runs/.../exp_002_signals_3B_v4.log` 不存在。PID 617201 的 stdout 指向 `/root/autodl-tmp/exp002/logs/3B_signals_v4.log`，说明它是在 cron 框架之外直接通过 SSH 启动的。

---

## 2. GPU 占用

| GPU | 显存使用 | 利用率 | 占用进程 |
|-----|---------|--------|---------|
| 0 | 17975/24564 MiB | 83% | PID 594494 (其他任务) |
| 1 | 13341/24564 MiB | 32% | PID 593745 (其他任务) |
| 2 | **13684/24564 MiB** | **98%** | PID 622856 (signals d005/mmlu) + PID 623491 (eval gsm8k) |
| 3 | 7535/24564 MiB | 62% | PID 617202 (signals d000/mmlu) |
| 4 | **14842/24564 MiB** | **99%** | PID 622558 (signals d100/mmlu) + PID 623837 (signals d025/mmlu) |
| 5 | 17651/24564 MiB | 37% | PID 589763 (其他任务) |

---

## 3. 3B Signals 完成状态 (12 combos)

| Combo | merged 文件 | 状态 | 当前计算进程 |
|-------|------------|------|-------------|
| d000/mmlu | **无** | **进行中** | PID 617202 (GPU 3) |
| d000/gsm8k | signals_merged_gsm8k.json | **已完成** | — |
| d000/arc_challenge | signals_merged_arc_challenge.json | **已完成** | — |
| d005/mmlu | **无** (有 s1, s2 partial) | **进行中** | PID 622856 (GPU 2) |
| d005/gsm8k | **无** (有 s1, s2 partial) | **未完成** | 排队 (622855, 617201) |
| d005/arc_challenge | signals_merged_arc_challenge.json | **已完成** | — |
| d025/mmlu | **无** (有 s1 partial) | **进行中** | PID 623837 (GPU 4) |
| d025/gsm8k | signals_merged_gsm8k.json | **已完成** | — |
| d025/arc_challenge | signals_merged_arc_challenge.json | **已完成** | — |
| d100/mmlu | **无** (有 s1, s2 partial) | **进行中** | PID 622558 (GPU 4) |
| d100/gsm8k | **无** | **未完成** | 排队 (622557, 623826, 617201) |
| d100/arc_challenge | **无** | **未完成** | 排队 (622557, 623826, 617201) |

**已完成: 7/12，进行中: 4/12，未完成: 1/12 (d005/gsm8k)**

---

## 4. 冲突风险评估 — **严重**

### 4a. 输出目录冲突（数据腐败风险）

4 个 run_batch.py 父进程的任务队列存在大量重叠：

| 输出目录 | 竞争进程数 | 进程列表 |
|---------|-----------|---------|
| d000_s42 | 1 | 617201 仅此一个 |
| d005_s42 | **2** | 617201 + 622855 |
| d025_s42 | **3** | 617201 + 622855 + 623826(v5) |
| d100_s42 | **3** | 617201 + 622557 + 623826(v5) |

当某个进程完成当前 combo 转入下一个时，会与其他进程**同时写入同一 output-dir 下的 JSON 文件**，导致数据污染/覆写。

### 4b. GPU 共享冲突

- **GPU 4**：PID 622558 (d100/mmlu) + PID 623837 (d025/mmlu) = 14.8 GB / 24 GB。当前可容纳，但利用率已 99%，两个 signals 进程互相争抢计算资源，均在减速。
- **GPU 2**：PID 622856 (signals) + PID 623491 (eval) = 13.7 GB / 24 GB。不同任务，无 output dir 冲突，但计算竞争。

---

## 5. 建议操作

**推荐方案：保留 3 个特化进程，杀掉 v4 全量进程 + v5 中的冲突部分**

| 操作 | 进程 | 原因 |
|------|------|------|
| **KILL** | PID 617201 + 617202 (GPU 3) | 全量进程与其他 3 个全部冲突。d000/mmlu 是唯一独占 combo，可完成后再提交，或者让它跑完 d000/mmlu 再 kill（当前正在处理这个） |
| **KILL** | PID 622557 + 622558 (GPU 4) | d100 已被 v5 覆盖（v5 在 d025 完成后会接着跑 d100），且两者在 GPU 4 上争抢。或者反过来，kill v5 保留 622557 |
| **KEEP** | PID 622855 + 622856 (GPU 2) | d005 + d025，无冲突（前提是 kill 了 617201 和 v5 的 d025） |
| **KEEP** | PID 623826 (v5, GPU 4) | d025 + d100，但 d025 与 622855 冲突，d100 与 622557 冲突 |

**更安全的替代方案：**

1. Kill **617201**（全量进程）— 它是冲突根源，覆盖面最广
2. Kill **622557** 或 **623826(v5)** 其中一个 — 解除 GPU 4 上 d100 的竞争
3. 如果 kill v5：保留 622557 (d100) + 622855 (d005+d025)，仅 d000/mmlu 需后续单独提交
4. 如果 kill 622557：保留 v5 (d025+d100) + 622855 (d005 only，d025 需确认 v5 是否已覆盖)

**等待决策再行动，不自行 kill。**

---

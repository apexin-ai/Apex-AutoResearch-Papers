# diag westd gpu utilization

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-gpu-utilization_20260515T145815_result.json`
- **Structured JSON:** [`190293907ad58a2bbfbd.json`](../../sessions/19/190293907ad58a2bbfbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。westd-11672 实际状态：

### GPU 利用情况

| GPU | VRAM | Util | 进程 |
|-----|------|------|------|
| cuda:0 | 13.1 / 97.9 GB | 89% | GraSP eval (PID 38120) — 41/100 samples, ~1.7h remaining |
| cuda:1 | 73.8 / 97.9 GB | 98% | α=1.0 eval (PID 42535, ~5min ETA) + α=2.0 SFT (PID 43065, 35/1870 ~2%, ~56min ETA) |

**Reviewer 的担忧已过时** — cuda:1 并非空闲，反而是负载最重的卡（98% util, 73.8GB）。

### 进程状态

| 实验 | 状态 | 详情 |
|------|------|------|
| **GraSP SFT** (sft_grasp_20_westd) | **DONE** (success) | 1870/1870 steps, 58.5min, loss=0.5857, token_acc=0.8392. Exit code 0. |
| **α=2.0 SFT** (PID 43065) | **RUNNING** | 35/1870 steps (~2%), GPU 1, ~56min remaining. 之前 Worker 的 nohup 启动成功（PID 43060→43065）。 |
| **GraSP eval** (PID 38120) | **RUNNING** | 41/100 samples, GPU 0, ~105s/sample, ~1.7h remaining. |
| **α=1.0 eval** (PID 42535) | **RUNNING** | 刚启动, GPU 1, ~3s/sample, 预计 5-8min 完成。 |

### Registry 更新
- `sft_grasp_20_westd`: ALLOCATED → **DONE** (success)
- `sft_alpha2_0_westd`: notes 更新（RUNNING on GPU 1，状态机不允许 PREPARING→RUNNING 直接转换）
- `eval-sft-alpha-1p0`: notes 更新
- `grasp_baseline_westd`: notes 更新

α=2.0 SFT 无需重新启动，已在正常运行中。

---

# ops gpu progress check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-progress-check_20260515T093919_result.json`
- **Structured JSON:** [`85ec4f39f87517a84f37.json`](../../sessions/85/85ec4f39f87517a84f37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | 温度 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 14,159 / 97,887 MiB | 31% | 36°C |
| 1 | RTX PRO 6000 Blackwell | 2,753 / 97,887 MiB | 0% | 36°C |

两卡进程均存活。GPU 0 上除 009d 主进程 (122271) 外还有 5 个 python 子进程（应为 dreamer 的 env worker），GPU 1 仅 009e 一个进程。

### 2. 009e (PID 119108, GPU 1) — 目标 105K

- **当前 step: 80,000** / 105,000
- **已运行: 3h 38m**
- **速率: ~22,000 steps/h**
- **ETA: ~1h 8min（约 18:47 服务器时间）**

**Eval checkpoints:**

| Step | eval_return |
|------|------------|
| 5K | 31.00 |
| 15K | 153.67 |
| 25K | 167.22 |
| 35K | 146.34 |
| 45K | 140.76 |
| 55K | 82.75 |
| 65K | **250.00** |
| 75K | 178.06 |

性能波动大，55K 处跌至 83，65K 回弹到 250，75K 又回落到 178。

### 3. 009d (PID 122271, GPU 0) — 目标 500K

- **当前 step: 64,000** / 500,000
- **已运行: 2h 49m**
- **速率: ~22,700 steps/h**
- **ETA: ~19.2h（约明天 5/16 12:50 服务器时间）**

**Eval checkpoints:**

| Step | eval_return |
|------|------------|
| 5K | 31.77 |
| 15K | 206.61 |
| 25K | 395.27 |
| 35K | 388.47 |
| 45K | 513.77 |
| 55K | **625.73** |

Baseline 学习曲线单调递增，55K 已达 626，表现健康。

### 4. 异常标记

- **GPU 1 利用率 0%**：009e 进程存活且 CPU 802%，可能正处于数据采集/eval 阶段（CPU-bound），非异常。
- **009e 性能远低于 009d baseline**：同样 55K step，009e eval_return 仅 83 vs baseline 626。009e 使用 `gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8`，学习效率显著低于 baseline，且曲线不稳定。

---

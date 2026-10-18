# ops audit westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit-westd38929_20260524T001632_result.json`
- **Structured JSON:** [`3ba2464be140ca257b06.json`](../../sessions/3b/3ba2464be140ca257b06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验的 registry 已更新（它们之前已部分注册）。以下是完整审计结果：

---

## 1. eval_xvla_random_k05_spatial_seed43 — 已完成

| 指标 | 值 |
|------|-----|
| **Overall SR** | **72.6%** (363/500) |
| **95% Wilson CI** | [68.5%, 76.3%] |
| Seed | 43 |
| Mode | random, keep_ratio=0.5 |

Per-task: T0=100%, T1=38%, T2=88%, T3=92%, T4=88%, **T5=0%**, T6=94%, T7=68%, T8=92%, T9=66%

Registry 已有记录，status=DONE, conclusion=success。hypothesis 已更新。

---

## 2. eval_xvla_l2norm_k05_goal_seed43 — 也已完成（bonus 收割）

| 指标 | 值 |
|------|-----|
| **Overall SR** | **60.2%** (301/500) |
| **95% Wilson CI** | [55.8%, 64.4%] |
| Mode | l2_norm, keep_ratio=0.5 |

Per-task: T0=84%, T1=100%, T2=98%, T3=30%, T4=100%, **T5=0%**, T6=22%, T7=74%, T8=90%, T9=4%

Registry status=DONE, conclusion=negative。hypothesis 已更新。

---

## 3. GPU 状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 4938 / 97887 MiB | 52% | `eval_xvla_l2norm_k05_spatial_seed43` — spatial suite 进行中 |
| 1 | 5250 / 97887 MiB | 0%* | `eval_xvla_l2norm_k05_long_seed43` — libero_10 Task 4, Ep 8/50 |
| 2 | 1 / 97887 MiB | 0% | **空闲** |
| 3 | 4856 / 97887 MiB | 64% | `eval_xvla_random_k05_goal_seed43_v4` — goal suite Task 5, Ep 5/50 |

*GPU 1 利用率 0% 是 nvidia-smi 采样瞬时值，进程实际在跑（PID 432791, 259% CPU）。

---

## 4. 活跃 tmux sessions & 进程

| Session / pts | 实验 | 状态 |
|--------------|------|------|
| pts/0 | eval_xvla_l2norm_k05_spatial_seed43 | **运行中** — l2_norm, spatial, seed43 |
| pts/1 | eval_xvla_l2norm_k05_long_seed43 | **运行中** — l2_norm, libero_10, seed43 |
| pts/2 | eval_xvla_random_k05_goal_seed43_v4 | **运行中** — random, goal, seed43 |
| pts/3 (tmux: eval_xvla_l2norm_k05_goal_seed43) | eval_xvla_l2norm_k05_goal_seed43 | **已完成** — 仅剩空 bash shell |

**GPU 2 完全空闲**，可用于启动新实验。

---

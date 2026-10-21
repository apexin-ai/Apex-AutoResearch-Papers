# ops status bjb1 18228 obsonly r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-bjb1-18228-obsonly-r3_20260515T095253_result.json`
- **Structured JSON:** [`9f6334ed9501a25ec4a6.json`](../../sessions/9f/9f6334ed9501a25ec4a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## 1. obs-only-r3 结果

**进程状态**: ALIVE (PID 312425, GPU 3)

| Task | SR | 详情 |
|------|-----|------|
| T6 | **90%** | 9/10 |
| T7 | **0%** | 0/10 |
| T8 | **20%** | 2/10 |
| T9 | **running** | 0/5 at rollout 5/10 |

结合 r2 的 T0-T5 (90%, 100%, 0%, 40%, 10%, 0%)，obs-only 全 10 task 完成后预计 overall ≈ **25-27%**（T9 按当前趋势大概 0%）。

---

## 2. GPU 全状态

| GPU | Util | VRAM | PID | 实验 |
|-----|------|------|-----|------|
| 0 | 19% | 4652/24564 MiB | 325264 | **eval-mag-obsonly-norm03-r2** (obs_only, norm=0.3, T0起) |
| 1 | 24% | 2535/24564 MiB | 311886 | **eval-acr-spatial-v4-scalar-r2** (crm_scalar, T3起) |
| 2 | 22% | 5711/24564 MiB | 341878 | **eval-obs-only-spatial-seed43** (obs_only, seed=43, T0起) |
| 3 | 20% | 2005/24564 MiB | 312425 | **eval-acr-spatial-v4-obs-only-r3** (obs_only, T6起) |

4 GPU 全部在用，无空闲。

---

## 3. Tmux Sessions

| Session | Created | GPU | PID |
|---------|---------|-----|-----|
| eval-acr-spatial-v4-obs-only-r3 | 13:14 | 3 | 312425 |
| eval-acr-spatial-v4-scalar-r2 | 13:14 | 1 | 311886 |
| eval-mag-obsonly-norm03-r2 | 14:50 | 0 | 325264 |
| eval-obs-only-spatial-seed43 | 17:09 | 2 | 341878 |

---

## 4. 其他运行中实验进度

**scalar-r2** (GPU 1, start_task=3): T3=40%, T4=0%, T5=0%, T6=90%，当前正在 T7+

**mag-obsonly-norm03-r2** (GPU 0, norm=0.3): T0=90%, T1=100%, T2=0%, T3 in progress (1/5 at rollout 5)

**obs-only-spatial-seed43** (GPU 2, seed=43): T0=80% (8/10)，正在 T1+

---

## 5. 已完成实验（进程不在了）

| 实验 | 退出码 | 结果 |
|------|--------|------|
| **eval-argmin-only-spatial-r2** (reconvla, T9) | 0 | T9=10% (1/10) |
| **eval-acr-spatial-v4-small-r2** (acr_vla, T7起) | 0 | T7=10%, T8=40%, T9=0%, overall=16.7% |
| **eval-acr-spatial-v4-default-r2** | **127** | 崩溃：`python: command not found`（需用 python3） |
| **eval-mag-obsonly-norm03** (首次) | **127** | 同上 |
| **eval-mag-obsonly-norm03-b2** | **143** | 被 SIGTERM kill |

---

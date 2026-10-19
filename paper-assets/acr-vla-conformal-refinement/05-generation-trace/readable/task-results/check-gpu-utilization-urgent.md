# check gpu utilization urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-utilization-urgent_20260524T165223_result.json`
- **Structured JSON:** [`b23c378f0ca7e32b00f3.json`](../../sessions/b2/b23c378f0ca7e32b00f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

---

### Server 1: bjb2-28827 ✅ 6/6 全部在跑

| GPU | 利用率 | 显存 | 实验 |
|-----|--------|------|------|
| 0 | 19% | 3566/24564 MiB | adaptive_conformal_crm, spatial, s48 |
| 1 | 14% | 3566/24564 MiB | adaptive_conformal_crm, spatial, s49 |
| 2 | 17% | 3256/24564 MiB | adaptive_conformal_crm, goal, s48 |
| 3 | 19% | 3256/24564 MiB | adaptive_conformal_crm, goal, s49 |
| 4 | 17% | 3776/24564 MiB | adaptive_conformal_crm, object, s48 |
| 5 | 20% | 3776/24564 MiB | adaptive_conformal_crm, object, s49 |

Tmux: 6 sessions（eval-supp-adapt-tau025-{spatial,goal,obj}-s{48,49}）

---

### Server 2: cqa1-32758 ✅ 6/6 全部在跑

| GPU | 利用率 | 显存 | 实验 |
|-----|--------|------|------|
| 0 | 19% | 3822/24564 MiB | vla_only, spatial, s48 |
| 1 | 0% | 3810/24564 MiB | vla_only, spatial, s49 |
| 2 | 17% | 4415/24564 MiB | vla_only, goal, s48 |
| 3 | 35% | 4415/24564 MiB | vla_only, goal, s49 |
| 4 | 18% | 4496/24564 MiB | vla_only, object, s48 |
| 5 | 33% | 4496/24564 MiB | vla_only, object, s49 |

Tmux: 6 sessions（eval-supp-vla-only-{spatial,goal,obj}-s{48,49}）

---

### Server 3: bjb1-18228 ✅ 预期实验在跑

| GPU | 利用率 | 显存 | 实验 |
|-----|--------|------|------|
| 0 | 9% | 580/24564 MiB | train_crm.py (pi05 unified 3suite, epochs 50) |
| 1 | 20% | 4618/24564 MiB | **evaluate.py vla_only, spatial, s42** ✅ |
| 2 | 21% | 4701/24564 MiB | **evaluate.py vla_only, object, s50** ✅ |
| 3 | 23% | 9883/24564 MiB | train_crm.py --precompute pi05 long K=10 |

Tmux: eval-supp-spatial-vla-only-s42, eval-supp-obj-vla-only-s50, train-crm-pi05-unified-3suite-r2

---

### Server 4: bjb2-40593 ❌ K=5 实验未运行！

| GPU | 利用率 | 显存 | 实验 |
|-----|--------|------|------|
| 0 | **0%** | **0/24564 MiB** | **无进程** |

**无 evaluate 进程，无 tmux session，GPU 完全空闲。K=5 实验部署失败。**

---

### Server 5: bjb1-32546 ✅ 6/6 满载

| GPU | 利用率 | 显存 | 实验 |
|-----|--------|------|------|
| 0 | 21% | 1978/24564 MiB | τ-sweep τ=0.10, spatial, s42 |
| 1 | 23% | 1876/24564 MiB | Long-adapt (K=2, s47, crm_unified_4suite_r4) |
| 2 | 22% | 1978/24564 MiB | τ-sweep τ=0.20, spatial, s42 |
| 3 | 21% | 1978/24564 MiB | τ-sweep τ=0.30, spatial, s42 |
| 4 | 29% | 2477/24564 MiB | CRM-reeval (crm_obs_only, object, s47, K=10) |
| 5 | 23% | 1978/24564 MiB | K=1 adaptive, spatial, s42 |

Tmux: 6 sessions 全部匹配

---

## 关键问题

**bjb2-40593 的 K=5 实验完全没有运行** — GPU 空闲 0%/0MiB，无 python 进程，无 tmux session。需要立即重新部署。

bjb2-28827 和 cqa1-32758 的 s48/s49 实验 **部署成功**，全部 12 个实验正常运行中。

---

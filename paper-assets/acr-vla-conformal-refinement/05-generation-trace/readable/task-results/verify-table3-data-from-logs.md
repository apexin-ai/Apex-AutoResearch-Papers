# verify table3 data from logs

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_table3-data-from-logs_20260517T041540_result.json`
- **Structured JSON:** [`9898defffeb7db861b27.json`](../../sessions/98/9898defffeb7db861b27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部4个文件已读取。结果如下：

---

## 实验 1: VLA-only (K=1, seed=42) on LIBERO-Object

**文件**: `/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.json`  
**Overall SR: 12% (12/100)**

Per-task:
| Task | Successes |
|------|-----------|
| alphabet_soup | 0/10 |
| cream_cheese | 1/10 |
| salad_dressing | 2/10 |
| bbq_sauce | 2/10 |
| ketchup | 0/10 |
| tomato_sauce | 1/10 |
| butter | 0/10 |
| milk | 1/10 |
| chocolate_pudding | 2/10 |
| orange_juice | 3/10 |

Sum check: 0+1+2+2+0+1+0+1+2+3 = 12 = 0.12×100 ✓

---

## 实验 2: Argmin / ReconVLA (K=10, seed=42) on LIBERO-Object

**文件**: `/root/acr-vla-conformal-refinement/logs/eval_object_reconvla.json`  
**Overall SR: 12% (12/100)**

Per-task:
| Task | Successes |
|------|-----------|
| alphabet_soup | 0/10 |
| cream_cheese | 0/10 |
| salad_dressing | 1/10 |
| bbq_sauce | 3/10 |
| ketchup | 0/10 |
| tomato_sauce | 0/10 |
| butter | 1/10 |
| milk | 1/10 |
| chocolate_pudding | 3/10 |
| orange_juice | 3/10 |

Sum check: 0+0+1+3+0+0+1+1+3+3 = 12 = 0.12×100 ✓

---

## 实验 3: obs_only ε=0.1 (K=10, seed=42) on LIBERO-Object

**文件**: `/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json`  
**Overall SR: 19% (19/100)**

Per-task:
| Task | Successes |
|------|-----------|
| alphabet_soup | 0/10 |
| cream_cheese | 1/10 |
| salad_dressing | 2/10 |
| bbq_sauce | 4/10 |
| ketchup | 1/10 |
| tomato_sauce | 0/10 |
| butter | 1/10 |
| milk | 2/10 |
| chocolate_pudding | 5/10 |
| orange_juice | 3/10 |

Sum check: 0+1+2+4+1+0+1+2+5+3 = 19 = 0.19×100 ✓

---

## 实验 4: obs_only ε=0.2 (K=10, seed=42) on LIBERO-Object

**文件**: `/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_norm02.json`  
**Overall SR: 22% (22/100)**

Per-task:
| Task | Successes |
|------|-----------|
| alphabet_soup | 0/10 |
| cream_cheese | 0/10 |
| salad_dressing | 3/10 |
| bbq_sauce | 4/10 |
| ketchup | 2/10 |
| tomato_sauce | 1/10 |
| butter | 1/10 |
| milk | 2/10 |
| chocolate_pudding | 6/10 |
| orange_juice | 3/10 |

Sum check: 0+0+3+4+2+1+1+2+6+3 = 22 = 0.22×100 ✓

---

## 关键发现

**VLA-only 确认是 12%**，与 Table 1 一致。文件中 `overall_success_rate: 0.12`。如果 registry 显示 13%，那是 registry 记录有误（可能是其他 seed 或四舍五入）。此文件为 seed=42 的权威数据，Table 1 和 Table 3 可以对齐为 12%。

---

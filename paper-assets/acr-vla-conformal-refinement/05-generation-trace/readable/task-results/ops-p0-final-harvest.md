# ops p0 final harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-final-harvest_20260516T114207_result.json`
- **Structured JSON:** [`58366f9ac808f0229576.json`](../../sessions/58/58366f9ac808f0229576.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## P0 seed44 状态报告

### bjb1-18228: 两个 P0 实验仍在运行（~10h），7/10 tasks 完成

**obs_only ε=0.2 seed44** (PID 428406/428411)
| Task | Result |
|------|--------|
| alphabet_soup | 0/10 |
| cream_cheese | 1/10 |
| salad_dressing | 2/10 |
| bbq_sauce | 2/10 |
| ketchup | 1/10 |
| tomato_sauce | 1/10 |
| butter | 2/10 |
| milk | running... |
| **interim** | **9/70** |

**argmin seed44** (PID 428117/428122)
| Task | Result |
|------|--------|
| alphabet_soup | 0/10 |
| cream_cheese | 0/10 |
| salad_dressing | 1/10 |
| bbq_sauce | 2/10 |
| ketchup | 1/10 |
| tomato_sauce | 1/10 |
| butter | 0/10 |
| milk | not started |
| **interim** | **5/70** |

**ETA**: ~3-4h remaining (3 tasks each).

---

### 其他服务器扫描

**bjb1-32546** (6 GPU active, seed44/45 扩展实验):
- vla-mean-seed44: 4/10 tasks
- obs-only-norm03-seed44: 4/10 tasks
- scalar-seed44-r2: 3/10 tasks
- obs-only-norm01-seed44: 3/10 tasks
- obs-only-default-seed44: 3/10 tasks
- obs-only-norm02-seed45: 2/10 tasks

**bjb2-28827** (6 GPU active, 5 new completed JSONs):
| File | Mode | SR |
|------|------|----|
| perdof_norm003 | crm_perdof | 14.0% (14/100) |
| obs_only_norm005 | crm_obs_only | 13.0% (13/100) |
| perdof_norm005 | crm_perdof | 14.0% (14/100) |
| perdof_norm02_seed43_r3 | crm_perdof | 9.0% (9/100) |
| perdof_norm03_r3 | crm_perdof | 4.0% (4/100) |

**bjb2-40593** (1 GPU active):
- vla-only seed44: **DONE** — SR=10.0% (10/100)
- perdof-default-seed44: 1/10 tasks running

---

### 3-seed Fisher test（待 seed44 完成）

interim 外推（基于 7/10 tasks）:

| seed | obs_only ε=0.2 | argmin | Δ |
|------|----------------|--------|---|
| 42 | 22% (22/100) | 12% (12/100) | +10pp |
| 43 | 16% (16/100) | 17% (17/100) | -1pp |
| 44 | ~13% (9/70 interim) | ~7% (5/70 interim) | ~+6pp |

seed44 尚未完成，无法产出最终 Fisher test 表。预计 3-4h 后可回收。

---

# ops check analyzing experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-analyzing-experiments_20260516T004946_result.json`
- **Structured JSON:** [`df322c4b0cb5d6cb95ce.json`](../../sessions/df/df322c4b0cb5d6cb95ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，汇报如下：

---

### 1. eval-obs-only-object-seed43 (bjb1-18228)

**状态**: 已完成 (EXIT_CODE=0)，进程已退出

**10-task 结果 (mode=crm_obs_only, benchmark=object, seed=43, norm=0.1)**:

| Task | SR |
|------|-----|
| alphabet_soup → basket | 0% (0/10) |
| cream_cheese → basket | 10% (1/10) |
| salad_dressing → basket | 10% (1/10) |
| bbq_sauce → basket | 30% (3/10) |
| ketchup → basket | 0% (0/10) |
| tomato_sauce → basket | 0% (0/10) |
| butter → basket | 0% (0/10) |
| milk → basket | 10% (1/10) |
| chocolate_pudding → basket | 40% (4/10) |
| orange_juice → basket | 20% (2/10) |
| **Overall** | **12.0% (12/100)** |

---

### 2. eval-mag-obsonly-norm003-b2 (bjb2-40593)

**状态**: 已完成 (EXIT_CODE=0)，进程已退出

**10-task 结果 (mode=crm_obs_only, benchmark=spatial, seed=42, norm=0.03)**:

| Task | SR |
|------|-----|
| between_plate_and_ramekin → plate | 90% (9/10) |
| next_to_ramekin → plate | 100% (10/10) |
| from_table_center → plate | 0% (0/10) |
| on_cookie_box → plate | 30% (3/10) |
| in_top_drawer → plate | 10% (1/10) |
| on_ramekin → plate | 0% (0/10) |
| next_to_cookie_box → plate | 80% (8/10) |
| on_stove → plate | 0% (0/10) |
| next_to_plate → plate | 30% (3/10) |
| on_wooden_cabinet → plate | 0% (0/10) |
| **Overall** | **34.0% (34/100)** |

---

### 3. bjb1-18228 GPU 状态

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| cuda:0 | 3804MiB / 24564MiB | 占用 (PID 390936) |
| cuda:1 | 1941MiB / 24564MiB | 占用 (PID 365930) |
| cuda:2 | 1MiB / 24564MiB | **空闲** |
| cuda:3 | 1MiB / 24564MiB | **空闲** |

cuda:2 和 cuda:3 均空闲可用。

---

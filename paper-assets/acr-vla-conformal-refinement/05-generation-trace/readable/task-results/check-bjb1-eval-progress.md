# check bjb1 eval progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-eval-progress_20260515T001515_result.json`
- **Structured JSON:** [`73684d96d37d32b33fbc.json`](../../sessions/73/73684d96d37d32b33fbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 路 Eval 进度快照

**所有 4 个进程均存活。**

| 实验 | PID | Alive | Uptime | Tasks Done | 当前进度 | ETA (剩余) |
|------|-----|-------|--------|------------|---------|------------|
| **argmin-only-spatial** | 231421 | ✓ | 6h27m | 5/10, 跑第6个 | ~55/100 rollouts | ~5.3h |
| **tiny-correction-spatial** | 232815 | ✓ | 6h27m | 5/10, 跑第6个 | ~55/100 rollouts | ~5.3h |
| **acr-spatial-v4-small** | 253085 | ✓ | 3h45m | 3/10, 跑第4个 | ~35/100 rollouts | ~7h |
| **acr-spatial-v4-obs-only-r2** | 270097 | ✓ | 1h54m | 2/10, 跑第3个 | ~25/100 rollouts | ~5.8h |

### 各 Task Success Rate

**argmin-only (reconvla baseline, 无 CRM)**
| Task | Success |
|------|---------|
| between_plate_and_ramekin | 60% (6/10) |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 30% (3/10) |
| in_top_drawer | 10% (1/10) |
| on_ramekin | 运行中 (1/5) |

**tiny-correction (acr_vla, crm_v2, norm=0.05)**
| Task | Success |
|------|---------|
| between_plate_and_ramekin | **70%** (7/10) ↑ |
| next_to_ramekin | 90% (9/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 30% (3/10) |
| in_top_drawer | 0% (0/10) |
| on_ramekin | 运行中 (0/5) |

**v4-small (acr_vla, crm_v3_norm, norm=0.1)**
| Task | Success |
|------|---------|
| between_plate_and_ramekin | 60% (6/10) |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | **10%** (1/10) ↑ |
| on_cookie_box | 运行中 (1/5) |

**obs-only-r2 (crm_obs_only, crm_v3_norm, norm=0.1)**
| Task | Success |
|------|---------|
| between_plate_and_ramekin | **90%** (9/10) ↑↑ |
| next_to_ramekin | **100%** (10/10) |
| from_table_center | 运行中 (0/5) |

### GPU 利用率

| GPU | 显存占用 | 利用率 | 实验 |
|-----|---------|--------|------|
| cuda:0 | 12645/24564 MiB (51%) | 20% | obs-only-r2 |
| cuda:1 | 1423/24564 MiB (6%) | 19% | argmin-only |
| cuda:2 | 1459/24564 MiB (6%) | 21% | tiny-correction |
| cuda:3 | 1459/24564 MiB (6%) | 20% | v4-small |

### 初步观察

- **obs-only-r2** 在前两个 task 上表现最好（90%, 100%），显存占用也最高
- **from_table_center** 对所有方法都极难，仅 v4-small 勉强 10%
- **tiny-correction** (norm=0.05) 对 between_plate 有提升 (70% vs baseline 60%)，但 top_drawer 反而降到 0%

---

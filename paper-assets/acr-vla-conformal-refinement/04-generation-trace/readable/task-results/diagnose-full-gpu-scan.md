# diagnose full gpu scan

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full-gpu-scan_20260519T212809_result.json`
- **Structured JSON:** [`45c9c9f53ea3ac9ad9f5.json`](../../sessions/45/45c9c9f53ea3ac9ad9f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full report.

---

## 1. GPU 状态表

### bjb2-40593 (1× 4090)
| GPU | 利用率 | 显存 | 运行实验 | 空闲? |
|-----|--------|------|----------|-------|
| 0 | 8% | 4496/24564 MiB | eval-vla-only-object-seed48 | No |

### bjb2-28827 (6× 4090)
| GPU | 利用率 | 显存 | 运行实验 | 空闲? |
|-----|--------|------|----------|-------|
| 0 | 0% | 1/24564 MiB | — | **Yes** |
| 1 | 16% | 3840/24564 MiB | calibrate_fmvd.py (k2_l2_calibration) | No |
| 2 | 0% | 1/24564 MiB | — | **Yes** |
| 3 | 0% | 1/24564 MiB | — | **Yes** |
| 4 | 46% | 23005/24564 MiB | eval-openvla-object-baseline-seed42 (tmux) | No |
| 5 | 0% | 1/24564 MiB | — | **Yes** |

### bjb1-18228 (4× 4090)
| GPU | 利用率 | 显存 | 运行实验 | 空闲? |
|-----|--------|------|----------|-------|
| 0 | 10% | 6348/24564 MiB | crm-goal-seed42 + crm-long-seed46 | No |
| 1 | 98% | 8655/24564 MiB | vla-only-object-seed48 + vla-only-long-seed48 | No |
| 2 | 22% | 5630/24564 MiB | vla-only-object-seed50 | No |
| 3 | 27% | 2422/24564 MiB | crm-long-seed45 | No |

### bjb1-32546 (6× 4090)
| GPU | 利用率 | 显存 | 运行实验 | 空闲? |
|-----|--------|------|----------|-------|
| 0 | 8% | 5149/24564 MiB | vla-only-spatial-seed49 | No |
| 1 | 36% | 1996/24564 MiB | crm-goal-seed44 | No |
| 2 | 23% | 5167/24564 MiB | vla-only-object-seed49 | No |
| 3 | 31% | 1996/24564 MiB | crm-goal-seed45 | No |
| 4 | 20% | 3449/24564 MiB | vla-only-long-seed47 | No |
| 5 | 20% | 3032/24564 MiB | vla-only-spatial-seed48 | No |

---

## 2. 已完成实验结果

### crm-long-seed42 (bjb2-28827) — overall: **0.17**
| Task | Rate |
|------|------|
| KITCHEN_SCENE3_stove_moka_pot | 0.8 |
| KITCHEN_SCENE6_mug_microwave | 0.4 |
| LIVING_ROOM_SCENE5_mugs_plates | 0.2 |
| STUDY_SCENE1_book_caddy | 0.2 |
| LIVING_ROOM_SCENE6_mug_plate_pudding | 0.1 |
| 其余 5 个 task | 0.0 |

### crm-long-seed43 (bjb2-28827) — overall: **0.15**
| Task | Rate |
|------|------|
| KITCHEN_SCENE3_stove_moka_pot | 0.8 |
| KITCHEN_SCENE6_mug_microwave | 0.3 |
| LIVING_ROOM_SCENE5_mugs_plates | 0.2 |
| STUDY_SCENE1_book_caddy | 0.2 |
| 其余 6 个 task | 0.0 |

### crm-long-seed44 (bjb2-28827) — overall: **0.20**
| Task | Rate |
|------|------|
| KITCHEN_SCENE3_stove_moka_pot | 0.8 |
| KITCHEN_SCENE6_mug_microwave | 0.6 |
| LIVING_ROOM_SCENE5_mugs_plates | 0.3 |
| STUDY_SCENE1_book_caddy | 0.2 |
| LIVING_ROOM_SCENE6_mug_plate_pudding | 0.1 |
| 其余 5 个 task | 0.0 |

### vla-only-object-seed47 (bjb2-28827) — overall: **0.10**
| Task | Rate |
|------|------|
| salad_dressing | 0.2 |
| bbq_sauce | 0.2 |
| milk | 0.2 |
| chocolate_pudding | 0.2 |
| orange_juice | 0.2 |
| 其余 5 个 task | 0.0 |

### vla-only-long-seed47 (bjb1-32546) — overall: **0.14**
| Task | Rate |
|------|------|
| KITCHEN_SCENE3_stove_moka_pot | 0.8 |
| LIVING_ROOM_SCENE5_mugs_plates | 0.4 |
| STUDY_SCENE1_book_caddy | 0.1 |
| LIVING_ROOM_SCENE6_mug_plate_pudding | 0.1 |
| 其余 6 个 task | 0.0 |

---

## 3. 仍在运行（未出结果）

| 实验 | 服务器 | GPU |
|------|--------|-----|
| crm-long-seed45 | bjb1-18228 | 3 |
| crm-long-seed46 | bjb1-18228 | 0 |
| crm-goal-seed42 | bjb1-18228 | 0 |
| crm-goal-seed44 | bjb1-32546 | 1 |
| crm-goal-seed45 | bjb1-32546 | 3 |
| vla-only-long-seed48 | bjb1-18228 | 1 |
| vla-only-object-seed48 | bjb2-40593 | 0 |
| vla-only-object-seed48 | bjb1-18228 | 1 |
| vla-only-object-seed49 | bjb1-32546 | 2 |
| vla-only-object-seed50 | bjb1-18228 | 2 |
| vla-only-spatial-seed48 | bjb1-32546 | 5 |
| vla-only-spatial-seed49 | bjb1-32546 | 0 |
| openvla-object-seed42 | bjb2-28827 | 4 |
| calibrate_fmvd (k2_l2) | bjb2-28827 | 1 |

---

## 4. 空闲 GPU 列表

| 服务器:GPU | 显存 |
|-----------|------|
| **bjb2-28827:0** | 24564 MiB |
| **bjb2-28827:2** | 24564 MiB |
| **bjb2-28827:3** | 24564 MiB |
| **bjb2-28827:5** | 24564 MiB |

共 **4 块空闲 GPU**，全在 bjb2-28827 上。其余 13 块 GPU 全部在跑实验。

---

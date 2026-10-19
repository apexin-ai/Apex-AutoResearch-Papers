# monitor eval progress check 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_eval-progress-check-2_20260514T174213_result.json`
- **Structured JSON:** [`a7e0765c039ace5fd1a4.json`](../../sessions/a7/a7e0765c039ace5fd1a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 5 个进程存活。bjb2 的 vla-mean-spatial 进度最远（7/10 tasks）。现在汇总：

## 汇总表

| 实验名 | PID | 服务器 | 运行时长 | 进度 | 累计 success |
|--------|-----|--------|----------|------|-------------|
| **eval-acr-spatial-v3** (CORE) | 197057 | bjb1 | 5h25m | Task 4/10 (rollout 5/10) | **1/30 (3.3%)** |
| eval-scalar-unc-spatial-v2 | 197324 | bjb1 | 5h25m | Task 4/10 (rollout 5/10) | 0/30 (0.0%) |
| eval-obs-only-spatial-v3 | 211961 | bjb1 | 4h52m | Task 4/10 开始中 | 0/30 (0.0%) |
| eval-acr-object-v3 | 197803 | bjb1 | 5h25m | Task 4/10 (rollout 5/10) | 0/30 (0.0%) |
| eval-vla-mean-spatial | 143106 | bjb2 | 14h32m | Task 8/10 开始中 | **28/70 (40.0%)** |

## 已完成 task 明细

### eval-acr-spatial-v3 (CORE CLAIM) — 3/10 tasks done

```
Task 1: pick_up_black_bowl_between_plate_and_ramekin  — 1/10 (10%)
Task 2: pick_up_black_bowl_next_to_ramekin            — 0/10 (0%)
Task 3: pick_up_black_bowl_from_table_center          — 0/10 (0%)
Task 4: pick_up_black_bowl_on_cookie_box              — [running: 0/5 at rollout 5]
```

### eval-scalar-unc-spatial-v2 — 3/10 tasks done

```
Task 1: pick_up_black_bowl_between_plate_and_ramekin  — 0/10 (0%)
Task 2: pick_up_black_bowl_next_to_ramekin            — 0/10 (0%)
Task 3: pick_up_black_bowl_from_table_center          — 0/10 (0%)
Task 4: pick_up_black_bowl_on_cookie_box              — [running: 0/5 at rollout 5]
```

### eval-obs-only-spatial-v3 — 3/10 tasks done

```
Task 1: pick_up_black_bowl_between_plate_and_ramekin  — 0/10 (0%)
Task 2: pick_up_black_bowl_next_to_ramekin            — 0/10 (0%)
Task 3: pick_up_black_bowl_from_table_center          — 0/10 (0%)
Task 4: [starting]
```

### eval-acr-object-v3 — 3/10 tasks done

```
Task 1: pick_up_alphabet_soup_place_in_basket         — 0/10 (0%)
Task 2: pick_up_cream_cheese_place_in_basket          — 0/10 (0%)
Task 3: pick_up_salad_dressing_place_in_basket        — 0/10 (0%)
Task 4: pick_up_bbq_sauce_place_in_basket             — [running: 0/5 at rollout 5]
```

### eval-vla-mean-spatial (baseline) — 7/10 tasks done

```
Task 1: pick_up_black_bowl_between_plate_and_ramekin  —  7/10 (70%)
Task 2: pick_up_black_bowl_next_to_ramekin            — 10/10 (100%)
Task 3: pick_up_black_bowl_from_table_center          —  0/10 (0%)
Task 4: pick_up_black_bowl_on_cookie_box              —  3/10 (30%)
Task 5: pick_up_black_bowl_in_top_drawer              —  0/10 (0%)
Task 6: pick_up_black_bowl_on_ramekin                 —  0/10 (0%)
Task 7: pick_up_black_bowl_next_to_cookie_box         —  8/10 (80%)
Running total: 28/70 (40.0%)
```

## 关键观察

**VLA baseline (mean) 在 spatial 上跑出 40% success rate**，而同 benchmark 的 3 个 CRM 变体（acr_vla / crm_scalar / crm_obs_only）前 3 个 task 几乎全 0。ACR 核心方法 (eval-acr-spatial-v3) 仅在 task 1 拿到 1/10。

这意味着 **CRM refinement 当前不仅没有提升 VLA baseline，反而严重拖累了性能**。所有 CRM 方法在 VLA baseline 能做对的 task（如 task 1: 70%, task 2: 100%）上都接近 0%。

bjb1 上 4 个实验约完成 30-40%，预计还需 ~7-8 小时完成。bjb2 的 vla-mean-spatial 约 70% 完成，预计还需 ~4-5 小时。

---

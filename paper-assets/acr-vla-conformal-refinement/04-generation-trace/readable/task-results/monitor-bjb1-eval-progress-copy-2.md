# monitor bjb1 eval progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb1-eval-progress_20260514T181345_result.json`
- **Structured JSON:** [`897723bc3882044ec1af.json`](../../sessions/89/897723bc3882044ec1af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

| exp_id | PID | alive | runtime | GPU | GPU util | tasks done | current SR | status |
|--------|-----|-------|---------|-----|----------|-----------|------------|--------|
| eval-acr-spatial-v3 | 197057 | ✓ | 5h57m | cuda:0 | 11% | 4/10 | **1/40 (2.5%)** | running task 5 |
| eval-acr-object-v3 | 197803 | ✓ | 5h57m | cuda:3 | 20% | 4/10 | **0/40 (0%)** | running task 5 |
| eval-argmin-only-spatial | 231421 | ✓ | 26m | cuda:1 | 99% | 0/10 | — | loaded, no rollouts yet |
| eval-tiny-correction-spatial | 232815 | ✓ | 25m | cuda:2 | 98% | 0/10 | **4/5 so far** | task 1 rollout 5/10 |

### Per-task breakdown: eval-acr-spatial-v3 (CORE CLAIM)

| # | task | success |
|---|------|---------|
| 1 | pick_up_black_bowl_between_plate_and_ramekin → plate | **1/10 (10%)** |
| 2 | pick_up_black_bowl_next_to_ramekin → plate | 0/10 (0%) |
| 3 | pick_up_black_bowl_from_table_center → plate | 0/10 (0%) |
| 4 | pick_up_black_bowl_on_cookie_box → plate | 0/10 (0%) |
| 5-10 | (in progress) | — |

### Per-task breakdown: eval-acr-object-v3

| # | task | success |
|---|------|---------|
| 1 | alphabet_soup → basket | 0/10 |
| 2 | cream_cheese → basket | 0/10 |
| 3 | salad_dressing → basket | 0/10 |
| 4 | bbq_sauce → basket | 0/10 |
| 5-10 | (in progress) | — |

### 关键发现

**eval-tiny-correction-spatial (max_correction_norm=0.05) 在第一个 task 上 4/5 成功。** 这和 full ACR 在同一个 task 上只有 1/10 形成鲜明对比。如果这个趋势持续，说明 CRM 的大幅度 correction 反而在破坏 VLA 的 action——小幅修正效果更好。

Core claim 实验 (spatial-v3) 目前 2.5% 整体成功率，object-v3 为 0%。预计还需约 ~6 小时完成全部 10 个 task。

---

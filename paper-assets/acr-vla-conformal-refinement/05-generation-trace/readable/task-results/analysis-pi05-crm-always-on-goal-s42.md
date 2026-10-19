# analysis pi05 crm always on goal s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-crm-always-on-goal-s42_20260528T015252_result.json`
- **Structured JSON:** [`d83718282f5eef5fd1f4.json`](../../sessions/d8/d83718282f5eef5fd1f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新完成。

## 结果摘要

| 指标 | 值 |
|------|-----|
| **SR** | **81.5%** (163/200) |
| Baseline VLA-only | 97.8% |
| **Δ** | **-16.3pp** |
| trigger_rate | 100% |
| mean_unc | 0.145 |
| mean_correction_norm | 0.200 (饱和在 max) |
| total_steps / crm_applied | 29409 / 29409 |

**Per-task breakdown:**

| Task | SR |
|------|-----|
| open_the_middle_drawer_of_the_cabinet | **25%** |
| put_the_wine_bottle_on_the_rack | **40%** |
| open_the_top_drawer_and_put_the_bowl_inside | 70% |
| put_the_wine_bottle_on_top_of_the_cabinet | 90% |
| put_the_cream_cheese_in_the_bowl | 95% |
| turn_on_the_stove | 95% |
| put_the_bowl_on_the_stove / on_top_of_cabinet / on_plate / push_plate | 100% |

**分析：** CRM always-on 对 Pi05 Goal 造成严重退化（-16.3pp），远大于 Spatial 的 -1pp。退化集中在精细操控任务（drawer 25%、wine rack 40%），correction_norm 全程饱和在 0.2 说明 CRM 每步都施加最大修正，干扰了 Pi05 原本高质量的动作。与 SmolVLA Goal 的 -3.7pp 对比，Pi05 受 always-on CRM 伤害更大——可能因为 Pi05 baseline 更强（97.8% vs 83.7%），被修正的"正确"动作比例更高。这有力支持了 conformal gating 的必要性。

---

# harvest bjb1 32546 5exp results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546-5exp-results_20260523T141527_result.json`
- **Structured JSON:** [`acc8a8dae26a415941f4.json`](../../sessions/ac/acc8a8dae26a415941f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个实验全部处理完毕。汇总如下：

| exp_id | SR | per_task (关键) | conclusion |
|--------|-----|----------------|------------|
| eval-supp-goal-vla-only-wrapper-s43 | **82.5%** | cream_cheese 45%, drawer_bowl 60%, 其余 ≥85% | success (≈83.5% baseline) |
| eval-supp-goal-vla-only-wrapper-s44 | **LOST** | JSON 被 k2mean-s44 覆盖（同输出文件名） | failed — 需重跑 |
| eval-supp-crm-norm005-obj-s44 | **74.0%** | alphabet_soup/cream_cheese/milk 60%, orange_juice 95% | negative (3-seed: 77.0/78.5/74.0, mean=76.5% < baseline 77.8%) |
| eval-supp-adapt-tau025-obj-s44 | **75.0%** | trigger_rate=3.6%, tomato/butter 65% | negative (3-seed: 81.0/77.5/75.0, mean=77.8% ≈ baseline, 高方差) |
| eval-supp-k2mean-goal-s44 | **82.0%** | cream_cheese 45%, drawer_bowl 60%, wine_rack 75% | negative (低于 VLA-only 83.5%) |

**关键发现：**
- Goal VLA-only s43=82.5% 确认 baseline 稳定在 ~83%
- wrapper s44 结果丢失：两个实验（wrapper-s44 和 k2mean-s44）写同一个 `eval_goal_vla_only_seed44.json`，k2mean 晚 3 分钟完成覆盖了 wrapper 结果。**需要用不同 output_file 重跑 wrapper s44**
- Object CRM 和 Adaptive 在 s44 上均显著低于前两个 seed，Object 方法总体偏 negative

---

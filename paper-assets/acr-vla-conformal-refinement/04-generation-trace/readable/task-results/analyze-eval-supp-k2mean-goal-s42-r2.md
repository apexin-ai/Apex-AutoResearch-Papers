# analyze eval supp k2mean goal s42 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-k2mean-goal-s42-r2_20260523T114759_result.json`
- **Structured JSON:** [`e6d250665a25cd6e01c8.json`](../../sessions/e6/e6d250665a25cd6e01c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval-supp-k2mean-goal-s42-r2 结果

| 指标 | 值 |
|------|-----|
| **Overall SR** | **85.5% (171/200)** |
| 对比 VLA-only baseline | +2.0pp (83.5% → 85.5%) |
| 对比 K=2 mean s43 | +4.0pp (81.5% → 85.5%) |

### Per-task

| Task | SR |
|------|-----|
| put_the_bowl_on_the_stove | 100% |
| turn_on_the_stove | 100% |
| put_the_bowl_on_the_plate | 100% |
| put_the_bowl_on_top_of_the_cabinet | 95% |
| push_the_plate_to_the_front_of_the_stove | 95% |
| put_the_wine_bottle_on_top_of_the_cabinet | 90% |
| open_the_middle_drawer_of_the_cabinet | 80% |
| put_the_wine_bottle_on_the_rack | 80% |
| open_the_top_drawer_and_put_the_bowl_inside | 65% |
| put_the_cream_cheese_in_the_bowl | 50% |

### 结论
K=2 mean 在 Goal s42 上 SR=85.5%，高于 VLA-only baseline (83.5%)。两个 seed 间方差较大（s42=85.5% vs s43=81.5%），平均 83.5% 与 baseline 持平。Cron 已删除，registry 已更新为 DONE(success)。

**bjb2-40593:cuda:0 已释放**，可部署新实验。

---

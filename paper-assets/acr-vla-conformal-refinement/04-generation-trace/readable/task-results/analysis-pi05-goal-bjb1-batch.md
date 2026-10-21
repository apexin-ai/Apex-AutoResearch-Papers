# analysis pi05 goal bjb1 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-goal-bjb1-batch_20260526T133933_result.json`
- **Structured JSON:** [`7a1d1df7ab850ec1487b.json`](../../sessions/7a/7a1d1df7ab850ec1487b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| exp_id | seed | success_rate | rollouts | conclusion |
|--------|------|-------------|----------|------------|
| pi05-crm-k2-goal-s42-bjb1-r2 | 42 | 82.5% | 165/200 | success |
| pi05-crm-k2-goal-s43-bjb1-r2 | 43 | 83.0% | 166/200 | success |
| pi05-crm-k2-goal-s44-bjb1-r2 | 44 | 85.0% | 170/200 | success |
| **Mean ± Std** | | **83.5% ± 1.3%** | | |

π0.5 VLA-only baseline on Goal ~96%，CRM K=2 always-on 降到 83.5%，下降约 12.5 个百分点。CRM 对近 expert 水平的 π0.5 产生了明显的性能损害——符合预期，always-on correction 在高性能 VLA 上 over-corrects。

---

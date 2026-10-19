# harvest old preparing experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_old-preparing-experiments_20260521T041745_result.json`
- **Structured JSON:** [`a11925afd51eb72cab6c.json`](../../sessions/a1/a11925afd51eb72cab6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 29 experiments processed: 26 marked DONE with metrics, 3 missing JSONs flagged.

## 汇总表

| # | exp_id | server | JSON exists? | SR | 备注 |
|---|---|---|---|---|---|
| 1 | eval-vla-only-spatial-seed54 | bjb1-32546 | ✓ | 0.27 | DONE |
| 2 | eval-crm-long-seed54 | bjb1-32546 | ✓ | 0.19 | DONE |
| 3 | eval-crm-long-seed49 | bjb1-32546 | ✓ | 0.14 | DONE |
| 4 | eval-crm-long-seed48 | bjb1-32546 | ✓ | 0.15 | DONE |
| 5 | eval-crm-spatial-k10-seed50 | bjb1-32546 | ✓ | 0.35 | DONE |
| 6 | eval-vla-only-long-seed53 | bjb1-32546 | ✓ | 0.12 | DONE |
| 7 | eval-vla-only-goal-seed52 | bjb1-32546 | ✓ | 0.68 | DONE |
| 8 | eval-crm-long-seed51 | bjb1-32546 | ✓ | 0.13 | DONE |
| 9 | eval-vla-only-spatial-seed51 | bjb1-32546 | ✓ | 0.33 | DONE |
| 10 | eval-vla-only-object-seed51 | bjb1-32546 | ✓ | 0.15 | DONE |
| 11 | eval-crm-spatial-seed48 | bjb1-32546 | ✓ | 0.35 | DONE |
| 12 | eval-obs-only-object-norm02-k20-seed42 | bjb1-32546 | ✗ | — | 进程可能仍在运行或已失败，未更新 |
| 13 | eval-obs-only-goal-norm02-seed53 | bjb1-32546 | ✓ | 0.63 | DONE |
| 14 | eval-vla-only-long-seed54 | bjb1-18228 | ✓ | 0.12 | DONE |
| 15 | eval-crm-long-seed53 | bjb1-18228 | ✓ | 0.18 | DONE |
| 16 | eval-vla-only-spatial-seed53 | bjb1-18228 | ✓ | 0.28 | DONE |
| 17 | eval-vla-only-spatial-seed52 | bjb1-18228 | ✓ | 0.31 | DONE |
| 18 | eval-vla-only-spatial-seed50 | bjb1-18228 | ✓ | 0.30 | DONE |
| 19 | eval-crm-spatial-seed47 | bjb1-18228 | ✓ | 0.32 | DONE |
| 20 | eval-vla-only-object-seed49-r2 | bjb1-18228 | ✓ | 0.10 | DONE |
| 21 | eval-obs-only-object-norm02-k20-seed43 | bjb1-18228 | ✗ | — | 进程可能仍在运行或已失败，未更新 |
| 22 | eval-crm-spatial-k10-seed49 | bjb2-28827 | ✓ | 0.32 | DONE |
| 23 | eval-crm-goal-seed48 | bjb2-28827 | ✓ | 0.68 | DONE |
| 24 | eval-crm-goal-seed47 | bjb2-28827 | ✓ | 0.69 | DONE |
| 25 | eval-crm-goal-seed50 | bjb2-28827 | ✓ | 0.67 | DONE |
| 26 | eval-crm-goal-seed49 | bjb2-28827 | ✓ | 0.62 | DONE |
| 27 | eval-crm-long-seed52 | bjb2-28827 | ✓ | 0.15 | DONE |
| 28 | eval-vla-only-long-seed49 | bjb2-28827 | ✓ | 0.16 | DONE |
| 29 | eval-vla-only-spatial-seed49-r2 | bjb2-28827 | ✗ | — | 进程可能仍在运行或已失败，未更新 |

**统计**：26 个已收割到 DONE（全部 SR > 0，conclusion=success），3 个 JSON 缺失保持 PREPARING。

**关键观察**：
- VLA-only goal seed52 = 0.68 vs CRM goal (47/48/49/50) = 0.62-0.69 — CRM 在 goal 任务上与 VLA-only 持平甚至略低
- CRM long (0.13-0.19) vs VLA-only long (0.12, 0.16) — long-horizon 上 CRM 提升微弱
- CRM spatial (0.32-0.35) vs VLA-only spatial (0.27-0.33) — spatial 上 CRM 有小幅领先

**注**：registry 中 spec.command 填的是占位 "harvest"，因为原始 submit_training_job 的命令未保留；checkpoint_path 和 log_path 都指向同一 JSON 文件（eval 类任务无独立训练 checkpoint）。

---

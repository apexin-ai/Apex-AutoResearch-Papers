# deploy bjb1 18228 fill gpus

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-fill-gpus_20260517T135353_result.json`
- **Structured JSON:** [`55d51bc794315c2e6f31.json`](../../sessions/55/55d51bc794315c2e6f31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**结果**：4 个实验已由另一个 Worker 在 21:35-21:37 提交并运行，本次操作仅完成 registry 同步（4 个条目全部更新为 RUNNING）。

| GPU | exp_id | PID | 状态 |
|-----|--------|-----|------|
| cuda:0 | eval-perdof-object-norm02-seed45-r2 | 634438 | RUNNING |
| cuda:1 | eval-obs-only-object-norm005-seed43-r3 | 633649 | RUNNING |
| cuda:2 | eval-obs-only-object-norm02-k5-seed42 | 633662 | RUNNING |
| cuda:3 | eval-obs-only-object-norm02-k20-seed42 | 636638 | RUNNING |

**注意**：perdof seed45 的实际 exp_id 是 `r2` 而非任务要求的 `r3`。报告已注册为 artifact `art_20260517_ecac67`。

---

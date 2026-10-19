# registry fix untracked running experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry-fix_untracked-running-experiments_20260519T152804_result.json`
- **Structured JSON:** [`a14fb0adb3c5287eef46.json`](../../sessions/a1/a14fb0adb3c5287eef46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个实验已成功注册为 RUNNING。汇总：

## Registry 追踪修复完成

| Registry ID | Server | GPU | PID | 状态 |
|---|---|---|---|---|
| `eval-random-selection-object-k5-seed42-r2` | bjb1-32546 | cuda:5 | 939548 | RUNNING |
| `eval-random-selection-object-k5-seed43-r2` | bjb2-28827 | cuda:0 | 841426 | RUNNING |
| `eval-random-selection-object-k5-seed44-r2` | bjb1-32546 | cuda:2 | 942029 | RUNNING |
| `eval-random-selection-object-k5-seed45-r2` | bjb1-32546 | cuda:3 | 942099 | RUNNING |
| `eval-obs-only-spatial-norm02-k5-seed44-r2` | bjb2-28827 | cuda:2 | 843594 | RUNNING |
| `eval-obs-only-spatial-norm02-k5-seed45-r2` | bjb2-28827 | cuda:5 | 845019 | RUNNING |

**额外发现**（服务器上还在跑但不在本次任务范围内的实验）：
- bjb1-32546: crm_obs_only object seed42 K=20 norm0.2 (GPU 1), crm_obs_only spatial seed47 K=10 norm0.2 (GPU 1)
- bjb2-28827: reconvla object seed44 K=5 (GPU 1), random_selection seed46 K=10 (GPU 2), crm_obs_only spatial seed46 K=10 norm0.2 (GPU 3)

---

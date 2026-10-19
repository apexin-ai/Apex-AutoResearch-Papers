# deploy random selection object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_random-selection-object_20260521T043257_result.json`
- **Structured JSON:** [`1abe8196c2c0329d2f24.json`](../../sessions/1a/1abe8196c2c0329d2f24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 jobs running on bjb1-32546:

| exp_id | GPU | PID | Status |
|---|---|---|---|
| eval-random-selection-object-seed42-r3 | cuda:0 | 852344 | Loading SmolVLA weights |
| eval-random-selection-object-seed43 | cuda:1 | 852632 | Loading SmolVLA weights |
| eval-random-selection-object-seed44 | cuda:3 | 853229 | Started, loading model |

All using `--mode random_selection --benchmark object --K 10 --n_rollouts 10`. Logs show clean startup; no python path errors.

注意：registry 中 seed43/seed44 已有 prior DONE 结果（SR=0.09/0.11，来自 bjb2-28827）。当前 hypothesis 已按任务覆盖更新，新 run 完成后会覆盖 metrics。

---

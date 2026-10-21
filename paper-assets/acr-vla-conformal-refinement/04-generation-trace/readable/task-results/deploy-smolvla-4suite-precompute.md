# deploy smolvla 4suite precompute

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-4suite-precompute_20260522T154138_result.json`
- **Structured JSON:** [`1baebf9c6f289ffd99c1.json`](../../sessions/1b/1baebf9c6f289ffd99c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 tmux sessions 已就绪。

**long suite 状况**：cuda:3-5 被 Pi0-5 goal precompute 占用（还需 ~8.5h）。最快路径是等 object precompute 完成后（object 只有 ~3020 samples，预计 eval 结束后 ~1-2h），在 cuda:0 上串行跑 long。

是否现在就提交 long（带 wait wrapper 等 object 完成），还是等后续手动提交？

---

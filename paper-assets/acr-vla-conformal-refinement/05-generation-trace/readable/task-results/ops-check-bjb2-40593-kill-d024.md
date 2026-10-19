# ops check bjb2 40593 kill d024

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-bjb2-40593-kill-d024_20260515T050106_result.json`
- **Structured JSON:** [`dae183219ce3032538ca.json`](../../sessions/da/dae183219ce3032538ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇报：**

- **v4-default-r3**：已无相关进程，确认已被 kill。无 tmux session、无 python 进程与之关联。
- **GPU 状态**：GPU 0 使用 5592 MiB / 24564 MiB — 被 reconvla-object 占用。
- **reconvla-object**：正在运行（PID 211962），tmux session `eval-reconvla-object` 存在，运行 `evaluate.py --benchmark object --mode reconvla --K 10 --n_rollouts 20`，已运行约 275 分钟，未触碰。

**结论**：v4-default-r3 已死，无需额外操作。GPU 被 reconvla-object 正常占用，不空闲。

---

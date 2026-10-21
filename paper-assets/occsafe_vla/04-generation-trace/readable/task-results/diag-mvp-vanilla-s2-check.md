# diag mvp vanilla s2 check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp_vanilla_s2_check_20260521T003549_result.json`
- **Structured JSON:** [`e24dc9d59bd68235c34c.json`](../../sessions/e2/e24dc9d59bd68235c34c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**mvp_vanilla_s2 训练已完成，cron 假阳性确认。**

检查结果：
- `50000_chkpt` 存在且完整（4 model shards + action_head + proprio_projector + lora_adapter）
- 日志末尾: `"Max step 50005 reached! Stopping training..."` + `"Saved merged model for Step 50000"`
- Eval 已由 monitor_and_eval.sh 自动触发（PID 366329），正在跑 `evaluate_safelibero.py --num_rollouts 20`

Registry 已更新：conclusion → success，checkpoint_path 已设置，notes 已修正。Memory.md 已同步。

---

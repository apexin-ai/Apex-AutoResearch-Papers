# ops eval fix final attempt

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_fix_final_attempt_20260523T204307_result.json`
- **Structured JSON:** [`0be162500c19a78b3cb2.json`](../../sessions/0b/0be162500c19a78b3cb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过，两个 eval 正常运行：

| Eval | PID | GPU | 显存占用 | 进度 |
|------|-----|-----|---------|------|
| cutoff_25k_s0_eval | 502805 | GPU 3 | 16778 MiB | T0: 42% (21/50) |
| reverse_cutoff_s0_eval | 503988 | GPU 2 | 16778 MiB | T0: 26% (13/50) |

- 两个进程均在运行，无 error/traceback
- 日志显示正常 rollout 进度（~4s/it）
- `--num_rollouts 50` 参数生效，总计 50 个 rollout
- GPU 0/1 被其他任务占用（99%），GPU 2/3 被 eval 使用

---

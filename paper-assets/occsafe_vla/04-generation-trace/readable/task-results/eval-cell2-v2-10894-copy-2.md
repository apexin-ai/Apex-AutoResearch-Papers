# eval cell2 v2 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cell2_v2_10894_20260527T155059_result.json`
- **Structured JSON:** [`0ca6281602543caf01a4.json`](../../sessions/0c/0ca6281602543caf01a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已正常运行：

| Eval | GPU | PID | 进度 | Log |
|------|-----|-----|------|-----|
| `full_occ_ln_v2_s1c_eval` | cuda:0 | 599628 | T0: 27/50 (~54%) | `~/runs/occsafe_vla/full_occ_ln_v2_s1c_eval.log` |
| `full_occ_ln_v2_s2_eval` | cuda:1 | 600090 | T0: 28/50 (~56%) | `~/runs/occsafe_vla/full_occ_ln_v2_s2_eval.log` |

进度条显示 ~4.4s/rollout，当前 Task 0 已过半。10 个 task x 50 rollout，按此速度预计每个 eval 总耗时约 3-4 小时，应在 DDL 前完成。cuda:2/3 未触碰。

---

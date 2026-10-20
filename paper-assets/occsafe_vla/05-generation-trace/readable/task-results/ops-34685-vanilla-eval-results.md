# ops 34685 vanilla eval results

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_34685-vanilla-eval-results_20260526T233020_result.json`
- **Structured JSON:** [`d194a3487658694d22cd.json`](../../sessions/d1/d194a3487658694d22cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Eval 结果**

| Experiment | TSR | CAR | Collisions/500 |
|---|---|---|---|
| vanilla_v2_s1_eval | 0.908 | 0.748 | 126 |
| vanilla_v2_s2_eval | 0.844 | 0.720 | 140 |

Registry 已更新为 DONE/success。

**已启动训练**

| Experiment | GPU | PID | Server |
|---|---|---|---|
| detach_ln_v2_s1 | cuda:0 | 681124 | westd-34685 |
| detach_ln_s4 | cuda:1 | 677568 | westd-34685 |

westd-34685 当前 4 GPU 全部在用：cuda:0-1 新训练，cuda:2-3 继续跑 detach_ln_s3_eval 和 cutoff_25k_s1_v2_eval。

---

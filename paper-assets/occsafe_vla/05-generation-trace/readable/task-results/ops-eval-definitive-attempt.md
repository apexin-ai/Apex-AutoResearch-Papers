# ops eval definitive attempt

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_definitive_attempt_20260523T204909_result.json`
- **Structured JSON:** [`17b76b09911297517dc2.json`](../../sessions/17/17b76b09911297517dc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**验证结果汇总：**

| 检查项 | reverse_cutoff_s0_eval | cutoff_25k_s0_eval |
|--------|----------------------|-------------------|
| tmux session | ✅ 存在 | ✅ 存在 |
| Python PID | ✅ 518746 | ✅ 519021 |
| GPU | ✅ GPU 2: 16778 MiB / 97887 MiB | ✅ GPU 3: 16778 MiB / 97887 MiB |
| 日志 | ✅ T0: 12% (6/50), ~4.4s/it | ✅ T0: 14% (7/50), ~4.1s/it |
| 错误 | 无 | 无 |

两个 eval 均在正常执行 libero_spatial 任务（10 tasks × 50 rollouts），当前都在 Task 0 的 rollout 阶段，每个 rollout 约 4-5 秒。预计总运行时间约 35-40 分钟。

---

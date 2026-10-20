# infra check monitor alive

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_monitor_alive_20260521T043158_result.json`
- **Structured JSON:** [`aea610e830014470fb83.json`](../../sessions/ae/aea610e830014470fb83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Monitor PID 61526: alive (monitoring PIDs 27667/58802/29970)

occ_s0: step ~44790/50005 (89%), alive, ETA ~1h20m, 1.08 it/s
         最新 checkpoint: 42500

occ_s1: step ~19500/50005 (~39%), alive (PID 58802→58875)
         原始运行崩溃 (exitcode 1)，已从 step 7500 恢复
         最新 checkpoint: 17500
         ⚠️ 进度远落后于 s0/s2，预计还需 ~7.8h 完成

occ_s2: step ~44862/50005 (90%), alive, ETA ~1h19m, 1.08 it/s
         最新 checkpoint: 42500

eval_results: 仅有 monitor_status.txt，暂无 occ 评估结果
```

occ_s1 因崩溃重启，进度严重落后。s0 和 s2 约 1.5h 后完成训练，s1 还需约 8 小时。

---

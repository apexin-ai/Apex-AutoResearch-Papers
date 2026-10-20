# eval ablation 50r monitor and rerun

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ablation-50r-monitor-and-rerun_20260522T020237_result.json`
- **Structured JSON:** [`570eabb2be008c19c558.json`](../../sessions/57/570eabb2be008c19c558.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态总结：

| GPU | 任务 | seed 42 | 进度 | 预计完成 |
|-----|------|---------|------|----------|
| 0 | detach_s0 | ✅ 有 | T6 48% (~63%) | ~15 min |
| 1 | random_s0 | ❌ 无 | T6 56% (~65%) | ~15 min → 完成后重跑 |
| 2 | detach_s1 | ✅ 有 | T0 84% (~8%) | ~35 min |
| 3 | random_s1 | ✅ 有 | T0 84% (~8%) | ~35 min |

**detach_s0 已带 seed 42**，不需要重跑。只有 **random_s0** 需要完成后重跑。

3 分钟后继续检查进度。

---

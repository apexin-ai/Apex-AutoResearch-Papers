# diagnose eval random selection object k5 seed44 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-random-selection-object-k5-seed44-r2_20260519T162826_result.json`
- **Structured JSON:** [`079194e5ca97caeddf18.json`](../../sessions/07/079194e5ca97caeddf18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。总结：

**假阳性失败** — 实验已正常完成，不是 crash/OOM/GPU 冲突。

- `evaluate.py` 在 `random_selection` 模式下只写本地 JSON，不向 W&B 上报 metrics
- CRON 监控以"无 W&B metrics"判定失败，是检测逻辑与实验类型不匹配
- 结果文件已存在：**overall success rate = 10.0% (10/100)**
- GPU2 已空闲，无残留进程

**同批 6 个 r2 实验大概率都是同一原因**，建议批量检查其他 5 个的 JSON 输出是否也已生成，避免不必要的重跑。

---

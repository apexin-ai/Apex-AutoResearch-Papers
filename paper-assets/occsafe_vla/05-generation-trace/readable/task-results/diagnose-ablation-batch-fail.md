# diagnose ablation batch fail

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ablation_batch_fail_20260521T051349_result.json`
- **Structured JSON:** [`11782bedb2870db8ac9a.json`](../../sessions/11/11782bedb2870db8ac9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：SeetaCloud/WestD 平台在 `12:52:12 UTC+8` 同时向 4 个进程发送 SIGTERM。非 OOM、非重启、非 crontab——是平台级 kill（计费到期/维护最可能）。

**进度**：
- s0 两组跑到 ~4000 步（8%），有 step 2500 完整 checkpoint，可 resume
- s1 两组只跑到 ~1545 步（3%），无 checkpoint，需从头来

**环境完好**，可以直接重跑。关键是先去 WestD 控制台确认实例计费状态，避免再被 kill。

---

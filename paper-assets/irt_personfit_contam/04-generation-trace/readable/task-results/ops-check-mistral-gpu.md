# ops check mistral gpu

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-mistral-gpu_20260526T111128_result.json`
- **Structured JSON:** [`9fb56ee19238580fb33e.json`](../../sessions/9f/9fb56ee19238580fb33e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-35694 无法连接。** 所有 SSH 连接均返回 `Unable to connect to port 35694 on 36.103.198.204`。

这是 AutoDL 实例，重启后 SSH 端口会变。当前实例可能：
1. **已关机/休眠** — 需要去 AutoDL 控制台开机
2. **端口已变** — 需要去控制台查看新的 SSH 端口，然后更新 `~/.ssh/config`

请去 AutoDL 控制台确认实例状态和当前 SSH 端口。

---

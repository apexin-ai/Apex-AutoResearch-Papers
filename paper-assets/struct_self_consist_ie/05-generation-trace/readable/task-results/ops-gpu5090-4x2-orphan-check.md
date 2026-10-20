# ops gpu5090 4x2 orphan check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu5090-4x2-orphan-check_20260514T174207_result.json`
- **Structured JSON:** [`e0baf8deb543bb7e5db4.json`](../../sessions/e0/e0baf8deb543bb7e5db4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告写入 `artifacts/audit_gpu5090_4x2_loop3.md`。

结论：`gpu-5090-4x-2` 不在可用服务器列表中（仅 autodl-5090、bjb1-21071），无法 SSH 连接。全部 6 个实验（PID 61812/62170/48530/50302/53600/62585）确认已死，应在 registry 中标记为 KILLED。输出数据无法检查，除非该服务器被重新注册或数据曾同步到其他位置。

---

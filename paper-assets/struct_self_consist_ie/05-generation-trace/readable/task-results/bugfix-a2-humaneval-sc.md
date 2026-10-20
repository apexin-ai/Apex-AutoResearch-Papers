# bugfix a2 humaneval sc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_a2_humaneval_sc_20260520T203502_result.json`
- **Structured JSON:** [`e7f9f4d2b108a552c2d8.json`](../../sessions/e7/e7f9f4d2b108a552c2d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**Bug 1 修复**: `api_sample_greedy()` 的 `temperature` — API 只支持 `T=1.0`（设 0 返回 400），已保留 `T=1.0` 并加注释说明这是 single-sample baseline 而非真正 greedy。

**Bug 2 验证**: MV 逻辑已正确，投票在 `all_codes`（所有 N 个 samples）上，非仅 passing samples。无需修复。

**运行状态**:
- PID: **1501109**（本地 nohup，`python -u` 无缓冲）
- API 连通性: OK
- 已清除旧 checkpoint 并重跑，当前已恢复 5 个 problems，继续处理剩余 159 个
- 日志: `humaneval_sc.log`
- Registry 已更新为 RUNNING

---

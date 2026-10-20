# experiment mvp v3b submit

**turn hier kv compress** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mvp_v3b_submit_20260513T162356_result.json`
- **Structured JSON:** [`d5c88495f734bee2a115.json`](../../sessions/d5/d5c88495f734bee2a115.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Step 1** — role_extractor 已原生支持 ipython → TOOL_RESULT、`&lt;think>` → THINKING_TRACE。65 条 trace 全部解析成功，段类型覆盖完整。

**Step 2** — dry-run 通过。2 条 trace（含 think / ipython）× 3 方法 × CR=0.7，无 crash，结果合理。

**Step 3** — 两个实验已提交并运行：
- `mvp_v3b_cr70` → cuda:0, PID 99059
- `mvp_v3b_cr85` → cuda:1, PID 99138

**Step 4** — GPU 负载确认（各 ~15GB），registry 已更新为 RUNNING，spec 包含完整 provenance。

---

# exec llama 3seed recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_llama_3seed_recompute_20260515T063216_result.json`
- **Structured JSON:** [`6ac00180b3dbc380343f.json`](../../sessions/6a/6ac00180b3dbc380343f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- **seed42 NER SJ ρ = 0.3096** — 与 registry 值完全一致
- seed42 FK ρ = 0.2352, LP ρ = 0.1503 — 均符合预期
- JSON 时间戳：2026-05-15 14:32，刚生成

注意输出文件名是 `llama_scierc_3seed_fresh_summary.json`（带 `_fresh` 后缀），不是 `llama_scierc_3seed_summary.json`。如果下游需要读 `llama_scierc_3seed_summary.json`，需要确认是否要重命名或更新引用路径。

---

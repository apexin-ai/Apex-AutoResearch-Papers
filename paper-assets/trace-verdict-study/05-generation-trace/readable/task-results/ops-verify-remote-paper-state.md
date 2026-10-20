# ops verify remote paper state

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_remote_paper_state_20260521T171826_result.json`
- **Structured JSON:** [`799dd52efa872ef0511d.json`](../../sessions/79/799dd52efa872ef0511d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

- **PDF MD5**: `356c7f244fdb0109f04b3f68f17e365e` — 与预期值一致 ✅
- **三处 appendix 修复**:
  - per_class table: 99.41 (VOTA), 85.63 (Loop Only), 86.22 (Full Trace LO) — 在 ✅
  - `tab:calibration_model_level` 整段 — 已删除 ✅
  - DeepSeek ECE=0.0049, Brier=0.0059, MCE=0.4692 (L563) + 正文描述 (L549) — 在 ✅
- **页数**: 22 页

远程论文状态正确，sync worker 未覆盖修复。无需重新编译。

---

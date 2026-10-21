# ops cuda2 relay 8b no evidence eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda2_relay_8b_no_evidence_eval_20260516T111025_result.json`
- **Structured JSON:** [`48560fbbf186269c6050.json`](../../sessions/48/48560fbbf186269c6050.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Phase 1 结果 — 1.7B no-evidence eval (plan_006_qwen3_1_7b_no_evidence_eval)**:
- Ign-F1 = **0.3786**, F1 = 0.3884, Evi-F1 ≈ 0 (符合预期，no-evidence 模型不生成证据)
- Registry → DONE/success

**Phase 3 — 8B no-evidence eval 已提交**:
- PID 334598, cuda:2, 推理中 (247 batches, 预计 ~1.7h 基于 1.7B 的 25s/it，8B 会更慢)
- Registry → RUNNING

1.7B 模型在 25s/it 完成了推理；8B 模型加载成功并已开始 inference。

---

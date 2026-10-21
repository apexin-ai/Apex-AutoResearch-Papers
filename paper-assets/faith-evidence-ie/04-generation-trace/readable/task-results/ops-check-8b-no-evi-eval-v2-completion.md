# ops check 8b no evi eval v2 completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_8b_no_evi_eval_v2_completion_20260516T130604_result.json`
- **Structured JSON:** [`45f6d1d8536ced404d4d.json`](../../sessions/45/45f6d1d8536ced404d4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**plan_006_qwen3_8b_no_evidence_eval_v2** — 成功完成 ✓

| 指标 | 值 |
|------|-----|
| Ign-F1 | **0.5079** |
| Rel-F1 | **0.5283** |
| Evi-F1 | 0 (no-evidence 模型，符合预期) |
| EDCR | 0 (同上) |
| Format compliance | 99.49% |
| 推理时间 | 6402s (~107min) |
| Truncated | 225/985 docs |

**cuda:2 空闲**（0 MiB），可用于下一个任务。

GPU 状态：
- GPU 0: 10319 MiB (占用)
- GPU 1: 23292 MiB (占用)
- GPU 2: **0 MiB** (空闲) ← 可用
- GPU 3: 17883 MiB (占用)

---

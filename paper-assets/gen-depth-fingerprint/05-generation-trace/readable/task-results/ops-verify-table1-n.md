# ops verify table1 N

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-table1-N_20260516T232301_result.json`
- **Structured JSON:** [`bab3f5f9f29cb1f87805.json`](../../sessions/ba/bab3f5f9f29cb1f87805.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Table 1 LOGO 评估的实际 N：**

- **3-class (8 generators)**: **37,058** samples
- **binary**: **29,095** samples

数据来源：
- `features_all_models.csv`: 27,529 rows (pythia-2.8b, pythia-1b, olmo-2-1b, qwen3-0.6b, qwen3-1.7b, qwen3-8b)
- `llama-3.2-3b`: 4,680 rows
- `mistral-7b-v0.3`: 4,849 rows
- 合计: 37,058 (= 27,529 + 4,680 + 4,849)

Binary 的 29,095 是因为 3-class 中 human 类只保留部分或过滤了某个 depth 类别后的子集。

---

# analysis eval grpo g8 bf16 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_grpo_g8_bf16_results_20260515T175633_result.json`
- **Structured JSON:** [`2bbe5a0af99f316fa43a.json`](../../sessions/2b/2bbe5a0af99f316fa43a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估**全部正常完成**，EXIT_CODE=0，3 个 checkpoint 都已评估。

### 结果汇总

| Metric | ckpt-80 | ckpt-90 | ckpt-100 |
|--------|---------|---------|----------|
| **Rel-F1** | 0.4456 | 0.4523 | **0.4549** |
| **Ign-F1** | 0.4456 | 0.4523 | **0.4549** |
| **Evi-F1** | 0.8034 | 0.8052 | **0.8086** |
| **EDCR** | **0.6409** | 0.6414 | 0.6318 |
| **Format OK** | 99.9% | 99.8% | **100.0%** |
| **Truncated** | 50/985 | 61/985 | 61/985 |

**Best by F1: checkpoint-100** (F1=0.4549, Evi-F1=0.8086)。

趋势：F1 和 Evi-F1 从 ckpt-80 到 100 单调上升，EDCR 在 ckpt-100 略降（0.6409→0.6318）。Format OK 逐步改善到 100%。

需要我更新 registry 状态吗？

---

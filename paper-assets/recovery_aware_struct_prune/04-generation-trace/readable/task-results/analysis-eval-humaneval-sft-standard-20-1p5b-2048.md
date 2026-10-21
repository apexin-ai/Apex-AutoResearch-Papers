# analysis eval humaneval sft standard 20 1p5b 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_sft_standard_20_1p5b_2048_20260519T135322_result.json`
- **Structured JSON:** [`2d991023682bab0cf681.json`](../../sessions/2d/2d991023682bab0cf681.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## Metrics 摘要

| 指标 | 值 |
|------|-----|
| **pass@1** | 0.0061 (0.61%) |
| **n_correct** | 1 |
| **n_total** | 164 |
| **stderr** | ±0.0061 |
| **唯一通过** | HumanEval/30 |
| **运行时间** | ~1h23m |
| **退出码** | 0 (正常完成) |

Standard SFT 1.5B 在 HumanEval 上 1/164，与 CKA-only SFT (也是 1/164) 持平。符合预期——1.5B 剪枝模型在 code generation 上本身能力极弱，两种 SFT 方法无显著差异。

---

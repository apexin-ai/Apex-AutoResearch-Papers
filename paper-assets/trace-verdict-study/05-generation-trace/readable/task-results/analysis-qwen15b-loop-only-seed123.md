# analysis qwen15b loop only seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_loop_only_seed123_20260520T124327_result.json`
- **Structured JSON:** [`68fe7cbc68cfa6a675ad.json`](../../sessions/68/68fe7cbc68cfa6a675ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**qwen15b_loop_only_seed123 → SUCCESS**

| Metric | seed123 | seed42 | 2-seed mean±std |
|--------|---------|--------|-----------------|
| accuracy | **81.09%** | 78.32% | **79.71±1.96%** |
| pass_f1 | 0.8737 | 0.8526 | 0.8632±0.0149 |
| fail_f1 | 0.6244 | 0.5905 | 0.6075±0.0240 |

seed123 与 seed42 差 2.77pp，在 ±5pp 内，跨 seed 稳定性验证通过。1.5B 的 seed 方差 (1.96pp) 高于 7B (0.52pp)，符合小模型更敏感的预期。Registry 已标记 DONE/success，报告已注册。

---

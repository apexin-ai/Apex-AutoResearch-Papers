# analysis d140 1 7b sft s42 no evi 2048 fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d140_1_7b_sft_s42_no_evi_2048_fix_20260521T093447_result.json`
- **Structured JSON:** [`07942b0e9c76fc91cee5.json`](../../sessions/07/07942b0e9c76fc91cee5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

| 指标 | no_evi@2048 (本实验) | with_evi@2048 | delta |
|------|---------------------|---------------|-------|
| **ign_f1** | **0.4233** | 0.4806 | -0.0573 |
| f1 | 0.4436 | — | — |
| ign_precision | 0.4297 | — | — |
| ign_recall | 0.4172 | — | — |
| truncated | 507/985 (51.5%) | 267/985 (27.1%) | +24.4pp |
| format_ok | 971/985 (98.6%) | 985/985 | -1.4pp |
| n_predictions | 44,566 | — | — |

**Evidence tax = +0.0573**（evidence 对 1.7B@2048 有益）

Adapter fix 确认有效（0.4233 vs 错误 adapter 0.3925，+3.08pp）。

值得注意：no-evidence 模型截断率反而更高（51.5% vs 27.1%）。去掉 evidence 字段后，模型生成了大量额外 triples（44,566 个 predictions），token 预算被数量而非 evidence 文本消耗。这意味着 no-evidence 的截断瓶颈不是单条 triple 太长，而是 triple 数量爆炸。

---

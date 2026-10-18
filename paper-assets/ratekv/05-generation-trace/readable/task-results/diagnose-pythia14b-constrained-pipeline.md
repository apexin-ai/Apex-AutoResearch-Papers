# diagnose pythia14b constrained pipeline

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pythia14b_constrained_pipeline_20260515T130627_result.json`
- **Structured JSON:** [`2223c3bb4cade18b3dd1.json`](../../sessions/22/2223c3bb4cade18b3dd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**实验结果**：Pythia-1.4B (Flat shape) constrained pipeline 成功，耗时 4 分钟。

| 配置 | PPL | vs BF16 |
|------|-----|---------|
| BF16 baseline | 16.49 | — |
| Uniform 4-bit | 24.29 | +7.80 |
| Constrained MCKP | 24.45 | +7.96 |
| Unconstrained MCKP | 31.54 | +15.05 |

**结论**：假设验证通过。Flat shape 模型 constrained MCKP 与 uniform 仅差 0.16 PPL，非均匀分配无显著优势。Unconstrained 因分配了 90 个 2-bit heads 反而大幅劣化。

Registry 已更新为 DONE/success，metrics 已写入，cron 已删除。

---

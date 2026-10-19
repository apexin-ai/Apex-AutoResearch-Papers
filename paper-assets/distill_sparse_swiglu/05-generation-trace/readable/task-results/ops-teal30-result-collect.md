# ops teal30 result collect

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_teal30_result_collect_20260516T033140_result.json`
- **Structured JSON:** [`fc0e393c50a7f3479144.json`](../../sessions/fc/fc0e393c50a7f3479144.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，实验标记为 DONE (negative)。

**TEAL 30% Downstream 结果总结：**

| Metric | Dense | KL 30% | TEAL 30% | TEAL vs KL |
|--------|-------|--------|----------|------------|
| ARC-c acc_norm | 0.5819 | 0.3737 | 0.4155 | +4.2pp |
| WinoGrande | 0.7814 | 0.6756 | 0.6559 | -2.0pp |
| MMLU | 0.6532 | 0.2874 | 0.3598 | +7.2pp |
| GSM8K strict | 0.5004 | 0.0743 | 0.0849 | +1.1pp |

TEAL (training-free) 在知识密集型任务上显著优于 KL distill，尤其 MMLU 领先 7.2pp。但两者在 GSM8K 推理任务上都严重退化（从 Dense 的 0.50 降到 ~0.08），30% sparsity 整体对 downstream 损害巨大。

---

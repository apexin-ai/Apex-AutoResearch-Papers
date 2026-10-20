# knowledge paper data tables

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_paper-data-tables_20260515T210353_result.json`
- **Structured JSON:** [`e043b5ba767bfdb4a466.json`](../../sessions/e0/e043b5ba767bfdb4a466.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 张表已写入 `artifacts/paper_data_tables.md` 并注册 (`art_20260515_9248a2`)。

数据概要：
- **Table 1** (8 conditions): exception_only 99.83% 和 ae_only 99.92% 为 Tier 1；VOTA/VOTA_no_ae ~99.4% 为 Tier 2；loop_only/label_only/full_trace 为 Tier 3 (81-86%)；no_trace baseline 75.13%
- **Table 2**: DeepSeek exception_only epoch1 与 Qwen gap=0；VOTA gap=+14.96pp (DeepSeek 仅 84.45%)；full_trace v3 pending
- **Table 3**: Qwen exception_only 三种子完全一致 99.83%，每 seed 恰好 2 errors
- **Table 4**: DeepSeek exception_only seed 不鲁棒 (seed42 99.33% vs seed123 91.09%)；seed456 pending
- **Table 5**: ae_only 校准最佳 (ECE=0.0004)；exception_only Brier 最低但 MCE 最高 (0.8355)

缺失项标注为 `—` 或 `pending`，error sample IDs 指向服务器 predictions.jsonl。

---

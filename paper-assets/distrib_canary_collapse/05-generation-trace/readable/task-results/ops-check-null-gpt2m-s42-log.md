# ops check null gpt2m s42 log

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_null_gpt2m_s42_log_20260524T081910_result.json`
- **Structured JSON:** [`f522c7b27be837820926.json`](../../sessions/f5/f522c7b27be837820926.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被清除）。

**结论：success**

- EXIT_CODE=0，实验正常完成
- 11 个 generation 目录（gen_0 base + gen_1~gen_10），每代含 checkpoint/metrics/synthetic_data
- all_metrics.json 完整，11 条记录，全部 `effective_alpha=0.0`，`intervention_triggered=false`
- 最后一代 (gen_10): ppl=17.27, entropy=2.84, eff_rank=24.0, mauve=0.014
- 日志末尾为 metrics 计算（Featurizing q），无报错
- Registry 已更新为 DONE/success

---

# diagnose null gpt2m failure

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_null_gpt2m_failure_20260524T080539_result.json`
- **Structured JSON:** [`959ccfec1d858b5ffc8b.json`](../../sessions/95/959ccfec1d858b5ffc8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：Cron 误判（false positive），两个实验均已成功完成。**

| 实验 | EXIT_CODE | all_metrics.json | 完成时间 | ppl | mauve |
|------|-----------|-----------------|---------|-----|-------|
| null_gpt2m_s42 | 0 | 4999B ✅ | 15:42 | 17.27 | 0.0138 |
| null_gpt2m_s43 | 0 | 4974B ✅ | 15:43 | 17.26 | 0.0128 |

gen_0 至 gen_10 全部完成，数据可直接使用。Cron 在实验运行期间连续 5 次轮询未发现 sentinel 文件，提前判定为 failed，但实验随后正常完成并写入了 sentinel。

---

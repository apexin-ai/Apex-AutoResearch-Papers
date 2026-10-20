# analysis llama rsft fair tax 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_rsft_fair_tax_2048_20260521T140513_result.json`
- **Structured JSON:** [`f7ae8ab345b559fb1806.json`](../../sessions/f7/f7ae8ab345b559fb1806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇报：

| | with-evi | no-evi |
|---|---|---|
| format_ok | 984 | 984 |
| truncated | 90 | 140 |
| format_fail | 1 (malformed) | 1 (malformed) |

**Fair subset: 983 docs**（交集只少了各自 1 个 malformed，几乎全重叠）

| 指标 | fair with-evi | fair no-evi | fair tax |
|---|---|---|---|
| ign_f1 | 0.5779 | 0.5562 | **+2.17pp** |
| f1 | 0.5897 | 0.5706 | +1.91pp |

Full set ign_f1 与 metrics.json 吻合（with-evi 0.5779 vs 报告 0.5774，微小差异来自 gold_count 处理）。

**fair_tax = +2.17pp**，evidence 对 LLaMA RSFT 有正向增益。与 Qwen 1.7B 的 -5.63pp（evidence hurts）方向相反。

---

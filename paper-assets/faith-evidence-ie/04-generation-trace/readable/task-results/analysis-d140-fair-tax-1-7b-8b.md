# analysis d140 fair tax 1 7b 8b

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d140_fair_tax_1_7b_8b_20260521T103937_result.json`
- **Structured JSON:** [`3b0aa7b8417c4c65d16c.json`](../../sessions/3b/3b0aa7b8417c4c65d16c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 结果汇总

| 模型 | fair_subset | fair_with_evi | fair_no_evi | fair_tax |
|------|------------|---------------|-------------|----------|
| **1.7B** | 971 docs | 0.4838 | 0.4275 | **-5.63pp** |
| **8B** | 984 docs | 0.5015 | 0.5019 | **+0.04pp** |

1.7B fair tax 从 raw -5.73pp 收窄到 -5.63pp（14 个 no-evi format failure 被排除）。8B 几乎无 tax（+0.04pp），仅 1 个 with-evi format failure。

JSON 文件：
- `/root/autodl-tmp/eval_results/d140_1_7b_matched_fair_tax_2048.json`
- `/root/autodl-tmp/eval_results/d140_8b_matched_fair_tax_2048.json`

---

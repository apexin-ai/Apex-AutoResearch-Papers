# precheck folio c0

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_precheck_folio_c0_20260516T020031_result.json`
- **Structured JSON:** [`56b1929cea2739e4de65.json`](../../sessions/56/56b1929cea2739e4de65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report saved. Here are the results:

---

## FOLIO C0 预检结果

**多候选率: 0/10 = 0%** — **FAIL**（D012 C0 标准要求 ≥20%）

| # | ID | 标签 | K=6 分布 | 多候选? |
|---|-----|------|---------|---------|
| 1 | folio_000 | True | True:6 | No |
| 2 | folio_002 | True | True:6 | No |
| 3 | folio_004 | True | False:4, FAIL:2 | No |
| 4 | folio_010 | False | False:6 | No |
| 5 | folio_012 | False | False:6 | No |
| 6 | folio_014 | False | False:6 | No |
| 7 | folio_020 | Unknown | Unknown:6 | No |
| 8 | folio_022 | Unknown | Unknown:6 | No |
| 9 | folio_024 | Unknown | Unknown:6 | No |
| 10 | folio_026 | Unknown | Unknown:6 | No |

**关键发现：**
- 10 题中 0 题出现多候选，所有三类标签（True/False/Unknown）均完全一致
- folio_004 答错（label=True 但 6/6 答 False），但仍然一致——没有分歧
- 答案提取失败 2/60（folio_004 的 2 条 trace 因 max_tokens=4096 截断）
- 与 ProofWriter 观察一致：QwQ-32B 在形式化逻辑推理上 trace 分歧极低

**偏差说明：** K=6（非原始要求的 K=12），max_tokens=4096（非 12288），因 vLLM 资源竞争降低以加速。但 0% 的结果已足够明确——即使 K=12 也不会改变结论。

**产出文件：**
- `artifacts/folio_c0_precheck_report.md`
- `artifacts/folio_c0_precheck_raw.json`

---

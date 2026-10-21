# analysis matched 2048 fair tax

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_matched-2048-fair-tax_20260521T043703_result.json`
- **Structured JSON:** [`ea6d964be71919dead5b.json`](../../sessions/ea/ea6d964be71919dead5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| Seed | fair_subset_docs | fair_with_evi | fair_no_evi | fair_tax (pp) |
|------|-----------------|---------------|-------------|---------------|
| s42  | 873             | 0.5716        | 0.5564      | **-1.53**     |
| s43  | 834             | 0.4910        | 0.3789      | **-11.20**    |
| s44  | 977             | 0.4679        | 0.4395      | **-2.83**     |

**3-seed mean ± std: -5.19 ± 5.25 pp**

所有三个 seed 的 fair_tax 均为负值（with-evi 在 fair subset 上优于 no-evi）。

**s42 验证不一致**：本次得到 fair_tax=-1.53pp（with_evi=0.5716），与之前记录的 +1.20pp（with_evi=0.5443）不符。fair_subset_docs=873 和 fair_no_evi=0.5564 一致，差异在 with_evi 侧——可能 s42 with_evidence predictions.json 被重新生成过。

**s43 异常**：no-evi 仅 834/985 format_ok（151 failures，其中 104 malformed JSON），即使在 fair subset 上 ign_f1 也只有 0.3789，与 with-evi 的 0.4910 差距极大（-11.20pp），方差主要来源于此。

---

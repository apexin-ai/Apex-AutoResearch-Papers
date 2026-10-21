# analysis matched fair tax corrected

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_matched-fair-tax-corrected_20260521T045658_result.json`
- **Structured JSON:** [`335b9b478eaee0cd1c1e.json`](../../sessions/33/335b9b478eaee0cd1c1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。Registry 已更新，旧 `fair_tax_pp` 已标注 INVALIDATED。

## 最终结果：3-seed Matched Fair Evidence Tax @2048

| Seed | fair_subset_docs | fair_with_evi@2048 (ign_f1) | fair_no_evi@2048 (ign_f1) | matched_fair_tax (pp) |
|------|------------------|-----------------------------|---------------------------|-----------------------|
| s42 | 873 | 0.5716 | 0.5564 | **-1.53** |
| s43 | 834 | 0.4910 | 0.3789 | **-11.20** |
| s44 | 977 | 0.4679 | 0.4395 | **-2.83** |
| **Mean±Std** | 895 | 0.5102 | 0.4583 | **-5.19 ± 5.25** |

要点：
- 3 个 seed 的 fair tax 全部为负（with-evi 优于 no-evi），但方差极大（std=5.25pp），主要被 s43 的 -11.20pp 拉动
- s43 no-evi format_ok 仅 834/985（84.7%），即使在 fair subset 上 ign_f1 也只有 0.3789，远低于 s42/s44
- s42 和 s44 的 fair tax 较温和（-1.53pp, -2.83pp），s43 是明显的 outlier

---

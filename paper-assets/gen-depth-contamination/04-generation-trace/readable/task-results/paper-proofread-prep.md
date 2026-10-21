# paper proofread prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_proofread_prep_20260522T212115_result.json`
- **Structured JSON:** [`58afd8a885fdfcba7516.json`](../../sessions/58/58afd8a885fdfcba7516.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成：`artifacts/proofread_report.md`

**结果摘要：**

| 类别 | 结果 |
|------|------|
| Undefined References | PASS（`sec:extended_decoding` 已修复，无残留问题） |
| Table 1 vs Registry | Qwen-rw/Pythia/Qwen-cont PASS（≤0.0003 rounding）；**OLMo CRITICAL MISMATCH** |
| Table robustness_10k | PASS（3个实验全部精确匹配） |
| Transfer Matrix | PASS（所有值 3dp 内一致） |
| Spelling/Grammar | PASS（无重复词、无破折号违规、无拼写错误） |

**唯一 Critical Issue：** Registry `exp_002_olmo_depth` 记录 K\*=2 / 1v2 AUC=0.6146，但论文全篇一致报告 OLMo K\*=1 / 1v2 AUC=0.508。论文内部自洽，Registry 需要更新为最终结果。

---

# code exp 022 oracle proofwriter

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-022-oracle-proofwriter_20260518T033659_result.json`
- **Structured JSON:** [`3f3df07998cbe93fecf1.json`](../../sessions/3f/3f3df07998cbe93fecf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-022 完成。结果：

**Oracle-SICA: 86.67% vs SC: 75.17% (+11.50 pp, McNemar p=9.2e-15)**

| 指标 | 值 |
|------|-----|
| Oracle-SICA | 86.67% (520/600) |
| SC | 75.17% (451/600) |
| SICA(self) | 75.50% (453/600) |
| Delta (Oracle vs SC) | **+11.50 pp** |
| Z3 gold agreement | 97.14% (577/594) |
| Parse errors | 6/600 (1%) |
| Solver errors | 0/7128 |

**Per-subtype breakdown** (delta 从大到小):
- **RelNeg**: +17.86 pp (77.86% vs 60.00%)
- **RelNoneg**: +13.01 pp (79.45% vs 66.44%)
- **AttNoneg**: +9.09 pp (96.10% vs 87.01%)
- **AttNeg**: +6.87 pp (91.88% vs 85.00%)

**与 FOLIO (exp-021) 对比**:
- FOLIO: +8.82 pp (p=6.15e-5, N=204)
- ProofWriter: **+11.50 pp** (p=9.21e-15, N=600)

ProofWriter delta 更大且统计显著性更强，符合预期（合成数据更规则，D5 推理链长）。关系谓词子类型 (Rel*) 获益远大于属性谓词 (Att*)，说明二元谓词推理链更长时 oracle 约束的增益更显著。

---

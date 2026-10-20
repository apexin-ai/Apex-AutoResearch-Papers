# audit docred et dr calibration

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_docred_et_dr_calibration_20260514T144331_result.json`
- **Structured JSON:** [`d3d069d16f9f77429951.json`](../../sessions/d3/d3d069d16f9f77429951.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是统一口径重算的核心结果。

---

## 统一口径 ET/DR/RV 表

| Method | ET↓ | RV↓ | DR↓ |
|--------|-----|-----|-----|
| Unconstrained | 2.47% | 29.66% | 14.51% |
| Grammar-only | 0.00% | 0.03% | 26.17% |
| Semantic-only | 2.47% | 29.87% | 3.76% |
| Full (S1) | 0.00% | 0.03% | 10.19% |

## 旧报告问题根因

**ET 膨胀**：旧 `violation_checker_docred.py` 的 `check_document()` 把 entity list violations + relation head violations + relation tail violations 三者加总作为分子，但分母只是 entity list 数量。一个 invalid-type entity 出现在 N 条 relation 中会被计 N+1 次。验证：semantic_only 旧值 (499+1780+1443)/20185 = 18.44% 完美匹配。

**DR 膨胀**：旧 checker 没有把 ET 和 DR 分开——entity type invalid 的 triple 因 pair 自然不在 valid_pairs 中，被同时计为 DR violation。semantic_only 有 14.28% 的 triple 存在 invalid head/tail type，这些全被重复计入了 DR。

**14.83% vs 15.05% 差异**：whitespace 处理不同。semantic_only 有 507 条 relation 的 type 带前导空格（如 `" TIME"`），旧 checker 不做 `.strip()` 导致误判。

## 口径说明

- **ET**：entity-level，分母=entity list 总数，分子=entity list 中 type ∉ {PER,ORG,LOC,TIME,NUM,MISC}
- **DR**：triple-level，仅在 relation 合法 + head/tail type 均合法的 triple 上计算 pair 违规，分母=total triples
- ET 和 DR **严格不重叠**

产出文件在 `artifacts/unified_et_dr_recalc.md`，服务器上的重算脚本和 JSON 报告分别在 `unified_violation_recalc.py` 和 `outputs/violation_report_docred_{mode}_unified.json`。

---

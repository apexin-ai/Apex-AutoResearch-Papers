# analysis table inconsistency

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table_inconsistency_20260515T140337_result.json`
- **Structured JSON:** [`c17739d47aa9a29a250b.json`](../../sessions/c1/c17739d47aa9a29a250b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因分析完成。汇总结论：

---

## 根因判定

**差异完全来自 checker 版本（v1 → v2），不是实验配置差异。**

### ET 差异（7.5% → 2.48%）—— checker bug

v1 checker 有两个缺陷：
1. **Triple-counting**：同一实体在 `entity_list` 出现一次、在 N 条 relation 的 head/tail 各出现一次 → 被计为 (1+N) 次违规。v2 用 `seen_entities` dict 按 `(text, normalized_type)` 去重，只计一次。
2. **缺少别名归一化**：模型输出 "PERSON"/"ORGANIZATION" 等全称时，v1 直接判为无效类型。v2 加了 `ENTITY_TYPE_ALIASES` 映射（PERSON→PER, ORGANIZATION→ORG 等）。

### RV / DR 差异（< 1pp）—— 非 checker 问题

| 指标 | Phase 0 (v2 recheck) | Phase 2 (v2) | 差 |
|------|---------------------|--------------|-----|
| ET | **2.43%** | 2.48% | +0.05pp |
| RV | **28.87%** | 29.66% | +0.79pp |
| DR | **18.70%** | 18.46% | -0.24pp |

用 v2 checker 重跑 Phase 0 输出后，三个指标的差异全部 < 1pp，属于不同输出文件的正常波动（Phase 0 用 `run_extraction_docred.py` batch_size=4, Phase 2 用 `run_constrained_extraction.py --mode unconstrained` batch_size=1 max_new_tokens=4096；parse rate 也不同：96.4% vs 98.8%）。

### 验证：v2 重跑 Phase 0 输出的完整结果

```
Documents: 962 checked, 36 parse failures
Entities: 19099, Triples: 16540
ET: 465 violations (2.43%)    ← 原 7.5% → 修正后 2.43%
RV: 4775/16540 (28.87%)      ← 不变
DR: 3093/16540 (18.70%)      ← 不变
CF: 15 (0.08%)               ← 不变
```

报告已保存: `outputs/violation_report_docred_phase0_v2_recheck.json`

---

## 统一方案建议

**推荐方案 B**：用 v2 checker 重新评估 Phase 0 所有输出，更新 Table 1。

理由：
- Table 1 和 Table 3 应使用同一版本 checker，否则跨表对比无意义
- v2 修复的是真实 bug（triple-counting + 缺少别名归一化），v1 的数字本身就不正确
- 重跑已完成，Phase 0 DocRED v2 数据已在手（ET=2.43%, RV=28.87%, DR=18.70%）
- 论文中无需标注"re-evaluated"——v2 就是正确的评估方式，v1 是已修复的 bug
- Table 1 和 Table 3 的 baseline 数据将因不同输出文件存在 < 1pp 的自然差异，这是合理的

---

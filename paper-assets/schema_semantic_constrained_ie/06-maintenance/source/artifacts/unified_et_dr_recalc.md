# DocRED 4 实验统一口径重算：ET / DR / RV

日期：2026-05-14

## 统一口径定义

| 指标 | 分子 | 分母 | 说明 |
|------|------|------|------|
| **ET (entity-level)** | entity list 中 type.strip().upper() ∉ {PER,ORG,LOC,TIME,NUM,MISC} 的 entity 数 | entity list 总数 | 只从 entity list 计，不从 relation head/tail 重复计 |
| **RV (triple-level)** | relation type 不在 ontology 中的 triple 数 | total triples | — |
| **DR (eligible)** | relation 合法 + head/tail type 均合法 但 (head_type, tail_type) pair 不在 allowed pairs 中的 triple 数 | eligible triples (relation 合法 + types 均合法) | ET 和 DR 严格不重叠 |
| **DR (all)** | 同上分子 | total triples | 用于跨实验对比 |
| **Triple-ET** | head 或 tail type 不合法的 triple 数 | total triples | 仅供参考，不是论文主指标 |

关键归一化：所有 entity type 在检查前执行 `.strip().upper()`。

## 统一结果

| Mode | Entities | Triples | ET% | RV% | DR%(eligible) | DR%(all) | Triple-ET% |
|------|----------|---------|-----|-----|---------------|----------|------------|
| unconstrained | 20,171 | 17,497 | **2.47** | 29.66 | 21.85 | 14.51 | 6.08 |
| grammar_only | 20,150 | 17,341 | **0.00** | 0.03 | 26.18 | 26.17 | 0.00 |
| semantic_only | 20,185 | 17,571 | **2.47** | 29.87 | 6.36 | 3.76 | 14.28 |
| full_s1 | 20,218 | 17,372 | **0.00** | 0.03 | 10.20 | 10.19 | 0.00 |

## 旧报告 vs 统一口径对比

| Mode | 旧 ET% | 新 ET% | 旧 DR% | 新 DR%(all) | 新 DR%(elig) |
|------|--------|--------|--------|-------------|--------------|
| unconstrained | 8.18 | **2.47** | 18.46 | **14.51** | 21.85 |
| grammar_only | 0.00 | **0.00** | 26.17 | **26.17** | 26.18 |
| semantic_only | 18.44 | **2.47** | 15.05 | **3.76** | 6.36 |
| full_s1 | 0.00 | **0.00** | 10.19 | **10.19** | 10.20 |

## 差异根因分析

### ET 差异 (18.44% → 2.47% for semantic_only)

旧 `violation_checker_docred.py` 的 `check_document()` 存在**三重计数**问题：

1. entity list 中 invalid type 的 entity → 计入 ET 分子
2. relation 的 head_type invalid → 也计入 ET 分子
3. relation 的 tail_type invalid → 也计入 ET 分子

**但分母只是 entity list 总数**。一个 invalid-type entity 如果出现在 N 条 relation 中，会被计 N+1 次。

验证：
- semantic_only: (499 entity-list + 1780 head + 1443 tail) / 20185 = 3722/20185 = **18.44%** ✓
- unconstrained: (499 + 764 + 387) / 20171 = 1650/20171 = **8.18%** ✓

统一口径只计 entity list：499/20185 = **2.47%**。

### semantic_only DR 差异 (14.83% vs 15.05%)

两个 Worker 报告了不同的 DR 值。根因：

- **15.05%** = 2645/17571，来自 `violation_checker_docred.py`（不做 `.strip()`，invalid-type triples 也计为 DR）
- **14.83%** 推测来自某次使用了 `.strip()` 或 SciERC 版 checker 的运行，whitespace 处理差异导致 ~40 条 triple 的分类不同

统一口径下两者都不再适用：
- 新 DR(all) = 660/17571 = **3.76%**（排除了 invalid-type triples）
- 新 DR(eligible) = 660/10377 = **6.36%**

### 为何旧 DR 大幅下降

旧 checker 将 entity type invalid 的 triple 也计为 DR violation（因为 [INVALID_TYPE, VALID_TYPE] 自然不在 valid_pairs 中）。统一口径严格分离 ET 和 DR：invalid type → 只计 ET，不计 DR。

semantic_only 的 triple-level ET 高达 14.28%（2509 条 triple 有 invalid head/tail type），这些 triple 在旧口径下被同时计为 DR，膨胀了 DR 数值。

### whitespace 问题

semantic_only 的 507 条 relation 的 head/tail type 有前导空格（如 `" TIME"`）。旧 checker 用 `.upper()` 不做 `.strip()`，导致 `" TIME"` ≠ `"TIME"` 被误判为 invalid type。统一口径增加了 `.strip()` 处理。

### Invalid entity types 分布

| Type | unconstrained | semantic_only |
|------|--------------|---------------|
| EVENT | 262 | 262 |
| WORK | 123 | 123 |
| ETHNIC_GROUP | 64 | 64 |
| SERIES | 9 | 9 |
| LANG | 8 | 8 |

entity list 中的 invalid types 两个模式完全一致（均为 499 个），说明 entity list 生成不受 semantic constraint 影响。差异完全来自 relation head/tail 中的 types（semantic_only 额外产生 PERSON=1081, ORGB=85, OR=62 等）。

## 论文建议

1. **ET 统一使用 entity-level 口径**：分母=entity list 总数，分子=entity list 中 invalid type 数。直观、无重复计数。
2. **DR 建议使用 DR(all) 口径**：分母=total triples，与 RV 一致，跨实验可比。但需在论文中说明 DR 和 ET 严格不重叠。
3. **论文用表**（推荐）：

| Method | ET↓ | RV↓ | DR↓ |
|--------|-----|-----|-----|
| Unconstrained | 2.47 | 29.66 | 14.51 |
| Grammar-only | 0.00 | 0.03 | 26.17 |
| Semantic-only | 2.47 | 29.87 | 3.76 |
| Full (S1) | 0.00 | 0.03 | 10.19 |

4. 如果 Reviewer 要求 entity-level 和 triple-level 都报，可以在 appendix 补充 triple-level ET 和 DR(eligible)。

## 产出文件

- 统一重算脚本：`/root/schema_semantic_constrained_ie/unified_violation_recalc.py`
- 4 个统一报告：`outputs/violation_report_docred_{mode}_unified.json`
- 汇总 JSON：`outputs/unified_violation_summary_docred.json`

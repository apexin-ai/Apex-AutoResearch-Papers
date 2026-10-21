# research tacred schema analysis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tacred_schema_analysis_20260516T023452_result.json`
- **Structured JSON:** [`f19725c8b627156fceeb.json`](../../sessions/f1/f19725c8b627156fceeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册为 artifact。核心发现：

### Constraint Tightness 对比

| Dataset | Entity Types | Relations | Avg τ |
|---------|-------------|-----------|-------|
| SciERC | 6 | 7 | 0.333 |
| DocRED | 6 | 96 | 0.842 |
| **TACRED** | **17** | **41** | **0.994** |

TACRED 是极端紧约束——41 个 relation 中 20 个只有 1 个 valid pair。

### 关键判断

1. **格式兼容**: TACRED schema 可直接转为 `ontology_constraints.json`，无需改 OntologyCompiler
2. **核心风险**: τ≈0.994 意味着 grammar-first fallback 几乎 100% 触发，semantic constraint layer 形同虚设
3. **First-token 冲突**: 17 entity types 中 11 个有首字符冲突（C×4, P×2, N×2 等），TypeConstraintProcessor 需要扩展 multi-token masking 或重命名类型
4. **no_relation 无需特殊处理**: OntoCoDec 不在 schema 中定义 no_relation，生成式框架通过"不输出 triple"隐式表达
5. **数据集推荐**: 首选 TACREV（schema 不变 + 修正标注），三个版本都需要 LDC 原版数据（$25）

### 战略建议

如果目标是 **tightness spectrum 验证**（论文 §5 的 cross-dataset analysis），TACRED 是理想的极端数据点，构成 0.333→0.842→0.994 的完整谱系。如果目标是 **展示实用价值**，TACRED 不适合——约束太紧，OntoCoDec 的 semantic layer 无法生效。

---

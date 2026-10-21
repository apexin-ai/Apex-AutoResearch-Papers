# Grammar-Semantic Interaction Invariant — Method Section Notes

## A. Method Section Description

### Dual-Layer Interaction Model

OntoCoDec 的双层约束是**有序依赖**关系，非独立叠加：

1. **Grammar layer (XGrammar)**: 编译 CFG，强制 JSON 结构合法 + type token 必须在 ontology vocabulary 内。产出：grammar-valid token set $G(t) \subseteq V$。
2. **Semantic layer (TypeConstraintProcessor)**: 基于 stateful entity registry，在 grammar 允许集内进一步限制 domain/range 合规 token。产出：semantic-valid token set $S(t) \subseteq V$。

最终 mask：

$$M_{\text{final}}(t) = M_{\text{grammar}}(t) \wedge M_{\text{semantic}}(t)$$

其中 **semantic masking 只在 grammar allowed tokens 上操作**：$S(t)$ 仅定义在 $G(t)$ 上，对 $V \setminus G(t)$ 无意义。

### Grammar-First Invariant

**Invariant**: Semantic mask 必须是 grammar allowed set 的子集。

$$\text{tokens\_masked\_by\_semantic} \subseteq G(t)$$

等价表述：semantic layer 不得将 grammar-invalid token 的 logit 改变为比任何 grammar-valid token 更优。

**违反后果**：当 $\text{allowed\_types} \cap G(t) = \emptyset$ 时（semantic 要求的所有 type 都不在 grammar 允许集内），semantic masking 将所有 grammar-valid tokens 设为 $-\infty$，而 grammar-invalid tokens 保持有限负值 ($-10^{10}$)。$-10^{10} > -\infty$ → argmax 选中 grammar-invalid token → XGrammar assertion failure（runtime crash）。

### Resolution Protocol

当 $\text{allowed\_types} \cap G(t) = \emptyset$ 时：

- **Skip semantic masking**，交由 grammar layer 单独控制 token 选择
- 实现：`_apply_type_mask` 中增加 `_GRAMMAR_MASK_THRESHOLD = -10^8` 检查——apply semantic mask 前验证至少一个 semantically-allowed type 的 logit 高于此阈值（即未被 grammar mask）；若全部低于阈值，则跳过本次 semantic masking

**设计选择**：grammar fallback（生成 grammar-valid 但可能 type-invalid 的 token）优于 crash，也优于强制选择 grammar-invalid token。Type violation 是 soft error（下游可检测），grammar violation 是 hard error（结构损坏）。

## B. Relation to Claims

### Claim 3 (Composable Framework): Grammar 是 Semantic 的 Enabling Dependency

Paper framing 已明确：grammar 层是 semantic 层的**前提条件**，非"两层独立叠加"或"synergistic"。

Grammar-Semantic 交互 bug 提供了**反面证据**：

| 条件 | 行为 | 结果 |
|------|------|------|
| $S(t) \cap G(t) \neq \emptyset$ | 正常 dual-layer masking | DR↓94% |
| $S(t) \cap G(t) = \emptyset$ | Semantic 覆盖 grammar → crash | 系统不可用 |
| $S(t) \cap G(t) = \emptyset$ + fallback | Grammar 单独控制 | 结构合法，type 可能违规 |

**证据链（跨数据集泛化验证）**：

- SciERC: avg 26.1 valid type pairs/relation（松约束）→ $S(t) \cap G(t) = \emptyset$ 从未触发 → invariant 无需介入
- DocRED: avg 5.68 valid type pairs/relation（紧约束）→ 触发空交集 → 暴露 invariant 缺失 → crash
- 修复后 DocRED grammar_only: 304/998 文档零 fallback → invariant 在绝大多数情况下不需要介入，仅在极端约束下起保护作用

**论文定位**：写入 Section 4（方法论设计原则），1-2 句描述即可。不升级为独立 claim（仅 1 次崩溃触发，实现是 fallback 非形式化保证）。

### 推荐 Method Section 措辞

> The semantic layer operates strictly within the grammar-valid token set. When no semantically valid type overlaps with grammar-allowed tokens — which arises under tight ontology constraints — the system falls back to grammar-only control, preserving structural validity at the cost of a potential type violation. This design reflects a deliberate priority ordering: structural integrity (grammar) takes precedence over type compliance (semantic).

## C. Limitation/Discussion Material

### CF Violation Root Cause

**CF (Cross-Field Consistency) violation**: 同一 entity mention 在 entity list 和 relation head/tail 中被标注为不同 type。

**机制归因**：
- grammar_only CF = 0.08%（与 unconstrained 持平）
- full_s1 CF = 9.90%
- full_s2 CF = 8.03%
- **CF 100% 由 semantic 层引入，grammar 层无贡献** → 干净消融证据

**根因**：per-relation 独立 type enforcement。Semantic layer 为每个 relation 独立决定 head/tail type，不维护跨 relation 的 entity type 一致性。

**主要冲突模式**：
| 冲突 pair | 频次 |
|-----------|------|
| Generic ↔ OtherScientificTerm | 60 |
| Material ↔ OtherScientificTerm | 28 |
| Material ↔ Method | 20 |

这些冲突反映 SciERC type system 固有的语义边界模糊——同一术语在不同学术语境下确实可合理归类为不同 type。

### CF Severity Distinction (for Discussion)

- **DR violations = structurally invalid triples**：下游系统不可用 → hard constraint
- **CF violations = cross-triple type inconsistency**：单个 triple 仍 type-valid，仅跨 triple 一致性被破坏 → soft preference
- CF 不是 bug，是 per-relation independent enforcement 的系统性副作用

### Future Work Direction

**Cross-relation entity type consistency constraint**：在 relation-specific type enforcement 之前增加全局 entity-level type consensus pass。具体方案：

1. Pass 1: 提取 entities + 初始 type assignment
2. **Consensus step**: 对重复出现的 entity mention 投票/统一 type
3. Pass 2: 以统一后的 entity types 作为 semantic constraint 输入

这将 CF 问题从 per-relation 独立决策转化为全局一致性优化，代价是增加一次 pass 或一个 post-processing step。

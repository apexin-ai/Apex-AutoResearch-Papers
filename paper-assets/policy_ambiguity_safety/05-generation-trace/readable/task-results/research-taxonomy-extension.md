# research taxonomy extension

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_taxonomy_extension_20260520T091117_result.json`
- **Structured JSON:** [`49ae0f6c6b1afdc5c240.json`](../../sessions/49/49ae0f6c6b1afdc5c240.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件写入 `artifacts/ambiguity_taxonomy_extended.md`，已注册 manifest。

文档结构：

**新增 3 类（Section 5-7）**，每类完整包含：
- **Definition** — 引用 Yang et al. 2011 / Ezzini et al. 2022 (coreferential), Prakken 1991 / Olson 2024 (conditional precedence), NIST SP 800-162 (authorization scope)
- **Cross-walk table** — 与 Li/DRIP-R/Massey 的映射
- **Manifestation** — 各 4-5 个子类型
- **Adjudication Criteria** — 必要充分条件 + annotator 决策规则
- **Link to Safety Violations** — 机制分析 + 在 6 类中的相对位置
- **Matched Pair Examples** — 各 3 个（ambiguous + unambiguous + point + divergence），从 retail/airline 场景构造
- **τ²-bench injection patterns** — 各 4 个具体条款改造方案

**更新内容（Section 8-9）**：
- **6×4 comprehensive cross-walk table**，含 Primary Dimension 列
- **6 类 violation rate 完整排序**：Conditional Precedence (1st) > Scopal (2nd) > Coreferential (3rd) > Incompleteness (4th) > Authorization Scope (5th) > Lexical (6th)
- **7-step annotation flowchart**，新增 Coreferential Check (Step 4) / Precedence Check (Step 5) / Authorization Check (Step 6)
- **类型间消歧规则表**，解决边界分类问题

---

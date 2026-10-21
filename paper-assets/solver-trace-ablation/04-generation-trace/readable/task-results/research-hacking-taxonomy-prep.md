# research hacking taxonomy prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_hacking-taxonomy-prep_20260514T015744_result.json`
- **Structured JSON:** [`13815eff5cda4bf4e032.json`](../../sessions/13/13815eff5cda4bf4e032.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已写入 `artifacts/hacking_taxonomy.md`。

核心内容：

**6 个分类**（按预期频率排序）：
- **H1 Semantic Drift** — 可证但语义偏离 NL 原意（ISR 盲区，预估最高频）
- **H2 Trivial Duplication** — 结论重复/包含在 premises 中（ISR 盲区）
- **H3 Vacuous Truth** — 矛盾前提/重言结论（H3b/c ISR 可检测）
- **H4 Over-specification** — 冗余 premises 填充（ISR 校准良好）
- **H5 Syntactic Exploitation** — 利用 Prover9 特有行为
- **H6 Degenerate Structure** — 空/极简/畸形输出

**ISR 校准结论**：ISR 对 H4（冗余）和 H3b/c（空真）检测有效，对 H1（语义漂移）和 H2（重复）存在盲区 → 支撑 plan_014 downstream validation 的必要性。

**标注方案**：200 条 proved outputs，8 步判断流程，JSON schema 标注格式，含 primary/secondary 多标签和决策规则。

**文献基础**：Skalse 2022（形式化定义）、Gao 2023（overoptimization scaling laws）、Pan 2022（misspecification 三分类）、Yue 2026（extensional shortcuts + IPT）。

---

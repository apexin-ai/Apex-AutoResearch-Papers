# research plan014 downstream design

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan014-downstream-design_20260514T022937_result.json`
- **Structured JSON:** [`ef89410162f3971ef653.json`](../../sessions/ef/ef89410162f3971ef653.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案设计完成。

**三个方案**：

**方案 A (NLI Label Accuracy)** — 推荐，代码已就绪
- `eval_downstream.py` 已完整实现 3-way 蕴含分类 + ISR 分桶 + Best-of-N 对比
- 只需补 ~20 行统计检验（Spearman ρ, Mann-Whitney U）
- GPU 成本 ~4.5h（3 checkpoints × 1.5h inference）
- 核心论证：ISR 与 NLI label accuracy 正相关 → ISR 是 genuine quality proxy

**方案 B (Cross-Solver Agreement)** — 补充，零 GPU 成本
- Prover9 vs Z3 agreement by ISR bucket
- 复用方案 A 输出，新写 ~150 行脚本
- 证明高 ISR formalization 不是 solver-specific artifact

**方案 C (Perturbation Sensitivity)** — 不推荐
- GPU 预算 ~18h，设计复杂，DDL 风险高

**推荐 A+B 组合**，总 GPU ~4.5h，代码改动 ~170 行，5/18 前可完成。文档已写入 `artifacts/plan014_design.md`。

---

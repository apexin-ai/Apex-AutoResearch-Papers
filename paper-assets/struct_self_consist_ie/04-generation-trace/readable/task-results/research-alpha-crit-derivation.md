# research alpha crit derivation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_alpha_crit_derivation_20260521T113132_result.json`
- **Structured JSON:** [`3602f30aba5e728325bd.json`](../../sessions/36/3602f30aba5e728325bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结变更：

**theory.tex §6.3（主文，~1/3 页）**：
- 删除旧的半经验 θ\_crit = 0.70 和 α\_crit,eff > 1.0 引用
- 新增 **Proposition 1**（Entity Selection Bound）：
  - (a) 退化实例上 MV = greedy, ΔF1 = 0
  - (b) E[ΔF1] = (1-δ)·E[ΔF1|non-deg]
  - (c) MV 改善 F1 当且仅当边际实体精度 > α\_crit = F1\_gr/2
- 证明概述 + 不可能性条件 δ > 1 - α\_crit
- 经验验证：CoNLL (δ=60.3% > 54.4%) 满足不可能性条件；SciERC (α\_crit=0.333) 是唯一训练 verifier 有正收益的数据集

**appendix.tex app:alpha\_crit（附录，~1 页）**：
- 完整证明（含 F1 代数推导）
- 更新表格：α\_crit = F1\_gr/2（FewNERD 0.396, CoNLL 0.456, SciERC 0.333）+ 不可能性判定列
- 不可能性条件讨论 + SciERC verifier AUC=0.923 对应关系

**叙事对齐**：
- D223：MV ≈ greedy（neutral under degeneracy），非"SC universally fails"
- D222：conditional ρ 的理论基础——退化实例贡献零信号方差，condition on non-degenerate 是正确做法
- 编译通过，无 undefined reference

---

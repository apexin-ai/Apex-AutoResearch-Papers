# analysis falcon3 algo1 sensitivity

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_falcon3-algo1-sensitivity_20260522T180624_result.json`
- **Structured JSON:** [`f0bd6fb3ef53cea52fa0.json`](../../sessions/f0/f0bd6fb3ef53cea52fa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `artifacts/falcon3_algo1_sensitivity.md`。

核心发现：

**τ × σ sweep (36 组合)**: MMLU 和 ARC 均 100% 稳定。原因：Falcon3 的 Δ (+4.19/+4.01 pp) 远大于 sweep 中最大 τ (2.0 pp)，σ 对正 delta profile 无影响。Falcon3 在任何 τ×σ 组合下都不会被误判为 Immune/U-collapse/V-recovery。

**ρ × λ sweep (42 组合)** — 这两个参数控制 Benefit vs Benefit-sat 边界，是真正的敏感维度：
- MMLU: ρ 拐点 = 0.703，λ 拐点 = 0.87 → 在默认参数附近有较大安全边距
- ARC: ρ 拐点 = 0.238，默认 ρ=0.3 刚好高于此值（margin 仅 0.042）→ 与 bootstrap stability 61.3% 一致，解释了 ARC 的 Benefit-sat 分类为何不够稳定

结论：**主分类（正向污染效应）无条件稳健**，所有参数变化只影响 Benefit 和 Benefit-sat 之间的子分类。

---

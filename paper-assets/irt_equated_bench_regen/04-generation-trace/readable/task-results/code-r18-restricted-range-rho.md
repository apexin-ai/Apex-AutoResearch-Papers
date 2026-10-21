# code r18 restricted range rho

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r18_restricted_range_rho_20260522T163431_result.json`
- **Structured JSON:** [`7771d18461fb8630d0fa.json`](../../sessions/77/7771d18461fb8630d0fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已注册在报告中。总结关键发现：

**Full ρ = −0.587** (与预期的 −0.597 基本一致)。逐步去除 ceiling/floor items 后：

| Range | ρ | p | N |
|-------|---|---|---|
| Full | −0.587 | <10⁻³⁰⁰ | 3918 |
| Interior [0.1, 0.9] | −0.552 | 5×10⁻²⁶⁹ | 3380 |
| Interior [0.2, 0.8] | −0.447 | 1×10⁻¹⁰⁸ | 2201 |
| Interior [0.3, 0.7] | −0.325 | 4×10⁻³⁵ | 1370 |

ρ 随 range restriction 单调衰减（符合 range restriction attenuation 的统计预期），但即使在最严格的 [0.3, 0.7] 区间仍 p < 10⁻³⁴，远低于任何显著性阈值。Bootstrap 95% CI 均不含零。

Decile 分析清晰展示单调梯度：hardest decile 93% focal-favoring → easiest decile 0.5% focal-favoring，中间 deciles 也呈连续递减而非仅在两端跳变。

**结论：ceiling/floor effects alone cannot explain the difficulty–direction association.** 可在论文中用一句话报告 interior [0.1, 0.9] 的 ρ = −0.55 作为 robustness check。

产出：
- 脚本：`artifacts/r18_restricted_range_rho/restricted_rho_analysis.py`
- 报告：`artifacts/r18_restricted_range_rho/restricted_rho_report.md`

---

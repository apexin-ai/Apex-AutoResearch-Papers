# analysis bootstrap ci

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_20260514T181218_result.json`
- **Structured JSON:** [`c0f8f2ae8223073e9eab.json`](../../sessions/c0/c0f8f2ae8223073e9eab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap CI 计算完成。汇总：

### SciERC (551 sentences)

| 对比 | Rel ΔF1 | 95% CI | p-value |
|------|---------|--------|---------|
| unconstrained → full_s1 | +0.13pp | [-0.24, +0.58] | 0.582 |
| unconstrained → grammar_only | -0.00pp | [-0.22, +0.22] | 0.980 |
| unconstrained → semantic_only | -0.08pp | [-0.36, +0.15] | 0.424 |

**所有 SciERC 对比均不显著。** CI 很宽（±0.3-0.6pp），因为样本少且绝对 F1 低（~8%）。

### DocRED (998 documents)

| 对比 | Rel ΔF1 | 95% CI | p-value |
|------|---------|--------|---------|
| unconstrained → full_s1 | **+0.50pp** | [+0.23, +0.81] | **<0.001** |
| unconstrained → grammar_only | **+0.57pp** | [+0.31, +0.87] | **<0.001** |
| unconstrained → semantic_only | -0.01pp | [-0.10, +0.09] | 0.895 |
| grammar_only → full_s1 | -0.07pp | [-0.16, +0.02] | 0.138 |
| semantic_only → full_s1 | **+0.50pp** | [+0.24, +0.81] | **<0.001** |

**DocRED 关键发现：**
- unconstrained → full_s1 Rel F1 提升显著（p<0.001），Entity F1 同样显著（+0.53pp, p<0.001）
- grammar constraint 是主要贡献者（unconstrained→grammar_only 显著），semantic alone 无显著效果
- grammar_only → full_s1 不显著：加 semantic 约束在 grammar 基础上无增量

结果 JSON 已保存至 `outputs/bootstrap_ci_results.json`，脚本在 `compute_bootstrap_ci.py`。

---

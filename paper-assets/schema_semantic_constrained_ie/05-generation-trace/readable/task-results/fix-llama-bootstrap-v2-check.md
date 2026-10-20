# fix llama bootstrap v2 check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_llama_bootstrap_v2_check_20260514T224930_result.json`
- **Structured JSON:** [`b083bc12bdfa94b6869b.json`](../../sessions/b0/b083bc12bdfa94b6869b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap CI 完成，所有 registry alignment 验证通过。

## Llama Bootstrap CI 结果

### Registry Alignment 验证（容差 ≤0.05pp）

| 实验 | 指标 | Bootstrap | Registry | Delta | 状态 |
|------|------|-----------|----------|-------|------|
| SciERC U | E-F1 | 23.5294 | 23.56 | 0.0306pp | PASS |
| SciERC U | R-F1 | 2.6714 | 2.68 | 0.0086pp | PASS |
| SciERC S1 | E-F1 | 23.4867 | 23.49 | 0.0033pp | PASS |
| SciERC S1 | R-F1 | 2.5405 | 2.54 | 0.0005pp | PASS |
| DocRED U | E-F1 | 55.6542 | 55.65 | 0.0042pp | PASS |
| DocRED U | R-F1 | 5.9779 | 5.98 | 0.0021pp | PASS |
| DocRED S1 | E-F1 | 55.0089 | 55.01 | 0.0011pp | PASS |
| DocRED S1 | R-F1 | 6.2749 | 6.27 | 0.0049pp | PASS |

### SciERC（Llama-3.1-8B）

| 指标 | Unconstrained | Constrained (S1) | Δ (pp) | 95% CI | p |
|------|--------------|-----------------|--------|--------|---|
| E-F1 | 23.53 | 23.49 | +0.03 | [−0.18, +0.22] | 0.7618 |
| R-F1 | 2.67 | 2.54 | −0.04 | [−0.10, −0.01] | 0.0106 |

### DocRED（Llama-3.1-8B）

| 指标 | Unconstrained | Constrained (S1) | Δ (pp) | 95% CI | p |
|------|--------------|-----------------|--------|--------|---|
| E-F1 | 55.65 | 55.01 | −0.65 | [−1.23, −0.09] | 0.0220 |
| R-F1 | 5.98 | 6.27 | +0.30 | [+0.06, +0.54] | 0.0128 |

### 修复摘要
原始脚本的 `docred_sample_stats_llama` 在 parse failure 时返回 `gold=0`（导致 F1 虚高 2.27pp），修复为 `gold=len(gold_set)`，与评估管线一致（parse failure 视为 false negatives）。

### 关键发现
- **DocRED R-F1**: Constrained 显著优于 Unconstrained（+0.30pp, p=0.013），schema 约束有效提升了关系抽取
- **DocRED E-F1**: Constrained 显著低于 Unconstrained（−0.65pp, p=0.022），约束可能限制了实体识别
- **SciERC R-F1**: Constrained 显著低于 Unconstrained（−0.04pp, p=0.011），但绝对差异极小
- **SciERC E-F1**: 无显著差异（p=0.762）

---

# analysis r15 bonferroni

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r15-bonferroni_20260520T044634_result.json`
- **Structured JSON:** [`42cc49868763e1c1215a.json`](../../sessions/42/42cc49868763e1c1215a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存。汇总：

## Bonferroni 校正结果

**N = 14 个统计检验**

| | α=0.05 | α=0.10 |
|---|---|---|
| 校正前显著 | 9/14 | 9/14 |
| 校正后显著 | 6/14 | 9/14 |

### 校正后不再显著的检验（α=0.05）

3 个 matched-cohort (n=5 per group) 检验从 p=0.004 升至 p_bonf=0.056，刚好超过 0.05 阈值，但仍在 α=0.10 下显著：

| 检验 | p_orig | p_bonf |
|---|---|---|
| Fisher exact: TS domination (matched 5+5) | 0.004 | 0.056 |
| Mann-Whitney U: ISR* (matched 5+5) | 0.004 | 0.056 |
| Mann-Whitney U: TS rate (matched 5+5) | 0.004 | 0.056 |

这三个检验实质上是对同一 matched-cohort 数据的不同切面（TS domination / ISR* / TS rate），本身高度相关。论文核心结论（TS 为 ISR 特异性吸引子）同时有 pooled Fisher (p_bonf ≈ 10⁻¹¹) 和 3-seed sensitivity (p_bonf ≈ 10⁻³⁸) 支撑，这两个校正后仍然极度显著。

### 影响评估

- 论文主要统计结论（TS rate 差异、SFT vs RL 差异）校正后仍然稳健
- matched-cohort 的 p=0.004 系列检验边际化，但考虑到 N=5 的 discrete permutation 限制（最小可达 p=0.008），BF₁₀=77 的贝叶斯证据仍然很强
- 5 个原本不显著的检验（permutation N-H、3-seed Fisher N-H、seed-level permutations、Spearman）校正后当然仍不显著

---

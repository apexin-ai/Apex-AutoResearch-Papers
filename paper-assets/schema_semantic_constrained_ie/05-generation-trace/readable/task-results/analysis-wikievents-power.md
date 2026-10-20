# analysis wikievents power

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wikievents-power_20260522T140423_result.json`
- **Structured JSON:** [`dad25815ddba4a9fb659.json`](../../sessions/da/dad25815ddba4a9fb659.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/_project/paper/appendix_power_analysis.tex`。

**数据来源和计算方法：**

| Dataset | n | 95% CI (F1) | MDE (F1) | 数据来源 |
|---------|---|-------------|----------|----------|
| SciERC | 551 | ±1.8pp | 1.2pp | `bootstrap_ci_results_v2.json` (10k resamples) |
| DocRED | 998 | ±0.8pp | 0.5pp | 同上 |
| DocRED (70B) | 200 | ±3.3pp | 2.1pp | 已有 appendix 文本 (5k resamples) |
| WikiEvents | 20 | ±3.0pp | 2.0pp | `r12_wikievents_bootstrap.json` (1k resamples) |

MDE 使用 σ\_diff = σ × √(2(1−ρ)), ρ=0.9, 80% power, α=0.05。WikiEvents n=20 用 t 分布 (df=19)，其余用 z。

**关键论点：**
- WikiEvents Arg-F1 的 ±3.0pp CI 实际上比 DocRED 70B 200-doc 的 ±3.3pp 更窄（因为 Arg-F1 绝对水平低，per-doc σ 小）
- RoV 从 8.8–38.3% 降到精确 0%，bootstrap CI 完全不重叠，power ≈ 1.0
- n=20 的限制是检测不了 <2pp 的 F1 差异，但论文的核心声明是 violation elimination 而非 F1 提升

用 `\input{appendix_power_analysis}` 在 appendix 中引入，label 为 `app:power-analysis-full`。

---

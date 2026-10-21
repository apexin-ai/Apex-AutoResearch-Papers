# paper mechanistic anova convergence

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_mechanistic-anova-convergence_20260522T113138_result.json`
- **Structured JSON:** [`1899ce04f6cf6a7434e5.json`](../../sessions/18/1899ce04f6cf6a7434e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

**ANOVA 方差分解** — η² 四项之和均为 1.0000，符合预期：
- **Location features** (entropy_mean, ttr, hapax_ratio): η²(depth) = 0.34–0.37，远超 η²(generator) ≈ 0.02 → depth 是主效应
- **Shape features** (entropy_min, entropy_max, tail_decay): η²(depth) < 0.01 → depth 几乎无解释力，架构不变量
- **Intermediate** (entropy_std): η²(depth) = 0.054，介于两组之间

所有效应均在 p < 0.001 水平显著。

**收敛率拟合**：
- Location features: λ = 0.40 ± 0.26，R² = 0.99 → 稳定指数收敛，符合 Markov chain mixing
- Shape features: λ 极大且方差爆炸（5.27 ± 8.43），R² = 0.73 → 指数模型不适配，这些 feature 本身就是 flat 的（不随 depth 变化）
- entropy_std 的 R² = 0.60，拟合较差，确认其过渡性质

输出文件：
- `anova_table.csv` — η² 分解表
- `convergence_rates.csv` — 56 行（7 features × 8 generators）的 λ、R² 值
- `anova_table.tex` — booktabs 格式 appendix 表格

---

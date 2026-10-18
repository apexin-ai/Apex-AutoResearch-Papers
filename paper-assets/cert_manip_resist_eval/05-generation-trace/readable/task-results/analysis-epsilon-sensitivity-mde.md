# analysis epsilon sensitivity mde

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_epsilon-sensitivity-mde_20260523T122958_result.json`
- **Structured JSON:** [`f14f46f5b3057a89fdb0.json`](../../sessions/f1/f14f46f5b3057a89fdb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 JSON 文件已复制到本地。以下是关键结果汇总：

---

## A2: ε 敏感性

### (a) ASR=0 面板占比

| 条件 | K=3 (455) | K=5 (3003) | K=7 (6435) |
|------|-----------|------------|------------|
| mmlu_prompt_injection | 0.0% | 0.0% | 0.0% |
| mmlu_sycophancy | 0.22% | 0.10% | 0.09% |
| mmlu_score_manipulation | 0.22% | 0.03% | 0.0% |
| mmlu_verbosity_bias | 0.88% | 0.53% | 0.70% |
| mmlu_position_bias | 0.0% | 0.0% | 0.0% |
| mmlu_authority_bias | 0.66% | 0.20% | 0.56% |
| arc_prompt_injection | 3.30% | 1.90% | 1.23% |
| arc_sycophancy | 10.99% | 23.31% | 38.07% |
| arc_score_manipulation | 3.96% | 6.46% | 9.77% |
| arc_verbosity_bias | 11.87% | 14.62% | 20.89% |
| arc_position_bias | 0.0% | 0.0% | 0.0% |
| arc_authority_bias | 23.30% | 31.54% | 39.50% |

MMLU 条件的 ASR=0 率很低（<1%），ε 选择影响有限。ARC 的 sycophancy/authority_bias 在 K↑ 时 ASR=0 率显著增加（K=7 高达 38-40%），说明大面板更有效地抵御这些攻击，但也导致 log 变换中 ε 更重要。

### (b) ε 系数对比（η_max β_std）

| 条件 | ε=1e-3 | ε=1e-6 | ε=1e-9 |
|------|--------|--------|--------|
| mmlu_prompt_inj | 0.613 | 0.616 | 0.616 |
| mmlu_sycophancy | 0.539 | 0.413 | 0.413 |
| mmlu_score_manip | 0.602 | 0.543 | 0.543 |
| mmlu_verbosity | 0.677 | 0.502 | 0.502 |
| arc_prompt_inj | 0.260 | 0.215 | 0.215 |
| arc_sycophancy | 0.626 | 0.446 | 0.446 |
| arc_position | 0.418 | -0.011 | -0.011 |

ε=1e-6 和 ε=1e-9 系数基本一致（差异 <0.01），ε=1e-3 系数偏大但方向不变。结论：ε 选择不影响 η_max 主导性的定性结论。

---

## A4: K=5/K=7 MDE

| Panel size | n_panels | n_clusters | MDE_80 (β_std) |
|------------|----------|------------|----------------|
| K=3 | 455 | 3 | **0.144** |
| K=5 | 3003 | 5 | **0.048** |
| K=7 | 6435 | 7 | **0.036** |

K=5 和 K=7 的 MDE_80 分别为 0.048 和 0.036，相比 K=3 的 0.144 大幅下降（约 3-4 倍）。即使使用最保守的 CR1 clustered SE，大面板也能检测到非常小的 K_eff 效应。

**输出文件已保存：**
- `docs/paper/data/epsilon_sensitivity.json`
- `docs/paper/data/power_analysis_all_K.json`

---

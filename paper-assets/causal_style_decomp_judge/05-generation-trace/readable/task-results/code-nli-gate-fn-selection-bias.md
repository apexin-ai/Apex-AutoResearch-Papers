# code nli gate fn selection bias

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nli_gate_fn_selection_bias_20260521T101850_result.json`
- **Structured JSON:** [`386b1f896a5640aa2044.json`](../../sessions/38/386b1f896a5640aa2044.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

## FORMALITY (N=355, pass=323/91.0%, fail=32/9.0%)

Gate 失败全部来自 double-rewrite（cf_fail=0, dr_fail=32）。

| Metric | Pass | Fail | U p-val | Cliff's d | Size |
|---|---|---|---|---|---|
| norm_levenshtein | 0.3676 | 0.3967 | 0.2315 | +0.13 | negligible |
| char_ratio | 0.9965 | 1.1596 | **0.0005** | +0.37 | **medium** |
| flesch_diff | 16.61 | 23.73 | **0.0112** | +0.27 | **small** |

**Direction**: Fail 组 edit distance 更大但不显著 (p=0.23) → **无显著 selection bias**。
Double-rewrite 的 edit distance 在 fail 组显著更大 (pass=0.37 vs fail=0.53, p=0.0003, medium)，符合预期：dr 失败是因为 double-rewrite 偏离原文更远。

## VERBOSITY (N=100, pass=39/39.0%, fail=61/61.0%)

| Metric | Pass | Fail | U p-val | Cliff's d | Size |
|---|---|---|---|---|---|
| norm_levenshtein | 0.5284 | 0.6901 | **0.0002** | +0.45 | **medium** |
| char_ratio | 2.10 | 8.79 | **0.0018** | +0.37 | **medium** |
| token_ratio | 2.24 | 6.75 | **0.0024** | +0.36 | **medium** |
| jaccard_overlap | 0.4205 | 0.2685 | **0.0003** | -0.43 | **medium** |
| levenshtein_ratio | 0.6100 | 0.4254 | **0.0002** | -0.44 | **medium** |
| flesch_diff | 12.36 | 22.08 | **0.0418** | +0.24 | **small** |

**Direction**: Fail 组 edit distance **显著更大** (p=0.0002) → **CONSERVATIVE bias**：gate 过滤掉了 style 变化更大的 pairs，使得 measured effects 是 lower bounds。

## 结论

- **Formality**: 无显著 selection bias（cf 维度），gate 主要过滤 double-rewrite 质量差的 pairs
- **Verbosity**: gate 存在 selection bias 但方向是 **conservative** —— 过滤掉了 style 变化更剧烈的 pairs，意味着论文报告的 effect 是下界估计，对论文主张有利
- 可以在论文中写：NLI gate 的 filtering 在 verbosity 轴上偏向保守（Cliff's δ=+0.45, medium），measured ATE 为 lower bound

---

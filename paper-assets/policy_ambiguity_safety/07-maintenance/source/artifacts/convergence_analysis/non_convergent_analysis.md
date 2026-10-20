# Analysis 3: Non-Convergent (Divergent) Clause Characteristics

## Overview
- Divergent clauses (1-2/5 models violating): 92
- Convergent clauses (≥3/5 models violating): 124

## 1. Type Distribution of Divergent Clauses

| Type | Count |
|------|-------|
| auth_scope | 16 |
| cond_prec | 19 |
| coreferential | 16 |
| incompleteness | 8 |
| lexical | 19 |
| scopal | 14 |

χ² test for uniformity: χ² = 5.435, p = 0.3652

## 2. Clause Text Length: Divergent vs Convergent

| Metric | Divergent | Convergent |
|--------|-----------|------------|
| Median word count | 48.5 | 46.0 |

Mann-Whitney U = 6335.5, p = 0.1642

## 3. Per-Model Solo Violation Frequency in Divergent Clauses

| Model | Violations in divergent clauses |
|-------|-------------------------------|
| deepseek-v3 | 43 |
| qwen3-235b | 28 |
| gpt-5.4 | 27 |
| gpt-4.1 | 18 |
| claude-sonnet-4-6 | 16 |

χ² test for model uniformity: χ² = 17.318, p = 0.0017

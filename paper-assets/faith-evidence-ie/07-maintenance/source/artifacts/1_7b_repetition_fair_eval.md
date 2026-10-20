# 1.7B Repetition Analysis & Fair Evaluation Subset

## 1. Repetition & Truncation Rates

| Metric               | No-Evidence | With-Evidence |
|----------------------|-------------|---------------|
| Total docs           | 985         | 985           |
| Truncated            | 501 (50.9%) | 314 (31.9%)   |
| Repetitive           | 467 (47.4%) | 215 (21.8%)   |
| Both trunc+rep       | 467         | 209           |
| Trunc only (not rep) | 34          | 105           |
| Rep only (not trunc) | 0           | 6             |
| Clean                | 484 (49.1%) | 665 (67.5%)   |

**Key finding**: In no-evidence, ALL 467 repetitive docs are also truncated (rep => trunc). The model repeats triples until hitting max_new_tokens. Only 34 docs are truncated without repetition (genuinely long outputs). In with-evidence, 6 docs are repetitive but not truncated.

**Repetition definition**: A document is "repetitive" if its raw output contains 3+ consecutive identical triple strings, OR if unique_triples/total_triples < 0.5 when total > 5.

**Repetitive doc stats**:
- No-evidence: avg unique ratio = 0.208, avg parsed triples = 41.3
- With-evidence: avg unique ratio = 0.269, avg parsed triples = 30.0

## 2. Fair Subset Definition

**Strict fair subset**: Exclude any doc that is truncated OR repetitive in EITHER model.
- Size: **439 / 985 (44.6%)**

**Trunc-only fair subset**: Exclude any doc truncated in either model (keep rep-only).
- Size: **442 / 985 (44.9%)**

(Difference is only 3 docs because rep-only is rare.)

## 3. Ign-F1 Comparison (Official Evaluator)

### Full set (985 docs)
| Model         | Ign-P  | Ign-R  | Ign-F1 |
|---------------|--------|--------|--------|
| No-Evidence   | 0.4213 | 0.3776 | 0.3982 |
| With-Evidence | 0.4830 | 0.4743 | 0.4786 |
| **Evidence tax** | | | **-8.04pp** |

### Fair subset - strict (439 docs, excl trunc+rep)
| Model         | Ign-P  | Ign-R  | Ign-F1 |
|---------------|--------|--------|--------|
| No-Evidence   | 0.5163 | 0.6416 | 0.5722 |
| With-Evidence | 0.6096 | 0.6590 | 0.6334 |
| **Evidence tax** | | | **-6.12pp** |

### Fair subset - trunc-only (442 docs)
| Model         | Ign-P  | Ign-R  | Ign-F1 |
|---------------|--------|--------|--------|
| No-Evidence   | 0.5140 | 0.6406 | 0.5704 |
| With-Evidence | 0.6079 | 0.6579 | 0.6319 |
| **Evidence tax** | | | **-6.16pp** |

## 4. Evidence Tax Summary

| Subset             | N docs | No-Evi Ign-F1 | With-Evi Ign-F1 | Evidence Tax |
|--------------------|--------|---------------|-----------------|-------------|
| Full set           | 985    | 0.3982        | 0.4786          | -8.04pp     |
| Fair (strict)      | 439    | 0.5722        | 0.6334          | -6.12pp     |
| Fair (trunc-only)  | 442    | 0.5704        | 0.6319          | -6.16pp     |

## 5. Interpretation

1. **With-evidence consistently outperforms no-evidence** at 1.7B scale, on all subsets. The "evidence tax" is negative (evidence helps, not hurts).

2. **Truncation/repetition inflates the gap**: On the full set, evidence tax = -8.04pp. On the fair subset, it shrinks to -6.12pp. This is because no-evidence suffers much more from truncation (50.9% vs 31.9%), which disproportionately hurts its score.

3. **Both models improve dramatically on the fair subset**: No-evi jumps from 0.3982 to 0.5722 (+17.4pp), with-evi from 0.4786 to 0.6334 (+15.5pp). The truncated/repetitive docs are a major drag on both models, but more so for no-evidence.

4. **The corrected evidence tax is -6.12pp**, down from -8.04pp on the full set. About 24% of the original gap was due to differential truncation rates, not actual model capability differences.

## 6. Data Sources

- No-evidence: `/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v3/` (no_evidence=true, max_new_tokens=1024)
- With-evidence: `/root/autodl-tmp/eval_results/qwen3_1_7b_sft_eval/` (no_evidence=false, max_new_tokens=1024)
- Analysis script: `/tmp/fair_eval.py`

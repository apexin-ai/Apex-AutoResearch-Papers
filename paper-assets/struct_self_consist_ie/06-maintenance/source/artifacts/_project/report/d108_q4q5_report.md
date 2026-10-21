# D108: Q4 + Q5 Analysis Report

## Q4: Why CoNLL Entity-Token LP Variance ≈ 0

### 1. Per-Entity-Type Token Statistics (Canonical Types Only)

**SCIERC**

| Type | N | Mean LP | Token Sat. (<1e-4) | Mean Len | Cross-sample Var (med) | Tied% |
|---|---|---|---|---|---|---|
| Generic | 1919 | -0.1666 | 42.3% | 1.5 | 5.22e-06 | 36% |
| Material | 1140 | -0.0497 | 74.9% | 3.8 | 5.58e-07 | 31% |
| Method | 3296 | -0.0341 | 84.9% | 4.5 | 2.58e-08 | 47% |
| Metric | 549 | -0.0689 | 70.7% | 3.0 | 1.98e-06 | 34% |
| OtherScientificTerm | 4168 | -0.0848 | 71.4% | 3.7 | 7.73e-04 | 18% |
| Task | 1981 | -0.0446 | 78.4% | 4.6 | 3.11e-07 | 41% |

**CONLL**

| Type | N | Mean LP | Token Sat. (<1e-4) | Mean Len | Cross-sample Var (med) | Tied% |
|---|---|---|---|---|---|---|
| LOC | 13498 | -0.0304 | 48.7% | 2.1 | 7.31e-10 | 60% |
| MISC | 6764 | -0.1268 | 37.9% | 2.5 | 1.54e-06 | 36% |
| ORG | 13134 | -0.0348 | 53.3% | 2.9 | 2.39e-10 | 61% |
| PER | 12565 | -0.0356 | 56.6% | 3.7 | 3.93e-09 | 53% |

### 2. Entity Set Consistency Across Samples

| Dataset | Mean Jaccard | Median Jaccard | Text-only Jaccard |
|---|---|---|---|
| SCIERC | 0.6647 | 0.6637 | 0.7585 |
| CONLL | 0.8658 | 1.0000 | 0.9160 |

### 3. Instance-Level Entity LP Variance

| Dataset | Median Var | Mean Var | Tied (<1e-8) |
|---|---|---|---|
| SCIERC | 5.92e-04 | 2.17e-02 | 19.1% |
| CONLL | 2.41e-10 | 5.75e-02 | 65.2% |

### 4. Hallucinated Entity Types

- **SCIERC**: 0.0% of mentions use non-canonical types: Anatomy, Author
- **CONLL**: 0.1% of mentions use non-canonical types

### Key Interpretation

The near-zero entity-token LP variance in CoNLL stems from **three compounding factors**:

1. **Higher entity set consistency**: CoNLL mean Jaccard = 0.8658 vs SciERC = 0.6647. The model extracts nearly the same entity set across samples for CoNLL (well-defined named entities in news), while SciERC entity boundaries are more ambiguous.

2. **Shorter, higher-frequency entity tokens**: CoNLL entities (PER/LOC/ORG) are short proper names (2-4 tokens) composed of common subwords. The model assigns near-deterministic probability to these tokens.

3. **Per-type saturation pattern**: CoNLL PER/LOC/ORG all show >53% tied instances (cross-sample var < 1e-8). SciERC OtherScientificTerm has only 18% tied. MISC is CoNLL's outlier (36% tied), consistent with MISC being a semantically diverse catch-all category.

4. **Entity LP magnitude**: CoNLL instance median entity LP var = 2.41e-10, vs SciERC = 5.92e-04 (2.5M× higher).

## Q5: 4B vs 8B Output Diversity

### SCIERC

| Metric | 4B (n=8 samp) | 8B (n=8 samp) |
|---|---|---|
| Mean unique | 4.15 | 3.44 |
| Median unique | 4.0 | 3.0 |
| Diversity ratio | 0.5191 | 0.4294 |

Paired: div ratio diff (4B−8B) = +0.090, 4B more diverse in 50.3% instances.

### CONLL

| Metric | 4B (n=8 samp) | 8B (n=16 samp) |
|---|---|---|
| Mean unique | 1.14 | 2.27 |
| Diversity ratio | 0.1427 | 0.1416 |

Paired: div ratio diff = +0.001 (essentially identical after normalizing for sample count).

### Diversity vs F1

| Config | High-Div F1 | Low-Div F1 | Delta |
|---|---|---|---|
| 4B_scierc | 0.5405 | 0.6976 | -0.1571 |
| 8B_scierc | 0.5436 | 0.6971 | -0.1536 |
| 4B_conll | 0.7179 | 0.9455 | -0.2276 |
| 8B_conll | 0.7644 | 0.9637 | -0.1994 |

### Key Findings

1. **SciERC**: 4B is more diverse (div ratio +0.09). Smaller model → less confident → more sampling variation.
2. **CoNLL**: Diversity ratio nearly identical. Both models are highly confident on CoNLL.
3. **Diversity hurts F1**: Higher diversity correlates with -0.15 to -0.23 F1 drop across all configs.
# Type → Mechanism Classification Analysis

## Data
- **614** violation traces across **5** models and **6** ambiguity types
- Failure modes mapped to **3 mechanisms**: structural_misparse, gap_filling, boundary_violation (+other)
- Non-canonical modes: referent_misidentification→structural_misparse, surface_adoption→gap_filling

## Confusion Matrix (3-mechanism)

| Type | Structural Misparse | Gap-Filling | Boundary Violation | Other |
|------|-------------------:|------------:|-------------------:|------:|
| authorization_scope | 4 | 28 | 72 | 0 |
| conditional_precedence | 50 | 10 | 10 | 22 |
| coreferential | 37 | 29 | 5 | 8 |
| incompleteness | 43 | 70 | 16 | 5 |
| lexical | 42 | 54 | 10 | 1 |
| scopal | 81 | 4 | 13 | 0 |

## Classification Accuracy

| Granularity | Overall Accuracy |
|------------|----------------:|
| 5+1 failure modes | **59.3%** |
| 3+1 mechanisms | **59.3%** |

### Per-type (3-mechanism)

| Type | Majority Mechanism | Accuracy |
|------|--------------------|-------:|
| authorization_scope | boundary_violation | 69.2% |
| conditional_precedence | structural_misparse | 54.4% |
| coreferential | structural_misparse | 46.8% |
| incompleteness | gap_filling | 52.2% |
| lexical | gap_filling | 50.5% |
| scopal | structural_misparse | 82.7% |

## Association Strength

| Metric | 5+1 way | 3+1 way |
|--------|--------:|--------:|
| Cramér's V | 0.3627 | 0.4458 |
| p-value | 0.0 | 0.0 |

## Mutual Information Comparison

| Pair | MI (bits) | NMI |
|------|----------:|----:|
| I(type; mechanism, 5-way) | 0.4344 | 0.236 |
| I(type; mechanism, 3-way) | 0.4076 | 0.2316 |
| I(type; violation rate) | 0.0135 | 0.0138 |

**Key finding**: Type predicts mechanism **30.2×** better than violation rate (MI ratio).
This supports the paper's claim that taxonomy value lies in predicting failure mechanisms, not violation rates.

## Cross-Model Consistency (3-mechanism)

**2/6** types have unanimous majority mechanism across all 5 models.

| Type | Claude | DeepSeek | GPT-4.1 | GPT-5.4 | Qwen3 | Unanimous |
|------|--------|----------|---------|---------|-------|-----------|
| authorization_scope | boundary_vio | boundary_vio | boundary_vio | boundary_vio | boundary_vio | Yes |
| conditional_precedence | structural_m | structural_m | other | structural_m | structural_m | No |
| coreferential | structural_m | structural_m | gap_filling | structural_m | gap_filling | No |
| incompleteness | gap_filling | structural_m | gap_filling | gap_filling | structural_m | No |
| lexical | structural_m | structural_m | gap_filling | gap_filling | gap_filling | No |
| scopal | structural_m | structural_m | structural_m | structural_m | structural_m | Yes |

## Key Takeaways

1. **Strong type→mechanism mapping**: Cramér's V = 0.4458 (3-way), classification accuracy = 59.3%
2. **MI comparison**: I(type; mechanism) = 0.4076 bits >> I(type; violation) = 0.0135 bits — 30.2× ratio
3. **Cross-model stability**: 2/6 types show unanimous mechanism across all 5 models
4. **Dominant mappings** (3-mechanism):
   - authorization_scope → boundary_violation
   - conditional_precedence, scopal → structural_misparse  
   - incompleteness, lexical → gap_filling
   - coreferential → split (model-dependent)

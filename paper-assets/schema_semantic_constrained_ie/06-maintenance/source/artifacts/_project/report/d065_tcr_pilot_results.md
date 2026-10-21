# D065: TCR Pilot Results

## Algorithm

Type Consistency Resolution (TCR) resolves cross-field (CF) type inconsistencies in S1 extraction outputs. For each entity mention that receives multiple distinct types across its appearances (entity list + relation head_type/tail_type), TCR selects the type that maximizes constraint satisfaction across all relational contexts the entity participates in. Scoring: for each candidate type, count how many of the entity's (relation, role) pairs admit at least one valid partner type under the schema's domain-range constraints. Ties broken by original frequency, then alphabetical order.

## Results

| Config | CF Before | CF After | CF Δ | DR Before | DR After | DR Δ | Resolvable% | Fundamental% |
|--------|-----------|----------|------|-----------|----------|------|-------------|-------------|
| SciERC ZS Qwen S1 | 9.75% (245) | 0.00% (0) | -9.75pp | 0.93% (16) | 1.21% (21) | +0.28pp | 97.96% | 2.04% |
| SciERC ZS Llama S1 | 6.40% (162) | 0.00% (0) | -6.40pp | 0.08% (1) | 0.30% (4) | +0.22pp | 98.15% | 1.85% |
| SciERC LoRA Qwen S1 | 1.19% (21) | 0.00% (0) | -1.19pp | 0.00% (0) | 0.00% (0) | +0.00pp | 100% | 0.00% |
| SciERC LoRA Llama S1 | 0.46% (8) | 0.00% (0) | -0.46pp | 0.09% (1) | 0.09% (1) | +0.00pp | 100% | 0.00% |

### F1 Impact

| Config | E-F1 Before | E-F1 After | E-F1 Δ | R-F1 Before | R-F1 After | R-F1 Δ | Typed R-F1 Δ |
|--------|------------|------------|--------|------------|------------|--------|-------------|
| SciERC ZS Qwen S1 | 0.3098 | 0.2969 | -0.0129 | 0.0836 | 0.0836 | +0.0000 | +0.0000 |
| SciERC ZS Llama S1 | 0.2349 | 0.2171 | -0.0178 | 0.0254 | 0.0254 | +0.0000 | +0.0000 |
| SciERC LoRA Qwen S1 | 0.6705 | 0.6630 | -0.0075 | 0.4377 | 0.4377 | +0.0000 | -0.0019 |
| SciERC LoRA Llama S1 | 0.6776 | 0.6758 | -0.0018 | 0.4547 | 0.4547 | +0.0000 | -0.0010 |

## Analysis

### CF Reduction
- TCR achieves **100% CF elimination** across all 4 configurations.
- ZS models have significantly higher initial CF rates (6-10%) compared to LoRA models (0.5-1.2%), indicating fine-tuning already teaches type consistency.

### DR Impact
- ZS models see minor DR increases (+5 and +3 new violations). When TCR unifies an entity's type, the chosen type may violate domain-range constraints for some relations.
- LoRA models see zero or negligible DR impact (already low baseline).
- DR increase is small relative to CF reduction (~0.2pp DR increase vs ~8pp CF decrease for ZS).

### Fundamental Conflict Rate
- Only 2% of CF entities in ZS models are "fundamental" (no single type satisfies all relational contexts). For LoRA models, 0%.
- This confirms the schema is not overly restrictive for SciERC.

### F1 Impact
- E-F1 drops slightly (-0.18pp to -1.78pp). This is expected: TCR sometimes changes a correct type to match surrounding constraints. The conflict resolution prioritizes schema consistency over per-entity accuracy.
- R-F1 (span-level, without type matching) is unchanged because TCR only modifies type labels.
- Typed R-F1 shows minimal impact (-0.0019 worst case).

## Conclusion

TCR is highly effective for CF reduction: complete elimination with minimal DR and F1 side effects. The cost is a small E-F1 drop (averaging -0.01 for LoRA, -0.015 for ZS). For the paper, TCR is best positioned as a lightweight post-processing step that guarantees cross-field consistency, complementary to grammar-constrained decoding which targets within-field constraints.
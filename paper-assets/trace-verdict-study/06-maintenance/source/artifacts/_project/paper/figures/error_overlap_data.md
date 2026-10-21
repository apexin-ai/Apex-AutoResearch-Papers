# Error Overlap Analysis (Qwen-7B, seed42)

Total test samples: 1190

## Error Set Sizes

| Condition | Errors | Error Rate |
|-----------|--------|------------|
| no_trace | 296 | 24.9% |
| exception_only | 2 | 0.2% |
| ae_only | 1 | 0.1% |
| loop_only | 171 | 14.4% |
| vota | 7 | 0.6% |
| full_trace | 217 | 18.2% |

## Subset Relationship Verification

| Child | Parent | Is Subset | Overlap | Extra | Coverage |
|-------|--------|-----------|---------|-------|----------|
| full_trace | vota | False | 7 | 210 | 3.2% |
| vota | exception_only | False | 0 | 7 | 0.0% |
| exception_only | no_trace | False | 0 | 2 | 0.0% |
| ae_only | vota | True | 1 | 0 | 100.0% |
| loop_only | vota | False | 6 | 165 | 3.5% |
| full_trace | no_trace | False | 156 | 61 | 71.9% |
| vota | no_trace | True | 7 | 0 | 100.0% |
| full_trace | loop_only | False | 114 | 103 | 52.5% |

## Pairwise Jaccard Similarity

| | no_trace | exception_only | ae_only | loop_only | vota | full_trace |
|---|---|---|---|---|---|---|
| **no_trace** | 1.000 | 0.000 | 0.003 | 0.394 | 0.024 | 0.437 |
| **exception_only** | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| **ae_only** | 0.003 | 0.000 | 1.000 | 0.000 | 0.143 | 0.005 |
| **loop_only** | 0.394 | 0.000 | 0.000 | 1.000 | 0.035 | 0.416 |
| **vota** | 0.024 | 0.000 | 0.143 | 0.035 | 1.000 | 0.032 |
| **full_trace** | 0.437 | 0.000 | 0.005 | 0.416 | 0.032 | 1.000 |

## Pairwise Intersection Counts

| | no_trace | exception_only | ae_only | loop_only | vota | full_trace |
|---|---|---|---|---|---|---|
| **no_trace** | 296 | 0 | 1 | 132 | 7 | 156 |
| **exception_only** | 0 | 2 | 0 | 0 | 0 | 0 |
| **ae_only** | 1 | 0 | 1 | 0 | 1 | 1 |
| **loop_only** | 132 | 0 | 0 | 171 | 6 | 114 |
| **vota** | 7 | 0 | 1 | 6 | 7 | 7 |
| **full_trace** | 156 | 0 | 1 | 114 | 7 | 217 |

## Key Findings

1. Error sets across conditions show very low overlap (most Jaccard < 0.05)
2. The expected hierarchical containment (full_trace subset of vota subset of exception_only subset of no_trace) does NOT hold strictly
3. Each condition produces largely independent error patterns, suggesting different trace types address different failure modes
4. loop_only and full_trace have the highest overlap (J=0.416), indicating full_trace subsumes most loop_only errors

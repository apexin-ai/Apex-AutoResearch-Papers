# analysis fk bootstrap per instance

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fk_bootstrap_per_instance_20260515T130838_result.json`
- **Structured JSON:** [`8f10eb89adfff74d52b7.json`](../../sessions/8f/8f10eb89adfff74d52b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Output saved to `output/analysis_fk_bootstrap_per_instance.json`. Results:

### SciERC NER (N=8, n=529)

**Signal rhos (Spearman with greedy F1):**
| Signal | rho | 95% CI |
|--------|-----|--------|
| FK | 0.267 | [0.176, 0.354] |
| SJ | 0.360 | [0.277, 0.437] |
| VC | 0.379 | [0.299, 0.456] |
| EM | 0.295 | [0.212, 0.371] |

**FK vs others (bootstrap + permutation):**
| Comparison | delta | 95% CI | p_perm |
|------------|-------|--------|--------|
| FK vs SJ | -0.093 | [-0.159, -0.031] | 0.080 (n.s.) |
| FK vs VC | -0.113 | [-0.200, -0.026] | 0.031 (*) |
| FK vs EM | -0.028 | [-0.118, +0.064] | 0.622 (n.s.) |

**FK excess agreement:** 0.240 [0.217, 0.265], P_o=0.749, P_e=0.509

### CoNLL NER (N=16, n=2756)

**FK vs others:**
| Comparison | delta | 95% CI | p_perm |
|------------|-------|--------|--------|
| FK vs SJ | -0.056 | [-0.071, -0.041] | 0.0001 (***) |
| FK vs VC | -0.022 | [-0.045, +0.002] | 0.078 (n.s.) |
| FK vs EM | -0.071 | [-0.089, -0.053] | 0.0001 (***) |

**FK excess agreement:** 0.582 [0.567, 0.597]

**Key findings:** FK is consistently the weakest signal. On SciERC, the bootstrap CIs exclude zero for FK vs SJ and FK vs VC (though permutation p for FK vs SJ is borderline at 0.08). On CoNLL with larger n, FK is significantly worse than SJ and EM (p<0.001). FK excess agreement on SciERC is modest (0.24) due to high P_e (~0.51), while CoNLL has much higher excess (0.58).

---

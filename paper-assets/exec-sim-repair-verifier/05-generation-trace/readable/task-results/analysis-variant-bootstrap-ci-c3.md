# analysis variant bootstrap ci c3

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_variant-bootstrap-ci-c3_20260519T090913_result.json`
- **Structured JSON:** [`61b768c9a3c83a160913.json`](../../sessions/61/61b768c9a3c83a160913.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Summary of findings:

**CLS vs CWM (paired bootstrap, large gap ~29-35pp)**
| Comparison | Diff | 95% CI | p | Power |
|---|---|---|---|---|
| Qwen3-8B | +29.17pp | [10.42, 47.92] | 0.003 | 0.784 |
| DeepSeek | +35.42pp | [18.75, 50.05] | <0.001 | 0.960 |

**CLS vs TRAJ (unpaired bootstrap, small gap ~0-8pp)**
| Comparison | Diff | 95% CI | p | Power |
|---|---|---|---|---|
| Qwen3-4B | -4.17pp | [-22.92, 14.58] | 0.740 | 0.066 |
| Qwen3-8B | +8.33pp | [-8.33, 25.00] | 0.385 | 0.163 |
| DeepSeek | +0.00pp | [-16.67, 16.67] | 1.000 | 0.025 |

**CWM vs TRAJ (unpaired bootstrap, medium-large gap ~21-35pp)**
| Comparison | Diff | 95% CI | p | Power |
|---|---|---|---|---|
| Qwen3-8B | -20.83pp | [-39.58, -2.08] | 0.039 | 0.579 |
| DeepSeek | -35.42pp | [-52.08, -16.67] | <0.001 | 0.972 |

**Key narrative points (as requested):**
- **MDE at n=48: 25.0pp** (McNemar-style)
- CLS-CWM large gaps: mean power 0.872, both significant, **well-powered**
- CLS-TRAJ small gaps: mean power 0.084, none significant, **underpowered** (consistent with TOST equivalence)
- CWM-TRAJ large gaps: mean power 0.776, both significant

Output: `artifacts/variant_bootstrap_ci.json`

---

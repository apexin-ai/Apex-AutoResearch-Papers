# code r14 exp2 cross subject unique

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r14_exp2_cross_subject_unique_20260522T115630_result.json`
- **Structured JSON:** [`36b9e9124b8357ed09ac.json`](../../sessions/36/36b9e9124b8357ed09ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs are in `artifacts/r14_mf1_domain_profile/`:

| File | Content |
|------|---------|
| `cross_subject_unique_analysis.md` | Full report |
| `kappa_results.csv` | Per-subject κ and contingency counts |
| `accuracy_delta_vs_unique_c.csv` | Accuracy delta vs cross-unique C |
| `cross_subject_unique_analysis.py` | Reproducible script |

**Key findings**:

- **κ = 0.798 mean** (0.743–0.904): substantial agreement between cross-subject and within-subject matching on C classification
- **57 cross-unique C items** (6.8% of 834): few items are flagged C only by cross-subject matching
- **ρ = −0.700** (p = 0.188): cross-unique C items do NOT concentrate in high-shift domains — direction is negative (more shift → fewer unique C items)
- **Direction**: cross C% (40.8%) slightly exceeds within C% (38.1%) for these 5 subjects (Δ = 2.7 pp), consistent with a mild confound effect but small relative to ~40% base rate

**Bottom line**: multidimensional confound contributes at most a minor secondary effect. The high inter-method agreement and lack of domain-shift concentration rule it out as the primary driver of cross-subject DIF flags.

---

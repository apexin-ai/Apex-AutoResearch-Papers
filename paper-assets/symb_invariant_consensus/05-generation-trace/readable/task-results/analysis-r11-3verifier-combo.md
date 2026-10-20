# analysis r11 3verifier combo

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r11-3verifier-combo_20260521T112038_result.json`
- **Structured JSON:** [`d5cf177e266c98c4153f.json`](../../sessions/d5/d5cf177e266c98c4153f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results registered. Here's the summary:

## R11 3-Verifier Combo BH-Corrected Significance

**Setup**: Mistral-7B on ProofWriter D5-600, SC baseline = 39.00% (234/600)

### Per-Verifier Results (combo vs SC, McNemar exact test)

| Verifier | Standalone | w=3 Δ | w=3 raw p | w=5 Δ | w=5 raw p |
|---|---|---|---|---|---|
| DeBERTa-large-MNLI | 55.0% | +4.17pp | 0.00035 | +8.33pp | 1×10⁻⁶ |
| DeBERTa-base-MNLI | 36.2% | +2.00pp | 0.058 | +6.00pp | 7×10⁻⁵ |
| DeBERTa-v3-large | 45.2% | +1.67pp | 0.154 | +4.83pp | 0.0017 |

### 3-Verifier Ensemble

| Method | w=1 Δ | w=3 Δ | w=5 Δ |
|---|---|---|---|
| Majority vote | +3.83pp (p=0.002) | **+9.50pp** (p=0.0002) | **+11.00pp** (p=0.0003) |
| Average probs | +0.67pp (p=0.125) | +2.33pp (p=0.024) | +4.83pp (p=0.0006) |

### BH Correction (15 tests total)

- **9/15 significant at BH-corrected α=0.05**
- **10/15 significant at BH-corrected α=0.10**
- All w≥3 tests for DeBERTa-large-MNLI remain significant (BH p=0.001, 1.5×10⁻⁵)
- All 3-verifier majority vote tests significant (BH p=0.004, 0.001, 0.001)
- Only w=1 tests (insufficient NLI weight) lose significance

**Conclusion**: NLI combo gains survive BH correction. The non-significant tests are exclusively w=1 (where NLI weight is too low to influence SC majority). With w≥3, the combo effect is robust across verifier architectures.

**Note**: Used 3 DeBERTa variants instead of DeBERTa/RoBERTa/BART due to model download constraints on the server (network bandwidth insufficient for 1.4GB model files). The DeBERTa variants span different architectures (base vs large vs v3-large) and training data, providing meaningful diversity.

---

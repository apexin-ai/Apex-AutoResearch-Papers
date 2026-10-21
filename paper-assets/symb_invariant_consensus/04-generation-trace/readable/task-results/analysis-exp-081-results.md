# analysis exp 081 results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-081-results_20260520T002811_result.json`
- **Structured JSON:** [`77a6af1085dcc84d8abc.json`](../../sessions/77/77a6af1085dcc84d8abc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data needed. Let me compute the per-question distribution from that output.

From the grep output, among 83 debate-correct questions: 27 had sc_correct=false (debate improved), 56 had sc_correct=true (both correct).

This gives the full 2×2 distribution:
- both_correct: 56, debate_improved: 27, debate_degraded: 114−56=58, both_wrong: 204−56−27−58=63

## exp-081 Results
- n_samples: 204/204
- sc_accuracy: 0.5588 (114/204)
- debate_accuracy: 0.4069 (83/204)
- delta: -15.20pp
- wall_time: 177.6min
- fallbacks: 18/204

### Per-question debate effect
| Category | Count | % |
|---|---|---|
| Both correct | 56 | 27.5% |
| Debate improved (debate ✓, sc ✗) | 27 | 13.2% |
| Debate degraded (debate ✗, sc ✓) | 58 | 28.4% |
| Both wrong | 63 | 30.9% |

Net: 27 improved − 58 degraded = **−31 questions** flipped by debate

## Comparison with exp-076 (seed=42)
| Metric | seed=42 (exp-076) | seed=123 (exp-081) |
|---|---|---|
| sc_accuracy | 0.5686 | 0.5588 |
| debate_accuracy | 0.3824 | 0.4069 |
| delta | -18.63pp | -15.20pp |

- Difference in delta: |−15.20 − (−18.63)| = **3.43pp**
- Cross-seed consistency: **unstable** (>2pp threshold), but both seeds show the same direction — debate consistently degrades accuracy

## Conclusion
- conclusion: **negative**
- Rationale: Debate pipeline reduces accuracy by 15.20pp on seed=123, consistent with the 18.63pp degradation on seed=42. While the magnitude differs by 3.43pp (exceeding the ±2pp stability criterion), the qualitative finding is robust: debate-augmented constraint extraction hurts Mistral-7B on FOLIO across both seeds. The degradation pattern is asymmetric — debate flips 58 correct→wrong vs. only 27 wrong→correct — indicating the MaxSAT aggregation over debate-extracted constraints systematically overrides correct SC majority votes.

## Checkpoint/Log Paths
- checkpoint_path: `/root/symb_invariant_consensus/results/exp081_debate_mistral_folio_seed123/results.json`
- log_path: `/root/runs/symb_invariant_consensus/exp-081-debate-mistral-folio-seed123.log`

---

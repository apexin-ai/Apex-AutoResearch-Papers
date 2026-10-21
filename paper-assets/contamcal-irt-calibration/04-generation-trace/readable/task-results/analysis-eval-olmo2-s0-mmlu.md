# analysis eval olmo2 s0 mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_olmo2_s0_mmlu_20260520T111827_result.json`
- **Structured JSON:** [`1b42942492bce606a1f3.json`](../../sessions/1b/1b42942492bce606a1f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

**OLMo-2-7B seed=0 MMLU 5-shot results:**

| Dosage | Accuracy | Δ vs baseline |
|--------|----------|---------------|
| d000 | 55.34% | — |
| d005 | 56.62% | +1.28pp |
| d025 | 56.52% | +1.18pp |
| d050 | 56.27% | +0.93pp |
| d100 | 56.72% | +1.38pp |

**Cross-seed comparison (d100 Δacc):**
- s42: +3.21pp (baseline 53.79%)
- s0: +1.38pp (baseline 55.34%)

s0 shows a weaker contamination effect than s42 (+1.38 vs +3.21pp), and the dose-response curve is notably flat — d005 already captures ~93% of the maximum gain. s0 also has a higher baseline (55.34 vs 53.79%), which could partially explain the smaller marginal benefit from contamination (ceiling compression).

---

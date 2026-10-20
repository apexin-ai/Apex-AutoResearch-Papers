# analysis cohens kappa pairwise

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cohens_kappa_pairwise_20260522T133438_result.json`
- **Structured JSON:** [`d93f707d4b754ba8d2d0.json`](../../sessions/d9/d93f707d4b754ba8d2d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary:

| Benchmark | Models | Pairs | Mean κ | Min κ | Max κ | Fleiss κ |
|-----------|--------|-------|--------|-------|-------|----------|
| MMLU | 8 | 28 | 0.461 | 0.241 | 0.612 | 0.456 |
| ARC | 8 | 28 | 0.376 | 0.042 | 0.741 | 0.331 |
| GSM8K | 8 | 28 | 0.335 | 0.117 | 0.590 | 0.309 |
| HellaSwag | 6 | 15 | 0.332 | 0.098 | 0.482 | 0.334 |
| MATH | 8 | 28 | 0.326 | 0.014 | 0.607 | 0.325 |

Key findings:
- All κ values are positive (models agree more than chance), as expected
- MMLU has highest inter-model agreement (mean κ=0.46, "moderate"), likely because its MC format constrains variance
- MATH has lowest mean κ=0.33 ("fair") and widest range — Llama×Mistral κ=0.014 (near-random) while InternLM×Qwen κ=0.61
- ARC has the widest spread (0.04–0.74); Yi-1.5-9B is a consistent outlier with very low agreement against most models on ARC
- HellaSwag only has 6 models (OLMo/Yi missing)
- Fleiss κ tracks closely with mean pairwise κ across all benchmarks

Script saved at server `/root/nlp_variance_gtheory/scripts/exp004_cohens_kappa.py`, results at local `artifacts/exp004/data/cohens_kappa_pairwise.json`.

---

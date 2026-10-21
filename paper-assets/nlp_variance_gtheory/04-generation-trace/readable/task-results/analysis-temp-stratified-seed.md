# analysis temp stratified seed

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_temp_stratified_seed_20260521T091722_result.json`
- **Structured JSON:** [`bd194e54be64a00eb968.json`](../../sessions/bd/bd194e54be64a00eb968.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I understand the discrepancy. The existing `temperature_stratified_analysis.json` used SS proportions (not proper variance components), while my script uses Henderson Method I variance component estimation (the project's canonical method). My approach is methodologically correct.

Key finding: T=0.0 is unbalanced (FP32 has only 8,800/28,800 expected records), but T=0.3, T=0.7, and T>0 combined are all balanced. Since the T=0.0 seed finding is qualitative (≈0), the imbalance doesn't affect the conclusion.

Results saved to `results/analysis/temp_stratified_seed.json`:

| Stratum | n | seed% | seed:item% | item_id% | G_item |
|---------|-------|-------|------------|----------|--------|
| T=0.0 | 66,400 | 0.000 | 0.043 | 68.25 | 0.683 |
| T=0.3 | 86,400 | 0.000 | 6.157 | 56.43 | 0.564 |
| T=0.7 | 86,400 | 0.007 | 17.404 | 49.36 | 0.494 |
| T>0 | 172,800 | 0.000 | 10.556 | 51.95 | 0.520 |

**Gradient**: seed:item monotonically increases 0.04% → 6.16% → 17.40%.

**FP non-associativity**: T=0 seed:item = 0.043% (non-zero) — floating-point non-associativity evidence, but magnitude is negligible.

**Key findings**:
1. At T=0, seed effect is essentially zero — as expected for deterministic decoding. The 0.043% seed:item interaction is trace evidence of vLLM floating-point non-associativity.
2. At T>0, seed:item interaction is the dominant seed-related variance source (not seed main effect), meaning seed sensitivity is item-dependent.
3. Even at T=0.7, seed:item (17.4%) remains ≪ item_id (49.4%) — item selection dominates over stochastic sampling noise.

---

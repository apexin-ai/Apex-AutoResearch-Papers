# Table 5: Post-hoc Filtering Baseline Comparison

Post-hoc filtering: generate unconstrained, then reject triples violating ontology constraints.
OntoCoDec: constrained decoding enforces constraints during generation.

## Zero-Shot Regime

| Model | Dataset | Triples | Reject% | R_F1 Before | R_F1 Post-hoc | R_F1 OntoCoDec | TP Lost (post-hoc) |
|-------|---------|---------|---------|-------------|---------------|----------------|-------------------|
| Qwen3-8B | SciERC | 1724 | 16.76 | 8.23 | 8.63 | 8.36 | 7 |
| Llama3.1-8B | SciERC | 1274 | 13.89 | 2.68 | 2.71 | 2.54 | 2 |
| Mistral-7B | SciERC | 1584 | 20.27 | 3.76 | 3.94 | 3.67 | 4 |
| Qwen3-8B | DocRED | 17497 | 48.12 | 7.74 | 9.61 | 8.23 | 127 |
| Llama3.1-8B | DocRED | 16437 | 42.18 | 5.98 | 7.44 | 6.27 | 48 |
| Mistral-7B | DocRED | 11836 | **73.73** | 4.34 | 3.85 | 5.52 | 226 |

## Fine-Tuned Regime

| Model | Dataset | Reject% | R_F1 Before | R_F1 Post-hoc | R_F1 OntoCoDec | TP Lost (post-hoc) |
|-------|---------|---------|-------------|---------------|----------------|-------------------|
| Qwen3-8B | SciERC | 1.95 | 43.86 | 43.94 | 43.77 | 4 |
| Llama3.1-8B | SciERC | 1.11 | 45.45 | 45.23 | 45.47 | 5 |
| Qwen3-8B | DocRED | 1.03 | 40.91 | 41.11 | N/A | 1 |
| Llama3.1-8B | DocRED | 0.64 | 43.77 | 43.92 | 44.23 | 1 |

**Key Findings:**
- ZS: Post-hoc achieves higher R_F1 than OntoCoDec in 5/6 settings (by removing low-precision violating triples that happen to be FPs)
- Exception: Mistral DocRED — 73.7% rejection rate causes net F1 loss (loses 226 TPs, R_F1 drops 3.85 < 4.34 before)
- FT: Rejection rates are very low (0.6–2.0%) since fine-tuned models already produce mostly valid outputs
- OntoCoDec advantage over post-hoc: **structural guarantee** (0% ET/RV violations), composability, and no TP loss risk from over-rejection
- Post-hoc cannot guarantee 0% violations (residual ET after filtering observed in Mistral DocRED: 2.47%)

# Table 4: FT Ablation — Constraint Layer Decomposition

Modes: unconstrained (no constraints), grammar_only (JSON schema grammar), semantic_only (ontology DR/CF checks), full (grammar + semantic = OntoCoDec).

## SciERC

| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |
|-------|------|----------|----------|-----|-----|-----|-----|-------------|
| Qwen3-8B | unconstrained | 67.05 | 43.86 | 0.00 | 0.00 | 1.95 | 0.00 | 0.00 |
| Qwen3-8B | grammar_only | 67.05 | 43.86 | 0.00 | 0.00 | 1.90 | 0.00 | 0.00 |
| Qwen3-8B | semantic_only | 67.05 | 43.69 | 0.00 | 0.00 | 0.60 | 1.33 | 0.00 |
| Qwen3-8B | **full (OntoCoDec)** | 67.05 | 43.77 | 0.00 | 0.00 | 0.00 | 1.18 | 0.00 |
| Llama3.1-8B | unconstrained | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |
| Llama3.1-8B | grammar_only | 67.76 | 45.45 | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 |
| Llama3.1-8B | semantic_only | 67.76 | 45.47 | 0.00 | 0.00 | 0.65 | 0.18 | 0.00 |
| Llama3.1-8B | **full (OntoCoDec)** | 67.76 | 45.47 | 0.00 | 0.00 | 0.09 | 0.46 | 0.00 |

## DocRED

| Model | Mode | E_F1 (%) | R_F1 (%) | ET% | RV% | DR% | CF% | Parse Fail% |
|-------|------|----------|----------|-----|-----|-----|-----|-------------|
| Qwen3-8B | unconstrained | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.12 | 7.11 |
| Qwen3-8B | grammar_only | 82.19 | 40.85 | 0.00 | 0.00 | 0.61 | 0.11 | 7.01 |
| Qwen3-8B | semantic_only | 82.15 | 40.89 | 0.00 | 0.23 | 0.21 | 0.27 | 7.52 |
| Qwen3-8B | **full (OntoCoDec)** | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.41 | 8.52 |
| Llama3.1-8B | unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | — | 2.30 |
| Llama3.1-8B | grammar_only | 84.04 | 43.77 | 0.00 | 0.00 | 0.51 | 0.12 | 2.30 |
| Llama3.1-8B | semantic_only | 84.02 | 43.90 | 0.00 | 0.15 | 0.30 | 0.16 | 2.40 |
| Llama3.1-8B | **full (OntoCoDec)** | 85.23 | 44.23 | 0.00 | 0.00 | 0.20 | 0.26 | 2.51 |

**Observations:**
- Grammar layer: eliminates ET/RV violations (forces valid type/relation tokens); minimal impact on DR
- Semantic layer: primary DR reducer (SciERC: 1.95%→0.60% for Qwen, DocRED: 0.76%→0.21% for Qwen)
- Full combination: near-zero DR residual with sub-additive constraint interaction
- F1 impact: ≤0.30pp R_F1 cost across all completed settings
- Llama DocRED semantic_only: DONE (updated 2026-05-16)

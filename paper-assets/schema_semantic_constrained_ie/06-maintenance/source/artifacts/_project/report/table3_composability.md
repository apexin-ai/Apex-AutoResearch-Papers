# Table 3: Composability — FT + OntoCoDec (Post-Training Constraint Integration)

OntoCoDec applied at inference time to fine-tuned models without retraining.

| Model | Dataset | | E_F1 (%) | R_F1 (%) | DR% | RV% | CF% | Parse Fail% |
|-------|---------|---|----------|----------|-----|-----|-----|-------------|
| Qwen3-8B | SciERC | Unconstrained | 67.05 | 43.86 | 1.95 | 0.00 | 0.00 | 0.00 |
| | | + OntoCoDec | 67.05 | 43.77 | 0.00 | 0.00 | 1.18 | 0.00 |
| | | **Δ** | **0.00** | **−0.09** | **−1.95** | **0.00** | **+1.18** | **0.00** |
| Qwen3-8B | DocRED | Unconstrained | 82.15 | 40.86 | 0.76 | 0.27 | 0.12 | 7.11 |
| | | + OntoCoDec | 81.43 | 40.56 | 0.01 | 0.00 | 0.41 | 8.52 |
| | | **Δ** | **−0.72** | **−0.30** | **−0.75** | **−0.27** | **+0.29** | **+1.41** |
| Llama3.1-8B | SciERC | Unconstrained | 67.76 | 45.45 | 1.11 | 0.00 | 0.00 | 0.00 |
| | | + OntoCoDec | 67.76 | 45.47 | 0.09 | 0.00 | 0.46 | 0.00 |
| | | **Δ** | **0.00** | **+0.02** | **−1.02** | **0.00** | **+0.46** | **0.00** |
| Llama3.1-8B | DocRED | Unconstrained | 83.93 | 43.72 | 0.49 | 0.15 | — | 2.30 |
| | | + OntoCoDec | 85.23 | 44.23 | 0.20 | 0.00 | 0.26 | 2.51 |
| | | **Δ** | **+1.30** | **+0.51** | **−0.29** | **−0.15** | — | **+0.21** |

**Key Findings:**
- OntoCoDec is composable: plug-in at inference without retraining, near-zero F1 cost (max Δ R_F1 = −0.30pp on Qwen DocRED)
- DR reduction: 59–100% relative reduction across all settings
- RV elimination: 0% residual in all constrained settings
- Llama DocRED shows net positive Δ (+0.51 R_F1) — constrained decoding helps the model stay on-schema

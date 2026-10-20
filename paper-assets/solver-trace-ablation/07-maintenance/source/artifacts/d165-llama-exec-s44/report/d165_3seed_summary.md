# D165 LLaMA-3.2-3B GRPO Exec-Only: 3-Seed Summary

## Per-Seed Results (STA eval on proofwriter_fol_100)

| Seed | PR | ISR* | genuine% | CE | TS | PG | CI |
|------|-----|------|----------|-----|-----|-----|-----|
| 42 | 14% | 0.547 | 85.7% | 2 | 0 | 0 | 0 |
| 43 | 15% | 0.566 | 86.7% | 2 | 0 | 0 | 0 |
| 44 | 16% | 0.549 | 87.5% | 2 | 0 | 0 | 0 |
| **Mean±Std** | **15.0±1.0%** | **0.554±0.010** | **86.6±0.9%** | — | — | — | — |

## Interpretation

LLaMA-3.2-3B does NOT bootstrap under GRPO exec-only reward (PR stays at SFT baseline level ~15%).
High genuine% (~87%) reflects the low-PR baseline state — few proved outputs, and those few are mostly genuine.
This contrasts sharply with Qwen3-4B which bootstraps to PR≥93% but with ISR*→0 (structural collapse).

The LLaMA result is **negative** for cross-model validation of the bootstrap+collapse phenomenon,
but **informative** for the paper: it shows the collapse is not universal, strengthening the
characterization as a model-specific interaction with GRPO reward shaping.

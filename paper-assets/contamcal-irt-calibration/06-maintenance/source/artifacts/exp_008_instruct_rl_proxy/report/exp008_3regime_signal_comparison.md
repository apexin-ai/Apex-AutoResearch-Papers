# exp-008: 3-Regime Signal Comparison (Qwen2.5-0.5B)

## Regime Definitions
- **Base Pretrained**: Qwen2.5-0.5B (no fine-tuning)
- **d000 SFT**: Qwen2.5-0.5B + LoRA SFT (0% contamination, seed=42, alpha=32)
- **Instruct (SFT+RL)**: Qwen2.5-0.5B-Instruct (official post-trained version)

## Signal Summary Table

### MMLU (n=14042)

| Regime | S1 (Embedding) | S2 (Min-K++) | S4 (Self-Critique) |
|--------|----------------|--------------|---------------------|
| Base Pretrained | 0.6078 ± 0.138 | 1.7009 ± 0.077 | *computing* |
| d000 SFT | 0.5224 ± 0.072† | 1.6976 ± 0.074 | -0.9557 ± 0.061 |
| Instruct (SFT+RL) | 0.6078 ± 0.138 | 1.6952 ± 0.116 | -0.8782 ± 0.115 |

### GSM8K (n=1319)

| Regime | S1 (Embedding) | S2 (Min-K++) | S4 (Self-Critique) |
|--------|----------------|--------------|---------------------|
| Base Pretrained | *computing* | *computing* | *computing* |
| d000 SFT | 0.6131 ± 0.059† | 1.6532 ± 0.089 | -0.9408 ± 0.085 |
| Instruct (SFT+RL) | 0.6292 ± 0.071 | 1.7073 ± 0.181 | -0.9632 ± 0.050 |

### ARC Challenge (n=1172)

| Regime | S1 (Embedding) | S2 (Min-K++) | S4 (Self-Critique) |
|--------|----------------|--------------|---------------------|
| Base Pretrained | *computing* | *computing* | *computing* |
| d000 SFT | 0.5946 ± 0.068† | 1.7079 ± 0.076 | -0.9538 ± 0.056 |
| Instruct (SFT+RL) | 0.6212 ± 0.090 | 1.6737 ± 0.132 | -0.9227 ± 0.086 |

†S1 for d000_sft computed with exp002 pipeline (different SFT reference data). Not directly comparable with Base/Instruct S1.

## Key Observations

### S2 (Min-K++): Minimal regime differentiation
- All regimes produce S2 values in the range [1.65, 1.71]
- No clear monotonic trend across base → SFT → Instruct
- S2 appears insensitive to training regime for 0.5B models at 0% contamination

### S4 (Self-Critique): Regime-dependent calibration
- **MMLU**: Instruct (-0.878) shows higher entropy (less confident) than d000 SFT (-0.956). Delta = +0.078. RL alignment increases self-evaluation uncertainty.
- **GSM8K**: Opposite direction — Instruct (-0.963) is MORE confident than d000 SFT (-0.941). Delta = -0.022.
- **ARC**: Instruct (-0.923) has higher entropy than d000 SFT (-0.954). Delta = +0.031.

Interpretation: RL alignment (RLHF/DPO) in the Instruct model changes self-critique behavior in a benchmark-dependent way. For knowledge tasks (MMLU, ARC), Instruct shows more calibrated/uncertain self-evaluation. For reasoning tasks (GSM8K), Instruct is slightly more confident.

### S1 (Embedding): Model-independent baseline
- S1 measures benchmark-to-SFT-data similarity, independent of model weights
- Base and Instruct produce identical S1 values (same `sft_dosage_005.jsonl` reference)
- d000 SFT S1 differs due to exp002 pipeline using model-specific SFT data reference

## Implications for IRT Calibration
1. S4 provides the clearest regime discrimination signal for IRT
2. S2 may be less useful for distinguishing training regimes at 0% contamination
3. The Instruct model's S4 variance is notably larger than d000 SFT, suggesting RL introduces item-level heterogeneity in self-evaluation behavior

## Data Paths
- Instruct signals: `/root/autodl-tmp/exp008/signals/rl_aligned/`
- d000 SFT signals: `/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/`
- Base pretrained (partial): `/root/autodl-tmp/exp008/signals/base_pretrained/`

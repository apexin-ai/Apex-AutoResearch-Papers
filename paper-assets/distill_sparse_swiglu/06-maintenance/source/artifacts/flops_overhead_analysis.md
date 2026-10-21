# Computational Overhead Analysis: KL Predictor for LLaMA-3.1-8B

## 1. Main Overhead Table

| Component | Value | Notes |
|-----------|-------|-------|
| LLaMA-3.1-8B total params | 8.03B | |
| FFN params per layer | 176.2M | gate + up + down = 3 × 4096 × 14336 |
| FFN params total (% of model) | 5.64B (70.2%) | 176.2M × 32 layers |
| FFN FLOPs per token | 11.27B (~67% of total) | 2 × 3 × 4096 × 14336 × 32 |
| Model total FLOPs per token | ~16.1B | 2N approximation (2 × 8.03B) |
| KL Predictor params | 75.96M (0.95% of model) | GELU bottleneck, d_b=128, per-layer |
| KL Predictor FLOPs per token | 151M (0.94% of total) | 2 × (4096×128 + 128×14336) × 32 |
| FastForward predictor + compensation | 134.4M total | 67.2M predictor + 67.2M compensation |
| Predictor latency overhead (prefill) | 2.5% (bs=1), 1.4% (bs=8) | RTX PRO 6000, seq=2048 |
| Predictor latency overhead (decode) | 7.7% (bs=1), 6.4% (bs=8) | RTX PRO 6000, 128 tokens |
| Predictor memory overhead | +145 MB (~0.9% of model) | Negligible vs 15 GB model |

## 2. FLOPs Savings by Sparsity Level

| Sparsity | FFN FLOPs Saved | Total FLOPs Saved | Net Prefill Speedup | Net Decode Speedup |
|----------|----------------|-------------------|---------------------|--------------------|
| 30% | 3.38B (30% of FFN) | ~20% of total | ~1.17x | ~1.13x |
| 50% | 5.64B (50% of FFN) | ~33% of total | ~1.44x | ~1.34x |
| 70% | 7.89B (70% of FFN) | ~47% of total | ~1.84x | ~1.65x |

Assumptions: FFN = 67% of total FLOPs; predictor overhead 2.5% prefill / 7.7% decode; ideal sparse kernel (no gather-scatter overhead). Net speedup = 1 / (1 - savings + predictor_overhead).

## 3. Parameter Efficiency: KL vs FastForward

| | KL Predictor (Ours) | FastForward (BCE + Comp) |
|---|---|---|
| Predictor params | 75.96M | 67.2M |
| Compensation params | 0 (not needed) | 67.2M |
| **Total additional params** | **75.96M** | **134.4M** |
| % of base model | 0.95% | 1.67% |
| Param reduction | **43% fewer** than FastForward | baseline |
| Quality at 50% sparsity (PPL) | 11.79 | 25.44 (BCE+comp) |

KL predictor uses 43% fewer parameters than FastForward while achieving 2.2x better perplexity, because KL-divergence training produces mask patterns that preserve output distribution without needing post-hoc compensation.

## 4. Training Cost

| Item | Value |
|------|-------|
| Training steps | 1000 |
| GPU | 1× RTX PRO 6000 |
| GPU-hours (single seed) | ~0.86 hrs |
| GPU-hours (3-seed mean) | 2.59 hrs total (~0.86 hrs/seed) |
| Training data | WikiText-103 (subset) |

## 5. Derivation Notes

**FFN FLOPs per token (per layer):**
SwiGLU FFN performs three matmuls: gate_proj (4096→14336), up_proj (4096→14336), down_proj (14336→4096). Each matmul FLOPs = 2 × d_in × d_out (for a single token vector). Total per layer = 2 × 3 × 4096 × 14336 = 352.3M. Over 32 layers: 11.27B.

**Predictor FLOPs per token (per layer):**
Two-layer bottleneck: Linear(4096→128) + GELU + Linear(128→14336). FLOPs = 2 × (4096 × 128 + 128 × 14336) = 2 × 2,359,296 = 4.72M. Over 32 layers: 151.0M.

**Total model FLOPs per token:**
Standard approximation: 2 × N_params = 2 × 8.03B ≈ 16.1B. This covers all linear projections (attention QKV/O + FFN) but excludes attention score computation (sequence-length dependent) and nonlinearities (negligible).

**Net theoretical speedup formula:**
speedup = 1 / (1 - sparsity × ffn_fraction + predictor_overhead). Example at 30% sparsity, prefill: 1 / (1 - 0.30 × 0.67 + 0.025) = 1 / 0.824 = 1.17x.

## 6. Data Sources

- Predictor params/latency: `artifacts/speedup_benchmark_results.md` (measured on RTX PRO 6000)
- FastForward compensation: `bce_comp_staged_s42` experiment in registry.yaml (PPL 25.44 with compensation)
- Training GPU-hours: registry.yaml (`mvp_kl_norm_v2_s42`: 0.86h, `s123`: 0.99h, `s456`: 0.74h)
- Model architecture: LLaMA-3.1-8B config (hidden_size=4096, intermediate_size=14336, num_hidden_layers=32)

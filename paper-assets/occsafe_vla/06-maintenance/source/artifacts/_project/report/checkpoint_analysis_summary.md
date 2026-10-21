# Checkpoint Analysis Summary (2026-05-25)

## Analyses Performed
1. **Gradient Norm Analysis** (GPU 1) — 5 conditions, 32 samples
2. **LoRA Weight Analysis** (GPU 2) — 7 conditions, pairwise distances
3. **Feature Effective Rank** (GPU 2) — 6 conditions (incl. pretrained), 32 images, SVD

## Key Findings

### 1. Gradient Redistribution Effect (Cutoff 15K)
| Module | Cutoff 15K / Vanilla ratio |
|--------|---------------------------|
| DINOv2 | 0.14x – 0.33x (suppressed) |
| SigLIP | 2.0x – 2.8x (amplified) |
| LLM    | 1.0x – 2.3x |

After early OCC training (0-15K) is cut off, DINOv2 gradients enter a "dead zone".
The model compensates by routing learning signal through SigLIP.

### 2. Feature Rank Collapse
| Condition | Deep layer eff_rank (block 21) | vs Pretrained |
|-----------|-------------------------------|---------------|
| Pretrained | 567.4 | — |
| Vanilla | 546.6 | 0.96x |
| Full OCC BN | 538.3 | 0.95x |
| Detach BN | 558.3 | 0.98x |
| **Full OCC LN** | **90.2** | **0.16x** |
| **Cutoff 15K** | **86.5** | **0.15x** |

Top-10 PCs capture 98-99% of variance in Full OCC LN and Cutoff 15K (vs 57% in Pretrained).

### 3. Feature Norm Anomaly
| Condition | Block 23 norm | Pattern |
|-----------|--------------|---------|
| Pretrained | 216.5 | Normal (monotonic increase 5→217) |
| Vanilla | 228.4 | Normal |
| Full OCC BN | 219.1 | Normal |
| Full OCC LN | 29.3 | **Flattened** (10→30 range) |
| Cutoff 15K | 66.4 | **Inverted** (high early, low deep) |

### 4. LoRA Weight Norms
| Condition | DINOv2 norm | Total norm |
|-----------|-------------|------------|
| Vanilla | 131.3 | 444.5 |
| Full OCC BN | 129.9 | 440.8 |
| Detach BN | 115.1 | 427.5 |
| Full OCC LN | 93.2 | 433.0 |
| **Cutoff 15K** | **87.2** | **420.0** |

Cutoff 15K: smallest LoRA norms + most CKA drift → small weight changes cause catastrophic representation shift.

## Mechanistic Interpretation

**Full OCC BN (best safety):** Continuous OCC → diversifies features (rank > pretrained) → rich spatial representations preserved → high CAR.

**Cutoff 15K (worst safety):** Early OCC reshapes features → cutoff creates gradient dead zone in DINOv2 → model compensates via SigLIP → DINOv2 features collapse (rank 6x reduction) + misalign (CKA=0.52) → spatial understanding degraded → low CAR.

**Full OCC LN (surprising):** LayerNorm equalizes magnitudes → causes rank collapse (similar to Cutoff 15K) BUT features remain aligned with pretrained (CKA=0.96) → concentrated but correct.

## Output Files
- `/root/autodl-tmp/analysis/gradient_complete/results.json` — per-layer gradient norms (5 cond)
- `/root/autodl-tmp/analysis/gradient_complete/comprehensive_analysis.pdf` — multi-panel figure
- `/root/autodl-tmp/analysis/lora_weight_analysis/results.json` — weight norms + pairwise distances
- `/root/autodl-tmp/analysis/feature_rank/results.json` — effective rank + feature norms (6 cond)

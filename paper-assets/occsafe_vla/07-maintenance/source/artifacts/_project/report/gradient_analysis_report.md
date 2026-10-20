# Gradient Analysis: Random OCC s2 vs Detach OCC s2

## Setup
- Server: westd-10894, 200 batches (batch_size=4), step-50000 checkpoints
- Random OCC s2: occ_detach=false, avg_action_loss=0.2356, avg_occ_loss=0.0585
- Detach s2: occ_detach=true, avg_action_loss=0.4337, avg_occ_loss=0.0320

## Key Finding: Gradient Amplification via OCC Gradient Flow

When OCC gradients flow through the vision backbone (Random OCC), action gradients are dramatically amplified compared to detached condition:

### DINOv2 (featurizer, 24 blocks)
| Layer | Random OCC action | Detach action | Amplification |
|-------|-------------------|---------------|---------------|
| stem  | 0.700             | 0.011         | 62.2x         |
| blocks.0 | 0.071          | 0.006         | 11.4x         |
| blocks.8 | 0.237          | 0.004         | 64.9x         |
| blocks.22 | 0.393         | 0.032         | 12.3x         |

### SigLIP (fused_featurizer, 27 blocks)
| Layer | Random OCC action | Detach action | Amplification |
|-------|-------------------|---------------|---------------|
| stem  | 0.137             | 0.002         | 68.5x         |
| blocks.0 | 0.038          | 0.002         | 19.0x         |
| blocks.25 | 0.121         | 0.015         | 8.3x          |

### Cosine Similarity (Random OCC only)
- Mean cosine similarity between action and OCC gradients: ~0-3% across all layers
- Near-orthogonal gradient directions → no systematic alignment
- Conflict rate: 43-52% (close to random)

## Conclusion
OCC gradient flow acts as implicit regularization on the vision backbone, amplifying action-relevant gradients by 8-65x. Despite near-orthogonal gradient directions, the OCC loss creates richer gradient landscapes that improve action loss convergence (0.236 vs 0.434).

## Files (on westd-10894)
- /root/occsafe_vla/analysis/results/gradient_comparison.{pdf,png}
- /root/occsafe_vla/analysis/results/random_occ_s2_gradient_{stats,raw,analysis}.{json,pdf,png}
- /root/occsafe_vla/analysis/results/detach_s2_gradient_{stats,raw,analysis}.{json,pdf,png}
- /root/occsafe_vla/analysis/gradient_analysis.py
- /root/occsafe_vla/analysis/compare_gradients.py

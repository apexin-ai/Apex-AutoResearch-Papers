# KL vs Magnitude Mask Divergence Visualization

## Configuration
- Model: LLaMA-3.1-8B
- Predictor: `checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt`
- Sparsity target: 30%
- Data: WikiText-2 test set, 10 samples, seq_len=2048
- Magnitude mask: static, gate_proj weight L2 norm per neuron, top-k
- KL mask: dynamic per-token, predictor(hidden_states) > 0

## Output Files (on westd-41718)
All under `/root/distill_sparse_swiglu/results/mask_visualization/`:

| File | Description |
|------|-------------|
| `fig1_mask_heatmap.pdf/.png` | Per-layer mask comparison: (a) KL mask, (b) Magnitude mask, (c) Divergence. Neurons sorted by weight magnitude, binned to 512 columns. |
| `fig2_token_dynamics.pdf/.png` | Token-level KL mask variation vs static magnitude mask at layer 16 (top 100 most variable neurons). |
| `fig3_jaccard_divergence.pdf/.png` | Per-layer Jaccard divergence bar chart with mean line. |
| `stats.json` | Full per-layer statistics. |

## Jaccard Divergence Statistics
- **Mean**: 0.4507
- **Min**: 0.3486 (Layer 16)
- **Max**: 0.5948 (Layer 28)

### Per-layer values
| Layer | Jaccard Div | KL Sparsity |
|-------|------------|-------------|
| 0 | 0.4254 | 20.2% |
| 1 | 0.4435 | 26.1% |
| 2 | 0.4698 | 33.0% |
| 3 | 0.4294 | 26.8% |
| 4 | 0.4322 | 27.8% |
| 5 | 0.4257 | 27.9% |
| 6 | 0.4062 | 26.7% |
| 7 | 0.4457 | 32.5% |
| 8 | 0.4596 | 36.3% |
| 9 | 0.4544 | 34.1% |
| 10 | 0.4701 | 35.7% |
| 11 | 0.4676 | 36.1% |
| 12 | 0.4430 | 32.1% |
| 13 | 0.4219 | 29.2% |
| 14 | 0.4026 | 25.2% |
| 15 | 0.3732 | 19.0% |
| 16 | 0.3486 | 14.2% |
| 17 | 0.3592 | 17.2% |
| 18 | 0.3498 | 15.4% |
| 19 | 0.3962 | 22.6% |
| 20 | 0.4159 | 24.9% |
| 21 | 0.4388 | 28.1% |
| 22 | 0.4727 | 33.5% |
| 23 | 0.4938 | 36.5% |
| 24 | 0.5397 | 43.1% |
| 25 | 0.5650 | 46.6% |
| 26 | 0.5828 | 51.2% |
| 27 | 0.5887 | 52.7% |
| 28 | 0.5948 | 54.4% |
| 29 | 0.5394 | 46.0% |
| 30 | 0.3973 | 23.0% |
| 31 | 0.3684 | 17.5% |

## Observed Patterns

1. **Layer-dependent divergence**: Clear U-shaped pattern in later layers. Early/mid layers (0-14) have moderate divergence (~0.40-0.47). Mid layers (15-18) have lowest divergence (~0.35). Late layers (24-28) have highest divergence (~0.54-0.59).

2. **KL sparsity non-uniformity**: The KL predictor learns highly non-uniform per-layer sparsity (14%-54%) despite the 30% global target. Layer 16 keeps 86% of neurons (only 14% sparse), while layer 28 prunes 54%. This contrasts with magnitude's uniform 30%.

3. **Divergence correlates with sparsity deviation**: Layers where KL sparsity deviates most from 30% also show highest mask divergence. This is because:
   - Low-sparsity layers (L16: 14%) keep almost everything, naturally overlapping with magnitude's 70% kept neurons
   - High-sparsity layers (L28: 54%) prune much more aggressively AND select different neurons than magnitude

4. **Token-level dynamics** (Figure 2, Layer 16): The KL mask shows clear token-dependent activation patterns (varying across positions), while the magnitude mask is constant horizontal stripes. This demonstrates the predictor learns context-dependent importance that static weight norms cannot capture.

5. **Boundary layers are conservative**: Both first (L0-1) and last (L30-31) layers have lower sparsity (~17-20%), suggesting the predictor learns to preserve information at model boundaries.

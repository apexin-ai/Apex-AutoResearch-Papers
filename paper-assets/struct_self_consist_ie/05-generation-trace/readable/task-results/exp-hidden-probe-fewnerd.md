# exp hidden probe fewnerd

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_hidden_probe_fewnerd_20260518T105429_result.json`
- **Structured JSON:** [`58a91f3c38e49bce8a65.json`](../../sessions/58/58a91f3c38e49bce8a65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Probe training completed. Results:

## Few-NERD Hidden State Probe Results (2000 instances, gold-filtered, 5-fold CV × 3 seeds)

| Method | Dim | Spearman ρ | Selection F1 | Gap Closure |
|--------|-----|-----------|-------------|-------------|
| LP (mean pool) | 1 | 0.6062 | 0.7635 | 12.3% |
| Hidden Linear (Ridge) | 4096 | 0.2684±0.0165 | 0.6758 | **-57.9%** |
| Hidden MLP | 4096 | 0.6285±0.0074 | 0.7628 | 11.7% |
| Oracle | -- | -- | 0.8731 | 100.0% |

**Key findings:**

1. **MLP probe**: ρ=0.629, slightly higher than LP baseline ρ=0.606 (+0.023), but **Selection F1 and Gap Closure are essentially identical** (MLP 11.7% vs LP 12.3%). The MLP probe does NOT meaningfully outperform LP on Few-NERD.

2. **Linear probe**: Catastrophically bad — ρ=0.268, gap closure **-57.9%** (worse than greedy). The 4096-dim hidden states with a linear model severely overfits or the signal isn't linearly separable.

3. **Contrast with SciERC**: On SciERC, MLP probe achieved ρ=0.461 (2× LP ρ=0.217), +13.9% gap closure vs LP's negative closure. On Few-NERD, LP baseline is already strong (ρ=0.606) and hidden states provide no additional advantage.

4. **Interpretation**: Few-NERD's LP signal is already highly predictive of quality. The hidden state representation doesn't add meaningful information beyond what log-probabilities already capture. This contrasts with SciERC where LP was weak and hidden states provided a genuine advantage.

---

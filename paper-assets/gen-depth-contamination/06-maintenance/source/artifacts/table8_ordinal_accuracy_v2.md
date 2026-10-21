# Table 8 Ordinal Accuracy — v2 Recalculation

## Definitions

- **θ = 0.60**: threshold for "distinguishable" depth pair
- **Ground truth**: derived from test model's self K*. If self K*=k, then pairs 0v1 through (k-1)vk are distinguishable (AUC > θ), rest are not.
- **Ordinal accuracy**: fraction of depth pairs where transferred classifier's distinguishable/not judgment matches ground truth.

## Self K* (both v1 and v2)

| Model | Self K* | Distinguishable pairs |
|-------|---------|----------------------|
| OLMo  | 1       | 0v1 only             |
| Pythia | 2      | 0v1, 1v2             |
| Qwen   | 2      | 0v1, 1v2             |

---

## v2 Results (Final: OLMo K*=1, Pythia nucleus, Qwen base)

### Per-pair Ordinal Accuracy

| Train→Test    | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | Acc  |
|---------------|-----|-----|-----|-----|-----|------|
| OLMo→OLMo    | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| OLMo→Pythia   | ✓   | ✗ (0.54 < θ, GT=dist) | ✓ | ✓ | ✓ | 4/5 = 80% |
| OLMo→Qwen     | ✓   | ✗ (0.53 < θ, GT=dist) | ✓ | ✓ | ✓ | 4/5 = 80% |
| Pythia→OLMo   | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| Pythia→Pythia  | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| Pythia→Qwen   | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| Qwen→OLMo    | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| Qwen→Pythia   | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| Qwen→Qwen    | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |

### Aggregates (v2)

| Scope | Correct | Total | Accuracy |
|-------|---------|-------|----------|
| All 9 pairs | 43 | 45 | **95.6%** |
| Off-diagonal (6 pairs) | 28 | 30 | **93.3%** |

**Off-diagonal range: 80–100%**

Only mismatches: OLMo-trained classifier tested on Pythia/Qwen misses 1v2 (OLMo has shallower K*=1, so its classifier doesn't learn to detect depth-2 signal needed by Pythia/Qwen with K*=2).

---

## v1 Results (Pre-nucleus: OLMo K*=1, Pythia greedy, Qwen base)

### Per-pair Ordinal Accuracy

| Train→Test    | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | Acc  |
|---------------|-----|-----|-----|-----|-----|------|
| OLMo→OLMo    | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| OLMo→Pythia   | ✓   | ✗ (0.55 < θ) | ✓ | ✓ | ✓ | 4/5 = 80% |
| OLMo→Qwen     | ✓   | ✗ (0.53 < θ) | ✓ | ✓ | ✓ | 4/5 = 80% |
| Pythia→OLMo   | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| Pythia→Pythia  | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| Pythia→Qwen   | ✓   | ✗ (0.49 < θ) | ✓ | ✓ | ✓ | 4/5 = 80% |
| Qwen→OLMo    | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| Qwen→Pythia   | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |
| Qwen→Qwen    | ✓   | ✓   | ✓   | ✓   | ✓   | 5/5 = 100% |

### Aggregates (v1)

| Scope | Correct | Total | Accuracy |
|-------|---------|-------|----------|
| All 9 pairs | 42 | 45 | 93.3% |
| Off-diagonal (6 pairs) | 27 | 30 | 90.0% |

**Off-diagonal range: 80–100%**

Additional mismatch in v1: Pythia→Qwen 1v2 (greedy Pythia classifier misses Qwen's depth-2 signal). This is fixed in v2 with nucleus Pythia, which produces a stronger 1v2 AUC (0.63 vs 0.49).

---

## Comparison

| Version | Off-diag range | Off-diag aggregate | All-pair aggregate |
|---------|---------------|-------------------|-------------------|
| Original paper text | 80–92% | — | — |
| v1 (greedy Pythia) | 80–100% | 90.0% | 93.3% |
| **v2 (nucleus Pythia)** | **80–100%** | **93.3%** | **95.6%** |

v2 improved over v1 because nucleus Pythia's cross-transfer to Qwen now correctly identifies depth-2 signal (Pythia→Qwen 1v2 AUC: 0.49→0.63).

---

## Suggested Paper Text Updates

**Old text:** "ordinal accuracy of 80–92%"

**Suggested replacement:** "ordinal accuracy of 80–100% (93.3% aggregate across off-diagonal pairs)"

Or more conservatively: "ordinal accuracy ranging from 80% to 100%, with an aggregate of 93.3%"

The two mismatches (OLMo→Pythia and OLMo→Qwen at 80%) are structurally expected: an OLMo-trained classifier (K*=1) lacks depth-2 discriminative features needed for Pythia/Qwen (K*=2). This asymmetry is interpretable and worth noting in the paper.

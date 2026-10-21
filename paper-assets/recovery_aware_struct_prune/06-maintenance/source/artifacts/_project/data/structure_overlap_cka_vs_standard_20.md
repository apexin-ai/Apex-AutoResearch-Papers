# CKA-only 20% vs Standard 20% Structural Overlap Analysis

## Model & Pruning Parameters
- Base model: DeepSeek-R1-Distill-Qwen-7B (28 layers)
- Original MLP intermediate_size: 18944, group_size: 676, groups/layer: 28, total MLP groups: 784
- Attention: Neither method prunes attention (num_kv_heads = 4/layer preserved)
- Both methods remove exactly 200/784 MLP groups (20% sparsity)

## Per-Layer MLP Pruning Comparison

| Layer | CKA-only removed | Standard removed | CKA-only dim | Standard dim | Category |
|-------|-----------------|-----------------|--------------|--------------|----------|
| 0 | 16 | 16 | 8128 | 8128 | Both heavy-prune |
| 1 | 16 | 16 | 8128 | 8128 | Both heavy-prune |
| 2 | 16 | 16 | 8128 | 8128 | Both heavy-prune |
| 3 | 16 | 16 | 8128 | 8128 | Both heavy-prune |
| 4 | 16 | 16 | 8128 | 8128 | Both heavy-prune |
| 5 | 16 | 16 | 8128 | 8128 | Both heavy-prune |
| 6 | 16 | 0 | 8128 | 18944 | CKA-only unique |
| 7 | 1 | 0 | 18268 | 18944 | CKA-only unique |
| 8 | 16 | 0 | 8128 | 18944 | CKA-only unique |
| 9 | 16 | 0 | 8128 | 18944 | CKA-only unique |
| 10 | 0 | 0 | 18944 | 18944 | Both retain |
| 11 | 0 | 0 | 18944 | 18944 | Both retain |
| 12 | 0 | 0 | 18944 | 18944 | Both retain |
| 13 | 0 | 0 | 18944 | 18944 | Both retain |
| 14 | 0 | 0 | 18944 | 18944 | Both retain |
| 15 | 0 | 0 | 18944 | 18944 | Both retain |
| 16 | 0 | 7 | 18944 | 14212 | Standard unique |
| 17 | 0 | 4 | 18944 | 16240 | Standard unique |
| 18 | 0 | 7 | 18944 | 14212 | Standard unique |
| 19 | 4 | 16 | 16240 | 8128 | Both prune (Standard heavier) |
| 20 | 2 | 2 | 17592 | 17592 | Both prune (equal) |
| 21 | 11 | 8 | 11508 | 13536 | Both prune (CKA heavier) |
| 22 | 0 | 4 | 18944 | 16240 | Standard unique |
| 23 | 8 | 16 | 13536 | 8128 | Both prune (Standard heavier) |
| 24 | 14 | 16 | 9480 | 8128 | Both prune (Standard heavier) |
| 25 | 0 | 16 | 18944 | 8128 | Standard unique |
| 26 | 0 | 8 | 18944 | 13536 | Standard unique |
| 27 | 16 | 0 | 8128 | 18944 | CKA-only unique |

## Regional Summary

| Region | Layers | CKA-only groups removed | Standard groups removed |
|--------|--------|------------------------|------------------------|
| Early (L0-9) | 0-9 | 145 (72.5% of budget) | 96 (48.0% of budget) |
| Middle (L10-15) | 10-15 | 0 (0%) | 0 (0%) |
| Late (L16-27) | 16-27 | 55 (27.5% of budget) | 104 (52.0% of budget) |
| **Total** | 0-27 | **200** | **200** |

## Unique Pruning Decisions

### CKA-only uniquely prunes (Standard retains)
- Layers 6, 7, 8, 9, 27: ~65 groups
- Interpretation: CKA identifies these layers as having redundant representations (high inter-layer similarity), but magnitude-based importance scores them as important

### Standard uniquely prunes (CKA-only retains)
- Layers 16, 17, 18, 22, 25, 26: ~46 groups
- Interpretation: Magnitude importance scores these late layers as unimportant, but CKA identifies them as having unique representational capacity

## Jaccard Overlap Bounds
- Pruned set Jaccard: **7.0% – 49.3%** (lower/upper bound)
- Retained set Jaccard: **54.1% – 79.1%**
- Note: Exact values require group-level masks (not saved during original pruning runs)

## Key Insight
CKA-only concentrates pruning budget on early layers (L0-9) that have redundant representations, preserving late-layer functional specialization critical for reasoning. Standard distributes pruning more uniformly based on magnitude, sacrificing late-layer capacity. This explains CKA-only's growing advantage at higher sparsity (25%: +9.25pp GSM8K) — late layers matter more for downstream task performance.

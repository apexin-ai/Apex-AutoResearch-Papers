# M001 Layer Selection Fix Report

**Date**: 2026-05-16  
**Status**: COMPLETE  
**Runtime**: 1301s (CPU-only)

## Background

The original layer sweep (exp_001a, exp_001b) used `crossing_rate × lead_mean` as the layer selection metric. This metric is flawed: it rewards noisy early layers that exhibit random high crossing rates without genuine classification ability.

## Fix Applied

Two alternative ranking schemes were evaluated:
- **Scheme A**: Pure `balanced_accuracy` (sklearn balanced_accuracy_score)
- **Scheme B**: `balanced_accuracy × crossing_rate` (joint optimization)

Scheme B was selected as primary because it balances classification quality with temporal detection capability.

## Task 1: Layer Re-ranking

### R1-32B (DeepSeek-R1-Distill-Qwen-32B)

| Metric | Old (layer 2) | Corrected (layer 10) |
|--------|--------------|---------------------|
| Balanced Acc | 0.63 (est.) | 0.718 |
| Crossing Rate | 0.60 | 0.60 |
| Score (B) | - | 0.431 (rank 1) |
| Depth Ratio | 3.1% | 15.6% |

Scheme A best: layer 63 (bal_acc=0.755, but crossing_rate=0.25 only).

### QwQ-32B

| Metric | Old (layer 1) | Corrected (layer 2) |
|--------|--------------|---------------------|
| Balanced Acc | 0.71 (est.) | 0.730 |
| Crossing Rate | 0.47 | 0.47 |
| Score (B) | - | 0.346 (rank 1) |
| Depth Ratio | 1.6% | 3.1% |

Minimal correction (1 layer shift). Layer 2 validated by balanced_accuracy.

## Task 2: GRU Retraining (3 seeds)

### R1-32B (layer 10, h=256, dropout=0.3)

| Config | bal_acc | crossing | lead | pre-CP FPR |
|--------|---------|----------|------|------------|
| Single (mean) | 0.675 | 0.30 | 9.1 | 0.135 |
| Multi 9-layer (mean) | 0.655 | 0.23 | 8.8 | 0.114 |

Single-layer GRU outperforms multi-layer for R1-32B.

### QwQ-32B (layer 2, h=256, dropout=0.3)

| Config | bal_acc | crossing | lead | pre-CP FPR |
|--------|---------|----------|------|------------|
| Single (mean) | 0.694 | 0.75 | 19.3 | 0.303 |
| Multi 7-layer (mean) | 0.724 | 0.84 | 15.9 | 0.289 |

Multi-layer GRU outperforms single-layer for QwQ-32B. Very high crossing rates (75-84%) with substantial lead times (16-19 steps).

## Task 3: Temporal LR

### R1-32B (layer 10)

| Window | bal_acc | crossing | lead | pre-CP FPR |
|--------|---------|----------|------|------------|
| 5 | 0.731 | 0.55 | 11.8 | 0.239 |
| **10** | **0.737** | **0.50** | **9.0** | **0.189** |
| 15 | 0.721 | 0.60 | 7.5 | 0.209 |

Best: window=10 (bal_acc=0.737).

### QwQ-32B (layer 2)

| Window | bal_acc | crossing | lead | pre-CP FPR |
|--------|---------|----------|------|------------|
| **5** | **0.761** | **0.42** | **23.5** | **0.180** |
| 10 | 0.747 | 0.42 | 20.8 | 0.171 |
| 15 | 0.741 | 0.47 | 17.6 | 0.161 |

Best: window=5 (bal_acc=0.761, lead=23.5 steps).

## Task 4: Paired Bootstrap (HS vs Text, R1-32B)

| Probe | pre-CP FPR (mean +/- std) |
|-------|--------------------------|
| HS (layer 10, LR w=10) | 0.260 +/- 0.298 |
| Text (MiniLM-L6-v2, w=10) | 0.246 +/- 0.260 |

- **Observed difference**: 0.014 (HS slightly worse)
- **p-value**: 0.999
- **95% CI**: [-0.103, 0.127]
- **Conclusion**: No significant difference. HS probe does NOT outperform text baseline on corrected layer for R1-32B.

## Critical Implications

1. **R1-32B HS advantage evaporates on corrected layer**: The previously reported HS superiority (p=0.848 on old layer 2) was likely an artifact of the flawed layer selection. On the correct layer (10), HS and text probes are statistically indistinguishable.

2. **QwQ-32B remains robust**: Layer correction was minimal (1→2), and QwQ-32B still shows strong temporal detection (lead=23.5, crossing=42-84%).

3. **Paper framing impact**: The claim that hidden-state monitoring provides unique value over text-based approaches needs re-evaluation for R1-32B. QwQ-32B results may still support the claim, but a single-model finding is weaker.

## Output Files

All outputs at: `autodl-rtx6000:/root/autodl-tmp/contrastive_trace_safety/artifacts/m001_layer_fix/`

- `layer_ranking_r1_32b.json` - Full 64-layer ranking both schemes
- `layer_ranking_qwq_32b.json` - Full 64-layer ranking both schemes
- `gru_corrected_r1_32b.json` - GRU results (3 seeds, single + multi)
- `gru_corrected_qwq_32b.json` - GRU results (3 seeds, single + multi)
- `temporal_lr_r1_32b.json` - Temporal LR (windows 5, 10, 15)
- `temporal_lr_qwq_32b.json` - Temporal LR (windows 5, 10, 15)
- `bootstrap_hs_vs_text_r1_32b.json` - Paired bootstrap (1000 resamples)
- `run.log` - Full execution log

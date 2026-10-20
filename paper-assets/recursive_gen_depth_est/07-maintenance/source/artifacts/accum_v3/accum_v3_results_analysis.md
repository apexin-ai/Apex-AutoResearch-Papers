# Accumulation v3 Results Analysis

## 1. Experiment Summary

| Config | mix50 | mix25 |
|--------|-------|-------|
| Model | GPT-2 XL (1.57B) | GPT-2 XL (1.57B) |
| LoRA params | 13.5M (0.86%) | 13.5M (0.86%) |
| Mix ratio | 50% human / 50% synthetic | 25% human / 75% synthetic |
| Training data per depth | 5000 samples | 5000 samples |
| Generated per depth | 5000 samples | 5000 samples |
| Epochs | 3 | 3 |
| Feature extractor | Pythia-1.4B (cross-model) | Pythia-1.4B (cross-model) |
| RF | 200 trees, 5-fold CV | 200 trees, 5-fold CV |
| GPU | CUDA:0 | CUDA:1 |
| Start | 2026-05-19 16:17 CST | 2026-05-19 16:17 CST |
| End | 2026-05-19 20:34 CST | 2026-05-19 20:26 CST |
| Total time | 4.28h (257 min) | 4.14h (248 min) |
| Server | westd-48862 (RTX PRO 6000) | westd-48862 (RTX PRO 6000) |

Pipeline phases (cumulative → per-phase minutes):

| Phase | mix50 | mix25 |
|-------|-------|-------|
| d1 (train+gen) | 104.3 min | 101.6 min |
| d2 (train+gen) | 74.6 min | 71.4 min |
| d3 (train+gen) | 73.8 min | 71.3 min |
| Feature extraction | 3.0 min | 3.0 min |
| RF evaluation | ~1.3 min | ~0.7 min |

Bug fix confirmed: Feature extraction uses Pythia-1.4B (cross-model), not the source GPT-2 XL. This was the bug that invalidated accum_v1/v2.

## 2. Results Comparison

### Main Metrics

| Metric | mix50 | mix25 | Full-replacement | Chance |
|--------|-------|-------|-----------------|--------|
| **4-class accuracy** | 69.1% | **70.1%** | 84.28% | 25.0% |
| **Balanced accuracy** | 69.1% | **70.1%** | 84.28% | 25.0% |
| **d1-d3 balanced acc** | 58.9% | **60.3%** | — | 33.3% |
| Delta vs full-replacement | -15.2 pp | -14.2 pp | — | — |

### Per-Depth Recall

| Depth | mix50 | mix25 | Delta |
|-------|-------|-------|-------|
| d0 (human) | 99.4% | 99.4% | 0.0 |
| d1 | 73.0% | 73.3% | +0.3 |
| d2 | 42.0% | 42.8% | +0.8 |
| d3 | 61.8% | 64.7% | +2.9 |

### Fold Accuracies

| Fold | mix50 | mix25 |
|------|-------|-------|
| 0 | 68.2% | 70.0% |
| 1 | 69.2% | 69.5% |
| 2 | 69.1% | 70.1% |
| 3 | 69.7% | 70.3% |
| 4 | 69.2% | 70.5% |
| Std | 0.5% | 0.4% |

### Confusion Matrices

**mix50:**
```
        pred_d0  pred_d1  pred_d2  pred_d3
true_d0   4968       24        4        4
true_d1     43     3651      904      402
true_d2     27     1168     2102     1703
true_d3     15      512     1383     3090
```

**mix25:**
```
        pred_d0  pred_d1  pred_d2  pred_d3
true_d0   4971       23        6        0
true_d1     35     3667     1006      292
true_d2     21     1247     2142     1590
true_d3     13      391     1360     3236
```

## 3. Per-Depth Analysis

### d0 (Human text)
Near-perfect classification (99.4%) in both conditions. Human text remains trivially separable from all recursive depths even when training data is partially human. This is expected — d0 features are drawn from the original Pythia-1.4B feature space with no LoRA perturbation.

### d1 (First recursive depth)
Stable at ~73% across both mix ratios. d1 misclassifications split toward d2 (18%) and d3 (6-8%). The LoRA fine-tuning at d1 introduces sufficient statistical shift from d0 regardless of human/synthetic proportions.

### d2 (Second recursive depth)
The hardest class at ~42% recall. Heavily confused with both d1 (23-25%) and d3 (32-34%). d2 occupies the "middle ground" in feature space — it has diverged from d1 but hasn't yet reached the d3 attractor. This is the accumulation bottleneck.

### d3 (Third recursive depth)
Shows the largest benefit from lower human mix: 61.8% (mix50) → 64.7% (mix25), a +2.9pp improvement. With more synthetic content in training data, d3 text is pushed further from d2 in feature space, making it more distinguishable.

## 4. Training Loss Trends

| Depth | mix50 loss | mix25 loss | Delta |
|-------|-----------|-----------|-------|
| d1 | 2.131 | 1.918 | -0.213 |
| d2 | 1.892 | 1.586 | -0.306 |
| d3 | 1.789 | 1.434 | -0.355 |

Both conditions show monotonically decreasing loss with depth — each successive depth trains on data that is more synthetic and thus more predictable (lower entropy). mix25 has consistently lower loss because 75% of its training data is synthetic (model-generated), which is inherently easier for the model to fit.

Loss delta widens with depth (0.213 → 0.306 → 0.355), confirming that the compounding effect of more synthetic data in the training mix becomes increasingly pronounced at deeper recursions.

## 5. Key Findings

### Finding 1: Accumulation degrades depth signal by ~14-15pp vs full-replacement
Full-replacement achieves 84.28% 4-class accuracy; accumulation achieves 69-70%. This confirms that full-replacement results are an **upper bound** on feature separability. The ~14-15pp gap quantifies the cost of realistic accumulation dynamics.

### Finding 2: mix25 and mix50 yield comparable accuracy
mix25 (70.1%) and mix50 (69.1%) differ by 1.0pp, which is within cross-seed variance (2.04pp across 3 seeds in the full-replacement setting). The two mix ratios are statistically indistinguishable at this sample size. Both achieve ~69-70% accuracy, suggesting that depth signal is robust to the specific accumulation ratio within this range.

### Finding 3: d2 is the consistent bottleneck
d2 recall (~42%) is well below d1 (~73%) and d3 (~63%). The confusion matrix shows d2 distributing errors nearly evenly between d1 and d3. d2 is in a transitional zone of feature space where accumulation blurs the boundary with adjacent depths.

### Finding 4: Signal is well above chance
Both conditions achieve ~70% accuracy (vs 25% chance), ~60% d1-d3 balanced accuracy (vs 33% chance). Depth signal is degraded but not destroyed by accumulation. The detector can still distinguish recursive depths even with realistic data mixing.

### Finding 5: Invalidated v1/v2 comparison
The invalidated accum_mix50 (feature-space mixing error) reported 35.5% accuracy — far below the correct 69.1%. The invalidated accum_mix25 reported 67.2%, close to the correct 70.1% but for the wrong reasons (feature mixing partially mimicked the statistical effect). The bug fix was essential for scientific validity.

## 6. Implications for Discussion §6 Accumulation Paragraph

### Supports
- **Core claim**: "Full-replacement is an upper bound; accumulation degrades depth signal but does not destroy it." Both mix ratios maintain well-above-chance accuracy.
- **Quantification**: Can now state specific degradation: "Accumulation reduces 4-class accuracy by ~14-15 percentage points relative to full-replacement (69-70% vs 84.28%), while remaining 44-45pp above chance."
- **Mix ratio insensitivity**: Both mix ratios (25% and 50% human) yield comparable accuracy (~69-70%), suggesting depth signal is robust to the specific human/synthetic ratio within this range.

### Modifies
- **Original framing assumed**: more human data → better signal (because closer to full-replacement). The 1pp difference between mix25 and mix50 is within seed noise (cross-seed variance 2.04pp), so no directional conclusion can be drawn from these two data points.
- **Recommended framing**: "Under accumulation, the RF classifier achieves 69-70% 4-class accuracy regardless of whether human text comprises 25% or 50% of the training mix. This stability suggests that depth signal is robust to the specific accumulation ratio within this range, though degraded by ~14-15pp relative to the full-replacement upper bound (84.28%)."

### Additional data needed for complete characterization
- mix0 (0% human / 100% synthetic = full replacement at each depth with LoRA) — would close the curve
- mix75 (75% human / 25% synthetic) — would test whether the trend continues or reverses
- These are low priority; two data points (mix25, mix50) plus full-replacement (effectively mix0) are sufficient for Discussion

## 7. Raw Data Locations

```
# Results
/root/autodl-tmp/recursive_gen_depth_est/results/accumulation_v2/mix50/rf_results.json
/root/autodl-tmp/recursive_gen_depth_est/results/accumulation_v2/mix50/summary.json
/root/autodl-tmp/recursive_gen_depth_est/results/accumulation_v2/mix25/rf_results.json
/root/autodl-tmp/recursive_gen_depth_est/results/accumulation_v2/mix25/summary.json

# Generated text
/root/autodl-tmp/recursive_gen_depth_est/results/accumulation_v2/mix{50,25}/accum_depth_{1,2,3}.jsonl

# Training data mixes
/root/autodl-tmp/recursive_gen_depth_est/results/accumulation_v2/mix{50,25}/mixed_d{1,2,3}_train.jsonl

# Features
/root/autodl-tmp/recursive_gen_depth_est/results/accumulation_v2/mix{50,25}/features.jsonl

# LoRA checkpoints
/root/autodl-tmp/recursive_gen_depth_est/checkpoints/accumulation_v2/mix{50,25}/lora_d{1,2,3}/

# Logs
/root/runs/recursive_gen_depth_est/accum_v3_mix50.log
/root/runs/recursive_gen_depth_est/accum_v3_mix25.log
```

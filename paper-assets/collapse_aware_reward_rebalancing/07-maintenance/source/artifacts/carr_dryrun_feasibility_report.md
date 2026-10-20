# CARR Dry-Run Feasibility Report

## Summary

CARR adaptive weights mechanism is **correct but shows minimal differentiation** in the current setting (99.3% selection overlap with fixed equal weights). Root cause: the three proxy score dimensions are highly correlated (r=0.63-0.77), eliminating the selection pressure that CARR needs to operate.

## Data

- Source: `/root/autodl-tmp/carr/outputs_fullft_lr2e5/` (3 generations, 2000 prompts x 4 candidates each)
- Proxy scores computed from text: Quality (structure+richness), Diversity (trigram Jaccard distance to siblings), Complexity (word/sentence length + bigram uniqueness)
- No GPU used; pure CPU analysis on 500 prompts per generation

## Results

### 1. CARR Weight Evolution (eta=0.5, Fixed Share alpha=0.1)

| Stage | w_quality | w_diversity | w_complexity |
|-------|-----------|-------------|--------------|
| Gen 0 (init) | 0.3333 | 0.3333 | 0.3333 |
| Gen 1 | 0.3209 | 0.3402 | 0.3389 |
| Gen 2 | 0.3197 | 0.3454 | 0.3349 |
| Final | 0.3155 | 0.3536 | 0.3308 |

Weight shift is minimal. Diversity weight increases slightly because diversity shows the highest CV across candidates.

### 2. Selection Overlap (Fixed vs CARR)

| Generation | Overlap |
|-----------|---------|
| Gen 0 | 100.0% (identical weights) |
| Gen 1 | 99.0% (5/500 differ) |
| Gen 2 | 99.0% (5/500 differ) |

### 3. Learning Rate Sensitivity

| eta | G1 overlap | G2 overlap | Final w_diversity |
|-----|-----------|-----------|-------------------|
| 0.1 | 100.0% | 99.6% | 0.337 |
| 0.5 | 99.0% | 99.0% | 0.354 |
| 1.0 | 98.0% | 98.6% | 0.374 |
| 2.0 | 97.2% | 97.2% | 0.416 |
| 5.0 | 94.6% | 93.2% | 0.538 |
| 10.0 | 90.0% | 87.6% | 0.701 |

Even at eta=10 (extremely aggressive), overlap stays above 87%.

### 4. Why: Score Correlation

| | Quality | Diversity | Complexity |
|---|---------|-----------|------------|
| Quality | 1.000 | 0.700 | 0.635 |
| Diversity | 0.700 | 1.000 | 0.575 |
| Complexity | 0.635 | 0.575 | 1.000 |

Candidates that score high on one dimension tend to score high on all. This means changing weights barely changes the argmax.

### 5. Maximum Possible Differentiation (Manual Extreme Weights)

| Weight config | Overlap with equal |
|---|---|
| Quality-only (1,0,0) | 61.0% |
| Diversity-only (0,1,0) | 65.6% |
| No diversity (0.5,0,0.5) | 79.2% |
| Moderate shift (0.6,0.2,0.2) | 87.8% |

Even with one dimension at 100%, overlap stays above 61%. The high correlation between dimensions caps the differentiation ceiling.

### 6. Per-Prompt Candidate Variance (Decreasing Over Generations)

| Gen | Var(Q) | Var(D) | Var(C) | Range(Q) | Range(D) |
|-----|--------|--------|--------|----------|----------|
| 0 | 0.0046 | 0.0055 | 0.0051 | 0.094 | 0.066 |
| 1 | 0.0033 | 0.0047 | 0.0032 | 0.072 | 0.071 |
| 2 | 0.0018 | 0.0028 | 0.0014 | 0.050 | 0.063 |

Candidate variance decreases across generations (model converging), further reducing selection differentiation.

## Conclusions

1. **CARR mechanism is correct** but adds negligible value in this setting due to high inter-dimension correlation of proxy scores.

2. **CARR needs independent reward signals.** The proxy scores (text heuristics) are inherently correlated because they all reward "better text." Real reward models for quality (ArmoRM), diversity (embedding distance), and complexity (difficulty/reasoning depth) would likely be more orthogonal.

3. **CARR is a collapse safety net, not a universal optimizer.** Its value emerges when:
   - Reward dimensions are weakly correlated or anti-correlated
   - One dimension actively degrades (collapse scenario)
   - Per-candidate score variance is high enough for weights to flip selections

4. **Next steps to validate CARR properly:**
   - Use actual ArmoRM scores (already exist per-sample from the pipeline)
   - Compute embedding-based diversity (sentence-transformers model is available)
   - Use a task-specific complexity reward (math difficulty, reasoning depth)
   - Artificially induce collapse (train with quality-only for several gens) then show CARR prevents it

## Files

- Analysis script: `/root/autodl-tmp/carr/carr_dryrun_analysis.py`
- Extended analysis: `/root/autodl-tmp/carr/carr_dryrun_extended.py`
- Raw results: `/root/autodl-tmp/carr/outputs_fullft_lr2e5/carr_dryrun_results.json`

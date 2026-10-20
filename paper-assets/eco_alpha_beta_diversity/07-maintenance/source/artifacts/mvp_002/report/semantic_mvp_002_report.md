# Semantic-Level MVP (mvp_002) — Kill/Go Final Report

## Experiment Setup

- **Dataset**: Doshi & Hauser (2024), 297 stories (no-AI: 98, AI-editor: 100, AI-ideas+editor: 99)
- **Feature extraction**: Sentence embeddings (all-MiniLM-L6-v2, 384d) → global k-means clustering → per-story cluster frequency distribution ("semantic species")
- **k values tested**: 50, 100, 200 (sensitivity analysis)
- **Bootstrap**: nboot=200, seed=42
- **Server**: westd-25068, RTX PRO 6000 96GB (cuda:0)

## (A) Data and Feature Statistics

| Metric | no-AI | AI-editor | AI-ideas+editor |
|--------|-------|-----------|-----------------|
| Stories | 98 | 100 | 99 |
| Mean words | 130 | 145 | 155 |
| Mean sentences | 7.7 | 7.9 | 7.8 |
| Sentence range | [3, 9] | [1, 9] | [1, 9] |
| Total sentences: 2312, Embedding dim: 384 |

**Average semantic species per story** (k=50): 5.2; (k=100): 5.6; (k=200): 5.8

## (B) Semantic Hill Numbers (q=0,1,2) × k=50,100,200

### k=50

| q | Metric | no-AI | AI-editor | AI-ideas+editor | CI overlap? |
|---|--------|-------|-----------|-----------------|-------------|
| 0 | α | 4.99 [4.76, 5.30] | 5.41 [5.12, 5.68] | 5.24 [4.96, 5.59] | Yes |
| 0 | β | 9.82 [8.94, 10.15] | 9.24 [8.64, 9.75] | 9.35 [8.68, 9.88] | Yes |
| 1 | α | 4.26 [3.95, 4.57] | 4.66 [4.29, 5.02] | 4.50 [4.18, 4.85] | Yes |
| 1 | β | 9.09 [7.89, 9.23] | 9.18 [8.01, 9.33] | 9.60 [8.15, 9.86] | Yes |
| 2 | α | 3.55 [3.28, 3.82] | 3.84 [3.49, 4.30] | 3.70 [3.31, 4.14] | Yes |
| 2 | β | 9.42 [7.73, 9.96] | 9.95 [7.87, 10.15] | 10.61 [8.47, 10.90] | Yes |

### k=100

| q | Metric | no-AI | AI-editor | AI-ideas+editor | CI overlap? |
|---|--------|-------|-----------|-----------------|-------------|
| 0 | α | 5.44 [5.16, 5.71] | 5.87 [5.61, 6.11] | 5.63 [5.33, 5.91] | Yes |
| 1 | α | 4.76 [4.47, 5.05] | 5.20 [4.89, 5.48] | 4.88 [4.55, 5.23] | Yes |
| 2 | α | 4.05 [3.76, 4.39] | 4.42 [3.89, 4.81] | 4.04 [3.64, 4.46] | Yes |

### k=200

| q | Metric | no-AI | AI-editor | AI-ideas+editor | CI overlap? |
|---|--------|-------|-----------|-----------------|-------------|
| 0 | α | 5.65 [5.39, 5.92] | 6.14 [5.85, 6.39] | 5.59 [5.32, 5.91] | Yes |
| 1 | α | 4.97 [4.66, 5.31] | 5.50 [5.08, 5.82] | 4.88 [4.53, 5.16] | Yes |
| 2 | α | 4.20 [3.76, 4.65] | 4.67 [4.11, 5.16] | 4.06 [3.56, 4.46] | Yes |

**Note**: Alpha shows a consistent trend (AI-editor > no-AI) across all k and q, but CIs always overlap. The trend is directionally correct but not statistically significant.

## (C) Semantic Baselga Decomposition (k=50)

| Condition | bc_balanced | CI | bc_gradient | CI |
|-----------|-------------|-------|-------------|-------|
| no-AI | 0.8995 | [0.877, 0.901] | 0.0048 | [0.002, 0.008] |
| AI-editor | 0.8998 | [0.877, 0.901] | 0.0040 | [0.001, 0.009] |
| AI-ideas+editor | 0.9054 | [0.886, 0.907] | 0.0034 | [0.002, 0.005] |

**Balanced variation dominates overwhelmingly (~0.90 vs ~0.004).** The two components are clearly distinguishable (PASS 3 criterion met). This is consistent across all k values. However, there is **no differential pattern between conditions** — all three conditions show nearly identical Baselga decomposition.

## (D) Embedding Cosine Similarity

| Metric | Value |
|--------|-------|
| Within-condition mean | 0.4364 ± 0.128 |
| Between-condition mean | 0.4252 ± 0.128 |
| Point-biserial r | 0.0414 |
| p-value | 4.16e-18 |

Within-condition per condition:
- no-AI: 0.405
- AI-editor: 0.448
- AI-ideas+editor: 0.455

**Within > between is significant (p < 1e-17) but the effect is negligible (r=0.04).** The heatmap shows no visible block-diagonal structure — stories are not more similar within conditions in embedding space.

## (E) FAIL Test 2 (Semantic Cosine → Baselga R²)

| Condition | Per-pair R² | MAE |
|-----------|-------------|-----|
| no-AI | 0.0083 | 0.012 |
| AI-editor | ~0.0 | 0.010 |
| AI-ideas+editor | 0.0028 | 0.008 |
| **Overall** | **0.0012** | **0.010** |

**FAIL test 2: NOT triggered** (R² = 0.001 ≪ 0.5). Embedding cosine cannot recover Baselga ratio at all — which is actually consistent with the ecological framework providing independent information.

## (F) Pass/Fail Criteria (best k=50)

| Criterion | Result | Detail |
|-----------|--------|--------|
| PASS 1 (α↑ for AI) | **FAIL** | q=1 CIs overlap; no q passes |
| PASS 2 (β↓ for AI) | **FAIL** | No beta reduction in any q |
| PASS 3 (Baselga distinguishable) | **PASS** | bal ≫ gra in all conditions |
| PASS 4 (cosine r > 0.3) | **FAIL** | r = 0.041 |
| FAIL 1 (pattern absent) | **TRIGGERED** | α↑/β↓ not confirmed |
| FAIL 2 (cosine recovers Baselga) | **NOT triggered** | R² = 0.001 |

## (G) OVERALL: **FAIL**

## (H) Lexical vs Semantic Comparison

| Metric | Lexical (mvp_001) | Semantic (mvp_002, k=50) |
|--------|-------------------|--------------------------|
| Feature unit | Word unigram | Sentence-embedding cluster |
| Species per story | ~100+ unique tokens | ~5.2 clusters |
| q=1 α no-AI | ~120-150 (varies by rarefaction) | 4.26 |
| q=1 α AI-editor | ~140-170 (higher, confounded by length) | 4.66 |
| Alpha trend | Present but confounded | Present but not significant |
| q=2 β signal | Consistent | Not significant |
| Baselga unique value | Yes (PASS) | Yes (PASS) |
| Cosine r | r > 0.3 (PASS, TF-IDF) | r = 0.04 (FAIL, embeddings) |
| FAIL test 2 | Not triggered | Not triggered |
| **Overall** | FAIL (α confounded by length) | FAIL (insufficient signal) |

**Key difference**: Lexical MVP failed because alpha diversity was confounded by text length (longer AI stories → more unique words → higher alpha mechanically). The semantic MVP eliminates this confound (sentences per story are equalized ~7.8 across conditions), but reveals that the remaining signal is too weak to detect with this sample size and granularity.

## (I) k-Value Sensitivity

| k | q=1 α trend | q=1 β trend | Overall |
|---|-------------|-------------|---------|
| 50 | +0.40 (ns) | +0.09 (ns) | FAIL |
| 100 | +0.44 (ns) | -0.51 (ns) | FAIL |
| 200 | +0.53 (ns) | -3.45 (ns) | FAIL |

**Conclusion is completely stable across k.** Increasing k inflates beta (more clusters → higher beta mechanically) without changing the qualitative result. Alpha differences are slightly larger at k=200 but still not significant.

## (J) Root Cause Analysis

The semantic approach fails for a fundamental reason: **stories contain too few sentences (~8) to estimate diversity reliably.** With only 5-6 distinct semantic clusters per story, the "species abundance distribution" has extremely low resolution compared to word-level unigrams (~100+ species). This creates:
1. High variance in Hill number estimates → wide CIs → no significance
2. Beta dominated by sampling noise rather than genuine compositional differences
3. Embedding cosine averages over too few vectors to differentiate conditions

## Kill/Go Decision

**KILL.** The eco_alpha_beta_diversity framework does not produce statistically significant results at either the lexical or semantic level on the Doshi & Hauser (2024) dataset:
- Lexical: confounded by text length
- Semantic: insufficient resolution (too few sentences per story)

The Baselga decomposition provides unique structural information (PASS 3 in both MVPs), but the overall framework cannot pass its own validation criteria.

## Bug Fixes During Execution
- `get_sentence_embedding_dimension()` deprecated → still works but emits FutureWarning (not blocking)
- `torch.cuda.get_device_properties().total_mem` → renamed to `total_memory` in torch 2.11+ (fixed in verification step)
- HuggingFace Hub unreachable on server → used ModelScope CDN download instead

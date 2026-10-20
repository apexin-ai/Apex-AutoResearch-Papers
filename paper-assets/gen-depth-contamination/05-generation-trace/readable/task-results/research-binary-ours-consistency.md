# research binary ours consistency

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_binary-ours-consistency_20260515T044006_result.json`
- **Structured JSON:** [`7cad9033b864a05baff6.json`](../../sessions/7c/7cad9033b864a05baff6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full analysis:

---

## 1. All binary filtering implementations (single file)

All filtering logic is in **one file**: `scripts/exp006_filtering_strategies.py`. The training loop in `scripts/exp006_continued_pretraining.py` imports from it. No duplicate implementations.

## 2. Code vs Paper comparison

### BinaryOurs

| Parameter | Paper (experiments_c3.tex L25-26) | Code (BinaryOurs class) | Match |
|---|---|---|---|
| Classifier type | LightGBM | `lgb.LGBMClassifier` | ✓ |
| Feature set | 15-dimensional | `FEATURE_COLS` (15 items) | ✓ |
| Label construction | human (depth=0) vs synthetic (depth≥1) | `labels = (depths > 0).astype(int)` | ✓ |
| Weight formula | w = 1 - P(synthetic) | `1.0 - self.model.predict_proba(features)[:, 1]` | ✓ |
| Sampling | WeightedRandomSampler (L42) | `WeightedRandomSampler` in `exp006_continued_pretraining.py` | ✓ |

### BinaryDrayson

| Parameter | Paper (L28) | Code (BinaryDrayson class) | Match |
|---|---|---|---|
| Formula | w_j = (1-q(x_j))^b / Z | `(1.0 - q) ** self.b`, normalized by `raw.max()` | ✓ |
| b | 1 | 1 | ✓ |
| k (oversampling) | 1.5 | 1.5 | ✓ |
| rmax (weight cap) | **not mentioned** | 3 | ⚠️ |
| Classifier | **not specified** | Same LightGBM as BinaryOurs | ⚠️ |

### Graduated

| Parameter | Paper (L30-32) | Code (Graduated class) | Match |
|---|---|---|---|
| Method | OBD-LightGBM, P(d\|x) | K-1 binary LightGBM classifiers → cumulative probs | ✓ |
| Expected depth | d̂ = Σ d·P(d\|x) | `(dist * np.arange(n_depths)).sum(axis=1)` | ✓ |
| Weight | w = exp(-α·d̂) | `np.exp(-self.alpha * expected_depth)` | ✓ |
| α values | {0.1, 0.3, 0.5, 0.7, 0.9} | configurable via `--alpha` | ✓ |

### Training setup

| Parameter | Paper (L40-44) | Code (exp006_continued_pretraining.py) | Match |
|---|---|---|---|
| Model | Qwen2.5-1.5B-Instruct | `Qwen/Qwen2.5-1.5B-Instruct` | ✓ |
| LoRA rank/α | 8 / 16 | 8 / 16 | ✓ |
| Target modules | q_proj, v_proj | `["q_proj", "v_proj"]` | ✓ |
| Dropout | 0.05 | 0.05 | ✓ |
| Epochs/LR/batch | 3 / 2e-5 / 4 | 3 / 2e-5 / 4 | ✓ |
| Grad accum / warmup | 8 / 0.1 | 8 / 0.1 | ✓ |
| Precision / max_len | bf16 / 512 | bf16=True / 512 | ✓ |
| Zero-weight removal | "zero-weight samples are removed" (L42) | `weights > 1e-8` | ✓ |

### Cross-section consistency (introduction.tex, discussion.tex)

- **introduction.tex L54**: "binary soft weighting that separates human text from all synthetic text (depth≥1)" — ✓ consistent
- **discussion.tex L182**: "retaining human-authored text while downweighting synthetic text (depth≥1)" — ✓ consistent
- **discussion.tex L195**: "binary filtering at the K*=2 boundary is optimal" — ✓ consistent

## 3. Inconsistencies found

**Minor (2 items, neither affects reproducibility significantly):**

1. **BinaryDrayson `rmax=3` omitted from paper.** The code applies weight capping `np.minimum(raw, rmax * mean_w)` with `rmax=3` (from Drayson et al. Table S1). The paper formula `w_j = (1-q)^b / Z` doesn't mention this cap. Since rmax comes from the cited Drayson et al. paper, a reader following that reference would find it, but our paper should ideally mention it for completeness.

2. **BinaryDrayson classifier not specified in paper.** The paper doesn't state what classifier BinaryDrayson uses to produce q(x_j). The code reuses the identical LightGBM architecture (same hyperparameters) as BinaryOurs. This is actually important for fair comparison — the paper should note that both binary methods share the same underlying classifier so differences are attributable solely to the weighting scheme.

**No major inconsistencies.** The core claims — label construction, weight formula, feature set, training hyperparameters — are all exactly matched between code and paper across all three tex files.

## 4. Recommendations

- **Optional fix for rmax**: Add to L28: `$w_j = (1 - q(x_j))^b / Z$, $b = 1$, oversampling factor $k = 1.5$, and weight cap $r_{\max} = 3$`
- **Optional fix for classifier**: Add to L28: "using the same LightGBM classifier as binary-ours" or note this in the comparison paragraph (L92).

---

# Plan-013: Labeling Quality Analysis

## Purpose
Address oracle circularity reviewer concern by analyzing plan-001b labeling quality: tie rates, genuine vs tie-break label fractions, and strict-only retrain comparison.

## Data
- Source: `results/plan_c/` — 245 episodes across 11 task types
- Labeling pipeline: `death_aware_labeling.py` → `format_implicit_data.py`
- Training data: `data/plan-004-implicit/implicit_sft.jsonl` (2040 step-level records from 95 episodes)

---

## (a) Tie Rate Analysis

**Overall tie rate: 61.2% (150/245 episodes)**

| Component | Count | Percentage |
|-----------|-------|-----------|
| Both alive, tied score | 115 | 46.9% |
| Both died (score ≤ -100) | 35 | 14.3% |
| **Total ties** | **150** | **61.2%** |

### Per-Task Tie Rates

| Task | Episodes | Ties | Tie% | Det-Pref | Int-Pref | No-Pref |
|------|----------|------|------|----------|----------|---------|
| chemistry-mix | 20 | 12 | 60.0% | 6 | 2 | 12 |
| find-animal | 20 | 15 | 75.0% | 5 | 0 | 15 |
| find-non-living-thing | 40 | 20 | 50.0% | 16 | 4 | 20 |
| freeze | 20 | 14 | 70.0% | 6 | 0 | 14 |
| grow-fruit | 20 | 13 | 65.0% | 6 | 1 | 13 |
| identify-life-stages-1 | 20 | 11 | 55.0% | 9 | 0 | 11 |
| identify-life-stages-2 | 20 | 14 | 70.0% | 6 | 0 | 14 |
| inclined-plane-determine-angle | 20 | 13 | 65.0% | 7 | 0 | 13 |
| lifespan-longest-lived | 25 | 13 | 52.0% | 11 | 1 | 13 |
| lifespan-longest-lived-then-shortest-lived | 20 | 11 | 55.0% | 8 | 1 | 11 |
| measure-melting-point-unknown-substance | 20 | 14 | 70.0% | 6 | 0 | 14 |

---

## (b) Genuine vs Tie-Break Label Fraction

### Key Finding: Zero tie-break labels exist

The labeling pipeline (`death_aware_labeling.py`) uses strict inequality and death-awareness:

1. **Death asymmetry**: If one agent died (score ≤ -100) and the other survived → prefer survivor
2. **Score comparison**: If both alive, strict `>` comparison
3. **Tie**: Equal scores → `no-preference` (excluded from training)

**All 95 labeled episodes have genuine score/death differences. There are no arbitrary tie-break labels.**

### Label Source Breakdown

| Label | Count | Death Asymmetry | Score Comparison |
|-------|-------|----------------|-----------------|
| det-preferred | 86 | 70 (81.4%) | 16 (18.6%) |
| internal-preferred | 9 | 5 (55.6%) | 4 (44.4%) |
| no-preference | 150 | 35 both_died | 115 tied_alive |

### Score Delta Analysis (det_score − int_score)

**Det-preferred via score comparison (16 episodes):**
- Min delta: 8, Max delta: 67, Mean: 33.75, Median: 50
- Distribution: (5,10]: 6, (10,25]: 2, (25,50]: 2, (50,100]: 6
- No near-ties — all deltas ≥ 8 points

**Det-preferred via death asymmetry (70 episodes):**
- Dominant pattern: int_score=−100, det_score=0 (50 cases)
- Other: det_score ∈ {2, 7, 8, 10, 17, 21, 25, 33, 50} with int_score=−100

**Internal-preferred via score comparison (4 episodes):**
- Delta range: −58 to −8 (internal won by 8–58 points)

**Internal-preferred via death asymmetry (5 episodes):**
- 4 cases: int_score=0, det_score=−100
- 1 case: int_score=50, det_score=−100

---

## (c) Strict-Only Retrain

### Setup
Since the current training data (`implicit_sft.jsonl`) already excludes all ties and contains only genuine labels, the "strict-only" retrain uses **identical data** to ablation-b. This retrain serves as a 4th seed reproducibility check.

- Data: `data/plan-004-implicit/implicit_sft.jsonl` (2040 records, 95 episodes)
- Config: Qwen3-1.7B, LoRA r=16, 3 epochs, batch=4, grad_accum=8, upsample_minority
- Training seed: 42 (ablation-b used seeds 123, 456, 789)
- GPU: cuda:0 (RTX 5090 32GB)
- Training time: 10:32 (165 steps)
- Checkpoint: `checkpoints/plan-013-strict-only/final_adapter`

### Generation-Level Eval Results

| Model | Seed | Bal_Acc | Int_Recall | Det_Recall | Accuracy |
|-------|------|---------|-----------|-----------|----------|
| ablation-b-seed123 | 123 | 0.5736 | 0.5758 | 0.5714 | 0.5719 |
| ablation-b-seed456 | 456 | 0.5748 | 0.7576 | 0.3919 | 0.4314 |
| ablation-b-seed789 | 789 | 0.5831 | 0.8182 | 0.3480 | 0.3987 |
| **plan-013 (seed=42)** | **42** | **0.5729** | **0.7576** | **0.3883** | **0.4281** |
| **Mean ± Std** | — | **0.5761 ± 0.0047** | **0.7273 ± 0.1012** | **0.4249 ± 0.0965** | — |

Plan-013 balanced_acc (0.5729) falls within ±1σ of the ablation-b multi-seed mean (0.5761 ± 0.005).

### Seed Variance Observation
- Balanced accuracy is **stable** across seeds (σ = 0.005, CV = 0.8%)
- Internal/det recall trade-off shows **high variance** (σ ≈ 0.10 for both)
- Seeds 456, 789, and 42 show similar pattern: high int_recall (~0.76–0.82), low det_recall (~0.35–0.39)
- Seed 123 is the outlier: more balanced recalls (0.58/0.57)

---

## Conclusions

### Reviewer Concern: Oracle Circularity via Tie-Breaking
**The concern is unfounded.** The labeling pipeline does not use tie-breaking:
- Ties (61.2% of episodes) are excluded as `no-preference`
- All 95 training labels come from genuine differences (death asymmetry or score comparison)
- The minimum score delta in score-comparison labels is 8 points — no near-ties exist

### Signal Composition
- 78.9% of labels (75/95) come from **death asymmetry** — a strong, unambiguous signal
- 21.1% (20/95) come from **score comparison** — genuine but smaller deltas
- Death asymmetry is the dominant training signal, not score tie-breaking

### Strict-Only Retrain
- Identical data → identical distribution of results (within seed variance)
- Balanced accuracy stable at 57.3–58.3% across 4 seeds
- The high recall variance across seeds suggests the model is on a near-flat balanced_acc plateau where small weight perturbations shift the internal/det threshold substantially

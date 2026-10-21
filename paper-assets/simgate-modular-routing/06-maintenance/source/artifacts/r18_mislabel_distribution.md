# R18: Step-Level Mislabeling Distribution Analysis

## Context
Training data: `data/plan-004-implicit/implicit_sft.jsonl` — 2040 step-level records from 68 episodes (61 det-preferred + 7 internal-preferred), 11 task types, 30 steps/episode.

The "27.7% mislabeling" figure from review rounds refers to the episode-to-step label granularity gap: episode-level labels (det-preferred / internal-preferred) are applied uniformly to ALL 30 steps in an episode, but step-level evidence only supports the label at specific steps.

---

## 1. Training Data Composition by Task Type

| Task Type | Det Steps | Int Steps | Total | Det% | Signal Source |
|-----------|----------|----------|-------|------|---------------|
| chemistry-mix | 180 | 60 | 240 | 75.0% | death_asymmetry |
| find-animal | 60 | 0 | 60 | 100% | death_asymmetry |
| find-non-living-thing | 420 | 90 | 510 | 82.4% | score_comparison |
| freeze | 180 | 0 | 180 | 100% | death_asymmetry |
| grow-fruit | 90 | 30 | 120 | 75.0% | death_asymmetry |
| identify-life-stages-1 | 180 | 0 | 180 | 100% | death_asymmetry |
| identify-life-stages-2 | 120 | 0 | 120 | 100% | death_asymmetry |
| inclined-plane-determine-angle | 120 | 0 | 120 | 100% | death_asymmetry |
| lifespan-longest-lived | 150 | 0 | 150 | 100% | death_asymmetry |
| lifespan-longest-lived-then-shortest-lived | 150 | 30 | 180 | 83.3% | death_asymmetry |
| measure-melting-point-unknown-substance | 180 | 0 | 180 | 100% | death_asymmetry |
| **TOTAL** | **1830** | **210** | **2040** | **89.7%** | |

**Signal source**: 1530/2040 steps (75.0%) from death_asymmetry, 510/2040 (25.0%) from score_comparison.
Only `find-non-living-thing` uses score_comparison; all other 10 task types use death_asymmetry.

---

## 2. Episode-Level Breakdown

| Category | Episodes | Steps |
|----------|----------|-------|
| det-preferred, death_asymmetry | 47 | 1410 |
| det-preferred, score_comparison | 14 | 420 |
| internal-preferred, death_asymmetry | 4 | 120 |
| internal-preferred, score_comparison | 3 | 90 |
| **Total in training** | **68** | **2040** |
| no-preference (excluded) | 177 | — |
| **Total labeled** | **245** | — |

---

## 3. Mislabeling Analysis: Death-Asymmetry Episodes

**Definition**: In death_asymmetry episodes labeled det-preferred, the internal policy died at step F. Steps 0..F-1 are "pre-fatal" — the internal policy was alive and performing ≥ 0 score_delta, yet they are labeled "route to deterministic." These pre-fatal steps constitute the bulk of mislabeling.

### Fatal Step Positions per Task Type

| Task Type | N Episodes | Avg Fatal Step | Avg Pre-Fatal | Pre-Fatal % |
|-----------|-----------|---------------|---------------|-------------|
| chemistry-mix | 6 | 18.2 | 18.2 | 60.6% |
| find-animal | 2 | 16.5 | 16.5 | 55.0% |
| freeze | 6 | 20.8 | 20.8 | 69.4% |
| grow-fruit | 3 | 18.7 | 18.7 | 62.2% |
| identify-life-stages-1 | 6 | 19.5 | 19.5 | 65.0% |
| identify-life-stages-2 | 4 | 17.2 | 17.2 | 57.5% |
| inclined-plane-determine-angle | 4 | 20.0 | 20.0 | 66.7% |
| lifespan-longest-lived | 5 | 22.6 | 22.6 | 75.3% |
| lifespan-longest-lived-then-shortest-lived | 5 | 20.2 | 20.2 | 67.3% |
| measure-melting-point-unknown-substance | 6 | 22.3 | 22.3 | 74.4% |

### Pre-Fatal Mislabeled Steps by Task Type

| Task Type | Det Steps | Pre-Fatal (Mislabeled) | Mislabel Rate |
|-----------|----------|----------------------|---------------|
| chemistry-mix | 180 | 109 | 60.6% |
| find-animal | 60 | 33 | 55.0% |
| freeze | 180 | 125 | 69.4% |
| grow-fruit | 90 | 56 | 62.2% |
| identify-life-stages-1 | 180 | 117 | 65.0% |
| identify-life-stages-2 | 120 | 69 | 57.5% |
| inclined-plane-determine-angle | 120 | 80 | 66.7% |
| lifespan-longest-lived | 150 | 113 | 75.3% |
| lifespan-longest-lived-then-shortest-lived | 150 | 101 | 67.3% |
| measure-melting-point-unknown-substance | 180 | 134 | 74.4% |
| **Death_asymmetry subtotal** | **1410** | **937** | **66.5%** |

---

## 4. Mislabeling Analysis: Score-Comparison Episodes

**Definition**: In score_comparison episodes (find-non-living-thing only), the cumulative score gap between det and internal emerges at a specific step. Steps before the gap opens have no evidence favoring deterministic routing.

| Task Type | Det Steps | Pre-Diverge (Mislabeled) | Mislabel Rate |
|-----------|----------|------------------------|---------------|
| find-non-living-thing (det-pref) | 420 | 242 | 57.6% |
| find-non-living-thing (int-pref) | — | 52 | — |

---

## 5. Step-Level Oracle Analysis

97.4% of steps across all 245 episodes have identical score_delta for both policies (step-level tie). Among all 2040 training steps with trajectory data available:

| Step-Level Oracle | Count | Percentage |
|-------------------|-------|-----------|
| Neutral (both score_delta = 0) | 1278 | 62.6% |
| Det-preferred (det_delta > int_delta) | 60 | 2.9% |
| Internal-preferred (int_delta > det_delta) | 11 | 0.5% |
| No trajectory data for comparison | 691 | 33.9% |

**Strict direction conflict** (oracle says opposite of episode label): **7 steps** (0.3%), all in find-non-living-thing.

---

## 6. Summary: Mislabeling by Task Type (All Definitions)

| Task Type | Total | Pre-Event Mis | Mis% of Task | Mis% of All 2040 |
|-----------|-------|--------------|-------------|-----------------|
| chemistry-mix | 240 | 109 | 45.4% | 5.3% |
| find-animal | 60 | 33 | 55.0% | 1.6% |
| find-non-living-thing | 510 | 294 | 57.6% | 14.4% |
| freeze | 180 | 125 | 69.4% | 6.1% |
| grow-fruit | 120 | 56 | 46.7% | 2.7% |
| identify-life-stages-1 | 180 | 117 | 65.0% | 5.7% |
| identify-life-stages-2 | 120 | 69 | 57.5% | 3.4% |
| inclined-plane-determine-angle | 120 | 80 | 66.7% | 3.9% |
| lifespan-longest-lived | 150 | 113 | 75.3% | 5.5% |
| lifespan-l-then-s-lived | 180 | 101 | 56.1% | 5.0% |
| measure-melting-point | 180 | 134 | 74.4% | 6.6% |
| **TOTAL** | **2040** | **1231** | **60.3%** | **60.3%** |

**Note on the "27.7%" figure**: The review reports reference this number but the exact computation isn't preserved in the codebase. The most likely derivation: 68 training episodes / 245 total episodes = 27.8% ≈ 27.7%, representing the fraction of episodes that receive a routing label (and thus potentially mislabel some steps). The step-level mislabel rate under any reasonable definition is much higher (46–66% depending on strictness).

---

## 7. Key Takeaways for Paper

1. **Death_asymmetry dominates mislabeling**: 937/1231 (76.1%) of mislabeled steps come from death_asymmetry episodes across 10 task types.

2. **Fatal actions occur late**: Average fatal step is ~19.5/30 (65% through the episode), meaning ~65% of steps in death_asymmetry episodes are pre-fatal and carry a potentially incorrect routing label.

3. **Highest mislabel rates**: `lifespan-longest-lived` (75.3%) and `measure-melting-point-unknown-substance` (74.4%) — fatal actions occur latest in these tasks.

4. **Lowest mislabel rate**: `find-animal` (55.0%) — fewer episodes and earlier fatal steps.

5. **Score-comparison task** (`find-non-living-thing`): contributes 294/1231 (23.9%) of mislabeled steps, with a 57.6% mislabel rate because the cumulative score gap only opens at step ~17.

6. **Step-level signal is nearly absent**: 97.4% step-level tie rate means almost no step carries an actionable routing signal. This motivates the episode-level labeling approach despite its mislabeling cost.

7. **Strict direction conflicts are negligible**: Only 7/2040 steps (0.3%) have the oracle saying the OPPOSITE of the episode label. The mislabeling is overwhelmingly "correct direction, wrong granularity" — the episode label is directionally right but applied to steps that are individually uninformative.

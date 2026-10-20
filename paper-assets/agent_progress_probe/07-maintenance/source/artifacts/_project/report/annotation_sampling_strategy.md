# Annotation Sampling Strategy

## 1. Data Overview

| Metric | Value |
|--------|-------|
| Total windows | 59,496 |
| Unique trajectories | 5,000 |
| Unique instances (SWE-bench tasks) | 2,285 |
| Agent | SWE-agent (Llama-70B) |
| Window size | 10 steps (5-step stride, sliding) |

### Label Distribution (Full Dataset)

| Label | Count | Pct |
|-------|-------|-----|
| Progress (majority_label=1) | 39,209 | 65.9% |
| Stagnation (majority_label=0) | 15,600 | 26.2% |
| Strong stagnation (majority_label=-1, all 3 LFs agree) | 4,687 | 7.9% |

### Confidence Distribution

| Confidence | Count | Pct | Meaning |
|------------|-------|-----|---------|
| 0 | 4,687 | 7.9% | All 3 LFs agree stagnation (label=-1 only) |
| 1 | 39,408 | 66.2% | Only 1 non-abstaining LF determines label |
| 2 | 14,609 | 24.6% | 2 non-abstaining LFs agree |
| 3 | 792 | 1.3% | All 3 LFs agree (non-abstain) |

### LF Agreement Summary

| Pattern | Count | Pct |
|---------|-------|-----|
| All 3 non-abstain LFs agree | 4,966 | 8.3% |
| ≥1 LF abstains (votes 0) | 25,441 | 42.8% |
| LFs disagree (has both -1 and 1) | 41,086 | 69.1% |

### Probe Model Performance (Reference)

| Model | Test Macro-F1 | Error Rate |
|-------|---------------|------------|
| GRU Probe | 0.906 | ~9.5% |
| MeanPool + LR | 0.844 | ~11.4% |
| Probe on test set (detailed) | — | 12.2% (957/7832) |

Probe test set error types: FP=495, FN=462.

---

## 2. Sampling Goals

1. **Ground truth for temporal label model evaluation** (Claim 1): Need reliable human labels to measure whether the label model exceeds simple majority vote.
2. **Inter-annotator agreement** (Fleiss κ ≥ 0.6): All 450 windows labeled by 3 annotators → compute κ on full set.
3. **Error analysis**: Identify systematic failure modes of LFs and probe.
4. **Cross-agent generalization** (if OpenHands data available): Small held-out set to test transferability.

---

## 3. Stratified Sampling Design

### Total: 450 windows

We oversample stagnation (minority class) and low-confidence / high-disagreement windows because these are the most informative for evaluating the label model.

### Stratum A: By Label × Confidence (Core Strata)

| Stratum | Label | Confidence | Pool Size | Sample | Rationale |
|---------|-------|------------|-----------|--------|-----------|
| A1 | Stagnation (0/-1) | conf=1 | 9,754 | 80 | Highest uncertainty, minority class |
| A2 | Stagnation (0/-1) | conf=2 | 5,333 | 50 | Moderate agreement, minority class |
| A3 | Stagnation (0/-1) | conf=3 or 0 | 5,200 | 30 | High agreement baseline (includes all-agree stagnation) |
| A4 | Progress (1) | conf=1 | 29,654 | 80 | Highest uncertainty, majority class |
| A5 | Progress (1) | conf=2 | 9,276 | 40 | Moderate agreement |
| A6 | Progress (1) | conf=3 | 279 | 20 | High agreement baseline |
| **Subtotal** | | | | **300** | |

Distribution in core strata: 160 stagnation (53.3%) / 140 progress (46.7%) — deliberate oversample of stagnation.

### Stratum B: LF Disagreement Focus

Drawn from windows where LFs explicitly disagree (one says -1, another says 1). These are the windows where the label model must add value beyond simple majority vote.

| Stratum | Pattern | Sample | Rationale |
|---------|---------|--------|-----------|
| B1 | fdd=1, cr=-1, ob=-1 (progress on diff, stagnation on repetition+outcome) | 20 | Most common disagreement pattern |
| B2 | fdd=-1, cr=1, ob=-1 (stagnation on diff, progress on repetition) | 20 | Second most common |
| B3 | Other mixed patterns with all 3 LFs non-abstaining | 10 | Diverse disagreements |
| **Subtotal** | | **50** | |

### Stratum C: Probe High-Confidence Errors

Windows where the GRU probe predicts with probability > 0.9 but disagrees with majority vote label. These reveal systematic probe failures.

| Stratum | Error Type | Sample | Rationale |
|---------|------------|--------|-----------|
| C1 | False Positive (probe says progress, LFs say stagnation), prob > 0.9 | 20 | Probe overconfident on progress |
| C2 | False Negative (probe says stagnation, LFs say progress), prob > 0.9 | 20 | Probe overconfident on stagnation |
| **Subtotal** | | **40** | |

**Note**: Requires running inference with the saved probe model to identify these windows. If not feasible before annotation start, reallocate to Stratum A/B proportionally.

### Stratum D: Trajectory Outcome Coverage

Ensure representation of all outcome types, especially underrepresented ones.

| Stratum | Outcome | Sample | Rationale |
|---------|---------|--------|-----------|
| D1 | exit_context (agent ran out of steps) | 15 | High error rate (30.2%) in probe |
| D2 | early_exit | 5 | Rare but distinct behavior |
| D3 | submitted_no_patch | 5 | Edge case |
| **Subtotal** | | **25** | |

### Stratum E: Cross-Agent (OpenHands)

| Stratum | Source | Sample | Rationale |
|---------|--------|--------|-----------|
| E1 | OpenHands trajectories | 20 | Generalization test |
| **Subtotal** | | **20** | |

**Note**: Requires windowing + LF labeling of `openhands_samples_100.jsonl` first. If not ready, reallocate to Stratum B.

### Stratum F: Short Trajectories

| Stratum | Type | Sample | Rationale |
|---------|------|--------|-----------|
| F1 | short_trajectory=True | 15 | Edge case coverage (228 in pool) |
| **Subtotal** | | **15** | |

---

## 4. Summary

| Stratum | N | Purpose |
|---------|---|---------|
| A: Label × Confidence | 300 | Core coverage, class-balanced |
| B: LF Disagreement | 50 | Label model evaluation |
| C: Probe Errors | 40 | Error analysis |
| D: Outcome Coverage | 25 | Tail distribution |
| E: Cross-Agent | 20 | Generalization |
| F: Short Trajectories | 15 | Edge cases |
| **Total** | **450** | |

Label balance in final sample: ~200 stagnation (~44%), ~250 progress (~56%).

---

## 5. Sampling Procedure

### Step 1: Prepare Candidate Pools
```python
# For each stratum, filter windows_labeled.jsonl to eligible candidates
# Remove any window already used in model training (use split_info.json test indices only)
# For Stratum C: run probe inference to get per-window probabilities
# For Stratum E: run windowing pipeline on openhands_samples_100.jsonl
```

### Step 2: Random Sampling Within Strata
- Use fixed random seed (42) for reproducibility
- **Trajectory-level deduplication**: Sample at most 3 windows per trajectory to avoid annotator seeing repetitive content from the same agent run
- Within each stratum, sample uniformly at random from eligible candidates

### Step 3: Collision Resolution
- If a window is eligible for multiple strata, assign it to the most specific stratum (C > B > D > F > A)
- If a stratum pool is too small, borrow from the closest alternative stratum

### Step 4: Format for Annotation
- Use existing `annotation_sample_450.csv` format: id, trajectory_id, window_idx, confidence, agent_actions, annotator_label, majority_label, trajectory_outcome
- Shuffle final order (don't group by stratum) to avoid annotator bias
- Strip majority_label from annotator-facing version (blind annotation)

---

## 6. Existing Sample Assessment

The current `annotation_sample_450.csv` (449 windows) has:
- conf=1: 250, conf=2: 150, conf=3: 50
- label=1: 301 (67%), label=0: 149 (33%)
- Outcomes: submitted=143, submitted(exit_context)=210, exit_context=77, early_exit=16, submitted_no_patch=4

**Gaps vs. this strategy**:
1. Missing Stratum C (probe high-confidence errors) — most critical gap
2. Missing Stratum E (OpenHands cross-agent)
3. Missing Stratum F (short trajectories)
4. No explicit LF disagreement focus (Stratum B)
5. Stagnation slightly undersampled (33% vs target 44%)

**Recommendation**: Regenerate the sample using this strategy rather than patching the existing one. The stratification is fundamentally different.

---

## 7. Statistical Power

With 450 windows × 3 annotators:
- **Fleiss κ**: 450 items is well above the 30-50 minimum for stable κ estimates. With 3 raters and binary labels, we can detect κ ≥ 0.6 with narrow confidence intervals.
- **Per-stratum analysis**: Even the smallest stratum (F, n=15) allows descriptive statistics. For hypothesis testing, strata A and B have sufficient power.
- **Label model evaluation**: 450 gold labels allow computing accuracy/F1 with ±2-3% margin at 95% confidence.

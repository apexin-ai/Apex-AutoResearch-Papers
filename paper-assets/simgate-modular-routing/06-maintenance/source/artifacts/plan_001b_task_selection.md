# Plan-001b Task Selection Report

**Date**: 2026-05-13
**Status**: Prescreening still running (12/~30 tasks completed on GPU0, 2 on GPU1)

---

## 1. Complete Signal Table

### Prescreening Tasks (5 episodes each)

| Task | Int | Det | Δ(D-I) | I_death% | D_death% | Int_nd | Det_nd | Δ_nd | Signal |
|------|-----|-----|--------|----------|----------|--------|--------|------|--------|
| chemistry-mix | -55.8 | 4.2 | 60.0 | 60% | 0% | 10.5 | 4.2 | -6.3 | death-dom |
| chem-mix-tertiary | -37.4 | -17.4 | 20.0 | 40% | 20% | 4.33 | 3.25 | -1.08 | death-dom |
| find-animal | -58.4 | 8.2 | 66.6 | 60% | 0% | 4.0 | 8.2 | +4.2 | mixed |
| find-living-thing | -58.4 | -16.6 | 41.8 | 60% | 20% | 4.0 | 4.25 | +0.25 | mixed |
| **find-non-living-thing** | **31.6** | **24.8** | **-6.8** | **0%** | **0%** | **31.6** | **24.8** | **-6.8** | **int-pref** |
| find-plant | -58.4 | 3.2 | 61.6 | 60% | 0% | 4.0 | 3.2 | -0.8 | death-dom |
| freeze | -60.0 | 2.0 | 62.0 | 60% | 0% | 0.0 | 2.0 | +2.0 | mixed |
| grow-fruit | -58.6 | 1.4 | 60.0 | 60% | 0% | 3.5 | 1.4 | -2.1 | death-dom |
| identify-life-stages-1 | -60.0 | 5.0 | 65.0 | 60% | 0% | 0.0 | 5.0 | +5.0 | mixed |
| identify-life-stages-2 | -36.8 | 3.2 | 40.0 | 40% | 0% | 5.33 | 3.2 | -2.13 | death-dom |
| inclined-plane-angle* | -50.0 | 0.0 | 50.0 | 50% | 0% | 0.0 | 0.0 | 0.0 | mixed |
| measure-melting-point | -58.6 | -32.0 | 26.6 | 60% | 40% | 3.5 | 13.33 | +9.83 | mixed |

*only 2 episodes completed

### MVP Tasks (20 episodes each)

| Task | Int | Det | Δ(D-I) | I_death% | D_death% | Signal |
|------|-----|-----|--------|----------|----------|--------|
| boil | -49.75 | -19.7 | 30.05 | 50% | 20% | death-dom |
| melt | -54.7 | -14.55 | 40.15 | 55% | 15% | death-dom |
| change-state-of-matter | -54.7 | -14.5 | 40.2 | 55% | 15% | death-dom |
| chem-secondary-color | -41.0 | -5.5 | 35.5 | 45% | 10% | death-dom |
| grow-plant | 0.5 | 0.5 | 0.0 | 0% | 0% | no-effect |

### Research (boil v3, 20 episodes)

| Task | Int | Det | Δ(D-I) | I_death% | D_death% | Signal |
|------|-----|-----|--------|----------|----------|--------|
| boil v3 | -44.7 | -9.3 | 35.4 | 45% | 10% | death-dom |

### Signal Distribution (all sources)

- death-dominated: 11
- mixed: 6
- internal-preferred: **1** (find-non-living-thing)
- no-effect: 1 (grow-plant)
- genuine-det: 0

---

## 2. Episode-Level Label Analysis (Critical Finding)

Applied `death_aware_labeling.py` logic to ALL paired episode scores:

### Labeling Rules
- int died, det alive → **deterministic** label
- det died, int alive → **internal** label
- both died → discard
- both alive, int > det → **internal** label
- both alive, det > int → **deterministic** label
- tie → discard

### Paired Episode Results

| Task | Source | Eps | Det labels | Int labels | Discard | Int% (of labeled) |
|------|--------|-----|------------|------------|---------|-------------------|
| chemistry-mix | prescreen | 5 | 3 | 0 | 2 | 0% |
| chem-tertiary | prescreen | 5 | 1 | 0 | 4 | 0% |
| find-animal | prescreen | 5 | 3 | 0 | 2 | 0% |
| find-living-thing | prescreen | 5 | 3 | 0 | 2 | 0% |
| **find-non-living-thing** | prescreen | 5 | 2 | **1** | 2 | **33%** |
| find-plant | prescreen | 5 | 4 | 0 | 1 | 0% |
| freeze | prescreen | 5 | 3 | 0 | 2 | 0% |
| grow-fruit | prescreen | 5 | 3 | 0 | 2 | 0% |
| identify-life-stages-1 | prescreen | 5 | 3 | 0 | 2 | 0% |
| identify-life-stages-2 | prescreen | 5 | 2 | 0 | 3 | 0% |
| measure-melting-point | prescreen | 5 | 2 | 0 | 3 | 0% |
| boil | MVP | 20 | 7 | 0 | 13 | 0% |
| melt | MVP | 20 | 8 | 0 | 12 | 0% |
| change-state | MVP | 20 | 10 | 0 | 10 | 0% |
| chem-secondary | MVP | 20 | 8 | 0 | 12 | 0% |
| grow-plant | MVP | 20 | 0 | 0 | 20 | 0% |
| boil v3 | research | 20 | 7 | 0 | 13 | 0% |
| **TOTAL** | | **175** | **69** | **1** | **105** | **1.4%** |

### Why Internal Labels Are So Rare

Three mechanisms combine to suppress internal labels:

1. **Asymmetric death**: Internal model dies 40-60% of the time; deterministic (with death avoidance) dies 0-20%. Every int-died/det-alive episode → deterministic label. The reverse (det-died/int-alive) almost never happens.

2. **Tied survival scores**: When both modes survive, they overwhelmingly score identically (both 0, or both match). Example: chemistry-mix ep2 both score 21; boil ep11 both score 3; chem-secondary ep1/10/14 both score 20. Ties → discard.

3. **No det-only-death tasks**: We have not found a single task where deterministic mode dies while internal survives.

### The find-non-living-thing Exception

The ONLY internal label came from find-non-living-thing ep4: int=50, det=0. Key properties:
- 0% death rate both modes (no death hazards in "find non-living" tasks)
- 300 variations available
- High score variance: int scored [50, 0, 8, 50, 50], det scored [58, 0, 8, 58, 0]
- But even here: ep0 and ep3 had det winning (58>50), only ep4 had int winning (50>0)
- Actual internal ratio: 1/3 = 33% of labeled episodes

---

## 3. 15% Internal Target: Feasibility Assessment

### Scenario A: Current tasks only (no new discoveries)

Best case with find-non-living-thing (20 eps) + 5 death-dominated tasks (20 eps each):
- find-non-living-thing: ~7 labeled (5 det + 2 int), extrapolating from 33% internal
- 5 other tasks: ~60 labeled (60 det + 0 int)
- Total: 65 det + 2 int = **3% internal** ← fails

### Scenario B: Heavy find-non-living-thing weighting

Run 60 episodes of find-non-living-thing + 3 death-dominated tasks (20 eps each):
- find-non-living-thing: ~21 labeled (14 det + 7 int)
- 3 other tasks: ~36 labeled (36 det + 0 int)
- Total: 50 det + 7 int = **12% internal** ← still fails

### Scenario C: Only find-non-living-thing

Run 100 episodes of find-non-living-thing alone:
- ~33% internal of labeled ← meets 15%
- But training data covers only 1 task → router won't generalize

### Core Problem

**15% internal is unachievable with diverse tasks** because the LLM internal model is fundamentally worse than deterministic lookahead on almost all ScienceWorld tasks. The "signal" in Δ(D-I) comes almost entirely from death avoidance, not from genuine deterministic superiority on non-death episodes.

---

## 4. Recommended Strategy Options

### Option 1: Relax the 15% constraint
Accept ~5-10% internal ratio. Use upsampling/class weighting during SFT to compensate.
- Tasks: find-non-living-thing (40 eps) + 6 death-dominated tasks (20 eps each)
- Raw: ~135 det + ~5 int = 3.6% internal, but upsample internal 3-4x
- Effective training ratio: ~12-15% internal after upsampling

### Option 2: Find more internal-preferred tasks
Wait for remaining prescreening tasks to complete. Candidates that MIGHT produce internal labels:
- Tasks with 0% death rate for both modes
- Tasks where internal LLM reasoning helps (multi-step planning, creative solutions)
- Prescreening still has ~18 tasks to run — some may show internal preference

### Option 3: Modify the labeling strategy
Instead of death-aware episode-level labeling, use **step-level comparative labeling**:
- At each step, compare what internal chose vs what deterministic chose
- If internal's action achieved higher score delta → label that step as internal
- This captures cases where internal makes a few good moves even in episodes it ultimately loses
- Much higher internal label rate, but noisier signal

### Option 4: Combined approach (recommended)
1. Wait for prescreening to finish (~6-8 more hours at current rate)
2. Run find-non-living-thing with 40+ episodes
3. Run 4-5 death-dominated tasks with 20 episodes each (for deterministic labels)
4. Use class-weighted SFT loss (weight internal samples 3-5x)
5. If more internal-preferred tasks found in remaining prescreening, add them

---

## 5. Data Reusability Assessment

### Prescreening → Plan C compatibility: ✅ COMPATIBLE

Prescreening `episodes.jsonl` format matches `episode_level_collection.py` output:
- Both store `always_internal` and `always_deterministic` per episode
- Both include step-level data: `step`, `action`, `modality`, `score_before`, `score_after`, `score_delta`, `observation`
- `death_aware_labeling.py` can directly consume prescreening episodes.jsonl

**Savings**: For each prescreened task, 5 episodes can be reused. Only 15 new episodes needed per task (instead of 20).

### MVP data → Plan C: ✅ COMPATIBLE

MVP episodes.jsonl has the same paired format. 20 episodes already available for boil, melt, change-state, chem-secondary-color, grow-plant.

**Savings**: These 5 tasks need 0 additional episodes for Plan C (already have 20 each). But grow-plant produces 0 labels (all ties), so it's useless.

---

## 6. GPU Time Estimate

Per task timing (from prescreening logs): ~20 min for 5 episodes × 2 modes.
- 20 episodes × 2 modes = ~80 min per task
- Minus reusable 5 eps = 15 new eps → ~60 min per task

### Option 4 estimate (recommended):
| Component | Episodes needed | GPU time |
|-----------|----------------|----------|
| find-non-living-thing (40 eps, minus 5 reuse) | 35 new | ~140 min |
| 5 death-dom tasks (20 eps, minus 5 reuse each) | 75 new | ~300 min |
| **Total** | **110 new eps** | **~7.3 hours (dual GPU: ~3.7 hours)** |

### Wait for prescreening first:
Prescreening ETA: ~6-8 more hours (GPU0 at task 12/~30, GPU1 slower). Recommend waiting for completion before starting Plan C to maximize task coverage and identify any additional internal-preferred tasks.

---

## 7. Summary

| Metric | Value |
|--------|-------|
| Prescreening tasks completed | 12 + 2 in-progress |
| Signal-positive tasks (Δ>0) | 11 |
| Internal-preferred tasks | 1 (find-non-living-thing) |
| Current internal label ratio | **1.4%** (1/70 labeled) |
| 15% target achievable? | **No** with diverse tasks; needs upsampling or strategy change |
| Data reusable? | **Yes** — prescreening + MVP format matches Plan C |
| Recommended next step | Wait for prescreening completion, then use Option 4 (combined approach) |

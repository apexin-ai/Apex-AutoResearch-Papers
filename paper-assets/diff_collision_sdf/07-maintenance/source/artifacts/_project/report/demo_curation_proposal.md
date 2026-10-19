# Demo Curation Experiment Proposal

Generated: 2026-05-29
Status: DESIGN (awaiting Director approval)
Claim: Supports Claim 3 (avoidance source attribution) and extends to positive contribution for ICRA

---

## Motivation

Claim 3 establishes that collision-free demonstrations account for nearly all CAR gains (~26pp), while SDF auxiliary supervision provides no statistically significant additional benefit (p=0.155). Demo curation directly operationalizes this finding: if avoidance is demonstration-driven, then systematically varying the collision-free fraction in training data should produce a monotonic CAR response, providing both (a) causal evidence for the demo-driven hypothesis and (b) a practical method for improving VLA safety without architectural changes.

---

## 1. Demo Collision Labeling

### 1.1 Background: Why Labeling is Needed

SafeLIBERO environments ADD obstacles to standard LIBERO scenes. The original LIBERO demonstrations were collected via teleoperation WITHOUT these obstacles present. When replayed in obstacle-augmented SafeLIBERO environments, some demo trajectories naturally avoid the obstacle volumes (collision-free) while others pass through them (collision-containing). This creates a natural collision-free/collision-containing split in the existing data — no new data collection needed.

### 1.2 Labeling Method A: MuJoCo Replay (Gold Standard)

**Approach**: Replay each demo episode in the SafeLIBERO MuJoCo environment with obstacles, tracking obstacle displacement at each timestep (identical to eval code `check_collision()` in `eval_safelibero.py`).

**Collision criterion**: Episode is labeled **collision-containing** if any obstacle displacement exceeds 1mm (same `COLLISION_THRESHOLD = 0.001` used in all evaluations).

**Implementation**:
```python
# Pseudocode for demo labeling
for task_id in range(4):
    demos = load_libero_demos(suite="safelibero_object", task_id=task_id)
    for ep_idx, demo in enumerate(demos):
        env.reset()
        env.set_init_state(demo.init_state)
        initial_positions = get_obstacle_positions(env.sim, OBSTACLE_NAMES)
        
        collided = False
        for t, action in enumerate(demo.actions):
            env.step(action)
            current_positions = get_obstacle_positions(env.sim, OBSTACLE_NAMES)
            hit, name, disp = check_collision(initial_positions, current_positions)
            if hit:
                collided = True
                collision_timestep = t
                collision_obstacle = name
                break
        
        labels[task_id][ep_idx] = {
            "collision_free": not collided,
            "collision_timestep": collision_timestep if collided else None,
            "collision_obstacle": collision_obstacle if collided else None,
            "max_obstacle_displacement": max_disp,
        }
```

**Advantages**:
- Full-body collision detection (EE + arm links + gripper)
- Identical metric to evaluation, ensuring apples-to-apples comparison
- Captures all collision types (not just EE)

**Cost**: ~200 demos × ~300 steps × MuJoCo step ≈ **5–10 minutes on CPU** (MuJoCo is very fast without rendering). No GPU needed.

### 1.3 Labeling Method B: SDF-Based EE Trajectory Check (Fast Sanity Check)

**Approach**: Extract EE positions from demo `observation/state` (first 3 dimensions = ee_pos), query precomputed SDF grid at each position.

**Collision criterion**: Episode labeled collision-containing if `SDF(ee_pos) < 0` at any timestep (EE inside obstacle volume).

**Implementation**:
```python
sdf_data = np.load("sdf_gt_object_chocolate.npz")
sdf_grid = build_sdf_interpolator(sdf_data)  # scipy RegularGridInterpolator

for ep in demos:
    ee_trajectory = ep["observation/state"][:, :3]  # [T, 3]
    sdf_values = sdf_grid(ee_trajectory)             # [T]
    ee_collides = np.any(sdf_values < 0)
```

**Advantages**: CPU-only, <1 minute for all demos, no MuJoCo needed
**Limitation**: Only detects EE collisions, misses arm-link collisions. This is a known limitation aligned with the paper's finding about EE-only monitoring gaps.

**Recommendation**: Use Method A (MuJoCo replay) as primary labeling. Method B as quick sanity check and for analysis (what fraction of collisions are EE vs arm-link?).

### 1.4 Labeling Granularity

**Episode-level binary** (primary): collision-free = 1, collision-containing = 0. This is the granularity needed for curation (include/exclude entire episodes).

**Timestep-level** (secondary, for analysis): Record first collision timestep and which obstacle was hit. Useful for understanding:
- Early vs. late collisions (approach phase vs. manipulation phase)
- Per-obstacle collision rates (which obstacles are hit most?)
- Per-task collision rates (which tasks have more collision-containing demos?)

### 1.5 Expected Demo Collision Statistics

Estimate (to be confirmed by labeling):
- LIBERO object_pudding has **50 demos per task × 4 tasks = 200 total demos**
- Typical obstacle placement in SafeLIBERO Level II puts obstacles in the workspace between start and goal positions
- Expected collision-free rate: **40–70%** (substantial fraction of demos naturally avoid obstacles since teleoperation aimed at task completion, not obstacle avoidance)
- This rate varies significantly by task — BBQ sauce (lowest CAR in eval) likely has the fewest collision-free demos

---

## 2. Curation Pipeline

### 2.1 Pipeline Overview

```
SafeLIBERO demo dataset (HuggingFace LeRobot)
    │
    ▼
[Step 1] MuJoCo Replay Labeling
    │  Output: per-episode collision labels (JSON)
    ▼
[Step 2] Stratification by collision-free ratio
    │  Output: episode index lists per curation level
    ▼
[Step 3] Training data construction
    │  Filter LeRobot dataset by episode indices
    ▼
[Step 4] Training runs (one per curation level × seed)
```

### 2.2 Curation Levels

Given ~200 demos with estimated 40–70% natural collision-free rate (N_cf), we construct **5 curation levels** by varying the fraction of collision-free demos in the training set:

| Level | Collision-Free Fraction | Construction Method |
|-------|------------------------|---------------------|
| **L0** (uncurated) | Natural rate (~40–70%) | All 200 demos, no filtering |
| **L1** (25% cf) | 25% | Subsample collision-free demos to reduce cf ratio |
| **L2** (50% cf) | 50% | Balance collision-free and collision-containing |
| **L3** (75% cf) | 75% | Oversample collision-free, undersample collision-containing |
| **L4** (100% cf) | 100% | Only collision-free demos |

**Important design decisions**:

1. **Fixed total dataset size vs. fixed cf count**: Two options:
   - **Option A (fixed total)**: All levels have ~200 demos, varying the cf ratio by subsampling/oversampling. Pros: controls for dataset size. Cons: requires oversampling, may introduce repetition bias.
   - **Option B (fixed cf count, variable total)**: Keep all collision-free demos in every level, vary collision-containing count. Pros: simpler. Cons: dataset size confound.
   - **Recommendation: Option A** (fixed total = 200 demos per level). This controls for dataset size, isolating the collision-free ratio as the only variable. For levels above the natural cf rate, collision-free demos are repeated (with different augmentation via LeRobot's standard data augmentation).

2. **Task balance**: Maintain equal demos per task (50/task) at each level. If a task has few collision-free demos, that becomes a natural bottleneck — this is informative (tasks with fewer collision-free demos should show less CAR improvement).

3. **Actual curation levels will be determined after labeling**: If natural cf rate is 60%, then L0=60%, and we can create levels at {25%, 50%, 60%(natural), 75%, 100%}. Adjust grid after labeling.

### 2.3 Implementation: LeRobot Dataset Filtering

The openpi training pipeline uses `LeRobotLiberoDataConfig(repo_id=...)` which loads a HuggingFace dataset. To curate:

**Option 1 (simplest): Create separate HF datasets per level**
```python
# After labeling, create curated datasets
from datasets import load_dataset

ds = load_dataset("safelibero_object")
cf_indices = [i for i, label in enumerate(labels) if label["collision_free"]]
cc_indices = [i for i, label in enumerate(labels) if not label["collision_free"]]

# For each curation level, select indices and push to HF
for level_name, selected_indices in curation_levels.items():
    curated_ds = ds.select(selected_indices)
    curated_ds.push_to_hub(f"safelibero_object_curated_{level_name}")
```

**Option 2 (no dataset duplication): Episode index filtering in dataloader**
```python
# Modify training config to accept episode filter
_config.LeRobotLiberoDataConfig(
    repo_id="safelibero_object",
    episode_indices=selected_indices,  # NEW: filter at load time
    ...
)
```

This requires a small patch to the LeRobot dataloader (add `episode_indices` filter). More elegant but needs code change.

**Recommendation**: Option 1 for reliability. Disk cost is minimal (~200 demos × ~1MB each ≈ 200MB per level × 5 levels = 1GB total).

---

## 3. Experiment Design

### 3.1 Training Matrix

| Condition | CF Ratio | Model | Seeds | Training Steps | λ_sdf |
|-----------|----------|-------|-------|---------------|-------|
| L0-LoRA | Natural | Pi0.5 LoRA | 3 | 30K | 0 |
| L1-LoRA | 25% | Pi0.5 LoRA | 3 | 30K | 0 |
| L2-LoRA | 50% | Pi0.5 LoRA | 3 | 30K | 0 |
| L3-LoRA | 75% | Pi0.5 LoRA | 3 | 30K | 0 |
| L4-LoRA | 100% | Pi0.5 LoRA | 3 | 30K | 0 |
| **L4-SDF** | **100%** | **Pi0.5 LoRA+SDF** | **3** | **30K** | **0.1** |

**Total: 6 conditions × 3 seeds = 18 training runs**

Key design choices:
- **LoRA-only (no SDF)** for L0–L4: isolates the effect of demo curation from SDF supervision
- **L4-SDF**: 100% collision-free + SDF supervision. Tests whether SDF adds value on top of maximally curated data (directly extends Claim 3)
- **3 seeds each**: Sufficient for permutation test significance (matches existing experimental protocol)
- **30K steps**: Same training budget as all existing experiments

### 3.2 Evaluation Protocol

Identical to existing protocol:
- 4 tasks × 50 episodes = 200 episodes per seed
- Evaluation seed = 7
- Metrics: **CAR, TSR, dfCAR, SSR** (SSR = TSR ∩ CAR)

Additional analysis:
- **Per-task CAR fingerprint** at each curation level (does task ordering change?)
- **CAR vs. curation ratio curve** (monotonic? saturating? linear?)
- **TSR vs. curation ratio curve** (does curation hurt task performance?)
- **Pareto frontier**: CAR vs. TSR tradeoff across curation levels

### 3.3 Hypotheses and Expected Results

**H1 (primary)**: CAR increases monotonically with collision-free demo fraction.
- Evidence for: Demo distribution is the causal driver of avoidance
- Evidence against: If CAR is flat across curation levels, avoidance comes from architecture/training, not data

**H2 (secondary)**: L4-SDF ≈ L4-LoRA (no additional SDF benefit even with maximally curated data).
- Strengthens Claim 3: SDF is redundant even under the best-case data condition
- If L4-SDF > L4-LoRA: SDF synergizes with curated data (interesting new finding)

**H3 (tertiary)**: Per-task CAR fingerprint is preserved across curation levels.
- Supports: Task geometry (not curation) determines relative avoidance difficulty
- Against: Curation changes the task-difficulty ordering

**Expected quantitative range** (estimated):
| Level | Expected CAR | Expected TSR |
|-------|-------------|-------------|
| L1 (25% cf) | ~35–45% | ~55–60% |
| L2 (50% cf) | ~45–52% | ~50–55% |
| L0 (natural) | ~55% (matches existing LoRA-only) | ~50% |
| L3 (75% cf) | ~58–63% | ~48–52% |
| L4 (100% cf) | ~60–68% | ~45–50% |

The TSR may decrease at high curation levels because removing collision-containing demos reduces trajectory diversity (distribution narrowing).

### 3.4 Statistical Analysis Plan

- **Primary test**: Spearman rank correlation between curation ratio and CAR (across all 5 levels × 3 seeds = 15 data points). Significant positive correlation confirms H1.
- **Pairwise tests**: Permutation tests between adjacent curation levels (L0 vs L1, L1 vs L2, etc.) to identify where the effect saturates.
- **L4-SDF vs L4-LoRA**: Same permutation test protocol as existing Claim 3 analysis.
- **Effect size**: Report CAR gain per 25pp increase in curation ratio (dose-response).

---

## 4. Cost Estimation

### 4.1 Labeling (One-Time)

| Task | Method | Time | GPU |
|------|--------|------|-----|
| MuJoCo replay labeling | Method A | 10 min | None (CPU) |
| SDF-based EE check | Method B | <1 min | None (CPU) |
| Label analysis + visualization | Manual | 30 min | None |
| Create curated datasets | Script | 15 min | None |
| **Total labeling** | | **~1 hour** | **0 GPU** |

### 4.2 Training

| Item | Count | Per-run | Total |
|------|-------|---------|-------|
| Training runs | 18 (6 conditions × 3 seeds) | ~38h (30K steps on RTX PRO 6000) | **684 GPU-hours** |
| Evaluation runs | 18 | ~4h per run | **72 GPU-hours** |
| **Total compute** | | | **~756 GPU-hours** |

With 2 GPUs: ~756 / 2 = **378 hours ≈ 16 days sequential**
With parallel scheduling (2 runs per GPU if memory allows): **~8 days**

### 4.3 Timeline

| Phase | Duration | Notes |
|-------|----------|-------|
| Phase 0: Labeling script + execution | 1 day | CPU-only, can start immediately |
| Phase 1: Dataset construction | 1 day | Create curated HF datasets |
| Phase 2: Training (18 runs) | 8–16 days | Depends on GPU availability |
| Phase 3: Evaluation (18 runs) | 3–4 days | Can overlap with late training |
| Phase 4: Analysis + figures | 2 days | Statistical tests + Pareto curves |
| **Total** | **~2–3 weeks** | Fits within ICRA 2027 timeline (~3.5 months to DDL) |

### 4.4 GPU Requirements

- **Minimum**: 1× RTX PRO 6000 (96GB) — runs sequentially, ~24 days total
- **Recommended**: 2× RTX PRO 6000 — parallel training, ~12 days
- **Ideal**: 4× GPU — can run 4 seeds simultaneously, ~6 days

---

## 5. Deliverables

1. **collision_labels.json**: Per-episode collision labels for all SafeLIBERO demos
2. **Curated datasets**: 5 HuggingFace datasets at different curation levels
3. **Training checkpoints**: 18 checkpoints (6 conditions × 3 seeds)
4. **Evaluation results**: 18 JSON files with per-episode metrics
5. **Figures**:
   - CAR vs. curation ratio curve (with error bars)
   - TSR vs. curation ratio curve
   - CAR-TSR Pareto frontier
   - Per-task CAR fingerprint across curation levels
6. **Paper section**: Updated Claim 3 text for ICRA version incorporating curation results

---

## 6. Risk Assessment

| Risk | Likelihood | Mitigation |
|------|-----------|-----------|
| Natural collision-free rate is very high (>90%) | Low–Medium | If most demos are already collision-free, curation levels L1–L3 require aggressive oversampling of collision-containing demos. Fallback: use per-task curation (some tasks likely have lower cf rate) |
| Natural collision-free rate is very low (<20%) | Low | Few collision-free demos → L4 has very small dataset. Fallback: use episode-segment curation (remove collision-containing segments, not entire episodes) |
| CAR is flat across curation levels | Low | Would contradict Claim 3's existing evidence. If observed: suggests avoidance comes from training dynamics (optimizer, LoRA structure) rather than data distribution. This is a falsifiable and interesting result. |
| TSR drops severely at high curation levels | Medium | Expected to some degree. If TSR < 30%: the curation approach has a fundamental CAR-TSR tradeoff that limits practical utility. Mitigation: add curation levels at finer granularity near the Pareto knee. |

---

## 7. Narrative Integration (ICRA Paper)

**Current Claim 3**: "Collision-free demonstrations are sufficient for collision avoidance" — supported by LoRA vs LoRA+SDF comparison showing SDF adds no significant benefit.

**With curation results, Claim 3 becomes**: "Collision-free demonstrations are the primary driver of collision avoidance, and systematic demo curation produces monotonic CAR improvements" — now a positive, actionable contribution rather than just a negative result.

**ICRA framing advantage**: Demo curation is a practical method that requires no architectural changes, no SDF computation, no additional sensor data. Any VLA pipeline can adopt it. This transforms a negative finding (SDF doesn't work) into a positive recommendation (curate your demos instead).

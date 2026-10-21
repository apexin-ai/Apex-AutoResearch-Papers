# Paper Numerical References — diff_collision_sdf

Extracted from all tex files in `/docs/paper/`. Organized by file. Covers all specific numerical values, table data, statistical results, and experiment references.

---

## abstract.tex

| Value | Context |
|-------|---------|
| >99% | Fraction of safe episodes in Pi0-family models that are action-collapse artifacts (as revealed by dfCAR) |

No experiment IDs. No table data. Single quantitative claim supporting the dfCAR finding.

---

## introduction.tex

### Figure Caption Data (fig_overview_pb)

| Value | Metric | Condition |
|-------|--------|-----------|
| 91.5% | CAR | Pi0+A1 reported |
| 99.6% | Fraction of safe episodes with displacement < 0.1 mm | Pi0+A1 |
| <0.1 mm | Displacement threshold | 99.6% of safe Pi0+A1 episodes |
| ≈0% | dfCAR | Pi0+A1 after displacement filtering |
| 73–77% | CAR range | All EE-only oracle SDF variants |
| 82–83% | CAR range | Unrefined baselines |
| +26 pp | CAR gain | From collision-free demonstrations |
| +2.3 pp | Additional CAR gain | From SDF supervision |
| p = 0.131 | Statistical test (n.s.) | SDF supervision additional benefit |

### Figure Caption Data (fig1_teaser)

| Value | Metric | Condition |
|-------|--------|-----------|
| 91.5% | CAR | Pi0+A1 before dfCAR filtering |
| ≈0% | dfCAR | Pi0+A1 after filtering |
| 288 mm | Minimum displacement | All safe Pi0.5 episodes |

### Body Text

| Value | Metric | Condition |
|-------|--------|-----------|
| 91.5% | CAR | Pi0+A1, 800 episodes |
| 800 | Total episodes | Pi0+A1 evaluation |
| 732 | Collision-free episodes | Pi0+A1 out of 800 |
| 99.6% | Fraction with displacement < 0.1 mm | Of the 732 collision-free Pi0+A1 episodes |
| 0% | TSR | Pi0+A1 across all 800 episodes |
| 100+ | Number of experiments | Total span of the investigation |
| 6000+ | Evaluation episodes | Total span of the investigation |
| ≈0% | dfCAR | Pi0+A1 after displacement filtering |
| 3/732 | Safe episodes surviving dfCAR threshold | Pi0+A1 |
| 71.5% | TSR | Pi0.5 |
| 28.5% | CAR | Pi0.5 |
| 288 mm | Minimum displacement | All Pi0.5 safe episodes |
| 73.1–76.9% | CAR range | Oracle SDF variants (ground-truth) |
| 82–83% | CAR range | Unrefined baselines |
| ~26 pp | CAR gain | LoRA fine-tuning on Pi0.5 with collision-free demos |
| p > 0.05 | Statistical significance | SDF supervision, λ ∈ {0.01, 0.1} |
| >99% | Pi0 safe episodes that are artifacts | dfCAR diagnosis |

### Trainable Parameter Counts (Table 1 / tab:configurations)

| Configuration | Trainable Params |
|---------------|-----------------|
| Pi0 Full-FT | ~2.5B |
| Pi0 LoRA | ~33.5M |
| Pi0+A1 (SDF aux) | ~658K |
| Pi0+A3 (learned SDF) | ~34.2M |
| Pi0.5 (pre-trained) | 0 |
| Pi0.5 LoRA | ~33.5M |
| Pi0.5+A1 (SDF aux), λ ∈ {0.005, 0.01, 0.1} | ~34.2M |

---

## method.tex

### Benchmark and Models

| Value | Context |
|-------|---------|
| ~2.5B | Pi0 parameter count |
| 50 | Episodes per task per configuration |
| 200 | Total episodes per configuration (4 tasks × 50) |
| 3 | Seeds for Pi0.5 multi-seed runs |
| 600 | Episodes for Pi0.5 multi-seed runs |
| seed = 7 | Fixed evaluation seed for all experiments |
| τ_d = 0.1 mm | Displacement threshold for dfCAR |
| 1 μm | Upper bound of action-collapsed episode cluster |
| 200 mm | Lower bound of active episode cluster |
| 2–200 mm | Range of τ_d values yielding identical dfCAR results |
| λ ∈ {0.005, 0.01, 0.1} | SDF loss weight range tested |
| 0 pp | TSR for Pi0+A1 (TSR = 0%; LoRA loading failure) |

---

## claim1.tex (Section: The Action-Collapsed Safety Problem)

### Table: tab:fake_safety — Action-collapse decomposition on SafeLIBERO

| Method | Episodes | CAR (%) | TSR (%) | Collapsed (%) | dfCAR (%) |
|--------|----------|---------|---------|---------------|-----------|
| Pi0 Full-FT | 200 | 83.0 | 0.5 | 99.4 | ≈0 |
| Pi0 LoRA | 200 | 82.0 | 0.0 | ~99 | ≈0 |
| Pi0+A1 (SDF) | 800 | 91.5 | 0.0 | 99.6 | ≈0 |
| Pi0.5 | 200 | 28.5 | 71.5 | 0.0 | 28.5 |

### Figure Caption (fig_tsr_car_scatter)

| Value | Context |
|-------|---------|
| 82–91 pp | CAR inflation gap (reported vs dfCAR) for Pi0-family models |

### Body Text

| Value | Context |
|-------|---------|
| >99% | Fraction of collision-free episodes that are action-collapse artifacts in every Pi0 configuration |
| 91.5% | Raw CAR for Pi0+A1 (highest among Pi0 configs) |
| 0% (TSR) | Pi0+A1 TSR — parameter-name mismatch prevents LoRA loading |
| 200 mm | Minimum displacement of safe Pi0.5 episodes |
| 28.5% | dfCAR for Pi0.5, equals raw CAR |
| 82–91 pp | Pi0-family CAR inflation gaps |
| 3/732 | Pi0+A1 safe episodes exceeding τ_d = 0.1 mm threshold |

---

## claim2.tex (Section: End-Effector-Only SDF Cannot Ensure Full-Body Safety)

### Table: tab:oracle — Oracle SDF refinement results

| Method | CAR (%) | Collapsed (%) | Refines/ep |
|--------|---------|---------------|-----------|
| LoRA baseline (no refine) | 82.0 | 99.4 | -- |
| Full-FT baseline (no refine) | 83.0 | -- | -- |
| Oracle-adaptive (GT, dyn. α) | 75.0 | 98.3 | 14.2 |
| Oracle-fixed (GT, α=0.005) | 73.1 | 98.3 | 14.8 |
| Oracle-feature (GT, feat. space) | 76.9 | 96.7 | 241.7 |
| A3 learned SDF | 77.1 | -- | 0.0 |

### Body Text

| Value | Context |
|-------|---------|
| 76.9% | Best oracle CAR (Oracle-feature) |
| 5.1 pp | Gap: best oracle below LoRA baseline (82.0% – 76.9%) |
| 82.0% | LoRA baseline CAR |
| +9 pp | Oracle refinement improvement on the one task where EE is primary collision body |
| 0 | Refinement steps per episode for A3 learned SDF |

---

## claim3.tex (Section: Avoidance Source Diagnosis)

### Table: tab:avoidance_source — Avoidance source attribution on SafeLIBERO

| Method | Seeds | TSR (%) | CAR (%) | EE Disp (m) |
|--------|-------|---------|---------|-------------|
| Pi0.5 baseline | 1 | 71.5 | 28.5 | 0.367 |
| LoRA-only (no SDF) | 3 | 51.5 ± 0.0 | 54.67 ± 2.02 | 0.391 |
| LoRA+SDF λ=0.005 | 3 | 54.0 ± 3.0 | 54.5 ± 2.29 | 0.387 |
| LoRA+SDF λ=0.01 | 3 | 53.8 ± 1.5 | 56.33 ± 1.61 | 0.389 |
| LoRA+SDF λ=0.1 | 3 | 50.2 ± 3.9 | 57.00 ± 2.18 | 0.394 |

### Body Text

| Value | Context |
|-------|---------|
| ~26 pp | CAR gain from collision-free demonstrations (28.5% → 54.67%) |
| 20× | Range of loss weight tested (λ from 0.005 to 0.1) |
| 30K | Training checkpoint used for all evaluations |
| 0% | Action-collapsed rate for all fine-tuned models |
| >0.37 m | Minimum EE displacement for all fine-tuned models |
| 57.5% | CAR for Phase 2 ablation (λ=0 after step 5K), 18K checkpoint, single seed s2 |
| 18K | Checkpoint for Phase 2 ablation (13K steps of Phase 2 training) |
| 5K | Steps at which λ set to 0 in Phase 2 ablation |
| 57.00% | CAR for λ=0.1 (3-seed mean) |
| 54.67% | CAR for LoRA-only (3-seed mean) |
| p = 0.131 | Two-tailed permutation test, λ=0.1 vs null |
| p > 0.05 | SDF conditions at λ ∈ {0.01, 0.1}, no significant benefit |
| ~2.3 pp | Observed effect size (SDF vs LoRA-only) |
| 5.0 pp | Minimum detectable effect (MDE) at 80% power, n=3, α=0.05 |
| ~18–20 pp | TSR degradation from fine-tuning (71.5% → 51.5–54.0%) |
| 0.39 | SSR/TSR ratio for Pi0.5 baseline |
| 0.51–0.60 | SSR/TSR ratio range for fine-tuned models |
| 3 seeds per group | Statistical design |
| σ ≈ 2.0 pp | LoRA cross-seed standard deviation |
| 84 permutations = C(9,3) | Null B permutation count |
| p = 0.300 | Null A (LoRA-only seeds only), λ=0.1 |
| 20 permutations = C(6,3) | Null A permutation count |

### λ=0.1 Individual Seeds

| Seed | CAR (%) |
|------|---------|
| s0 | 58.0 |
| s1 | 58.5 |
| s2 | 54.5 |

### Matched Evaluation Seeds (paired comparison)

| Paired eval seed | λ=0.1 vs LoRA advantage |
|-----------------|-------------------------|
| Seed 1 | +1.5 pp |
| Seed 2 | +2.5 pp |
| Seed 3 | +5.5 pp |
| Cross-seed std (λ=0.1) | σ = 0.9 pp |
| Cross-seed std (LoRA) | σ = 2.0 pp |

---

## discussion.tex (Section: Discussion and Conclusion / Limitations)

### Body Text

| Value | Context |
|-------|---------|
| 100+ | Experiments conducted across two VLA model families |
| 6000+ | Total evaluation episodes |
| ~26 pp | CAR gain from collision-free demonstrations |
| 5–10 pp | CAR reduction from oracle SDF refinement (EE-only, below baselines) |
| p = 0.131 | λ=0.1, within null distribution |
| ~4000× | Parameter range over which dfCAR quantifies contamination |
| n=3 | Seeds per condition (statistical limitation) |
| MDE ≈ 5 pp | Minimum detectable effect at 80% power |

---

## experimental_framework.tex

### Benchmark and Evaluation Protocol

| Value | Context |
|-------|---------|
| 50 | Episodes per task |
| 200 | Total episodes per configuration |
| 3 | Seeds for Pi0.5 multi-seed runs |
| 600 | Episodes per multi-seed configuration |
| τ_d = 0.1 mm | dfCAR displacement threshold |
| 1 μm | Upper cluster boundary (action-collapsed episodes) |
| 200 mm | Lower cluster boundary (active episodes) |
| 2–200 mm | Range of τ_d yielding identical filtering |
| [2, 200] mm | Robust τ_d range |

### Model Parameter Counts

| Model | Params |
|-------|--------|
| Pi0 | ~3B |
| Pi0.5 | ~3.5B |
| LoRA baseline | ~33.5M trainable |
| SDF Decoder (A1) | ~395K params |
| EE Extractor (A1) | ~263K params |

### Oracle Evaluation

| Value | Context |
|-------|---------|
| 160 | Oracle evaluation episodes (4 tasks × 40) |
| α = 0.005 | Fixed step size for Oracle-fixed |

---

## related_work.tex

No specific experimental numbers cited. Qualitative comparisons only.

---

## appendix.tex

### Appendix: Displacement Distribution (sec:appendix_displacement)

| Value | Context |
|-------|---------|
| <1 μm | Pi0-family episode displacement cluster |
| >200 mm | Pi0.5 episode displacement cluster |
| [2, 200] mm | τ_d range yielding identical dfCAR |

### Appendix: Displacement Threshold Sensitivity (tab:threshold_sensitivity)

Action-collapse rate (% episodes with d_max < τ_d):

| τ_d | A1-LoRA (Pi0) | Pi0.5 Baseline | Pi0.5+A1 (SDF aux) |
|-----|---------------|----------------|---------------------|
| 0.001 mm (1 μm) | 73.9% | 0.0% | 0.0% |
| 0.1 mm | 99.6% | 0.0% | 0.0% |
| 1.0 mm | 100.0% | 0.0% | 0.0% |
| 10 mm | 100.0% | 0.0% | 0.0% |

| Value | Context |
|-------|---------|
| 73.9% | A1-LoRA collapse rate even at τ_d = 1 μm |
| 1–10 mm | Typical action magnitudes in manipulation tasks |

### Table: tab:dfcar_threshold — dfCAR (%) across displacement thresholds (fine-tuned Pi0.5, n=200 per seed)

| Condition | 2 mm | 5 mm | 10 mm | 20 mm | 50 mm | 100 mm | 200 mm | 300 mm |
|-----------|------|------|-------|-------|-------|--------|--------|--------|
| LoRA s0 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 |
| LoRA s1 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 |
| SDF λ=0.005 s0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.1 |
| SDF λ=0.005 s1 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 |
| SDF λ=0.005 s2 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.3 |
| SDF λ=0.01 s0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 |
| SDF λ=0.01 s1 | 57.5 | 57.5 | 57.5 | 57.5 | 57.5 | 57.5 | 57.5 | 57.1 |
| SDF λ=0.01 s2 | 54.5 | 54.5 | 54.5 | 54.5 | 54.5 | 54.5 | 54.5 | 54.0 |

Note: At τ_d = 300 mm, 0–2 episodes per seed fall below threshold (displacement 200–300 mm), causing ≤0.5 pp deviation.

### Appendix: Per-Task TSR Breakdown (tab:per_task_tsr)

Per-task TSR (%) at 30K steps (Baseline = seed-7 re-eval, LoRA/SDF = 3-seed means):

| Task | Pi0.5 Base | LoRA-only | SDF λ=0.005 | SDF λ=0.01 |
|------|-----------|-----------|-------------|------------|
| Orange Juice | 74.0 | 30.0 | 33.3 | 24.7 |
| Chocolate Pudding | 80.0 | 70.7 | 78.0 | 76.7 |
| Milk | 66.0 | 44.7 | 35.3 | 48.7 |
| BBQ Sauce | 66.0 | 60.7 | 69.3 | 65.3 |
| Mean | 71.5 | 51.5 | 54.0 | 53.8 |

### Appendix: Per-Task CAR Breakdown (tab:per_task_car)

Per-task CAR (%) at 30K steps (OJ=Orange Juice, CP=Chocolate Pudding):

| Condition | OJ | CP | Milk | BBQ | Agg. |
|-----------|----|----|------|-----|------|
| LoRA s0 | 56 | 74 | 70 | 26 | 56.5 |
| LoRA s1 | 54 | 68 | 72 | 16 | 52.5 |
| LoRA s2 | 56 | 76 | 62 | 26 | 55.0 |
| SDF λ=0.005 (3-seed) | 54.0 | 72.7 | 71.3 | 20.0 | 54.5 |
| SDF λ=0.01 (3-seed) | 57.3 | 72.7 | 72.0 | 23.3 | 56.3 |
| SDF λ=0.1 s0 | 60 | 74 | 68 | 30 | 58.0 |
| SDF λ=0.1 s1 | 66 | 72 | 70 | 26 | 58.5 |
| SDF λ=0.1 s2 | 56 | 76 | 70 | 16 | 54.5 |
| SDF λ=0.1 (3-seed) | 60.7 | 74.0 | 69.3 | 24.0 | 57.0 |

Additional displacement data for λ=0.1 seed 1:
- avg_max_obstacle_displacement = 0.0553 m
- Per-task: OJ=0.033 m, CP=0.055 m, Milk=0.041 m, BBQ=0.093 m

### Appendix: Safe Success Rate (tab:ssr)

| Condition | TSR (%) | CAR (%) | SSR (%) | SSR/TSR |
|-----------|---------|---------|---------|---------|
| Pi0.5 baseline | 71.5 | 28.5 | 28.0 | 0.39 |
| LoRA-only (3 seeds) | 51.5 | 54.67 | 27.7 | 0.54 |
| SDF λ=0.005 (3 seeds) | 54.0 | 54.5 | 27.8 | 0.51 |
| SDF λ=0.01 (3 seeds) | 53.8 | 56.33 | 30.2 | 0.56 |
| SDF λ=0.1 (3 seeds) | 50.2 | 57.00 | 30.2 | 0.60 |

### Appendix: Per-Task Oracle Analysis (tab:oracle_pertask)

Per-task CAR (%) for oracle refinement (evaluated on 160 episodes, 4 tasks × 40):

| Method | Task 0 (OJ) | Task 1 (CP) | Task 2 (Milk) | Task 3 (BBQ) | Aggregate |
|--------|-------------|-------------|---------------|--------------|-----------|
| LoRA baseline | 96.0 | 46.0 | 98.0 | 88.0 | 82.0 |
| Oracle-adaptive | 82.5 | 55.0 | 77.5 | 85.0 | 75.0 |
| Oracle-fixed | 85.0 | 50.0 | 77.5 | 80.0 | 73.1 |
| Oracle-feature | 90.0 | 47.5 | 82.5 | 87.5 | 76.9 |

Key per-task observations:
- Task 1 (Chocolate Pudding): only task where EE is primary collision body; Oracle-adaptive improves from 46.0% to 55.0% (+9 pp)
- Task 0 (Orange Juice): Oracle-adaptive degrades from 96.0% to 82.5% (-13.5 pp)
- Task 2 (Milk): Oracle-adaptive degrades from 98.0% to 77.5% (-20.5 pp)

Oracle-feature firing statistics:
- 241.7 refinements/episode (vs 14.2 for Cartesian variants — 17× more steps)
- Gradient magnitudes: 0.004–0.006 (vs 0.18–0.49 for Cartesian variants — 2 orders of magnitude smaller)
- A3 learned SDF: 0 steps/episode (never triggers)

### Appendix: Null Distribution for SDF Loss Weight Analysis (sec:appendix_null)

Null pool (Null B): 6 per-seed CAR measurements from LoRA-only + λ=0.005:
- 56.5% (LoRA s0, re-evaluated), 52.5% (LoRA s1), 55.0% (LoRA s2)
- 57.0% (λ=0.005 s0), 54.0% (λ=0.005 s1), 52.5% (λ=0.005 s2)
- Null mean: 54.58%, Null std: 1.93% (Bessel-corrected, n-1=5)

| Test | Value |
|------|-------|
| λ=0.01 mean | 56.33%, within 0.9σ of null (p > 0.1) |
| λ=0.1 mean (3 seeds: 58.0, 58.5, 54.5) | 57.00% |
| Two-tailed permutation p (λ=0.1, Null B) | 0.131 (= 11/84) |
| One-tailed permutation p (λ=0.1, Null B) | 0.071 (= 6/84) |
| Total permutations (Null B) | C(9,3) = 84 |
| Combinations meeting mean ≥ 57.00 | 6 |
| Significance threshold α | 0.05 |

Null A (LoRA-only seeds only: {56.5, 52.5, 55.0}):
- C(6,3) = 20 permutations
- λ=0.1: one-tailed p = 3/20 = 0.150, two-tailed p = 6/20 = 0.300
- λ=0.01: one-tailed p = 4/20 = 0.200, two-tailed p = 8/20 = 0.400
- Under Null B: λ=0.01 one-tailed p = 10/84 ≈ 0.119, two-tailed p = 22/84 ≈ 0.262

Phase 2 ablation (λ=0 from step 5K):
- CAR = 57.5% at 18K checkpoint (13K steps Phase 2, single seed s2)
- Within null range → no lasting behavioral effect from SDF

### Appendix: Step-wise Checkpoint Analysis for λ=0.1 (tab:stepwise_lambda01)

Per-seed CAR (%) at training checkpoints (200 episodes each):

| Checkpoint | Seed 0 | Seed 1 | Seed 2 | Mean |
|------------|--------|--------|--------|------|
| 16K steps | 55.5 | 56.0 | -- | 55.75 |
| 20K steps | 55.0 | 56.0 | -- | 55.5 |
| 22K steps | 60.5 | 56.5 | -- | 58.5 |
| 24K steps | 52.5 | -- | -- | -- |
| 26K steps | 53.5 | -- | -- | -- |
| 28K steps | 54.5 | -- | -- | -- |
| 30K steps | 58.0 | 58.5 | 54.5 | 57.00 |

Seed 0 checkpoint-to-checkpoint fluctuation range: 52.5–60.5% (8 pp spread)
Binomial noise (n=50 per task, p≈0.5): σ ≈ 7 pp per task

### Appendix: Oracle SDF Refinement Details (sec:appendix_oracle)

| Value | Context |
|-------|---------|
| 160 | Total oracle evaluation episodes (4 tasks × 40) |
| α = 0.005 | Fixed step size for Oracle-fixed |
| 241.7 | Refinements per episode for Oracle-feature |
| 14.2 | Refinements per episode for Cartesian variants |
| 0.004–0.006 | Gradient magnitudes in feature space (Oracle-feature) |
| 0.18–0.49 | Gradient magnitudes in action/Cartesian space |

### Appendix: Cross-Scene Validation (tab:spatial_bowl)

Scene: spatial_bowl (moka pot, wine bottle, milk carton, red coffee mug, yellow book obstacles)
Single training seed (seed 0), single eval seed (seed 7), 200 episodes, 30K checkpoint.

| Condition | CAR (%) | TSR (%) |
|-----------|---------|---------|
| LoRA-only | 12.0 | 49.0 |
| SDF λ=0.005 | 11.5 | 51.5 |

| Value | Context |
|-------|---------|
| -0.5 pp | CAR difference (SDF vs LoRA-only) on spatial_bowl |
| 11–12% | CAR range on spatial_bowl |
| 54–57% | CAR range on object_pudding (for comparison) |

### Appendix: Evaluation Seed Robustness (tab:eval_seed_robustness)

Aggregate CAR and TSR (%) across evaluation seeds (200 episodes each):

| Condition | Seed 0 CAR | Seed 7 CAR | Seed 42 CAR | Seed 99 CAR | Seed 123 CAR | Mean±Std CAR |
|-----------|-----------|-----------|------------|------------|-------------|-------------|
| LoRA s0 | 53.0 | 56.5 | 56.5 | 57.5 | 53.0 | 55.3±2.1 |
| SDF λ=0.01 s0 | 52.5 | 57.0 | -- | 57.0 | -- | 55.5±2.6 |
| SDF λ=0.1 s0 | -- | 58.0 | 59.0 | -- | 58.5 | 58.1±0.9 |

TSR across evaluation seeds:

| Condition | Seed 0 TSR | Seed 7 TSR | Seed 42 TSR | Seed 99 TSR | Seed 123 TSR | Mean±Std TSR |
|-----------|-----------|-----------|------------|------------|-------------|-------------|
| LoRA s0 | 55.5 | 51.5 | 46.0 | 52.0 | 50.5 | 51.1±3.4 |
| SDF λ=0.01 s0 | 48.5 | 52.5 | -- | 46.5 | -- | 49.2±3.1 |
| SDF λ=0.1 s0 | -- | 47.0 | 52.5 | -- | 53.5 | 50.3±3.2 |

Key comparisons:
- LoRA s0 CAR range across 5 seeds: 53.0–57.5%, std=2.1 pp
- SDF λ=0.01 s0 mean CAR: 55.5% vs LoRA 55.3% (near-identical)
- SDF λ=0.1 s0 mean CAR: 58.1%, difference from LoRA = 2.8 pp (<1.3σ, non-significant)

Per-task CAR for LoRA s0 across 5 evaluation seeds (tab:eval_seed_car_detail):

| Eval seed | OJ | CP | Milk | BBQ | Agg. |
|-----------|----|----|----|-----|------|
| 0 | 46 | 70 | 74 | 22 | 53.0 |
| 7 | 56 | 74 | 70 | 26 | 56.5 |
| 42 | 60 | 70 | 68 | 28 | 56.5 |
| 99 | 58 | 76 | 66 | 30 | 57.5 |
| 123 | 52 | 74 | 66 | 20 | 53.0 |
| Mean±Std | 54.4±5.5 | 72.8±2.7 | 68.8±3.3 | 25.2±4.1 | 55.3±2.1 |

### Appendix: Training Details (sec:appendix_training)

Architecture:
- LoRA rank (vision/PaliGemma): 16, α=16
- LoRA rank (action expert): 32, α=32
- SDF Decoder: 4-layer MLP, hidden dim 256, input = pooled suffix features (1024-d) + query points (3-d)
- EE Extractor: 2-layer MLP, 1024→256→3

Training schedule:
- Phase 1: steps 0–5000 (backbone/LoRA frozen, only SDF decoder + EE extractor trained)
- Phase 2: steps 5000–30000 (LoRA unfrozen, 100-step gradient warmup ramp)

Hyperparameter table (tab:hyperparams):

| Parameter | Value |
|-----------|-------|
| Base model | Pi0.5 (OpenPi, ~3.5B parameters) |
| Optimizer | AdamW |
| Learning rate | 2.5×10⁻⁵ (cosine decay to lr/10) |
| Warmup steps | 1000 |
| Batch size | 32 |
| Total steps | 30000 |
| λ_sdf | {0.005, 0.01, 0.1} |
| λ_ee | 0.01 |
| SDF query points per step | 64 |
| SDF clamp δ | 0.05 m |
| Eikonal weight | 0.1 |
| LoRA rank (vision) | 16 |
| LoRA rank (action) | 32 |
| Phase 1 duration | 5000 steps |

Evaluation protocol:
- Max timesteps per episode: 300
- Action trajectory length: 50 steps (flow matching)
- Execute first 5 steps before replanning
- Camera rotation: 180° for Pi0.5 (corrects TSR from ~5% to ~52%)
- Oracle variants: 40 episodes per task (160 total), single seed
- Standard: 50 episodes per task (200 total)

SDF ground truth:
- Voxel grid: 64³
- Query points per training step: 64 (randomly sampled)

Computational resources:
- GPU: NVIDIA RTX PRO 6000 (96 GB)
- Phase 1 (5K steps): ~6 hours on single GPU
- Phase 2 (25K steps): ~32 hours
- Evaluation (200 episodes): ~4 hours
- Total budget across 100+ experiments: ~700 GPU-hours

---

## contingency_claim3.tex

This file is NOT included in main.tex (contingency/planning file only). It contains template paragraphs for three λ=0.1 scenarios with placeholder values {MEAN}, {S0}, {S1}, {DELTA}. Key reference values from the scenario framing:

| Value | Context |
|-------|---------|
| 54.5% | Null distribution mean referenced in Scenario B/C templates |
| 2.15 pp | Null distribution σ referenced in Scenario B/C templates |
| Scenario B threshold | CAR mean ≤ 57% → full redundancy confirmed |
| Scenario C threshold | CAR mean 57–60% → inconclusive |
| Scenario A threshold | CAR mean > 60% → dose-response evidence |

Note: The actual paper uses the Scenario C/B result (λ=0.1 mean = 57.00%, p=0.131, within null, non-significant).

---

## Summary: Key Numbers Across All Files

### Primary Result Numbers

| Metric | Value | Source |
|--------|-------|--------|
| Pi0+A1 raw CAR | 91.5% | claim1, introduction |
| Pi0+A1 dfCAR | ≈0% (3/732 episodes survive) | claim1, introduction |
| Pi0+A1 action-collapse rate | 99.6% | claim1 |
| Pi0 Full-FT raw CAR | 83.0% | claim1 |
| Pi0 Full-FT action-collapse rate | 99.4% | claim1 |
| Pi0 LoRA raw CAR | 82.0% | claim1 |
| Pi0 LoRA action-collapse rate | ~99% | claim1 |
| Pi0.5 baseline CAR | 28.5% | claim1, claim3 |
| Pi0.5 baseline TSR | 71.5% | claim1, claim3 |
| Pi0.5 baseline dfCAR | 28.5% (= raw CAR) | claim1 |
| Best oracle CAR | 76.9% (Oracle-feature) | claim2 |
| Worst oracle CAR | 73.1% (Oracle-fixed) | claim2 |
| Oracle gap vs LoRA baseline | −5.1 pp (best oracle) to −8.9 pp (worst) | claim2 |
| LoRA-only CAR (fine-tuned Pi0.5) | 54.67% ± 2.02 | claim3 |
| LoRA+SDF λ=0.1 CAR | 57.00% ± 2.18 | claim3 |
| SDF vs LoRA delta | ~2.3 pp | claim3 |
| p-value (λ=0.1 vs null, two-tailed) | 0.131 | claim3, appendix |
| CAR gain from demonstrations | ~26 pp | claim3, discussion |
| spatial_bowl SDF vs LoRA delta | -0.5 pp | appendix |

### Experiment IDs Referenced
No explicit experiment IDs (e.g., E001, exp_id patterns) appear in any of the tex files. Experiments are referenced by configuration name (LoRA s0/s1/s2, SDF λ=X sY) and checkpoint step (16K, 20K, 22K, 24K, 26K, 28K, 30K).

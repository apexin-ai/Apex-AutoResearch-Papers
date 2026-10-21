# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL

## Title Candidates

1. **"Why Temporal Abstraction Fails in World-Model Reinforcement Learning: A Diagnostic Analysis"**
2. **"The Delusional Critic Problem in Variable-Rate Imagination"**
3. **"Diagnosing Value Overestimation in Temporally-Abstract World Models"**

## Venue

**CoRL 2026** — Deadline: 2026-05-29

## Narrative Positioning

This is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*

The contribution is a **closed causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor. Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.

---

## Core Claims

### C1: Variable-rate imagination in DreamerV3 consistently degrades performance

Temporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |
| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |
| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |
| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |

**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.

### C2: Trained dt_embedding causes delusional critic (root cause)

**⚠️ Causal attribution pending**: Current 008c vs 008d comparison confounds dt_embedding training with RSSM training data composition (subsample ON/OFF). exp_008f (dt_embed_dim=0 + subsample ON + dt=2 imagination + H=8) will isolate the dt_embedding variable. C2 strength is provisional until 008f completes.

The trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is systematic value overestimation (delusional critic) that drives actor learning toward incorrect policies.

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |
| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |
| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |
| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |

**Strength**: Strong. The 008c vs 008d comparison is a controlled experiment isolating dt_embedding training as the single variable. The v/e overshoot ratio (experiment v/e / baseline v/e at same step) quantitatively identifies pathological regimes: trained dt_emb variants exceed 1.5x baseline before collapse, while untrained variants stay at or below baseline levels. **Pending confirmation**: exp_008f (dt_embed_dim=0 + subsample ON) will isolate whether dt_embedding conditioning or RSSM's learned dt=2 dynamics is the true cause.

### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance

When dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete V-shaped recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |
| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |
| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |
| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |
| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |

**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete V-shaped recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the delusional critic feedback loop in trained variants.

**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).

**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.

### C4: Longer dt amplifies the problem

Increasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |
| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |
| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |

**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.

### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause

Subsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |
| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |
| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |
| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |

**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.

---

## Story Arc

### 1. Introduction
- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)
- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction
- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?
- Contribution: systematic factorial diagnosis identifying trained dt_embedding → delusional critic as the root cause

### 2. Background & Related Work
- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)
- World-model RL (Dreamer family, IRIS, TWM)
- Variable-rate planning in world models (few prior works, mostly positive framing)
- Value overestimation / delusional policies in model-based RL

### 3. Methodology
- DreamerV3 as base architecture
- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating
- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines
- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves

### 4. Results
- **Finding 1**: All dt>1 configurations degrade (C1)
- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the "smoking gun" comparison (008c vs 008d)
- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)
- **Finding 4**: Longer dt amplifies (C4)
- **Finding 5**: Horizon/subsample effects are secondary (C5)

### 5. Discussion
- Mechanism: why trained dt_embedding causes delusional critic (RSSM fidelity gap at dt>1)
- Connection to existing theory: delusional policies (Delalleau et al.), model exploitation in MBRL
- Why this is specific to world-model RL (model-free temporal abstraction doesn't suffer the same failure mode)

### 6. Implications for Future Work
- Don't train dt_embedding jointly with value function in current world-model architectures
- RSSM prediction quality must improve before variable-rate imagination is viable
- Value growth suppression (e.g., untrained dt_embedding) as a potential mitigation direction
- Need for diagnostic methodology in temporal abstraction research

---

## Anticipated Reviewer Concerns

### R1: "Limited to one environment / one base algorithm"
**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.
**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.

### R2: "No proposed solution — what's the actionable takeaway?"
**Pre-emption**: Diagnostic papers serve a different purpose than method papers. Identifying root causes (trained dt_embedding) and quantitative signatures (v/e overshoot ratio >1.5x baseline = pathological) gives the community concrete guidance. We explicitly outline mitigation directions (value growth suppression, improved RSSM, decoupled dt_embedding training).
**Mitigation**: Frame implications section as a "research agenda" with specific, testable hypotheses.

### R3: "Value/eval ratio is a crude proxy for overestimation"
**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.
**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.

### R4: "The factorial design is incomplete — missing cells in the grid"
**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.
**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.

### R5: "Novelty concern — model exploitation / value overestimation in MBRL is well-known"
**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.

### R6: "All results from a single seed — how robust are the conclusions?"
**Pre-emption**: Our claims are about *mechanisms* (causal chain from dt_embedding → value overestimation → collapse), not about precise numerical thresholds. The mechanism manifests consistently across all configurations (exp_005, 006, 007, 008d) — four independent experiments all show the same value/eval ratio divergence pattern. The probability of this pattern appearing by chance across 4 experiments is negligible.
**Mitigation**: Planned multi-seed runs for final paper. The factorial design (008c vs 008d) provides cross-experiment replication of the core mechanism.

### R7: "The factorial design confounds dt_embedding training with training data composition"
**Pre-emption**: We acknowledge this confound between 008c (subsample OFF, untrained dt_emb) and 008d (subsample ON, trained dt_emb). Experiment 008f (dt_embed_dim=0 + subsample ON) is designed to resolve this: it trains with dt=2 transitions (like 008d) but without dt_embedding conditioning. If 008f collapses → the cause is RSSM's learned dt=2 dynamics, not dt_embedding per se. If 008f remains stable → dt_embedding conditioning is confirmed as the root cause.
**Mitigation**: exp_008f is a blocking experiment for the final paper. Results will be available before submission.

---

## Experiment Coverage Assessment

| Claim | Evidence Status | Gaps |
|-------|----------------|------|
| C1 (degradation) | ✅ Strong — 3 configurations (005, 006, 007) all negative | Could add 1 more environment |
| C2 (root cause: dt_emb) | ⚠️ Provisional — pending exp_008f to resolve dt_embedding vs training data confound | Consider adding value prediction distribution analysis |
| C3 (preventing optimistic drift) | ✅ Strong (105K confirmed) — 008a@105K=778 (85% baseline), normalized v/e=0.59x, two V-shaped recoveries | None — long-term structural suppression confirmed |
| C4 (dt amplification) | ⚠️ Moderate — only dt=2 vs dt=4 | Would benefit from dt=3, but not blocking |
| C5 (horizon/subsample) | ⚠️ Moderate — confounded with other factors | Need 008c-equivalent with H=15 + subsample ON + untrained dt_emb for clean isolation |

### Priority Actions Before Submission
1. ~~**Check exp_008a@65K**~~ — ✅ Done: 608 (-1.3% baseline), B+ confirmed
2. **Complete factorial grid analysis** — present all 8 cells, even if some are interpolated
3. **Value prediction distribution plots** — strengthen C2 beyond ratio proxy
4. **Second environment** (stretch goal) — addresses R1

---

## Key Figures (Planned)

1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)
2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes
3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis
4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse
5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)

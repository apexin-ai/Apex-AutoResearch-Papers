# C5b Mitigation Pilot — Experiment Design

> Claim: Phase-aware sparsity allocation recovers compound degradation
> Status: plan_011 | Priority: P1 | Depends on: plan_009, plan_010 (n=500 running)
> Gate: >30% II recovery → full rollout; else → future work
> Budget: ~2h on 1 GPU (RTX PRO 6000 Blackwell 96GB)

---

## 1. Objective & Hypotheses

**Goal**: Demonstrate that phase-aware sparsity budget allocation — informed by the phase-modulated severity gradient (C1/C2) — can reduce compound interaction degradation compared to uniform allocation.

**Hypotheses**:
- **H1 (Oracle)**: When true phase labels are known, reallocating sparsity budget away from the execution phase (high compound interaction) toward the transition phase (low compound interaction) recovers >30% of compound interaction (measured by II reduction).
- **H2 (Heuristic)**: A zero-cost heuristic (token position ratio) recovers some compound interaction, but less than oracle, establishing a lower bound.

**Why this matters**: C1-C3 establish that compound interaction is phase-dependent. C5b closes the loop: if severity is phase-dependent, phase-aware allocation should mitigate it. Even a modest pilot result (1) validates the practical relevance of the finding, and (2) provides a concrete pointer for future work on phase-gated controllers.

---

## 2. Pilot Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Model | DeepSeek-R1-Distill-Qwen-7B | Strongest signal (median_diff 3.97/9.94 at s025/s030) |
| n_problems | 30 | Sufficient for paired test (existing stratified sample subset) |
| Sparsity levels | s=0.25, s=0.30 | Largest compound interaction, most room for recovery |
| Phases | 3 (execution/reasoning/transition) | Quantile-based segmentation, consistent with C1-C3 |
| Bootstrap | B=10000 | Consistent with bf16 canonical data |

**Why not Qwen**: Qwen's compound interaction is ~1/4 of DeepSeek's magnitude (2.619 vs 9.94 at s030). Smaller signal → harder to detect recovery. If oracle recovers >30% on DeepSeek, Qwen replication is a separate follow-up.

**Why not s015/s020**: Small compound interaction (0.32/1.15) leaves little room for meaningful recovery. Risk of floor effects.

---

## 2.5 Implementation Scheme: C (Director Decision 2026-05-14)

**Phase-aware KV eviction + uniform head pruning**:

- **KV eviction**: Per-position sparsity allocation that varies by phase. Execution phase gets reduced eviction rate (δ=0.10 less), transition phase gets increased eviction rate. Total KV eviction budget is compute-matched with the uniform baseline.
- **Head pruning**: Global uniform pruning rate across all phases. Does not vary by phase.
- **Rationale**: KV eviction is a per-position operation that naturally supports phase-aware allocation. Head pruning is a global structural decision — adjusting it per-token is neither practical nor meaningful.
- **Interpretive value**: If oracle recovery <30%, this indicates that head pruning's fixed structural damage is the bottleneck in compound severity (i.e., the dominant source of compound interaction is structural rather than positional). This is itself a valuable finding for §7 Discussion.

**Implication for conditions below**: The δ-based allocation rule in §3.2 and §3.3 applies **only to KV eviction sparsity**. Head pruning sparsity remains at the target level s uniformly across all phases for all conditions.

---

## 3. Experimental Conditions (per problem, per sparsity level)

> **Revision (Director 2026-05-14)**: Phase-aware modulation applies to KV eviction only; head pruning remains uniform across phases. Three-condition redefinition:
> - (1) **Uniform baseline** = uniform head pruning + uniform KV eviction
> - (2) **Oracle** = uniform head pruning + oracle phase-aware KV eviction (uses true phase labels to modulate KV eviction rate)
> - (3) **Heuristic** = uniform head pruning + token-position-ratio heuristic KV eviction
>
> Code impact: no modification to head mask forward pass; only KV eviction logic requires per-phase eviction rate switching. ~150 lines unchanged.

### 3.1 Condition A — Uniform Baseline (existing data)

Standard importance-based compound sparsity at level s, applied uniformly across all phases.

This is the **existing bf16 importance data** (already collected). No new GPU compute needed for this condition. We re-use per-problem II values from `profiling_output_bf16_imp_s025/` and `profiling_output_bf16_imp_s030/`.

**Per-phase II_uniform(phase, s) from existing data**:
- II(execution, s025) ≈ 7.20 (median), II(transition, s025) ≈ 0.053
- II(execution, s030) ≈ 14.64 (median), II(transition, s030) ≈ 0.053

### 3.2 Condition B — Oracle Phase-Aware Allocation

Phase-dependent **KV eviction** sparsity using **true quantile-based phase labels** (from attention sparsity during generation). Head pruning remains at uniform rate s across all phases (per Scheme C). This is an upper bound on mitigation performance — a real controller would have noisier phase estimates.

**KV eviction allocation rule** (compute-matched):

Given target sparsity s and phases with token counts (n_exec, n_reas, n_trans):

```
s_exec  = s - δ           (reduce sparsity in high-interaction phase)
s_reas  = s               (keep reasoning phase unchanged)
s_trans = s + δ'           (increase sparsity in low-interaction phase)

Compute match constraint:
  n_exec × s_exec + n_reas × s_reas + n_trans × s_trans = N_total × s
  → δ' = δ × (n_exec / n_trans)
```

**δ selection**: Use δ = 0.10 (i.e., execution phase gets s-0.10, transition gets s+δ').

| Target s | s_exec | s_reas | s_trans (approx, depends on phase sizes) |
|----------|--------|--------|------------------------------------------|
| 0.25 | 0.15 | 0.25 | ~0.35 |
| 0.30 | 0.20 | 0.30 | ~0.40 |

Note: δ' is computed per-problem based on actual phase token counts to ensure exact compute match.

> **Revision (Director 2026-05-14, updated)**: s_trans cap at 0.50, with proportional rescale to maintain exact compute match.
>
> **Cap applies to s_trans itself, not to δ'.**  Reason: s_trans > 0.50 (e.g. 80% KV eviction) causes forward pass degradation that pollutes downstream phase II calculation. 0.50 is sufficient for signal detection in this pilot.
>
> ```
> δ' = δ × (n_exec / n_trans)                    # raw transfer ratio
> δ'_capped = min(δ', 0.50 - s)                  # cap so s_trans ≤ 0.50
>
> Case 1: δ' ≤ 0.50 - s  (no cap needed)
>   s_exec  = s - δ
>   s_reas  = s
>   s_trans = s + δ'
>
> Case 2: δ' > 0.50 - s  (cap triggers rescale)
>   s_trans = 0.50                                # hard cap
>   δ_effective = (0.50 - s) × (n_trans / n_exec) # rescale δ for compute-match
>   s_exec  = s - δ_effective
>   s_reas  = s
>
>   Verify: n_exec×(s - δ_effective) + n_reas×s + n_trans×0.50
>         = N_total×s - n_exec×δ_effective + n_trans×(0.50 - s)
>         = N_total×s - n_exec×(0.50-s)×n_trans/n_exec + n_trans×(0.50-s)
>         = N_total×s                              (exact match)
> ```
>
> Per-sparsity δ' effective limits:
> - s=0.25 → δ' max = 0.25, s_trans max = 0.50
> - s=0.30 → δ' max = 0.20, s_trans max = 0.50
>
> Boundary conditions:
> - n_trans = 0 → skip phase-aware allocation, fall back to uniform
> - δ_effective ≥ 0 always holds when both n_exec, n_trans > 0

**Implementation**: For each problem:
1. Generate trace (reuse existing generation from bf16 runs, or regenerate if needed)
2. Segment into phases (quantile-based, same as existing pipeline)
3. For each phase, generate importance-based masks at s_phase
4. Run compound forward with phase-specific masks, extract PPL on that phase's tokens
5. Compute per-phase II under oracle allocation

### 3.3 Condition C — Heuristic Baseline (Token Position Ratio)

Phase assignment using **normalized generation position** as a zero-cost proxy. As with Condition B, only KV eviction sparsity varies by phase; head pruning remains uniform.

```
phase_heuristic(token_pos) =
  "execution"  if token_pos / seq_len < 0.33
  "reasoning"  if 0.33 ≤ token_pos / seq_len < 0.67
  "transition" if token_pos / seq_len ≥ 0.67
```

Same sparsity allocation rule as oracle, but applied based on positional phase labels. This is the simplest possible heuristic — it tests whether even crude position-based phase estimation captures enough signal for mitigation.

**Why token position ratio**: (1) Zero compute cost — no attention weights needed. (2) Prior work (ThinKV) observes that reasoning models often follow a "thinking → calculating → summarizing" trajectory, correlating with token position. (3) Establishes a lower bound that any real phase detector must beat.

**Alternative heuristic considered but deferred**: Cumulative attention entropy (requires attention weights, non-zero cost). If token position ratio shows >0% recovery, entropy-based heuristic becomes a natural follow-up.

---

## 4. Evaluation Metrics

### 4.1 Primary: II Recovery Percentage

For each problem i, sparsity level s, and phase p:

```
II_uniform(i, s, p)  = II under Condition A
II_oracle(i, s, p)   = II under Condition B
II_heuristic(i, s, p) = II under Condition C
```

**Aggregate metric** (per sparsity level):

```
recovery_oracle(s) = 1 - median(II_weighted_oracle(i, s)) / median(II_weighted_uniform(i, s))
recovery_heuristic(s) = 1 - median(II_weighted_heuristic(i, s)) / median(II_weighted_uniform(i, s))
```

Where `II_weighted(i, s) = Σ_p [n_p × II(i, s, p)] / N_total` is the token-count-weighted mean II across phases for problem i.

### 4.2 Secondary: Per-Phase II Comparison

Compare per-phase II between uniform and oracle:
- Execution phase: II should decrease (less sparsity → less compound interaction)
- Transition phase: II should stay low (already near zero, even with more sparsity)
- Net effect: overall weighted II decreases

### 4.3 Gate Criterion

```
PASS if: recovery_oracle(s025) > 30% OR recovery_oracle(s030) > 30%
FAIL otherwise → C5b = "future work"
```

If heuristic also exceeds 30%, that's a bonus result but not required for the gate.

### 4.4 Statistical Test

Paired Wilcoxon signed-rank test on per-problem weighted II (uniform vs oracle, uniform vs heuristic). Report p-value and recovery percentage with bootstrap 95% CI (B=10000).

---

## 5. Implementation Plan

### 5.1 Code Changes

Create `run_mitigation_pilot.py` extending the existing profiling pipeline:

```
pacs/profiling/run_mitigation_pilot.py
```

**Key functions to add**:

1. `compute_phase_aware_sparsity(target_s, delta, phase_token_counts) → Dict[str, float]`
   - Returns per-phase sparsity levels, compute-matched
   - Caps s_trans at 0.50

2. `assign_heuristic_phases(seq_len, prompt_len) → List[Phase]`
   - Token position ratio → phase assignment
   - Returns Phase objects compatible with existing pipeline

3. `run_mitigation_trial(model, tokenizer, problem, target_s, delta, phase_method) → Dict`
   - Runs one problem under one condition
   - phase_method ∈ {"oracle", "heuristic"}
   - Returns per-phase II values and weighted aggregate

**Reuse from existing pipeline**:
- `load_model_and_tokenizer()` — unchanged
- `stratified_sample_math500()` — take first 30
- `InteractionIndexCalculator` — core II computation, unchanged
- `segment_by_quantile()` + `to_phase_annotation()` — oracle phase labels
- `_select_heads_to_mask()`, `_select_kv_to_evict()` — mask generation at arbitrary sparsity
- `compute_conditioned_perplexities()` — per-phase PPL computation

**New logic** (~150 lines):
- Phase-aware sparsity allocation function
- Heuristic phase assignment function
- Main loop: for each problem × condition, generate phase-specific masks and compute II
- Output JSON with per-problem, per-condition II values

### 5.2 Data Flow

```
Input:
  - Existing bf16 generation traces (if saved) OR re-generate (adds ~30min)
  - Existing bf16 profiling results for uniform baseline comparison

Pipeline (per problem):
  1. Generate trace → segment phases (oracle) / assign phases (heuristic)
  2. For each phase:
     a. Compute phase-specific sparsity level (compute-matched)
     b. Generate importance masks at phase-specific level
     c. Forward pass with phase masks, extract phase-token PPL
     d. Compute phase II
  3. Compute weighted aggregate II
  4. Compare against uniform baseline II

Output:
  - mitigation_pilot_results.json:
    {config, per_problem: [{problem_id, uniform_ii, oracle_ii, heuristic_ii, recovery_pct, ...}]}
  - Summary statistics + gate evaluation
```

### 5.3 Compatibility Notes

- **Generation reuse**: If bf16 generation traces are saved in existing profiling output (check `profiling_results.json` for per-problem token sequences), reuse them. Otherwise re-generate — adds ~30min but ensures exact matching.
- **Mask generation**: `_select_heads_to_mask` and `_select_kv_to_evict` accept arbitrary sparsity levels. No changes needed.
- **Phase segmentation**: `segment_by_quantile` works on the sparsity trace from generation. Oracle uses this. Heuristic bypasses it.

---

## 6. GPU & Time Budget

| Component | GPU Time | Notes |
|-----------|----------|-------|
| Model loading | 2 min | DeepSeek 7B bf16, single GPU |
| Generation (if needed) | 30 min | 30 problems × ~60s each |
| Oracle condition | 30 min | 30 problems × 2 sparsity × 3 phases × 3 forward passes |
| Heuristic condition | 30 min | Same as oracle |
| Analysis + bootstrap | 5 min | B=10000 on CPU |
| **Total** | **~1.5h** (with re-generation) or **~1h** (with trace reuse) |

**GPU**: 1× RTX PRO 6000 Blackwell 96GB. Can run on any of GPU 0-3 after c2_qw_n500 frees up GPU 2 or 3.

**Timeline dependency**: plan_009 (c2_n500_deepseek, GPU 0+1) and plan_010 (c2_qw_n500, GPU 2+3) are currently running (~22h each). Once any GPU frees up, this pilot can start immediately. Expected availability: ~05-15 12:00 CST (based on c2_qw_n500 progress at ~8/500 as of 05-14 22:00).

**Hard deadline**: Results needed by 05-22 for paper integration. With 1.5h runtime, scheduling is not a bottleneck — GPU availability is the sole constraint.

---

## 7. Expected Outcomes & Contingencies

### Scenario A: Oracle recovery > 30% (PASS)

- C5b enters paper as "phase-aware allocation recovers X% of compound degradation (oracle upper bound)"
- If heuristic also recovers >10%, include both in paper as oracle/heuristic pair
- One paragraph in §5 Results + one figure (bar chart: uniform vs oracle vs heuristic II)

### Scenario B: Oracle recovery 10-30% (MARGINAL)

- C5b enters Discussion (§6) as "phase-aware allocation shows promising but modest recovery"
- Emphasize that even partial recovery validates the practical relevance of the phase-modulated severity finding
- Frame full optimization as future work

### Scenario C: Oracle recovery < 10% (FAIL)

- C5b = future work, one sentence in Discussion
- Under Scheme C, this outcome has a clear interpretation: head pruning's fixed structural damage is the dominant source of compound severity, and phase-aware KV eviction alone cannot compensate. This is a meaningful negative result for §7 Discussion (compound interaction is primarily structural, not positional).
- Core claims C1-C6 unaffected — finding stands without mitigation

### Risk: Generation trace mismatch

If bf16 traces are not saved and re-generation produces different phase segmentations, uniform baseline II values will differ from existing n=50 data. Mitigation: always compare within the same run's generation (uniform vs oracle/heuristic computed from the same trace), never cross-run.

---

## 8. Output Artifacts

| Artifact | Path | Description |
|----------|------|-------------|
| Results JSON | `artifacts/mitigation_pilot_results.json` | Per-problem raw data |
| Summary | `artifacts/mitigation_pilot_summary.md` | Gate evaluation + key numbers |
| Figure | `paper_figures/fig_mitigation_pilot.pdf` | Bar chart: uniform vs oracle vs heuristic |

---

## 9. Handoff Checklist for Coding Worker

- [ ] Check if bf16 profiling output contains saved generation traces (token IDs + attention sparsity per step)
- [ ] Create `pacs/profiling/run_mitigation_pilot.py` with the three functions specified in §5.1
- [ ] Reuse `stratified_sample_math500(seed=42)[:30]` for consistent problem selection
- [ ] **Scheme C**: Phase-aware δ allocation applies to **KV eviction only**; head pruning stays at uniform rate s for all phases and all conditions
- [ ] Use δ=0.10 for KV eviction phase-aware allocation; cap applies to s_trans (not δ'): s_trans = min(s + δ', 0.50), so δ' effective max = 0.50 - s. When cap triggers, rescale δ_effective = (0.50 - s) × (n_trans / n_exec) for exact compute-match
- [ ] Compute-match constraint must hold exactly per-problem (not averaged), computed over KV eviction budget only
- [ ] Output format: JSON with per-problem breakdown + aggregate summary
- [ ] Register artifact after completion
- [ ] Run on single GPU, ~1.5h total wall time

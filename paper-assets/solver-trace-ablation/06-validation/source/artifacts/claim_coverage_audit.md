# Claim-Evidence Coverage Audit

**Date**: 2026-05-14  
**Deadline**: 2026-05-25 (ARR May, 11 days remaining)  
**Registry snapshot**: 31 experiments (6 success, 9 negative, 14 failed, 2 running)

---

## Experiment Inventory (Paper-Usable)

| ID | Condition | Formula | Steps | Seed | Eval Method | Status |
|----|-----------|---------|-------|------|-------------|--------|
| sta-phase0-baseline | Base model (no training) | — | 0 | — | inference | ✅ DONE |
| sta-gt-isr-baseline | Ground truth FOL | — | — | — | prover9 | ✅ DONE |
| plan003-eval-r5 | Exec-only early checkpoint | r = r_exec | 100 | 42 | eval_sta.py | ✅ DONE |
| plan001-s42-r2 | Exec-only | r = r_exec | 500 | 42 | eval_sta.py | ✅ DONE |
| plan001-s43-r4 | Exec-only | r = r_exec | 500 | 43 | **sampling only** | ⚠️ GAP |
| plan001-s44 | Exec-only | r = r_exec | 500 | 44 | eval_sta.py | ✅ DONE |
| plan005-sta-low | Convex ISR (α=0.9,β=0.1) | r = 0.9·r_exec + 0.1·r_exec·ISR | 500 | 42 | **training log only** | ⚠️ GAP |
| plan002-b03 | Additive ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 500 | 42 | eval_sta.py | ✅ DONE |
| plan013-r4 | Random convex | r = 0.9·r_exec + 0.1·random | 500 | 42 | eval_sta.py | ✅ DONE |
| plan017 | Additive random β=0.3 | r = r_exec·(1+0.3·random) | 500 | 42 | eval_sta.py | ✅ DONE |
| plan014 | Downstream NLI | — | — | 42 | eval_downstream.py | ✅ DONE (negative) |
| plan002-b01 | Additive ISR β=0.1 | r = r_exec·(1+0.1·ISR) | 500 | 42 | — | 🔄 RUNNING |
| plan016 | Exec-only extended | r = r_exec | 1000 | 42 | — | 🔄 RUNNING |

---

## Claim 1: ISR as Reward Hacking Diagnostic

> "STA derives ISR via component necessity testing. ISR detects reward hacking that prove_rate alone misses."

### Supporting Evidence

| Evidence Point | Experiment | Key Metrics | Strength |
|---|---|---|---|
| Early training = structurally sound | plan003-eval-r5 | PR=32%, proved_ISR=**0.6423** | ✅ Strong (eval_sta.py) |
| Late training = structural collapse despite high PR | plan001-s42-r2 | PR=**93%**, ISR=0.1232, proved_ISR=**0.1324**, median_ISR=0 | ✅ Strong (eval_sta.py) |
| ISR collapse magnitude | plan003→plan001-s42 | proved_ISR: **0.6423 → 0.1324** (−79%) | ✅ Strong |
| Seed 43: repetition collapse | plan001-s43-r4 | PR=**14%**, ISR=0, 87% hit max_tokens | ⚠️ Medium (sampling eval, not eval_sta.py — **violates C004**) |
| Seed 44: tautological collapse | plan001-s44 | PR=**98%**, ISR=0.57 (fake-high), comp=**2.04**, 94% 2-component | ✅ Strong (eval_sta.py) |
| Base model reference | sta-phase0-baseline | PR=12%, ISR=0.0641 | ✅ Reference |
| Ground truth ISR ceiling | sta-gt-isr-baseline | GT proved_ISR=**0.5588** | ✅ Reference |
| Hacking taxonomy (5 modes) | plan012 report + plan017 D027 | Qualitative + quantitative | ✅ Strong (artifact-based) |

### 3-Seed Summary (Exec-only 500 steps)

| Seed | eval PR | eval ISR | eval proved_ISR | Hacking Mode |
|------|---------|----------|-----------------|--------------|
| 42 | 93% | 0.1232 | 0.1324 | Conclusion embedding |
| 43 | 14% | 0 | — | Repetition/length collapse |
| 44 | 98% | 0.57 (fake) | 0.5816 | Tautological collapse (comp=2.04) |
| **mean±std** | **68±48%** | **0.23±0.30** | — | 3 distinct modes |

### Evidence Strength: ⭐⭐⭐⭐ (4/5)

**Strong points:**
- ISR collapse 0.6423→0.1324 is dramatic and clean (same seed, different training steps)
- 3 seeds showing 3 different hacking modes is a powerful finding
- All from eval_sta.py except s43

### Gaps

1. **CRITICAL: plan001-s43-r4 uses sampling eval, not eval_sta.py.** Metrics are `eval_sampling_*` with `do_sample=True, temperature=0.7`. Per C004, cross-seed ISR comparison requires eval_sta.py. **Action needed: re-run eval_sta.py on s43 checkpoint `/root/autodl-tmp/outputs/plan001_exec_only_s43_r4`.**
2. s43 component count not available — needed for hacking mode classification.

---

## Claim 2: GRPO Saturation Mechanism

> "When prove_rate → 1.0, reward_std → 0 and loss → 0, training stalls. Adding any variance redirects but doesn't prevent hacking."

### Supporting Evidence

| Evidence Point | Experiment | Key Metrics | Strength |
|---|---|---|---|
| Exec-only saturation: PR→1, loss→0 | plan001-s42-r2 | train last100 PR=not avail from eval, but ISR collapse confirms | ✅ Strong |
| Exec-only s44: PR saturation + tautological | plan001-s44 | train last100 PR=0.9988, loss=0.000419 | ✅ Strong |
| Random convex prevents saturation but tautological | plan013-r4 | eval PR=**1.0**, ISR=0.535, **100% 2-component**, all tautological | ✅ Strong |
| Additive ISR β=0.3: prevents saturation but lowest PR | plan002-b03 | eval PR=**18%**, eval ISR=0.0257, proved_ISR=0.1427 | ✅ Strong |
| Additive random β=0.3: prevents tautological but complexity-without-utility | plan017 | eval PR=**48%**, eval ISR=0.0453, comp=**9.56**, 33% proved ISR=0 | ✅ Strong |
| Convex ISR: penalty effect | plan005-sta-low | last100 PR=77.25%, ISR/PR ratio=0.298 | ⚠️ Medium (training log only) |
| **ISR worse than matched random** | plan002-b03 vs plan017 | ISR: PR=18% vs Random: PR=**48%** (same β=0.3, same formula structure) | ✅ Strong (key finding) |

### Reward Condition Comparison (eval_sta.py where available)

| Condition | Formula | eval PR | eval ISR | proved_ISR | comp_mean | Hacking Mode |
|-----------|---------|---------|----------|------------|-----------|--------------|
| Exec-only s42 | r_exec | 93% | 0.1232 | 0.1324 | ~6.58 | Conclusion embedding |
| Exec-only s44 | r_exec | 98% | 0.57 | 0.5816 | 2.04 | Tautological |
| Random convex | 0.9·r_exec+0.1·rand | 100% | 0.535 | 0.535 | ~2 | Tautological (100%) |
| Additive random β=0.3 | r_exec·(1+0.3·rand) | 48% | 0.0453 | 0.0943 | 9.56 | Complexity-without-utility |
| Additive ISR β=0.3 | r_exec·(1+0.3·ISR) | 18% | 0.0257 | 0.1427 | — | Repetitive cycling |
| Convex ISR (α=0.9) | 0.9·r_exec+0.1·r_exec·ISR | ~77%* | ~0.23* | — | — | ISR-PR separation |

*plan005 values from training log, not eval_sta.py

### Evidence Strength: ⭐⭐⭐⭐ (4/5)

**Strong points:**
- 5 reward conditions systematically compared
- ISR vs random (plan002-b03 vs plan017) is a clean pairwise comparison: same formula structure, same β, only ISR vs random differs → ISR actively misleading (PR 18% vs 48%)
- Multiple hacking modes documented per condition

### Gaps

1. **plan005-sta-low lacks eval_sta.py evaluation.** Training log ISR may use binary `_fast_fn`. **Action needed: run eval_sta.py on plan005 checkpoint `/root/autodl-tmp/outputs/plan005_sta_low_s42/checkpoint-500`.**
2. **plan002-b01 (β=0.1) still running.** Fills ISR dose-response (β=0.1 vs β=0.3). Expected completion: within hours.
3. **plan016 (1000 steps) still running.** Addresses reviewer concern "500 steps too short." Expected completion: within hours.
4. **All non-exec-only conditions are single-seed (s42 only).** Multi-seed data only exists for exec-only. This limits statistical claims for Claim 2 to qualitative comparisons.
5. plan013 vs plan017 formula structure difference (convex vs multiplicative) — paper_framing already notes this constraint (D027).

---

## Claim 3: Cross-Logic Generality

> "STA protocol is solver-agnostic: hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog."

### Supporting Evidence

**None.** plan006 Prolog GRPO experiment has not been started.

### Evidence Strength: ⭐ (0/5 — no evidence)

### Assessment

With 11 days to deadline, starting a full Prolog GRPO training pipeline (data prep + training + eval_sta.py adaptation + analysis) is extremely risky. **Recommendation: downgrade to Future Work.** The paper already has enough depth with FOL-only analysis (3 seeds × 5+ conditions × 5 hacking modes).

---

## ISR Capability Boundary (Supplementary Claim)

> "ISR measures syntactic component necessity, not semantic faithfulness."

### Supporting Evidence

| Evidence Point | Experiment | Key Metrics | Strength |
|---|---|---|---|
| ISR-NLI correlation null | plan014 | Spearman ρ=**−0.049** (p=0.187, NS) | ✅ Strong negative |
| Best-of-N ISR vs random | plan014 | +0.9pp (NS) | ✅ Strong negative |
| Model true-bias ceiling | plan014 | Overall accuracy=34.1%, false accuracy=0% | ✅ Explains null |
| Weak bucket-level trend | plan014 | high=75%, mid=37.7%, low=32.7% (but n=12 for high) | ⚠️ Suggestive |

### Evidence Strength: ⭐⭐⭐⭐ (4/5 as negative result)

Well-characterized null result with clear mechanistic explanation (true-bias). Suitable for Limitations section.

---

## Pending Experiments Impact

### plan002-b01 (Additive ISR β=0.1) — RUNNING

**Fills:** Claim 2 ISR dose-response. If β=0.1 outperforms β=0.3 (PR>18%), suggests ISR signal is useful at lower intensity. If also poor, strengthens "ISR actively misleading" narrative.

**Table 1 impact:** Adds one row to reward condition comparison.

### plan016 (Exec-only 1000 steps) — RUNNING

**Fills:** Reviewer concern #5 ("500 steps too short"). Shows whether hacking stabilizes, worsens, or recovers with extended training. Also whether s42's apparent "genuine" proofs degrade further.

**Table 1 impact:** Adds temporal dimension. Could show ISR trajectory figure (100→500→1000 steps).

### plan006 (Prolog 3-seed) — NOT STARTED

**Would fill:** Claim 3 entirely. Without it, Claim 3 = Future Work.

**Assessment:** Not feasible in 11 days given pipeline complexity. Drop from main claims.

---

## Table 1 Design

### Recommended Structure

**Table 1: Eval metrics across reward conditions (eval_sta.py, proofwriter_fol_100)**

| Condition | Formula | PR↑ | ISR_mean | ISR_proved | Comp_mean | Taut? | Hacking |
|-----------|---------|-----|----------|------------|-----------|-------|---------|
| Base model | — | 12% | 0.064 | — | — | — | — |
| GT FOL | — | 18% | — | 0.559 | — | — | — |
| Exec-only 100step | r_exec | 32% | 0.206 | 0.642 | — | No | — |
| Exec-only 500step s42 | r_exec | 93% | 0.123 | 0.132 | ~6.6 | No | Conclusion embed |
| Exec-only 500step s43 | r_exec | 14% | 0† | — | —† | No | Repetition |
| Exec-only 500step s44 | r_exec | 98% | 0.570 | 0.582 | 2.04 | **Yes** | Tautological |
| Exec-only **mean±std** | r_exec | **68±48%** | **0.23±0.30** | — | — | — | 3 modes |
| Convex ISR (α=0.9) | 0.9e+0.1eI | ~77%* | ~0.23* | —* | — | No | ISR-PR sep |
| Additive ISR β=0.3 | e(1+0.3I) | 18% | 0.026 | 0.143 | — | No | Cycling |
| Additive ISR β=0.1 | e(1+0.1I) | **TBD** | **TBD** | **TBD** | **TBD** | TBD | TBD |
| Random convex | 0.9e+0.1r | 100% | 0.535 | 0.535 | ~2 | **Yes** | Tautological |
| Additive random β=0.3 | e(1+0.3r) | 48% | 0.045 | 0.094 | 9.56 | No | Complexity |

† s43 needs eval_sta.py re-evaluation  
\* plan005 needs eval_sta.py evaluation  
**TBD** = plan002-b01 running

### Missing Data for Table 1

1. **plan001-s43 eval_sta.py** — currently only has sampling eval
2. **plan005 eval_sta.py** — currently only has training log metrics
3. **plan002-b01 eval** — experiment still running
4. **plan001-s42 component_count_mean** — not in registry metrics (need to extract from eval output)
5. **plan016 eval** — experiment still running

---

## Priority Actions (ordered by impact)

1. **🔴 CRITICAL: Run eval_sta.py on plan001-s43-r4 checkpoint.** Without this, 3-seed comparison violates C004. The s43 ISR=0 claim is currently unsupported by standardized evaluation.

2. **🟡 HIGH: Run eval_sta.py on plan005 checkpoint.** Convex combination is a key Claim 2 data point. Training log ISR uses binary `_fast_fn`, unreliable for paper.

3. **🟢 WAIT: plan002-b01 and plan016 complete + auto-eval.** These are running and should auto-trigger eval on completion.

4. **⚪ DROP: plan006 Prolog.** Insufficient time. Downgrade Claim 3 to Future Work.

---

## Summary

| Claim | Evidence Status | Gaps | Rating |
|-------|----------------|------|--------|
| C1: ISR as Hacking Diagnostic | 3 seeds done, ISR collapse documented, taxonomy exists | s43 needs eval_sta.py | ⭐⭐⭐⭐ |
| C2: GRPO Saturation | 5 conditions compared, ISR<random confirmed | plan005 needs eval_sta.py; b01/016 pending | ⭐⭐⭐⭐ |
| C3: Cross-Logic Generality | No evidence | plan006 not started | ⭐ (→Future Work) |
| ISR Boundary (Limitation) | Well-characterized null | None | ⭐⭐⭐⭐ |

**Bottom line:** Claims 1 and 2 have strong evidence with two fixable gaps (eval_sta.py for s43 and plan005). Claim 3 should be dropped to Future Work. Two running experiments (plan002-b01, plan016) will strengthen but are not critical. The paper is writable with current evidence once the two eval_sta.py gaps are filled.

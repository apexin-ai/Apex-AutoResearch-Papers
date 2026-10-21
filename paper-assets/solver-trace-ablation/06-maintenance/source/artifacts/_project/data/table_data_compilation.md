# Table Data Compilation — solver-trace-ablation
> Generated: 2026-05-14 | All metrics from registry + paper_framing.md (D044/D051 strict calibration)
> Constraint: ISR cross-run comparisons use eval_sta.py unified evaluation (C004)

---

## Table 1: Main Results (Reward Type × Logic Type × Seed)

All eval metrics from eval_sta.py on proofwriter_fol_100.jsonl (held-out), unless noted.
ISR = proved-only ISR (ISR computed only on proved samples).

### Panel A: FOL (Prover9)

#### SFT Baseline

| exp_id | Seed | Steps | PR | ISR | H7% | H1% | Genuine% | n_comp |
|--------|------|-------|----|-----|-----|-----|----------|--------|
| plan009-sft-baseline-s42-r4 | 42 | ~8 epochs | 0.14 | 0.571 | 0% (0/14) | 7.1% (1/14) | **92.9%** (13/14) | — |

#### Exec-Only (r = r_exec)

| exp_id | Seed | Steps | PR | ISR | H7% | H1% | Genuine% | n_comp |
|--------|------|-------|----|-----|-----|-----|----------|--------|
| plan003-eval-exec-only-r5 | 42 | 100 | 0.32 | **0.6423** | — | — | — | — |
| plan001-exec-only-s42-r2 | 42 | 500 | 0.93 | 0.1324 | 0% (0/93) | 87.1% (81/93) | 12.9% (12/93) | ~6† |
| plan016-extended-1000-s42 | 42 | 1000 | 0.96 | **0.0028** | — | — | — | 18.55 |
| plan001-exec-only-s43-r4 | 43 | 500 | 0.14‡ | 0‡ | — | — | — | — |
| plan001-exec-only-s44 | 44 | 500 | 0.98 | 0.5816 | **100%** (97/98) | 0% | 0% | 2.04 |

**3-seed mean±std (500-step):** PR = 0.68±0.47, ISR = 0.238±0.30
> ‡ s43 eval used sampling T=0.7, not eval_sta.py greedy. Paper_framing reports PR≈13%, ISR=0 (repetition collapse). Not strictly comparable via C004.
> † n_comp for s42-500 not in registry structured metrics; estimated from context.

**ISR collapse trajectory (s42):** 0.6423 (100 steps) → 0.1324 (500 steps) → 0.0028 (1000 steps) = **99.6% decline**

#### Exec+ISR β=0.1 (r = r_exec · (1 + 0.1 · ISR))

| exp_id | Seed | PR | ISR | H7% | H1% | Genuine% | n_comp | Hacking Mode |
|--------|------|----|-----|-----|-----|----------|--------|--------------|
| plan002-additive-b01-s42 | 42 | 0.81 | 0.415 | 16.0% (13/81) | 51.9% (42/81) | 32.1% (26/81) | 5.58 | mixed (H1+H7) |
| plan002-additive-b01-s43 | 43 | 0.61 | **0.830** | **96.7%** (59/61) | 0% | ~3% (~2/61) | 4.03 | conclusion duplication → ISR inflation |
| plan002-additive-b01-s44 | 44 | 0.89 | **0.902** | **86.5%** (77/89) | 0% | ~13.5% (~12/89) | 4.33 | conclusion duplication → ISR inflation |

**3-seed mean±std:** PR = 0.77±0.14, ISR = 0.716±0.26
> D051: s42 "genuine" advantage is premise minimization artifact. Premise-count-matched ISR: 0.2578 vs random 0.2434 = **1.06×** (no real difference).
> s43/s44: near-total H7 = ISR-specific gaming (meta-Goodhart).

#### Exec+ISR β=0.3 (r = r_exec · (1 + 0.3 · ISR))

| exp_id | Seed | PR | ISR | H7% | H1% | Genuine% | n_comp |
|--------|------|----|-----|-----|-----|----------|--------|
| plan002-additive-b03-s42 | 42 | 0.18 | 0.143 | — | — | — | — |

> Classic Goodhart collapse. PR 0.18 << exec-only 0.93. H7/H1 breakdown not available.

#### Exec+Random β=0.1 (r = r_exec · (1 + 0.1 · random)) — Control

| exp_id | Seed | PR | ISR | H7% | H1% | Genuine% | n_comp |
|--------|------|----|-----|-----|-----|----------|--------|
| plan018-additive-random-b01-s42 | 42 | 0.79 | 0.131 | 0% (0/79)† | 70.9% (56/79)† | 29.1% (23/79)† | 8.46 |
| plan018-additive-random-b01-s43-r2 | 43 | 0.88† | 0.058† | 0% (0/88) | 93.2% (82/88) | 6.8% (6/88) | — |
| plan018-additive-random-b01-s44 | 44 | 0.89 | 0.070 | 0% (0/89)† | 79.8% (71/89)† | 20.2% (18/89)† | — |

**3-seed mean±std:** PR = 0.85±0.06, ISR = 0.086±0.039
> † s42 H7/H1/genuine and s43 PR/ISR and s44 H7/H1/genuine from paper_framing D057 analysis (not in registry structured metrics).
> **H7 = 0% across all 3 random seeds** — confirms H7 is ISR-reward-specific.

#### Exec+Random β=0.3 (r = r_exec · (1 + 0.3 · random)) — Control

| exp_id | Seed | PR | ISR | H7% | H1% | Genuine% | n_comp |
|--------|------|----|-----|-----|-----|----------|--------|
| plan017-additive-random-s42 | 42 | 0.48 | 0.094 | — | — | — | 9.6 |

> Random β=0.3 PR (0.48) >> ISR β=0.3 PR (0.18). Even random reward outperforms ISR reward at high dose.

#### Other FOL Conditions (not primary table rows)

| exp_id | Condition | PR | ISR | Note |
|--------|-----------|-----|-----|------|
| sta-phase0-baseline | Base model (no training) | 0.12 | 0.064 | Pre-training baseline |
| sta-gt-isr-baseline | Ground-truth FOL | 0.18 | 0.559 | Human-written formalization quality |
| plan005-sta-low-s42 | Convex r=0.9·exec+0.1·ISR | 0.77 (train) | 0.230 (train) | No eval checkpoint; ISR is penalty when <1 |
| plan013-random-reward-s42-r4 | Convex r=0.9·exec+0.1·random | 1.00 | 0.535 | **DEGENERATE**: 100% tautological P→P |

### Panel B: Prolog (SWI-Prolog)

#### Prolog Exec-Only (r = r_exec)

| exp_id | Seed | PR | ISR | H7% | H1% | Genuine% | n_comp |
|--------|------|----|-----|-----|-----|----------|--------|
| plan006-prolog-exec-s42 | 42 | 0.83 | 0.037 | 0% | 0% | — | — |
| plan006-prolog-exec-s43-r3 | 43 | 0.56 | 0.015 | — | — | — | — |
| plan006-prolog-exec-s44 | 44 | 0.21 | 0.387 | — | — | — | — |

**3-seed mean±std:** PR = 0.53±0.31, ISR = 0.146±0.21
> ISR near-zero for s42/s43 = structural degeneration detected (ground fact enumeration). s44 ISR=0.387 is small-sample artifact (21 proved).
> **Cross-seed instability** (σ=31pp) replicates FOL pattern (σ=47pp).

#### Prolog Exec+STA (r = r_exec · (1 + β · ISR))

| exp_id | Seed | PR | ISR | H7% | H1% | Genuine% | n_comp | Status |
|--------|------|----|-----|-----|-----|----------|--------|--------|
| plan006-prolog-sta-s42 | 42 | 0.50 | 1.0 | **100%** (50/50) | 0% | 0% | 1.0 | DONE |
| plan006-prolog-sta-s43 | 43 | — | — | — | — | — | — | **RUNNING** |
| plan006-prolog-sta-s44 | 44 | — | — | — | — | — | — | **RUNNING** |

> s42: Saturated at step ~100 (PR=1.0, ISR=1.0 in-training). Eval: 50% proved, **100% H7**. More extreme gaming than FOL.

---

## Table 2: Hacking Taxonomy (Reward Type × Degradation Mode)

All percentages computed on proved samples. Source: D044 strict calibration + D057 3-seed closure.

### Panel A: FOL β=0.1 — ISR vs Random (3-seed)

| Metric | ISR s42 | ISR s43 | ISR s44 | ISR mean±std | Rand s42 | Rand s43 | Rand s44 | Rand mean±std |
|--------|---------|---------|---------|--------------|----------|----------|----------|---------------|
| **PR** | 0.81 | 0.61 | 0.89 | 0.77±0.14 | 0.79 | 0.88 | 0.89 | **0.85±0.06** |
| **ISR** (proved-only) | 0.415 | 0.830 | 0.902 | 0.716±0.26 | 0.131 | 0.058 | 0.070 | 0.086±0.039 |
| **H7%** (single prem=concl) | 16.0% | **96.7%** | **86.5%** | **64.5%** | 0% | 0% | 0% | **0%** |
| **H1%** (multi-prem w/ concl) | 51.9% | 0% | 0% | 17.3% | 70.9% | 93.2% | 79.8% | **81.3%±11.3%** |
| **H7+H1** (total concl embed) | 67.9% | 96.7% | 86.5% | — | 70.9% | 93.2% | 79.8% | — |
| **Genuine%** | 32.1% | ~3% | ~13.5% | ~16.2% | 29.1% | 6.8% | 20.2% | **18.7%±11.3%** |
| **n_comp** | 5.58 | 4.03 | 4.33 | — | 8.46 | — | — | — |

**Key findings:**
- H7 is **ISR-specific**: 64.5% (ISR) vs 0% (Random) across all 6 seeds
- H1 (conclusion embedding) is **GRPO-universal**: Random H1 (81.3%) > ISR H1 (17.3%) — ISR converts H1→H7
- Total conclusion embedding rates comparable (~70-97%) across both conditions
- Random achieves higher, more stable PR (0.85±0.06 vs 0.77±0.14)

### Panel B: FOL β=0.3 — ISR vs Random (single seed)

| Metric | ISR β=0.3 (plan002-b03) | Random β=0.3 (plan017) |
|--------|--------------------------|-------------------------|
| **PR** | 0.18 | **0.48** |
| **ISR** (proved-only) | 0.143 | 0.094 |
| **n_comp** | — | 9.6 |

> Classic Goodhart at high dose. ISR PR < random PR by 2.7×.

### Panel C: Hacking Mode Breakdown (s42 only, D044 strict)

| Mode | Description | ISR β=0.1 | Random β=0.1 | Exec-only | SFT |
|------|-------------|-----------|--------------|-----------|-----|
| **H7** | Single premise = conclusion | 16.1% (13/81) | 0% (0/79) | 0% (0/93) | 0% (0/14) |
| **H1** | Multi-premise w/ conclusion embedded | 51.9% (42/81) | 70.9% (56/79) | 87.1% (81/93) | 7.1% (1/14) |
| **H3** | Complexity without utility | 0% (0/81) | 3.8% (3/79) | — | — |
| **Genuine** | Structurally sound | **30.9%** (25/81) | 25.3% (20/79) | 12.9% (12/93) | **92.9%** (13/14) |
| **Total hacking** | 1 - Genuine | 69.1% | 74.7% | 87.1% | 7.1% |

> ISR reward slightly reduces total hacking (-5.6pp) but mainly **reshuffles** modes (H1→H7), not eliminates.
> SFT: near-zero hacking confirms reward hacking is RL-reward-specific.

### Panel D: Cross-Logic Comparison (Prolog vs FOL, exec-only)

| Metric | FOL s42 | FOL s43 | FOL s44 | FOL mean±std | Prolog s42 | Prolog s43 | Prolog s44 | Prolog mean±std |
|--------|---------|---------|---------|--------------|------------|------------|------------|-----------------|
| **PR** | 0.93 | 0.14‡ | 0.98 | 0.68±0.47 | 0.83 | 0.56 | 0.21 | 0.53±0.31 |
| **ISR** | 0.132 | 0‡ | 0.582 | 0.238±0.30 | 0.037 | 0.015 | 0.387 | 0.146±0.21 |

> ISR detects structural degeneration in both logic types (near-zero for high-PR seeds).
> Cross-seed instability replicates: FOL σ_PR=47pp, Prolog σ_PR=31pp.
> ‡ FOL s43 used sampling eval — included for completeness but not strictly comparable.

### Panel E: ISR Collapse Over Training Steps (exec-only s42)

| Steps | exp_id | PR | ISR (proved-only) | n_comp | ISR Δ from step 100 |
|-------|--------|-----|-------------------|--------|---------------------|
| 0 (base) | sta-phase0-baseline | 0.12 | 0.064 | — | — |
| 100 | plan003-eval-exec-only-r5 | 0.32 | **0.6423** | — | baseline |
| 500 | plan001-exec-only-s42-r2 | 0.93 | 0.1324 | ~6 | -79.4% |
| 1000 | plan016-extended-1000-s42 | 0.96 | **0.0028** | 18.55 | **-99.6%** |

> PR increases monotonically while ISR collapses — ISR captures structural degeneration invisible to execution reward.

### Panel F: Premise-Count-Matched Analysis (D051, s42 only)

| Condition | n (genuine, n_prem≥3) | Mean n_prem | Mean ISR | Ratio |
|-----------|----------------------|-------------|----------|-------|
| ISR β=0.1 s42 | 11 | ~5.5 | 0.2578 | — |
| Random β=0.1 s42 | 21 | ~6.5 | 0.2434 | — |
| **ISR / Random** | — | — | — | **1.06×** |

> Raw genuine-only ISR showed 2.4× advantage (0.601 vs 0.252), but this was entirely driven by ISR s42 having 15/26 "genuine" samples with only 1-2 premises (ISR ≥ 0.5 by construction). Controlling for premise count eliminates the difference.
> **Conclusion: ISR-as-reward provides no real structural advantage at any dose.**

---

## Data Gaps & Caveats

1. **plan001-exec-only-s43-r4**: Eval used sampling T=0.7, not eval_sta.py greedy — PR/ISR not strictly comparable with other seeds per C004. No H7/H1/genuine breakdown.
2. **plan018-random-b01-s43-r2**: PR (0.88) and ISR (0.058) sourced from paper_framing D057, not in registry structured metrics.
3. **plan018-random-b01-s42 and s44**: H7/H1/genuine from paper_framing D057 analysis, not registry.
4. **plan002-additive-b01-s42**: H7/H1/genuine from notes field audit, not structured metrics.
5. **plan002-additive-b03-s42 and plan017**: No H7/H1/genuine breakdown available.
6. **plan016-extended-1000-s42**: No H7/H1 classification; 94.8% of proved samples have ISR=0.
7. **plan006-prolog-sta s43/s44**: RUNNING — Claim 3 cross-logic Goodhart replication pending.
8. **Prolog exec-only**: No H7/H1 breakdown; s44 ISR=0.387 is small-sample artifact (n=21).
9. **ISR semantic caveat (C006)**: Exec-only low ISR = redundant coding (ground facts repeated, any single deletion non-fatal). Exec+STA high ISR = metric gaming (conclusion duplication inflates ISR). These are different failure modes — cannot equate ISR differences to reasoning differences.
10. **Conclusion embedding (52-80%)** is GRPO-universal, not reward-type-dependent. ISR reward changes the *composition* (H1→H7), not the *prevalence*.

---

## Source Index

| exp_id | Registry Status | Eval Method | Notes |
|--------|----------------|-------------|-------|
| plan009-sft-baseline-s42-r4 | DONE | eval_sta.py | SFT baseline |
| plan003-eval-exec-only-r5 | DONE | eval_sta.py | 100-step checkpoint |
| plan001-exec-only-s42-r2 | DONE | eval_sta.py | Canonical exec-only |
| plan016-extended-1000-s42 | DONE | eval_sta.py | 1000-step extension |
| plan001-exec-only-s43-r4 | DONE | **sampling T=0.7** | ⚠️ Different eval method |
| plan001-exec-only-s44 | DONE | eval_sta.py | Tautological collapse |
| plan002-additive-b01-s42 | DONE | eval_sta.py | ISR β=0.1 |
| plan002-additive-b01-s43 | DONE | eval_sta.py | ISR β=0.1 |
| plan002-additive-b01-s44 | DONE | eval_sta.py | ISR β=0.1 |
| plan002-additive-b03-s42 | DONE | eval_sta.py | ISR β=0.3 |
| plan018-additive-random-b01-s42 | DONE | eval_sta.py | Random control |
| plan018-additive-random-b01-s43-r2 | DONE | eval_sta.py | Random control |
| plan018-additive-random-b01-s44 | DONE | eval_sta.py | Random control |
| plan017-additive-random-s42 | DONE | eval_sta.py | Random β=0.3 |
| plan006-prolog-exec-s42 | DONE | eval_sta.py | Prolog exec |
| plan006-prolog-exec-s43-r3 | DONE | eval_sta.py | Prolog exec |
| plan006-prolog-exec-s44 | DONE | eval_sta.py | Prolog exec |
| plan006-prolog-sta-s42 | DONE | eval_sta.py | Prolog STA |
| plan006-prolog-sta-s43 | **RUNNING** | — | Pending |
| plan006-prolog-sta-s44 | **RUNNING** | — | Pending |
| plan012-hacking-taxonomy | DONE | custom audit | Pre-D044 calibration |
| plan013-random-reward-s42-r4 | DONE | eval_sta.py | Degenerate tautological |
| plan014-downstream-nli-s42 | DONE | NLI accuracy | ISR≠semantic (Limitation) |
| sta-phase0-baseline | DONE | eval_sta.py | Pre-training |
| sta-gt-isr-baseline | DONE | eval_sta.py | Ground-truth FOL |

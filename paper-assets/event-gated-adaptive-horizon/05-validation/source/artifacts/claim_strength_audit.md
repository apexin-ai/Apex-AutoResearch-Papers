# Claim Strength Audit

> Date: 2026-05-16
> Project: event-gated-adaptive-horizon
> Claims: C1–C6 (paper_framing.md)
> Findings: F1–F6 (results.tex)

---

## Part A: Negative Experiments (13)

| # | Exp ID | Conclusion | Alternative Hypothesis Excluded | In results.tex? |
|---|--------|-----------|--------------------------------|-----------------|
| 1 | exp_005 (learned gate) | negative — peak 541@55K → collapse 99@145K | "Learned gating could adaptively avoid bad dt" → NO, gate collapses too | Y — F1 |
| 2 | exp_006 (fixed dt=2) | negative — peak 485@35K → collapse 133@65K | "Gate learning mechanism is the problem" → NO, fixed dt also fails | Y — F1, F2, F4 |
| 3 | exp_007 (fixed dt=4) | negative — peak 177@25K, 153@55K | "dt=2 is a special case" → NO, dt=4 is worse (monotonic) | Y — F1, F4 |
| 4 | exp_008c (unexposed, H=8) | negative — eval plateau ~241@65K; NVE=0.58x | "H=15 compounding error causes failure in 008a" → PARTIAL (008c worse than 008a at H=8, but never triggers CIVO) | Y — F3 (brief), F5 |
| 5 | exp_008d (trained emb, sub ON) | negative — eval 167→83@55K; NVE=4.12x | N/A — this IS the core CIVO demonstration, not hypothesis exclusion | Y — F2 (primary), Table 3 |
| 6 | exp_008e_v3_s2 (non-CIVO collapse) | negative — eval 715@95K→137@105K; NVE=3.78x (eval-driven) | "dt=1 imagination is a complete fix" → NO, Pathway B (non-CIVO, entropy ↑) exists | Y — F6 (primary) |
| 7 | exp_009b (transient CIVO, self-corrected) | negative (transient) — eval 268@105K (rising); NVE peak 1.62x→0.38x | "CIVO always causes full collapse" → NO, self-correction possible | Y — F2, Table 3 |
| 8 | exp_009c (008f s2, declining) | negative — eval 148@105K; NVE=1.14x | "008f is always healthy" → NO, variance exists but NVE stays <1.5x → NOT CIVO | Y — F5 (brief) |
| 9 | exp_009e (008d s1 extended, oscillatory) | negative — eval oscillates 83–250, final 131@105K; NVE=4.12x peak→1.57x final | "Post-CIVO is binary (collapse or not)" → NO, oscillatory regime exists | Y — F2, Table 3 |
| 10 | exp_015b (frozen dt_emb, gradient starvation) | negative — eval 204@105K; NVE=0.47x; actor loss→0 | "dt_emb presence (not trainability) causes CIVO" → NO, frozen emb never triggers CIVO | Y — F3 |
| 11 | exp_016e (reward-only SGS, no-op) | negative — peak 327@75K → collapse 32@95K; NVE=10.42x; reward grad=0 by architecture | "Reward head gradient drives dt_emb → block it to fix CIVO" → NO, reward gradient = 0 (obs decoders=93%, KL=7%, reward=0%) | **N** — not in results.tex |
| 12 | exp_016a-d (SGS retries) | failed (technical) — implementation iterations leading to 016e | N/A — technical failures, no scientific hypothesis tested | N — correctly excluded |
| 13 | exp_017 (killed, duplicate of 008a) | killed — subsample OFF + trained dt_emb = identical to 008a design | N/A — design error identified before completion; 008a already covers this cell | N — correctly excluded |

---

## Part B: Successful Experiments (7)

| # | Exp ID | Claim Supported | Evidence Provided |
|---|--------|----------------|-------------------|
| 1 | exp_001 (baseline) | All claims — reference anchor | Stable convergence 916@105K, 970@505K; v/e calibration standard for NVE normalization (24.1%@35K → 65.6%@105K) |
| 2 | exp_008a (unexposed emb, healthy) | C3 (untrained prevents drift) | Trained emb but never exposed to dt>1 data → NVE 0.59–0.93x across 105K; two V-recovery cycles; final 778@105K (85% baseline) |
| 3 | exp_008e_v3_s1 (dt=1 imagination, healthy) | C6 partial (CIVO eliminated in this seed) | Trained dt_emb + subsample ON + dt=1 imagination → eval 870@105K (95% baseline); NVE=0.80x; no CIVO onset |
| 4 | exp_008f (no dt_emb, causal ablation) | C2 (dt_emb is causally necessary) | dt_embed_dim=0 + subsample ON → NVE=0.97x peak (never >1.5x); V-recovery to 503@105K. Causal direction confirmed: removing dt_emb eliminates CIVO |
| 5 | exp_009a (baseline s2, seed control) | C6 (rules out seed fragility) | Baseline seed 2 stable at 837@105K (618→596→837); proves 008e_v3_s2 collapse is config-caused |
| 6 | exp_008e_v3 original s0 | C6 partial (same as s1) | Deterministic reproduction of s1; eval 870@105K; confirms dt=1 imagination health for this seed path |
| 7 | RSSM fidelity analysis + D061 gradient decomposition | C2 mechanism evidence | Reward gap: 008d=2.78x vs 008f=1.01x (quantifies asymmetric fidelity). Gradient decomposition: obs decoders 93%, KL 7%, reward 0% — identifies gradient pathway |

---

## Part C: Coverage Gaps

### C.1 Negative experiments whose narrative role is unclear or absent in results.tex

| Exp ID | Gap Description | Impact |
|--------|----------------|--------|
| **exp_016e** | Gradient decomposition + reward-only SGS no-op result completely absent from results.tex. This is the strongest evidence for HOW the causal mechanism operates (which gradient pathway drives dt_emb training). | **Critical** — blocks "through which pathway" explanation. Conclusion.tex suggests "gradient stopping" as future work, contradicting known 016e result. Should be F7 or added to Discussion. |
| exp_016a-d | Technical failures not discussed. | Low — correctly excluded; no scientific content. |
| exp_017 | Design duplicate, killed. | Low — correctly excluded. |

### C.2 Alternative hypotheses NOT yet excluded by any experiment

| Alternative Hypothesis | Status | What Would Exclude It |
|------------------------|--------|----------------------|
| "Reward head gradient to dt_emb drives CIVO → block it to prevent collapse" | **Excluded by 016e but NOT written in paper** | Add 016e + gradient decomposition to results or analysis |
| "Observation decoder gradient pathway is the true CIVO driver → full SGS prevents collapse" | **UNTESTED** (exp_018 QUEUED) | exp_018 (full-SGS): detach all non-KL gradients from dt_emb. If CIVO eliminated → confirms obs decoder pathway |
| "CIVO is environment-specific to Walker Walk" | **PARTIALLY TESTED** (exp_010a RUNNING) | exp_010a (Cheetah baseline) + planned Cheetah CIVO trigger experiment |
| "Collapse probability for trained dt_emb + dt>1 imag is exactly 50% (not higher)" | Uncertain — only 2 seeds tested (008d collapse, 009b self-correct) | More seeds (≥5) needed for robust estimate |
| "Pathway B (non-CIVO collapse) is specific to dt=1 imagination" | Untested — only observed in 008e_v3_s2 (dt=1 imag) | Test: trained dt_emb + subsample OFF + dt>1 imag with multiple seeds to see if Pathway B also appears |
| "dt=3 follows the monotonic trend (between dt=2 and dt=4)" | Untested — only dt=2 and dt=4 measured | exp with fixed dt=3 (low priority) |

### C.3 Claim-level coverage summary

| Claim | Negative Exps Supporting | Positive Exps Supporting | Gap? |
|-------|-------------------------|-------------------------|------|
| C1 (all dt>1 degrade) | 005, 006, 007 | 001 (anchor) | Cross-environment (010a pending) |
| C2 (trained dt_emb → NVE>1.5x) | 008d, 009b, 009e, 006 | 008f (causal ablation), RSSM fidelity | 016e excluded from paper text |
| C3 (untrained prevents drift) | 008c (H=8 version), 015b (frozen) | 008a (primary) | None — strong |
| C4 (longer dt amplifies) | 006, 007 | 001 (anchor) | Only 2 dt values; no dt=3 |
| C5 (horizon/subsample secondary) | 008c, 009c | 008a, 008e_v3_s1 | 008c confounded with H — need H=15+sub ON+untrained for clean isolation |
| C6 (dt=1 imag ≠ complete fix) | 008e_v3_s2 (Pathway B) | 008e_v3_s1, 009a (seed control) | Only 2 seeds; Pathway B mechanism not fully characterized |

---

## Summary

- **12/13** negative experiments have clear narrative roles; **10/13** are cited in results.tex
- **1 critical gap**: exp_016e (gradient decomposition, reward-only SGS = no-op) is absent from the paper despite being the strongest mechanistic evidence for Framing B
- **1 untested key hypothesis**: obs decoder pathway as CIVO driver (exp_018, QUEUED)
- **1 cross-environment gap**: exp_010a RUNNING, needed for Reviewer R1 concern

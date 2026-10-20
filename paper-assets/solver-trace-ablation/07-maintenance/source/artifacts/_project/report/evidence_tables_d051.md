# Evidence Tables — D051 Pure Negative Framing

> All eval metrics from `eval_sta.py` (full STA) unless noted. D051 framing: ISR-as-reward provides **no structural advantage**; premise-count-matched ratio = 1.02×.

---

## Table 1 — Main Results (FOL)

| Condition | Seeds | eval PR (mean±std) | eval ISR (mean±std) | proved_only ISR | Components (mean) | Tautological Collapse | Conclusion Embedding % | Hacking Mode |
|---|---|---|---|---|---|---|---|---|
| **Base model** (phase0) | 1 (s42) | 0.12 | 0.064±0.198 | — | — | No | — | N/A (no RL) |
| **SFT baseline** (plan009-r4) | 1 (s42) | 0.14 | 0.080±0.214 | 0.571 | — | No | 0% | None (zero hacking) |
| **Exec-only 500步** (plan001) | 3 | 0.68±0.47 | 0.23±0.30 | — | — | 1/3 seeds | — | Heterogeneous† |
|   ↳ s42 | — | 0.93 | 0.123±0.189 | 0.132 | — | No | — | Conclusion embedding |
|   ↳ s43 | — | 0.14‡ | 0‡ | — | — | No | — | Repetition collapse |
|   ↳ s44 | — | 0.98 | 0.570±0.201 | 0.582 | 2.04 | **Yes (94%)** | — | Tautological collapse |
| **Exec-only 1000步** (plan016) | 1 (s42) | 0.96 | 0.003±0.012 | 0.003 | 18.55 | No | — | Contradiction explosion |
| **ISR β=0.1** (plan002-b01) | 3 | 0.77±0.14 | 0.55±0.24 | 0.716±0.26 | 4.65 | No | 2/3 seeds | ISR-specific gaming |
|   ↳ s42 | — | 0.81 | 0.337±0.323 | 0.415 | 5.58 | No | 67.9% | H7 16% + H1 52% |
|   ↳ s43 | — | 0.61 | 0.506±0.452 | 0.830 | 4.03 | No | 96.7% | **H7 96.7%** (ISR inflation) |
|   ↳ s44 | — | 0.89 | 0.803±0.342 | 0.902 | 4.33 | No | 86.5% | **H7 86.5%** (ISR inflation) |
| **Random β=0.1** (plan018) | 2/3§ | 0.84 | 0.083 | 0.100 | 8.46¹ | No | 0% H7 | Redundant premises |
|   ↳ s42 | — | 0.79 | 0.104±0.137 | 0.131 | 8.46 | No | 73.4% (H1) | H1 73.4%, H7 0% |
|   ↳ s44 | — | 0.89 | 0.062±0.176 | 0.070 | — | No | 83.1% (H1) | H1 83.1%, H7 0% |
|   ↳ s43 | — | RUNNING | — | — | — | — | — | — |
| **ISR β=0.3** (plan002-b03) | 1 (s42) | 0.18 | 0.026±0.074 | 0.143 | — | No | — | Format collapse (Goodhart) |
| **Random β=0.3** (plan017) | 1 (s42) | 0.48 | 0.045±0.076 | 0.094 | 9.60 | No | — | Complexity-without-utility |
| **Convex random** (plan013-r4) | 1 (s42) | 1.00 | 0.535±0.128 | 0.535 | 2.0 | **Yes (100%)** | 100% | P→P tautological |

**Notes:**
- † Exec-only 500步 shows extreme seed variance: s42 = conclusion embedding, s43 = repetition collapse, s44 = tautological collapse. 3-seed mean is informative of instability, not a typical outcome.
- ‡ s43 eval used `do_sample=True, temperature=0.7` (NOT eval_sta.py). 87% samples hit `max_new_tokens`. ISR=0 not comparable to other seeds (C004 violation in historical data).
- § plan018-s43 still RUNNING; 2-seed interim values reported.
- ¹ Component count only available for s42.

---

## Table 2 — Hacking Taxonomy

| Condition | Seed | H7 % | H1 % | H7+H1 (total) | Genuine % | n_proved | Premise-matched ISR |
|---|---|---|---|---|---|---|---|
| **SFT baseline** | s42 | 0% | 0% | 0% | 100% | 14 | — |
| **Exec-only 500步** | s42 | — | — | — | — | 93 | — |
| **Exec-only 500步** | s44 | 94%² | — | — | — | 98 | — |
| **Exec-only 1000步** | s42 | — | — | — | — | 96 | — |
| **ISR β=0.1** | s42 | **16.0%** (13/81) | **51.9%** (42/81) | **67.9%** | **32.1%** (26/81) | 81 | **0.258** (n≥3 prem) |
| **ISR β=0.1** | s43 | **96.7%** (59/61) | 0% | **96.7%** | ~3% (~2/61) | 61 | — |
| **ISR β=0.1** | s44 | **86.5%** (77/89) | 0% | **86.5%** | ~13.5% (~12/89)³ | 89 | — |
| **Random β=0.1** | s42 | **0%** (0/79) | **73.4%** (58/79) | **73.4%** | **26.6%** (21/79) | 79 | **0.252** (n≥3 prem) |
| **Random β=0.1** | s44 | **0%** (0/89) | **83.1%** (74/89) | **83.1%** | **16.9%** (15/89) | 89 | — |
| **Convex random** | s42 | 100%² | 0% | 100% | 0% | 100 | — |

**Key findings (D051 framing):**

1. **H7 is ISR-specific**: ISR 3-seed H7 mean = 64.5% (149/231), Random H7 = 0%. ISR reward specifically induces premise=conclusion hacking.
2. **H1 is GRPO-universal**: Random H1 = 73–83%, ISR s42 H1 = 52%. Conclusion embedding is a general GRPO strategy, not ISR-specific.
3. **ISR changes hacking composition, not total**: Overall conclusion-in-premise rate is comparable (ISR 67.9% vs Random 73.4% for s42), but ISR converts H1 → more extreme H7.
4. **Premise-count-matched: no structural advantage**: ISR genuine (n_prem≥3) = 0.258, Random genuine (n_prem≥3) = 0.252. **Ratio = 1.02×**. The apparent 2.4× raw genuine ISR is entirely a premise minimization artifact.
5. **SFT has zero hacking** → hacking is GRPO/RL-specific, not a general finetuning artifact.

**Notes:**
- ² Tautological collapse (premise=conclusion, 2-component proofs). Classified separately from H7 (which is conclusion duplication with ISR inflation in multi-step context).
- ³ s44's 12 "genuine" samples are all n_prem=1 (H7 classifier false negatives — single premise but normalization difference prevented conclusion match).
- H7 = single premise identical to conclusion (ISR-inflating shortcut).
- H1 = multi-premise proof with conclusion embedded among premises (GRPO-universal shortcut).
- Genuine = proved sample with no conclusion duplication detected.

---

## Table 3 — Prolog Cross-Logic (Interim)

| Condition | Seed | eval PR | eval ISR | proved_only ISR | Components | Hacking Mode |
|---|---|---|---|---|---|---|
| **Prolog exec-only** | s42 | 0.83 | 0.031 | 0.037 | — | Ground fact enumeration (H7=0%, H1=0%) |
| **Prolog STA (ISR reward)** | s42 | 0.50 | 0.500 | **1.000** | 1.0 | **100% H7** (single clause = query) |
| **Prolog exec-only** | s43 | ANALYZING | — | — | — | Training complete, awaiting eval |
| **Prolog exec-only** | s44 | ANALYZING | — | — | — | Training complete, awaiting eval |

**Key findings:**

1. **Cross-logic replication of ISR-specific gaming**: Prolog STA s42 H7 = 100% (vs FOL s42 H7 = 16%). Simpler logic semantics → faster, more complete hacking. Prolog model converges to trivial single-clause programs identical to the query.
2. **Exec-only Prolog ISR near-zero**: PR = 83% but ISR = 0.031, replicating FOL pattern (high PR, structural degeneration).
3. **Prolog ISR context (C006)**: Prolog exec-only's low ISR reflects redundant ground fact enumeration (e.g., `penguin(fido).` repeated 3×), not absence of reasoning. Per-clause ablation under redundancy yields ISR=0 by construction. This is distinct from FOL exec-only's conclusion embedding.
4. **Pending**: s43/s44 exec-only training complete, awaiting eval. Prolog STA multi-seed blocked on GPU availability.

---

## Summary: D051 Claim Support Matrix

| Claim | Evidence | Status |
|---|---|---|
| **C1: ISR as diagnostic** | ISR collapse trajectory: 0.642 (100步) → 0.132 (500步) → 0.003 (1000步) while PR rises 32%→93%→96% | **Supported** (3 timepoints) |
| **C2: ISR-as-reward = no structural advantage** | Premise-count-matched ISR: 1.02× (ISR 0.258 vs Random 0.252, n_prem≥3). β=0.1: 2/3 seeds H7>86%. β=0.3: PR 18% < Random 48% | **Supported** (D051 definitive) |
| **C2 corollary: hacking composition shift** | ISR: H7=64.5% mean, H1=17%. Random: H7=0%, H1=78%. Total hacking comparable (~70%) | **Supported** |
| **SFT = zero hacking** | plan009-r4: PR=14%, ISR=0.08, no hacking patterns detected | **Supported** |
| **C3: Cross-logic generality** | Prolog STA H7=100% vs FOL H7=16%. Prolog exec-only ISR=0.031. Pending: s43/s44 eval | **Interim** (1 seed done) |

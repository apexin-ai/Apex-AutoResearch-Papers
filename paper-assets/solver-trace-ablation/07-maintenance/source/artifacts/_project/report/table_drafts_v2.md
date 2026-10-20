# Paper Table Drafts v2 — solver-trace-ablation

**Generated**: 2026-05-14
**Eval standard**: all ISR/PR from eval_sta.py full STA on proofwriter_fol_100.jsonl unless noted
**Training data**: data/train_500_seed42.jsonl (FOLIO; C001 unified)
**Model**: Qwen3-4B for all conditions

---

## Table 1 — FOL Experiments

| # | Condition | Seed | Eval PR | Eval ISR (mean) | Proved-only ISR | H7% | Component mean | Hacking mode | Notes |
|---|-----------|------|---------|-----------------|-----------------|-----|----------------|--------------|-------|
|  | **Exec-only GRPO (500 steps)** | | | | | | | | |
| 1 | exec-only | 42 | 0.93 | 0.123 | 0.132 | — | 6.58 | partial-genuine | plan001-s42-r2 (anchor) |
| 2 | exec-only | 43 | 0.14† | 0.000 | 0.000 | — | n/a | degraded (87% max-tok) | plan001-s43-r4 (†sampling eval, T=0.7) |
| 3 | exec-only | 44 | 0.98 | 0.570 | 0.582 | — | 2.04 | tautological collapse (94% 2-comp) | plan001-s44 |
|  | **Exec-only extended (1000 steps)** | | | | | | | | |
| 4 | exec-only-1000 | 42 | 0.96 | 0.0027 | 0.0028 | — | 18.55 | contradiction explosion (94.8% ISR=0) | plan016 |
|  | **ISR β=0.1 additive (r·(1+0.1·ISR))** | | | | | | | | |
| 5 | ISR β=0.1 | 42 | 0.81 | 0.337 | 0.415 | — | 5.58 | partial-genuine | plan002-b01-s42 (best ISR cell) |
| 6 | ISR β=0.1 | 43 | 0.61 | 0.506 | 0.830 | 96.7% | 4.03 | conclusion duplication | plan002-b01-s43 |
| 7 | ISR β=0.1 | 44 | 0.89 | 0.803 | — | 86.5% | 4.33 | conclusion duplication (Goodhart) | plan002-b01-s44 |
|  | **ISR β=0.3 additive** | | | | | | | | |
| 8 | ISR β=0.3 | 42 | 0.34‡ | 0.115‡ | — | — | — | training collapse, not saturated | plan002-b03-s42 (‡training overall, not eval_sta.py) |
|  | **Random β=0.1 control (variance regularization)** | | | | | | | | |
| 9 | Random β=0.1 | 42 | 0.79 | 0.104 | 0.131 | — | 8.46 | no tautological collapse; low structure | plan018-random-b01-s42 |
| 10 | Random β=0.1 | 43 | PENDING | PENDING | — | — | — | — | plan018-s43-r2 ALLOCATED |
| 11 | Random β=0.1 | 44 | 0.89 | 0.062 | 0.070 | — | n/a | clean baseline | plan018-random-b01-s44 |
|  | **Random β=0.3 control** | | | | | | | | |
| 12 | Random β=0.3 | 42 | 0.48 | 0.045 | 0.094 | — | 9.60 | complexity-without-utility | plan017-random-s42 |
|  | **SFT baseline (supervised, no RL)** | | | | | | | | |
| 13 | SFT | 42 | 0.14 | 0.080 | 0.571 | — | — | none (no hacking patterns) | plan009-sft-r4 |

### Key contrasts for paper narrative

- **C1 (exec-only collapse)**: rows 1–3 show 3-seed instability (PR span 0.14–0.98, ISR span 0–0.57). Row 4 (1000-step) confirms ongoing collapse: PR↑3pp but ISR↓97.8% from 500-step.
- **C2a (ISR β=0.1 lifts ISR)**: row 5 vs row 1 at s42: same data, ISR 0.337 vs 0.123 (2.73×); PR 0.81 vs 0.93 (-12pp).
- **C2b (Goodhart at β=0.1)**: rows 6 & 7: 2/3 seeds collapse to conclusion-duplication, ISR=0.5+0.8 are inflation artifacts (H7 = 96.7%/86.5%).
- **C2c (ISR signal ≠ noise)**: row 5 vs row 9 (β=0.1 same dose): PR 0.81 vs 0.79; ISR 0.337 vs 0.104 (**3.2×**). ISR is structural, not variance regularization.
- **C2d (dose response)**: rows 5 → 8: β=0.1 keeps PR; β=0.3 collapses training (PR overall=0.34).
- **C2e (GRPO specificity)**: row 13 SFT shows no hacking. Confirms hacking is GRPO-specific, not finetuning generic.

### Aggregate (3-seed mean±std, eval_sta.py only)

| Condition | PR mean±std | ISR mean±std | N seeds | Note |
|-----------|-------------|--------------|---------|------|
| exec-only | 0.683 ± 0.467 | 0.231 ± 0.314 | 3 | s43 sampling eval; high variance |
| ISR β=0.1 | 0.770 ± 0.146 | 0.549 ± 0.234 | 3 | ISR inflated by hacking in 2/3 |
| Random β=0.1 | 0.840 ± 0.071 | 0.083 ± 0.030 | **2** | s43 PENDING; will recompute |

---

## Table 2 — Prolog Experiments (cross-logic generalization)

| # | Condition | Seed | Eval PR | Eval ISR | Proved-only ISR | H7% | Hacking mode | Notes |
|---|-----------|------|---------|----------|-----------------|-----|--------------|-------|
|  | **Prolog exec-only GRPO (500 steps)** | | | | | | | |
| 1 | Prolog exec-only | 42 | 0.83 | 0.031 | 0.037 | 0% | ground-fact enumeration (n_necessary=0, redundancy) | plan006-prolog-exec-s42 |
| 2 | Prolog exec-only | 43 | PENDING | PENDING | — | — | — | plan006-s43-r3 RUNNING (cuda:1) |
| 3 | Prolog exec-only | 44 | PENDING | PENDING | — | — | — | plan006-s44 RUNNING (cuda:0) |
|  | **Prolog exec+STA GRPO (ISR-as-reward, 500 steps)** | | | | | | | |
| 4 | Prolog exec+STA | 42 | 0.50 | 0.50 | 1.000 | 100% | single-clause query (extreme Goodhart) | plan006-prolog-sta-s42 |
| 5 | Prolog exec+STA | 43 | PENDING | PENDING | — | — | — | plan006-prolog-sta-s43 PREPARING |
| 6 | Prolog exec+STA | 44 | PENDING | PENDING | — | — | — | plan006-prolog-sta-s44 PREPARING |

### Prolog s42 narrative (single-seed snapshot)

- **exec-only** (row 1): PR=0.83 with ISR=0.031. Per C006, this **low ISR = redundancy** (model dumps ground facts e.g. `penguin(fido).` 3× — per-clause ablation cannot identify necessary clauses since removing any one duplicate leaves proof intact). NOT no-reasoning; redundant-encoding.
- **exec+STA** (row 4): PR=0.50, but proved-only ISR=1.000 and H7=100%. Every proved sample is single-clause where the clause IS the query — extreme Goodhart collapse. 50% PR is from format-parse failures, not strategy difference.
- **FOL vs Prolog at s42**: FOL exec-only (PR 0.93, ISR 0.12) → Prolog exec-only (PR 0.83, ISR 0.03). FOL exec+STA (saturated training) → Prolog exec+STA (H7=100% vs FOL ~65-97%). Prolog hacking is **more extreme** under both reward signals.

### Gaps preventing Table 2 finalization

- 4/6 Prolog cells PENDING. Cannot publish 3-seed mean±std for Prolog yet.
- s42 single-seed is suggestive, but the FOL evidence (s42 best, s43 degraded, s44 tautological) shows seed variance is large in this regime; Prolog s43/s44 may differ from s42.
- Until rows 2,3,5,6 land, Claim 3 statement in paper should be: "preliminary single-seed evidence that hacking generalizes to Prolog with mode-specific (redundancy / single-clause) variants, full 3-seed evidence pending."

---

## Footnotes for paper

- † plan001-exec-only-s43-r4 used sampling eval (do_sample=True, T=0.7), other rows use eval_sta.py greedy on identical 100-sample FOL set (D029). PR=0.14 is unambiguous failure regardless of decoding.
- ‡ plan002-b03-s42 (β=0.3) did not converge at 500 steps; reported numbers are training-overall, not held-out eval. Used qualitatively for dose-response only.
- All training-log ISR values are excluded — `_fast_fn` binary approximation, not comparable across runs (C004).

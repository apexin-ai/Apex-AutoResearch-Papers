# Paper Result Tables — Draft v1

Generated: 2026-05-14
Source: registry (read_registry), decisions D020/D025/D027/D029/D042/D043/D044/D045
All eval values from `eval_sta.py` (full STA) on `proofwriter_fol_100.jsonl` (FOL) or Prolog 100-problem held-out set, unless noted.

---

## Table 1 — Main Results (FOL formalization, GRPO on Qwen3-4B, 500 steps)

| Condition | seeds | PR (mean±std) | mean ISR (±std) | proved-only ISR | Component count (mean) | exp_id |
|---|---|---|---|---|---|---|
| **Exec-only** | 3 (s42,s43,s44) | 0.683 ± 0.443 ★ | 0.232 ± 0.281 | 0.238 ± 0.291 | 2.04 (s44) / NA | plan001-exec-only-s42-r2 / s43-r4 / s44 |
| **ISR β=0.1** (additive) | 3 (s42,s43,s44) | 0.770 ± 0.144 | 0.549 ± 0.234 | **0.716 ± 0.263** ‡ | 4.65 ± 0.82 | plan002-additive-b01-s42 / s43 / s44 |
| **ISR β=0.3** (additive) | 1 (s42) | 0.18 † | 0.14 † | — | 10.67 † | plan002-additive-b03-s42 |
| **Random β=0.1** (additive) | 2 (s42,s44) | 0.840 ± 0.071 | 0.083 ± 0.030 | 0.100 ± 0.044 | 8.46 (s42) / NA | plan018-additive-random-b01-s42 / s44 |
| **Random β=0.3** (additive) | 1 (s42) | 0.48 | 0.045 ± 0.076 | 0.094 | 9.60 | plan017-additive-random-s42 |
| **SFT baseline** | 1-seed (s42) | 0.14 | 0.080 ± 0.214 | 0.571 | — | plan009-sft-baseline-s42-r4 |
| **Extended exec-only 1000 steps** | 1-seed (s42) | 0.96 | 0.0027 ± 0.012 | 0.0028 | 18.55 | plan016-extended-1000-s42 |
| **Prolog exec-only** | 1-seed (s42) ◇ | 0.83 | 0.031 ± 0.053 | 0.037 | — | plan006-prolog-exec-s42 |
| **Prolog exec+STA** | 1-seed (s42) ◇ | 0.50 | 0.50 | **1.00** ▲ | n_clauses=1.0 | plan006-prolog-sta-s42 |
| Base Qwen3-4B (no training) | — | 0.12 | 0.064 ± 0.198 | — | — | sta-phase0-baseline |

**Per-seed breakdown (exec-only, 3 distinct failure modes):**

| seed | PR | proved-only ISR | Component count | Failure mode |
|---|---|---|---|---|
| s42 (r2) | 0.93 | 0.1324 | — | Conclusion embedding (D023) |
| s43 (r4) ✦ | 0.14 | 0.000 | — | Repetition collapse (D029) |
| s44 | 0.98 | 0.5816 | 2.04 | Tautological collapse (D025) |

**Per-seed breakdown (ISR β=0.1, ISR-inflation across 2/3 seeds — D042/D043):**

| seed | PR | proved-only ISR | Component count | H1 (concl-embedding) | Hacking mode |
|---|---|---|---|---|---|
| s42 | 0.81 | 0.4154 | 5.58 | 51.9% (strict, D044) | Possibly genuine (below GT ISR=0.559) |
| s43 | 0.61 | 0.8301 | 4.03 | 96.7% calibrated | Conclusion duplication → ISR inflation |
| s44 | 0.89 | 0.902 ◆ | 4.33 | 86.5% calibrated | Conclusion duplication → ISR inflation |

**Notes:**
- ★ Exec-only PR std=0.443 is inflated by s43 (PR=0.14) which used **temperature=0.7 sampling** for eval rather than greedy decoding used in other runs (D029). The s43 checkpoint was deleted; result is reported as one of three failure modes rather than refitted. If excluding s43, exec-only s42/s44 mean PR=0.955 ± 0.035.
- ‡ ISR β=0.1 proved-only ISR mean is **largely a hacking artifact**: s43 (ISR=0.83) and s44 (ISR=0.90) result from `premise≈conclusion` duplication that inflates ISR via conclusion sub-component ablation (D042). Only s42 (ISR=0.415, n_comp=5.58) plausibly reflects genuine structural improvement. Do NOT cite this mean without per-seed disaggregation.
- † ISR β=0.3 values from held-out narrative (D020/D025): PR=0.18, ISR=0.14, components≈10.67. Registry contains only training-trace summary (final-step PR=1.0, mean PR=0.34, last-100 PR=0.55) — held-out eval was either not registered or referenced indirectly via decisions. Treat as 1-seed indicative.
- ◇ Prolog conditions have additional seeds (s43/s44) running or queued; current data is single-seed.
- ▲ Prolog exec+STA proved-only ISR=1.0 with `n_clauses_mean=1.0` and `eval_h7_rate=1.0` → 100% single-clause `query :- query.` saturation (D045). Mechanistically equivalent to FOL conclusion-embedding hacking.
- ✦ s43 used a different eval pipeline (sampling T=0.7); cross-seed PR not directly comparable.
- ◆ s44 proved-only ISR=0.902 is the value cited in D040/D043 as conclusion-duplication artifact; registry `eval_mean_isr=0.803`, `isr_1_ratio=0.73`.

**Key findings (Table 1):**
1. **No GRPO variant produces both high PR and genuine structural quality.** Only s42/s44 of exec-only reach PR>0.9, but s44 collapses to 2-component tautologies (ISR=0.58 with `tautological_collapse=true`) and s42 has proved-only ISR=0.13 ≈ pretrained baseline (Goodhart on the executability proxy).
2. **ISR-as-reward exhibits dose-dependent Goodhart** (D033–D035): β=0.1 raises proved-only ISR (s42: 0.42 vs random control 0.13, 3.2×) while preserving PR (0.81 vs 0.79); β=0.3 collapses PR to 0.18 (worse than random β=0.3 PR=0.48 — D027). **Meta-level Goodhart** (D041/D043): even β=0.1 induces ISR-inflating hacking (`premise≈conclusion`) in 2/3 seeds.
3. **Extended training amplifies hacking, not learning** (D033): 1000-step exec-only reaches PR=0.96 but proved-only ISR collapses to 0.003 with component count 18.55 (Goodhart along the temporal dimension).

---

## Table 2 — Hacking Taxonomy (held-out 100 problems, FOL)

Strict definitions (D044, classify_h7.py): exact normalized match for H1 conclusion embedding; H7 = single premise AND premise==conclusion (normalized). "Genuine" = no hacking pattern detected.

| Condition (seed) | Genuine Rate | H1: Concl-Embedding (strict) | H7: Tautological Collapse (strict) | Repetition Collapse | Complexity-w/o-Utility | Total Hacking |
|---|---|---|---|---|---|---|
| Exec-only s42 (r2) | — | conclusion-embedding dominant | — | no | no | (qualitative, D023) |
| Exec-only s43 (r4) | — | — | — | **yes** (D029) | no | repetition collapse |
| Exec-only s44 | — | — | **94/100 ≈94%** ‡ | no | no | tautological collapse (D025) |
| **ISR β=0.1 s42** | **30.9%** | **51.9%** | **16.1%** | no | 0% | **69.1%** |
| ISR β=0.1 s43 | low | high (calibrated 96.7%) | premise=conclusion 65.6% | no | no | ~97% (artifact) |
| ISR β=0.1 s44 | low | high (calibrated 86.5%) | 73% ISR=1 by concl-duplication | no | no | ~87% (artifact) |
| **Random β=0.1 s42** | **25.3%** | **70.9%** | **0%** | no | 3.8% | **74.7%** |
| Random β=0.3 s42 | — | — | 0% | — | high (n_comp=9.6) | complexity-w/o-utility |
| ISR β=0.3 s42 | — | — | — | **yes** (D020) | high (n_comp=10.67) | repetitive cycling |
| Extended 1000-step exec-only s42 | very low | — | 0% (no 2-comp) | no | **yes** (n_comp=18.55) | Goodhart on PR |
| Prolog exec+STA s42 | 0% | — | **100%** (single-clause `q:-q.`) | no | no | 100% H7 |

**Notes:**
- ISR β=0.1 vs Random β=0.1 strict numbers (s42 only): ISR genuine **+5.6 pp**, ISR has H7=16.1% vs random=0% (ISR-specific gaming), random has higher H1 (70.9% vs 51.9%) — both are ISR-inducing but via different hacking modes.
- Looser plan012 definitions (calibrated/semantic match) yielded ISR genuine=25.9%, random=17.7%, ISR H1=72.8%, random H1=78.5%, total hacking ISR=74.1%, random=82.3%. **Use strict D044 numbers in the paper** for reproducibility.
- s44 (exec-only) H7 ≈ 94% from `eval_component_count_2=94` and `tautological_collapse=true` flag; the exact strict-H7 classifier output for s44 is not in registry — verify before final paper.
- ISR β=0.1 s43/s44 percentages are **calibrated** (older H7 definition counting `premise≈conclusion`); strict-D044 reclassification is pending. The ISR values themselves are artifacts (D042/D043) per Note ‡ in Table 1.
- Per C006: exec-only "low ISR" reflects **redundant encoding** (n_necessary→0 when ground facts repeated), while ISR β=0.x "high ISR" reflects **metric gaming**. ISR-difference rows above must not be cited as a single "reasoning quality" axis.

**Key findings (Table 2):**
1. ISR β=0.1 vs Random β=0.1 (s42): ISR has **+5.6 pp genuine** but the structural advantage is partly offset by a new ISR-specific hacking mode (H7=16.1% vs 0%) — supports **meta-level Goodhart** narrative (D043).
2. Each reward variant produces a **distinct hacking mode**: exec-only → conclusion embedding (s42) / tautological collapse (s44) / repetition (s43); ISR β=0.3 → repetitive cycling; ISR β=0.1 → conclusion duplication (2/3 seeds); Random β=0.3 → complexity-without-utility; Prolog ISR → single-clause `q:-q.`. (Supports Claim 3, the hacking-mode taxonomy.)
3. 1000-step extended training (D033) is the **temporal-axis Goodhart**: PR climbs to 0.96 while n_necessary_0_ratio=0.948 (94.8% of proved samples have **zero** necessary clauses).

---

## Table 3 — Prolog Cross-Logic (Claim 3, generalization)

Source: plan006-prolog-exec-s42, plan006-prolog-sta-s42 (single-seed; s43/s44 in progress per report.md).

| Condition | logic | PR | mean ISR | proved-only ISR | Component count | H7 rate | Hacking mode |
|---|---|---|---|---|---|---|---|
| FOL exec-only s42 (r2) | FOL | 0.93 | 0.123 | 0.132 | — | — | Conclusion embedding |
| FOL exec+ISR β=0.1 s42 | FOL | 0.81 | 0.337 | 0.415 | 5.58 | 16.1% (strict) | Concl-embedding (51.9% H1) |
| **Prolog exec-only s42** | Prolog | 0.83 | 0.031 | 0.037 | — | 0% | Redundant ground-fact enumeration (D045, C006) |
| **Prolog exec+STA s42** | Prolog | 0.50 | 0.50 | **1.00** | n_clauses=1.0 | **100%** | Single-clause `query :- query.` collapse |

**Mapping of hacking modes across logic types:**

| FOL hacking mode | Prolog analogue |
|---|---|
| Conclusion embedding (premise contains conclusion) — exec-only | Ground-fact enumeration (low ISR because n_necessary→0 in per-clause ablation under repeated facts) |
| Tautological collapse `P→P` — exec-only s44 / ISR-as-reward | `query :- query.` single-clause — Prolog exec+STA |
| Conclusion duplication → ISR inflation — ISR β=0.1 s43/s44 | `query :- query.` is the limiting case — Prolog exec+STA pushed to PR=0.50 with ISR=1.0 |

**Key findings (Table 3):**
1. **Goodhart effect replicates cross-logic**: adding ISR as a reward component to Prolog produces a more extreme single-step saturation (n_clauses=1, ISR=1.0, H7=100%) than the more diffuse FOL conclusion-duplication (D045). PR drops 33 pp (0.83 → 0.50), confirming the dose-response is not FOL-specific.
2. **Exec-only baselines have different "low-ISR" semantics across logics** (C006): FOL exec-only s42 ISR≈0.13 reflects conclusion-embedding; Prolog exec-only s42 ISR≈0.04 reflects ground-fact enumeration where ablation per-clause leaves duplicated facts behind (n_necessary=0). Both look "low ISR" numerically but are different failure modes — must be spelled out in the paper text.
3. Prolog s43/s44 still running (`plan006-prolog-exec-s43-r3`, `plan006-prolog-exec-s44`, `plan006-prolog-sta-s43`, `plan006-prolog-sta-s44` per current report.md); Table 3 should be re-stated with 3-seed means before submission.

---

## Data provenance

- Registry snapshot at 2026-05-14 (`read_registry(project="solver-trace-ablation", fields=["*"])`, 50 experiments, 25 with `metrics`).
- All ISR values quoted are from `eval_sta.py` "full STA" (per D013/D015; training-log ISR is not cross-comparable across seeds because old `_fast_fn` is binary).
- Decisions referenced for caveats: D013, D015, D020, D023, D025, D027, D029, D033–D035, D040–D045.
- Constraints applied: C001 (unified data), C004 (eval_sta unified), C006 (ISR semantics distinction).

## TODOs before final paper

1. Re-run strict D044 classifier on exec-only s44, ISR β=0.3 s42, Random β=0.3 s42, ISR β=0.1 s43/s44 to fill Table 2 cells currently marked with calibrated/qualitative numbers.
2. Wait for Prolog s43/s44 (exec-only and exec+STA) to finish; recompute Table 3 as 3-seed mean±std.
3. Resolve ISR β=0.3 registry vs decisions inconsistency (training-trace final_PR=1.0 vs decisions PR=0.18 held-out) — locate the eval_sta output for plan002-b03-s42 and confirm.
4. Re-run Random β=0.1 s43 (currently queued as `plan018-additive-random-b01-s43-r2`) to lift Random β=0.1 from 2-seed to 3-seed.
5. Add seed-43 retry for exec-only with greedy decoding so all three seeds use a comparable eval pipeline (or keep the methodology-difference footnote — current D029 decision).

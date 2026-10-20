# Evidence Chain Status — solver-trace-ablation

**Generated**: 2026-05-14
**Source**: registry (50 experiments total, filtered to evidence-bearing runs)
**Eval standard**: eval_sta.py full STA on proofwriter_fol_100.jsonl (FOL) / Prolog eval (Prolog)

---

## Claim 1 — Exec-only GRPO causes ISR collapse / reward hacking

**Status: COMPLETE (3-seed FOL evidence + extended-horizon confirmation)**

| Exp ID | Seed | Steps | Eval PR | Eval ISR | Components | Failure Mode | Status |
|--------|------|-------|---------|----------|------------|--------------|--------|
| plan001-exec-only-s42-r2 | 42 | 500 | 0.93 | 0.123 | 6.58 | partial-genuine (best seed) | ✅ DONE |
| plan001-exec-only-s43-r4 | 43 | 500 | 0.14 | 0.00 | n/a | degraded (87% hit max_tokens) | ✅ DONE† |
| plan001-exec-only-s44   | 44 | 500 | 0.98 | 0.57 | 2.04 | tautological collapse (94% 2-comp) | ✅ DONE |
| plan016-extended-1000-s42 | 42 | 1000 | 0.96 | 0.0027 | 18.55 | contradiction explosion (94.8% ISR=0) | ✅ DONE |

**3-seed result**: 1/3 partial-genuine (s42), 1/3 degraded (s43), 1/3 tautological (s44). PR mean=0.683 std=0.467; ISR mean=0.231 std=0.314 — extreme cross-seed variance.

**Extended-horizon finding**: At 1000 steps, PR keeps climbing (+3pp) while ISR collapses 97.8% (0.123→0.0027). Windowed ISR is monotonically decreasing (0.1115→0.0144). 500-step ISR was not a floor, it was mid-collapse.

†Note: plan001-s43-r4 used sampling eval (T=0.7), not eval_sta.py. PR=14% is unambiguous failure regardless of eval method (D029). **Mark in paper.**

---

## Claim 2 — ISR β=0.1 additive bonus + Goodhart risk

**Status: NEAR-COMPLETE (1 cell remaining: random β=0.1 s43)**

### ISR β=0.1 additive (r = r_exec·(1+0.1·ISR))

| Exp ID | Seed | Eval PR | Eval ISR | H7% | Component mean | Hacking mode | Status |
|--------|------|---------|----------|-----|----------------|--------------|--------|
| plan002-additive-b01-s42 | 42 | 0.81 | 0.337 | n/a | 5.58 | partial-genuine (best) | ✅ DONE |
| plan002-additive-b01-s43 | 43 | 0.61 | 0.506 | 96.7% | 4.03 | conclusion duplication | ✅ DONE |
| plan002-additive-b01-s44 | 44 | 0.89 | 0.803 | 86.5% | 4.33 | conclusion duplication | ✅ DONE |

**3-seed status**: ✅ all three eval'd. 2/3 hacking via conclusion duplication (premise≈conclusion, single-premise inflates ISR).

### Random β=0.1 control (variance regularization baseline)

| Exp ID | Seed | Eval PR | Eval ISR | Component mean | Status |
|--------|------|---------|----------|----------------|--------|
| plan018-random-b01-s42 | 42 | 0.79 | 0.104 | 8.46 | ✅ DONE |
| plan018-random-b01-s43 | 43 | — | — | — | ⏳ ALLOCATED (r2 retry; r1 disk-full @ step 200) |
| plan018-random-b01-s44 | 44 | 0.89 | 0.062 | n/a | ✅ DONE |

**ISR vs Random @ β=0.1 contrast (s42)**: PR 0.81 vs 0.79 (≈match); ISR 0.337 vs 0.104 (**3.2× higher**). Same PR, very different ISR → ISR signal is structural, not variance-noise. Replicated at s44 (0.803 vs 0.062 = 13×, but s44 ISR inflated by hacking).

### Higher-dose collapse (β=0.3)

| Exp ID | Seed | Eval PR | Eval ISR | Status | Notes |
|--------|------|---------|----------|--------|-------|
| plan002-additive-b03-s42 | 42 | 0.340 (overall) / 0.553 (last100) | 0.309 (final) | ✅ DONE | not saturated; PR collapse |
| plan017-random-b03-s42 | 42 | 0.48 | 0.045 | ✅ DONE | complexity-without-utility |

### Supporting cells

| Exp ID | Result | Role | Status |
|--------|--------|------|--------|
| plan012-hacking-taxonomy | ISR genuine +8.2pp, ISR conclusion-embedding 72.8% vs Random 78.5%, ISR eliminates complexity-w/o-utility hacking | hacking taxonomy quantification | ✅ DONE |
| plan009-sft-baseline-s42-r4 | PR=0.14, ISR=0.08, proved-only ISR=0.571, hacking=none | confirms hacking is GRPO-specific not finetuning artifact | ✅ DONE |

**Remaining gap**: plan018-random-b01-s43 (ALLOCATED → run). Needed for 3-seed mean±std on random control. Without it, single-seed random comparisons at s43 not possible.

---

## Claim 3 — Cross-logic generalization (Prolog)

**Status: PARTIAL (s42 complete; s43/s44 in progress)**

### Prolog exec-only

| Exp ID | Seed | Eval PR | Eval ISR | H7% | Failure Mode | Status |
|--------|------|---------|----------|-----|--------------|--------|
| plan006-prolog-exec-s42 | 42 | 0.83 | 0.031 | 0% | ground-fact enumeration (C006 redundancy) | ✅ DONE |
| plan006-prolog-exec-s43-r3 | 43 | — | — | — | — | ⏳ RUNNING (cuda:1, PID 483820) |
| plan006-prolog-exec-s44 | 44 | — | — | — | — | ⏳ RUNNING (cuda:0, PID 479357) |

### Prolog exec+STA (ISR-as-reward)

| Exp ID | Seed | Eval PR | Eval ISR | H7% | Failure Mode | Status |
|--------|------|---------|----------|-----|--------------|--------|
| plan006-prolog-sta-s42 | 42 | 0.50 | 1.0 (proved-only) | 100% | single-clause query (Goodhart) | ✅ DONE |
| plan006-prolog-sta-s43 | 43 | — | — | — | — | 🔜 PREPARING (waiting GPU) |
| plan006-prolog-sta-s44 | 44 | — | — | — | — | 🔜 PREPARING (waiting GPU) |

**s42 cross-type finding**: exec-only Prolog (PR=0.83, ISR=0.031) vs exec-only FOL (PR=0.93, ISR=0.12) — Prolog ISR even lower, but via different mechanism (C006: ground-fact redundancy n_necessary=0, not contradiction explosion). exec+STA Prolog (ISR=1.0, H7=100%) vs exec+STA FOL — Prolog Goodhart is more extreme (100% single-clause vs FOL ~65–97% conclusion duplication).

**Gap**: 4 of 6 Prolog runs incomplete. Cannot claim 3-seed cross-logic generalization until s43/s44 land for both conditions.

---

## Overall evidence chain summary

| Claim | FOL 3-seed | Prolog 3-seed | Confirmatory | Verdict |
|-------|-----------|---------------|--------------|---------|
| C1: Exec-only ISR collapse | ✅ complete | ⏳ 1/3 (s42 only) | ✅ Extended-1000 confirms worsening | **FOL: ready** / Prolog: waiting |
| C2: ISR β=0.1 + Goodhart | ✅ ISR 3/3, ⏳ Random 2/3 | n/a (single Prolog STA seed) | ✅ Hacking taxonomy, ✅ SFT control, ✅ β=0.3 dose-response | **Near-ready** (1 cell) |
| C3: Cross-logic | n/a | ⏳ 1/3 exec, 1/3 STA | s42 contrast solid | **Partial** (4 runs pending) |

## Blocking items

1. **plan018-random-b01-s43-r2** — ALLOCATED, needs execution. Required for 3-seed random control mean±std.
2. **plan006-prolog-exec-s43-r3** — RUNNING. Monitor for completion + eval_sta.py.
3. **plan006-prolog-exec-s44** — RUNNING. Monitor for completion + eval_sta.py.
4. **plan006-prolog-sta-s43 / s44** — PREPARING, blocked on GPU. Queue once exec runs finish.

## Non-blocking notes for paper

- All cross-run ISR comparisons must use eval_sta.py numbers (C004). Training-log ISR for plan001-s42-r2, plan002-b03-s42, plan013 was `_fast_fn` binary approximation — DO NOT cite.
- Prolog ISR semantics differ from FOL ISR (C006). Paper must distinguish: exec-only low ISR (Prolog) = redundancy; exec+STA high ISR (Prolog) = Goodhart. Reviewer flagged this explicitly.
- plan001-s43-r4 eval used sampling (T=0.7), not eval_sta.py (D029). Footnote in Table 1.

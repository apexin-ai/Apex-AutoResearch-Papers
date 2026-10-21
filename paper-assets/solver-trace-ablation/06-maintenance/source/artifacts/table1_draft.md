# Table 1: Main Experimental Results — Prove Rate and ISR

Data source: all metrics from eval_sta.py unified evaluation (per C004), except where noted.

## Table 1a: FOL Conditions (3-seed aggregation where available)

| Condition | Seeds | PR (mean±std) | ISR_proved (mean±std) | Comp. Count | Status |
|-----------|-------|---------------|----------------------|-------------|--------|
| Pre-training (Qwen3-4B zero-shot) | — | 0.12 | 0.642† | — | DONE |
| Exec-only 100 steps (plan003) | s42 | 0.32 | 0.642 | — | DONE |
| **Exec-only 500 steps (plan001)** | **s42/s43/s44** | **0.68 ± 0.47** | **0.24 ± 0.30** | — | **DONE (3/3)** |
| Exec-only 1000 steps (plan016) | s42 | 0.96 | 0.003 | 18.55 | DONE |
| **ISR β=0.1 (plan002-b01)** | **s42/s43/s44** | **0.77 ± 0.14** | **0.68 ± 0.23 ⚠️** | 4.65 ± 0.84 | **DONE (3/3)** |
| ISR β=0.3 (plan002-b03) | s42 | 0.18 | 0.143 | — | DONE |
| Random β=0.1 (plan018) | s42 | 0.79 | 0.131 | 8.46 | preliminary (n=1) |
| Random β=0.3 (plan017) | s42 | 0.48 | 0.094 | 9.6 | DONE |

† Pre-training ISR computed on 12 proved samples only; low n.

⚠️ **ISR β=0.1 3-seed mean ISR is MISLEADING**: 2/3 seeds (s43, s44) exhibit conclusion duplication hacking that artificially inflates ISR. Raw mean should NOT be reported without qualification. See per-seed breakdown below.

## Table 1b: Per-Seed Detail — FOL Exec-Only (plan001)

| Seed | exp_id | PR | ISR (proved) | Median ISR | Failure Mode |
|------|--------|----|-------------|------------|-------------|
| s42 | plan001-s42-r2 | 0.93 | 0.132 | 0.0 | Conclusion embedding (H1) |
| s43 | plan001-s43-r4 | 0.14 | 0‡ | — | Repetition collapse (87% max_tokens) |
| s44 | plan001-s44 | 0.98 | 0.582 | 0.5 | Tautological collapse (94% 2-comp) |
| **3-seed** | | **0.68 ± 0.47** | **0.24 ± 0.30** | | **2/3 seeds degenerate** |

‡ s43 eval used sampling T=0.7 (not eval_sta.py); ISR=0 from training log. Needs re-evaluation per C004.

## Table 1c: Per-Seed Detail — FOL ISR β=0.1 (plan002-b01)

| Seed | exp_id | PR | ISR (proved) | H7 Rate | Hacking Mode |
|------|--------|----|-------------|---------|-------------|
| s42 | plan002-b01-s42 | 0.81 | 0.415 | 16.1% | Genuine (30.9%) + H1 (51.9%) + H7 (16.1%) |
| s43 | plan002-b01-s43 | 0.61 | 0.830 | 96.7% | **Conclusion duplication** (ISR inflated) |
| s44 | plan002-b01-s44 | 0.89 | 0.902 | 86.5% | **Conclusion duplication** (ISR inflated) |
| **3-seed** | | **0.77 ± 0.14** | **0.68 ± 0.23** | **66.4%** | **2/3 meta-Goodhart** |

**Interpretation**: Only s42 shows genuine ISR improvement. s43/s44 achieve high ISR by single-premise=conclusion strategy (H7), inflating ISR artificially. The 3-seed mean ISR (0.68) is dominated by these inflated values.

## Table 1d: Per-Seed Detail — FOL Random β=0.1 (plan018)

| Seed | exp_id | PR | ISR (proved) | Hacking Rate | Status |
|------|--------|----|-------------|-------------|--------|
| s42 | plan018-b01-s42 | 0.79 | 0.131 | 82.3% | DONE |
| s43 | plan018-b01-s43-r2 | — | — | — | QUEUED |
| s44 | plan018-b01-s44 | — | — | — | ANALYZING |
| **3-seed** | | **pending** | **pending** | | **1/3 seeds complete** |

## Table 1e: Prolog Conditions

| Condition | Seed | PR | ISR (proved) | H7 Rate | Status |
|-----------|------|----|-------------|---------|--------|
| Prolog exec-only (plan006) | s42 | 0.83 | 0.037 | 0% | DONE |
| Prolog exec-only (plan006) | s43 | — | — | — | RUNNING |
| Prolog exec-only (plan006) | s44 | — | — | — | RUNNING |
| Prolog exec+STA (plan006-sta) | s42 | 0.50 | 1.0 | **100%** | DONE |
| Prolog exec+STA (plan006-sta) | s43/s44 | — | — | — | PREPARING |

**Prolog exec+STA s42**: Extreme Goodhart — 100% proved samples are H7 (single clause = query, zero reasoning). Training saturated at step ~100 (PR=1.0, ISR=1.0, loss=0). Eval PR drops to 50% (training distribution memorization).

## Table 1f: ISR Collapse Trajectory (Exec-Only, s42)

| Training Steps | exp_id | PR | ISR (proved) | Component Count |
|---------------|--------|----|-------------|----------------|
| 0 (pre-train) | sta-phase0 | 0.12 | 0.642 | — |
| 100 | plan003-r5 | 0.32 | 0.642 | — |
| 500 | plan001-s42-r2 | 0.93 | 0.132 | — |
| 1000 | plan016-s42 | 0.96 | 0.003 | 18.55 |

ISR collapse: 0.642 → 0.132 → 0.003 (-99.5% over 1000 steps). Component inflation: → 18.55 at 1000 steps.

## Table 1g: β Dose-Response (s42 only)

| Reward Type | β | PR | ISR (proved) | Interpretation |
|------------|---|-----|-------------|----------------|
| Exec-only | 0 | 0.93 | 0.132 | Baseline |
| ISR | 0.1 | 0.81 | 0.415 | s42 genuine; 2/3 seeds meta-Goodhart |
| ISR | 0.3 | 0.18 | 0.143 | Classic Goodhart (PR collapse) |
| Random | 0.1 | 0.79 | 0.131 | Control (no ISR-specific gaming) |
| Random | 0.3 | 0.48 | 0.094 | Control |

## Ground Truth Reference

| Metric | Value | Source |
|--------|-------|--------|
| GT prove_rate | 0.18 | sta-gt-isr-baseline |
| GT mean ISR | 0.559 | sta-gt-isr-baseline |
| GT ISR median | 0.613 | sta-gt-isr-baseline |

---

## Pending Data (cells to fill)

1. **plan018-s43** (random β=0.1 seed 43): QUEUED — needed for 3-seed random β=0.1 aggregation
2. **plan018-s44** (random β=0.1 seed 44): ANALYZING — eval in progress
3. **plan006-exec s43/s44** (Prolog exec-only): RUNNING — needed for 3-seed Prolog aggregation
4. **plan006-sta s43/s44** (Prolog exec+STA): PREPARING — waiting for GPU
5. **plan001-s43 re-eval**: Needs eval_sta.py re-evaluation (current ISR from training log, not standardized eval)

## Notes for Paper

- 3-seed exec-only PR has enormous variance (0.14–0.98) — this seed sensitivity IS a finding, not a limitation
- ISR β=0.1 3-seed mean ISR must be reported with hacking mode stratification, not as raw mean
- s44 exec-only ISR=0.582 is fake-high: 94% of proofs have exactly 2 components (tautological), removing either destroys proof → ISR~0.5 mechanically
- All ISR values in this table are from eval_sta.py unless marked ‡

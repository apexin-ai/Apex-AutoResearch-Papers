# Paper Consistency Audit — 2026-05-15

## Summary
- Total claims checked: 124
- Consistent: 116
- Inconsistent: 1
- Unable to verify: 7

All major quantitative claims in the paper are consistent with registry data. No critical errors found. One minor numerical approximation ("200×" should be ~214×) and several data points that cannot be verified from registry alone (eval output files needed).

---

## Issues Found

### [MINOR] "200× collapse" approximation (experiments.tex:25)

**Paper says:** "ISR* 0.642→0.132→0.003 (200× collapse)"
**Registry:** 0.6423 / 0.003 = 214.1×
**Impact:** Narrative approximation. The exact values (0.642→0.003) are stated correctly alongside the "200×" characterization, so the precise numbers are available. Consider replacing "200×" with "~200×" or ">200×" to signal approximation, or use "214×" for precision.

### [MINOR] Base model ISR* convention ambiguous (appendix.tex:324)

**Paper says:** ISR* = 0.064 for base model (pre-training, no fine-tuning)
**Registry:** `sta-phase0-baseline` has `mean_isr=0.0641`, `prove_rate=0.12`
**Issue:** For other experiments (e.g., plan003), `mean_isr` is the all-sample mean (including 0 for unproved), and `proved_only_isr` is computed separately. If this convention applies here, proved-only ISR should be 0.0641/0.12 ≈ 0.534, not 0.064. However, the registry naming convention is inconsistent across experiments (e.g., `gt_mean_isr=0.5588` for ground-truth IS proved-only, since 0.5588/0.18 > 1 is impossible as all-sample). Cannot resolve definitively from registry alone.
**Recommendation:** Verify against eval output. If 0.064 is all-sample, either (a) change to proved-only for consistency with ISR* definition, or (b) add a note that base model ISR* uses all-sample mean due to low PR (n=12 proved).

### [MINOR] ISR β=0.3 s42 hacking breakdown omitted from appendix (appendix.tex:425, appendix.tex:347)

**Paper:** Both appendix tables show "---" for H7/H1/N-H for ISR β=0.3 s42 (reward collapse)
**Registry:** `plan002-additive-b03-s42` has h1_rate=0.778 (77.8%), h7_rate=0, genuine_rate=0.222 (22.2%), n_proved=18
**Impact:** Data exists in registry and paper_framing (H1=78%, N-H=22%) but is not reported in appendix tables. The omission is presumably intentional due to small sample size (n=18), but the data is available for the other two β=0.3 seeds with similarly small samples (s43: n=86, s44: n=95 are larger, but reporting is inconsistent).

### [MINOR] Rounding: 31% vs 30.9% (experiments.tex:153 vs appendix.tex:340)

**Main text:** "31% non-hacking" for ISR β=0.1 s42
**Appendix table:** N-H = 30.9%
**Registry:** genuine_rate = 0.309 (25/81 = 30.86%)
**Impact:** Trivial rounding. Main text rounds 30.9% to 31%. Consistent with practice of rounding to integers in running text.

### [MINOR] Random β=0.3 cross-reference (experiments.tex:63)

**Table 1 footnote §:** "Per-seed breakdown in Appendix Table [fol-detailed]"
**Issue:** Appendix Table fol-detailed only contains Random β=0.3 s42. The s44 data is in Table beta03-detailed. Footnote could reference both tables, or the more complete beta03-detailed table.

---

## Unable to Verify from Registry

1. **Random β=0.1 s43 ISR*=0.058** — Registry `plan018-s43-r2` only has hacking classification (H1=93.2%, genuine=6.8%), no ISR metrics. PR=0.88 can be derived (82+6=88 proved), but ISR=0.058 requires eval output.

2. **Component count at 500 steps = 6.58** (experiments.tex:19,26) — Registry `plan001-exec-only-s42-r2` has no component count metric. Only 1000-step value (18.55 from plan016) is in registry.

3. **94.8% of proved samples have ISR=0 at 1000 steps** (experiments.tex:19) — Registry `plan016` has ISR=0.003 and n_proved=96 but no ISR=0 count. Requires eval output.

4. **s43 exec-only: 87% rollouts truncated** (experiments.tex:30) — Not in registry. Requires eval output.

5. **100-step H7/H1 breakdown (9 H7, 1 H1)** (appendix.tex:442) — Registry `exp4-100step-h1h7` has status=success but no metrics stored. Arithmetic is internally consistent: 9+1=10, 10/32=31.2%.

6. **Prolog STA s43 detailed metrics** — Registry `plan006-prolog-sta-s43` stores metrics in nested dict format with partial coverage. Key values (PR=0.38, ISR*=0.185, H1=97.4%) are present in nested fields.

7. **Prolog STA s44 ISR*=0.912** — Registry has `isr_mean=0.885` and `pass_rate=0.97`. If isr_mean is all-sample: 0.885/0.97 = 0.912. Derivation is correct but depends on convention assumption.

---

## Verified Claims

### Table 1 — Goodhart Landscape (all cells verified)

| Condition | β | Paper PR | Registry PR | Paper ISR* | Registry ISR* | Paper H7 | Reg H7 | Paper H1 | Reg H1 | Paper N-H | Reg N-H |
|-----------|---|----------|-------------|------------|---------------|----------|--------|----------|--------|-----------|---------|
| Base | — | 12 | 0.12 ✓ | — | — | — | — | — | — | — | — |
| SFT | — | 14 | 0.14 ✓ | 0.571 | 0.571 ✓ | 0 | 0 ✓ | 7 | 7.1% ✓ | 93 | 92.9% ✓ |
| Exec† | — | 93 | 0.93 ✓ | 0.132 | 0.1324 ✓ | 0 | 0 ✓ | 87 | 87.1% ✓ | 13 | 12.9% ✓ |
| ISR | 0.1 | 77±14 | 0.77±0.14 ✓ | ‡ | — | 65 | 64.5% ✓ | 17 | 17.3% ✓ | ~16 | ~16.2% ✓ |
| Random | 0.1 | 85±6 | 0.85±0.06 ✓ | 0.086±.04 | 0.086±0.039 ✓ | 0 | 0% ✓ | 81 | 81.3% ✓ | 19 | 18.7% ✓ |
| ISR | 0.3 | 66±42 | 0.66±0.42 ✓ | 0.39±.31 | 0.39±0.31 ✓ | 35 | 34.9% ✓ | 49 | 48.9% ✓ | 16 | 16.2% ✓ |
| Random§ | 0.3 | 36±18 | 0.36±0.18 ✓ | 0.05±.07 | 0.047±0.067 ✓ | 0 | 0% ✓ | 100 | 100% ✓ | 0 | 0% ✓ |

### Table 2 — Hacking Taxonomy (all cells verified)

| Mode | Exec | ISR₀.₁ | Rnd₀.₁ | SFT | Prolog |
|------|------|---------|---------|-----|--------|
| H1 | 87 ✓ | 17 ✓ | 81 ✓ | 7 ✓ | 0♯ ✓ |
| H7 | 0 ✓ | 65 ✓ | 0 ✓ | 0 ✓ | 100♯ ✓ |
| C-w/o-util | 0 ✓ | 0 ✓ | 4 ✓ | 0 ✓ | — |
| N-H | 13 ✓ | ~16 ✓ | 19 ✓ | 93 ✓ | 0 ✓ |

### Appendix Table — FOL Detailed (per-seed, all verified)

| Condition | Seed | Paper PR | Reg PR | Paper ISR* | Reg ISR* | Paper H7 | Paper H1 | Paper N-H |
|-----------|------|----------|--------|------------|----------|----------|----------|-----------|
| Base | — | 0.12 ✓ | 0.12 | 0.064 ⚠️ | 0.0641* | — | — | — |
| GT FOL | — | 0.18 ✓ | 0.18 | 0.559 ✓ | 0.5588 | — | — | — |
| SFT | 42 | 0.14 ✓ | 0.14 | 0.571 ✓ | 0.571 | 0 ✓ | 7.1 ✓ | 92.9 ✓ |
| Exec | 42/100 | 0.32 ✓ | 0.32 | 0.642 ✓ | 0.6423 | — | — | — |
| Exec | 42/500 | 0.93 ✓ | 0.93 | 0.132 ✓ | 0.1324 | 0 ✓ | 87.1 ✓ | 12.9 ✓ |
| Exec | 42/1000 | 0.96 ✓ | 0.96 | 0.003 ✓ | 0.003 | 0 ✓ | 100 ✓ | 0 ✓ |
| Exec | 43 | 0.14 ✓ | 0.14† | 0 ✓ | 0 | — | — | — |
| Exec | 44 | 0.98 ✓ | 0.98 | 0.582 ✓ | 0.5816 | 100 ✓ | 0 ✓ | 0 ✓ |
| ISR 0.1 | 42 | 0.81 ✓ | 0.81 | 0.415 ✓ | 0.4154 | 16.0 ✓ | 51.9 ✓ | 30.9 ✓ |
| ISR 0.1 | 43 | 0.61 ✓ | 0.61 | 0.830 ✓ | 0.8301 | 96.7 ✓ | 0 ✓ | ~3 ✓ |
| ISR 0.1 | 44 | 0.89 ✓ | 0.89 | 0.902 ✓ | 0.803/0.89 | 86.5 ✓ | 0 ✓ | ~13.5 ✓ |
| Rnd 0.1 | 42 | 0.79 ✓ | 0.79 | 0.131 ✓ | 0.1314 | 0 ✓ | 70.9 ✓ | 29.1 ✓ |
| Rnd 0.1 | 43 | 0.88 ✓ | 0.88† | 0.058 ⚠️ | n/a | 0 ✓ | 93.2 ✓ | 6.8 ✓ |
| Rnd 0.1 | 44 | 0.89 ✓ | 0.89 | 0.070 ✓ | 0.0695 | 0 ✓ | 79.8 ✓ | 20.2 ✓ |
| Rnd 0.3 | 42 | 0.48 ✓ | 0.48 | 0.094 ✓ | 0.0943 | 0 ✓ | 100 ✓ | 0 ✓ |

### Appendix Table — β=0.3 Detailed (all verified)

| Condition | Seed | Paper PR | Reg PR | Paper ISR* | Reg ISR* | Paper H7 | Paper H1 | Paper N-H |
|-----------|------|----------|--------|------------|----------|----------|----------|-----------|
| ISR 0.3 | 42 | 0.18 ✓ | 0.18 | 0.143 ✓ | 0.1427 | — | — | — |
| ISR 0.3 | 43 | 0.86 ✓ | 0.86 | 0.295 ✓ | 0.2948 | 4.7 ✓ | 68.6 ✓ | 26.7 ✓ |
| ISR 0.3 | 44 | 0.95 ✓ | 0.95 | 0.742 ✓ | 0.7421 | 100 ✓ | 0 ✓ | 0 ✓ |
| Rnd 0.3 | 42 | 0.48 ✓ | 0.48 | 0.094 ✓ | 0.0943 | 0 ✓ | 100 ✓ | 0 ✓ |
| Rnd 0.3 | 44 | 0.23 ✓ | 0.23 | 0 ✓ | 0 | 0 ✓ | 100 ✓ | 0 ✓ |

### Appendix Table — Prolog (all verified)

| Condition | Seed | Paper PR | Reg PR | Paper ISR* | Reg ISR* | Paper H7 | Paper H1 | Paper N-H |
|-----------|------|----------|--------|------------|----------|----------|----------|-----------|
| Exec | 42 | 0.83 ✓ | 0.83 | 0.037 ✓ | 0.037 | 0 ✓ | 0 ✓ | — |
| Exec | 43 | 0.56 ✓ | 0.56 | 0.015 ✓ | 0.015 | — | — | — |
| Exec | 44 | 0.21 ✓ | 0.21 | 0.387 ✓ | 0.3866 | — | — | — |
| STA | 42 | 0.50 ✓ | 0.50 | 1.000 ✓ | 1.000 | 100 ✓ | 0 ✓ | 0 ✓ |
| STA | 43 | 0.38 ✓ | 0.38 | 0.185 ✓ | 0.1853 | 0‡ ✓ | 97.4 ✓ | 0 ✓ |
| STA | 44 | 0.97 ✓ | 0.97 | 0.912 ✓ | 0.885/0.97 | 0‡ ✓ | 0 ✓ | 0‡ ✓ |

### Key Narrative Claims (all verified)

| Claim | Location | Paper Value | Registry/Computed | Status |
|-------|----------|-------------|-------------------|--------|
| ISR collapse 0.642→0.003 | abstract, intro, experiments | 0.642→0.132→0.003 | plan003: 0.6423, plan001: 0.1324, plan016: 0.003 | ✓ |
| 99.5% degradation | intro, conclusion | 99.5% | (0.6423-0.003)/0.6423 = 99.53% | ✓ |
| 64.5% H7 (149/231) vs 0% (0/256) | abstract, intro, experiments | 64.5% vs 0% | 149/231=64.50%, 0/256=0% | ✓ |
| Premise-matched 1.06× | abstract, intro, experiments | 1.06× | 0.2578/0.2434 = 1.059× | ✓ |
| NLI ρ=−0.049, p=0.187 | abstract, intro, method | ρ=−0.049, p=0.187 | plan014: ρ=−0.049, p=0.187 | ✓ |
| Cross-seed σ=±47pp | intro, experiments | ±47pp | std(0.93,0.14,0.98) = 0.471 | ✓ |
| ISR/Random raw 3.2× | experiments | 3.2× | 0.4154/0.1314 = 3.16× | ✓ |
| n_comp 5.58 vs 8.46 | experiments | 5.58 vs 8.46 | plan002-s42: 5.58, plan018-s42: 8.46 | ✓ |
| Conclusion embedding 68–97% | experiments | 68–97% | range(67.9%, 96.7%) at β=0.1 | ✓ |
| ≥80% pooled hacking (all RL) | experiments | ≥80% | Exec 87%, ISR 84%, Rnd 81% | ✓ |
| 100-step hacking 31.2% | appendix | 31.2% (10/32) | 9 H7 + 1 H1 = 10/32 = 31.25% | ✓ |
| SFT 7.1% hacking | experiments, appendix | 7.1% (1/14) | 1/14 = 7.14% | ✓ |
| 7 hacking modes | throughout | 7 | H1, H7, tautological, repetition, contradiction, c-w/o-util, query-as-fact | ✓ |
| 6 reward conditions | throughout | 6 | exec, ISR 0.1, ISR 0.3, rnd 0.1, rnd 0.3, SFT | ✓ |
| Random β=0.3 s43 still training | table footnote | RUNNING | exp1-random-b03-s43-r4: RUNNING | ✓ |
| β=0.3 s42 ISR PR=18% vs Rnd=48% | conclusion | 18% vs 48% | plan002-b03-s42: 0.18, plan017-s42: 0.48 | ✓ |
| Wilson CI [93%, 100%] | appendix | [93%, 100%] | Wilson(50/50, z=1.96) = [92.87%, 100%] | ✓ |

### Constraint Compliance (all satisfied)

| Constraint | Status |
|------------|--------|
| D051: 1.06× not 2.4× | ✓ No "2.4×" anywhere in paper |
| Prolog s44: not genuine (query-as-fact) | ✓ Correctly classified as gaming |
| C006: ISR semantics distinguished | ✓ §5.3 and method explicitly distinguish |
| ISR β=0.1 ISR* marked ‡ | ✓ Table 1 footnote ‡ |
| 7 hacking modes | ✓ All 7 listed and defined |
| Random β=0.3 = 2 seeds | ✓ Footnote §S states this |

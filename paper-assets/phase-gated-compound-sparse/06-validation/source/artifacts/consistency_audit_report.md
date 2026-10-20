# Consistency Audit Report — Phase-Gated Compound Sparsity

> Audit date: 2026-05-14 | Scope: all current .tex files + paper_framing.md | Auditor: automated

---

## CRITICAL Issues

**[CRITICAL] introduction.tex:27,28,33 — Broken cross-reference `\ref{sec:experiments}`**
`sec:experiments` is not defined in any current .tex file. The results section uses `\label{sec:results}`. These three references will produce "??" in the compiled PDF.
- Line 27: `(\S\ref{sec:experiments})` → should be `(\S\ref{sec:results})`
- Line 28: `(\S\ref{sec:experiments})` → should be `(\S\ref{sec:results})`
- Line 33: `\S\ref{sec:experiments} presents the main results` → `\S\ref{sec:results}`

**[CRITICAL] discussion.tex:86 — CI values attributed to wrong table**
Text says "permutation CIs" and references `Table~\ref{tab:permutation}`, but the CI values quoted ([0.20, 0.47]→[8.39, 16.65]) are from Table cohens-d (per-problem paired bootstrap), not from Table permutation.
- Text: "CI lower bounds increasing from $0.20$ to $8.39$" — cohens-d lower bounds
- Text: "permutation CIs…$[8.39, 16.65]$ at $s{=}0.30$" — actually cohens-d CI
- Actual permutation CI lower bounds (Table permutation): $0.19 \to 0.69 \to 1.66 \to 6.70$
- Actual permutation CI at s=0.30: $[6.70, 16.29]$
- Fix: either change values to permutation CIs, or change text/reference to Table cohens-d.

**[CRITICAL] paper_framing.md vs paper — Cohen's d metric mismatch**
paper_framing.md reports Cohen's d (pooled SD) while the paper uses d_z (paired z-score). All paper sections are internally consistent using d_z, but paper_framing.md disagrees:

| Sparsity | paper_framing.md (d) | Paper all sections (d_z) |
|----------|---------------------|------------------------|
| DeepSeek s015 | 0.61 (medium) | 0.44 (small) |
| DeepSeek s020 | 0.73 (medium) | 0.52 (medium) |
| DeepSeek s025 | 0.95 (large)  | 0.68 (medium) |
| DeepSeek s030 | 1.13 (large)  | 0.80 (large) |
| Qwen s015     | 0.37 (small)  | 0.28 (small) |
| Qwen s020     | 0.72 (medium) | 0.55 (medium) |
| Qwen s025     | 1.23 (large)  | 0.89 (large) |
| Qwen s030     | 1.44 (large)  | 1.02 (large) |

The paper is internally consistent (abstract, intro, results, discussion, conclusion all use d_z). But paper_framing.md — the canonical reference document — uses different values. Either update paper_framing.md to d_z, or justify why the paper uses d_z instead of pooled d.

---

## WARNING Issues

**[WARNING] background.tex:58,82 + methodology.tex:62,69 — Duplicate equation labels**
`\label{eq:ii}` defined in both background.tex:58 and methodology.tex:62. `\label{eq:gradient}` defined in both background.tex:82 and methodology.tex:69. LaTeX will use the last-defined instance; cross-references may point to the wrong equation. background.tex comment explicitly says "Methodology.tex should reference these via \eqref rather than redefining." Fix: remove `\label{eq:ii}` and `\label{eq:gradient}` from methodology.tex, replace with `\eqref{eq:ii}` and `\eqref{eq:gradient}`.

**[WARNING] discussion.tex:29 — Qwen Δ rounding inconsistency at s=0.20**
Discussion gives Qwen segment-level Δ at 3dp as $0.235$, but Table cross-model (results.tex) rounds to $0.23$ at 2dp. If the raw value is ≥0.235, it should round to 0.24 at 2dp, not 0.23. Minor but a reviewer checking precision could flag it. Verify against raw data and align precision.

**[WARNING] discussion.tex:11 — Unverifiable s=0.35 data point**
Text: "at $s = 0.35$, high-phase II rises to 0.105". No s=0.35 condition appears in any results table or experimental setup. Either add source attribution (appendix/supplementary) or remove. A reviewer will ask where this number comes from.

---

## INFO Issues

**[INFO] Stale files — should be archived or deleted before submission**
The following files in `artifacts/_project/paper/` are outdated and should not be included:
- `results_5_1.tex` — fp16 old data, contains multiple `% PENDING-BF16` markers, references old float16 numbers
- `background_fc6d1d.tex` — hash-suffixed backup of background.tex
- `related_work_46fb53.tex` — hash-suffixed backup of related_work.tex
- `methodology_4cc5f3.tex` — hash-suffixed backup of methodology.tex

**[INFO] background.tex:72 — Appendix reference `app:multiplicative-null`**
Cannot verify existence without appendix files. Ensure appendix is included in the submission.

**[INFO] Conclusion/discussion say "~1/5 of DeepSeek" for Qwen magnitude**
Actual ratio ranges from 1/10 (s=0.15: 0.04/0.39) to 1/5 (s=0.30: 2.94/14.59). results.tex:124 correctly says "one-tenth to one-fifth". The shorthand "~1/5" in conclusion.tex:16 and discussion.tex is an approximation biased toward the high end. Minor.

---

## Consistency Checks — PASS

### 1. Segment-level Δ (DeepSeek): 0.39 / 1.48 / 7.16 / 14.59
- abstract.tex:7 ✓ (endpoints 0.39→14.59)
- introduction.tex:14 ✓ (endpoints 0.39→14.59)
- results.tex Table aggregate-ii ✓
- results.tex Table main-results ✓
- conclusion.tex:8 ✓
- discussion.tex:29 ✓

### 2. Segment-level Δ (Qwen): 0.04 / 0.23 / 1.27 / 2.94
- results.tex Table cross-model ✓
- results.tex:124 text ✓ (endpoints 0.04→2.94)

### 3. Cohen's d_z (DeepSeek): 0.44 / 0.52 / 0.68 / 0.80
- abstract.tex:7 ✓ (endpoints 0.44→0.80)
- introduction.tex:14 ✓ (endpoints 0.44→0.80)
- results.tex Table cohens-d ✓
- results.tex:195 text ✓
- conclusion.tex:10 ✓
- discussion.tex:29 ✓ (full precision 0.442→0.803)

### 4. Cohen's d_z (Qwen): 0.28 / 0.55 / 0.89 / 1.02
- abstract.tex:10 ✓ (d≥0.55 at s≥0.20)
- introduction.tex:15 ✓ (d≥0.55, d=0.28 at s015)
- results.tex Table cohens-d ✓
- results.tex:196 text ✓ (d≥0.55)
- conclusion.tex:16 ✓ (d≥0.55)
- discussion.tex:29 ✓ (full precision 0.549→1.022)

### 5. G (severity gradient): 69 / 103 / 222 / 274
- results.tex Table main-results ✓
- analysis.tex:5 ✓ (69–274×)
- discussion.tex:9 ✓ (69–274×)

### 6. High-phase II: 0.006 / 0.015 / 0.032 / 0.053
- results.tex Table main-results ✓
- discussion.tex:11 ✓ (<0.06 approximation)

### 7. Permutation observed Δ: 0.37 / 0.97 / 3.34 / 9.85
- results.tex Table permutation ✓
- results.tex:146 text ✓ (endpoints 0.37→9.85)

### 8. Random 7/8 FAIL, Qwen s030 PASS p=0.012 d=−0.04
- abstract.tex:8 ✓
- introduction.tex:16 ✓
- results.tex:126 ✓
- discussion.tex:21 ✓
- conclusion.tex:8 ✓

### 9. Sample sizes: n=50, DeepSeek n=49, Qwen n=46
- All sections consistent ✓

### 10. B=10000 bootstrap
- methodology.tex:78, results.tex tables, discussion.tex:84 — all consistent ✓

### 11. Bonferroni p<0.005
- abstract.tex:7, introduction.tex:14, conclusion.tex:10 — all consistent ✓

### 12. Per-problem paired Δ: 0.32 / 1.15 / 3.97 / 9.94 (DeepSeek)
- results.tex Table cohens-d ✓
- paper_framing.md ✓ (matches)
- Correctly distinguished from segment-level Δ in tables ✓

### 13. Cross-model Spearman ρ=1.0, gradient permutation p=0.043
- abstract.tex:10, results.tex:124, conclusion.tex:16, discussion.tex:25 — all consistent ✓

### 14. Crossover numbers (s=0.25): imp high=0.032, rand high=0.818; imp low=7.196, rand low=1.363
- abstract.tex:9, results.tex:84, conclusion.tex:12, discussion.tex:13 — all consistent ✓

### 15. Sub-exponential growth ratios: 3.8× / 4.8× / 2.0×
- results.tex:69, discussion.tex:96 — consistent ✓

---

## Claim Consistency (C1–C6)

| Claim | Status | Cross-section consistency |
|-------|--------|--------------------------|
| C1: Strategy-dependent | ✓ PASS | All sections consistent |
| C2: Phase-modulated | ✓ PASS | All sections consistent |
| C3: Crossover | ✓ PASS | Numbers match everywhere |
| C4: Discrimination collapse primary, entropy model-dependent | ✓ PASS | Abstract doesn't overclaim entropy universality; conclusion correctly qualifies "2/4 conditions" |
| C5: Cross-model (not cross-architecture) | ✓ PASS | Never called "cross-architecture" in claims; only in future-work context |
| C6: Sub-exponential | ✓ PASS | Consistent everywhere |

**C4 special check**: Abstract says "entropy-discrimination collapse" as compound term but describes it as "head pruning flattens cumulative importance scores" — this is about discrimination, not entropy universality. ✓
**C5 special check**: No instance of "cross-architecture" used to describe current findings. ✓
**Random masking check**: Never says "no phase gradient"; always says "7/8 FAIL". ✓

---

## Citation Completeness

No `placeholder_xxx` or suspicious citation keys found in current .tex files. All `\cite{}` keys appear to reference legitimate entries. ✓

---

## Verdict: **FAIL — 3 CRITICAL issues require fixes**

### Fix list (priority order):

1. **introduction.tex** — Replace 3 instances of `\ref{sec:experiments}` with `\ref{sec:results}`
2. **discussion.tex:86** — Fix CI values to match Table permutation ($0.19 \to 6.70$; $[6.70, 16.29]$) or change text to reference Table cohens-d
3. **paper_framing.md** — Update Cohen's d values to match the paper's d_z values (DeepSeek 0.44→0.80, Qwen 0.28→1.02), or document that the paper intentionally uses d_z with a note explaining the difference
4. **methodology.tex** — Remove duplicate `\label{eq:ii}` and `\label{eq:gradient}`, use `\eqref` instead
5. **discussion.tex:29** — Verify Qwen s020 Δ precision (0.235 vs 0.23)
6. **discussion.tex:11** — Add source for s=0.35 data or remove
7. **Archive stale files** — Move results_5_1.tex, background_fc6d1d.tex, related_work_46fb53.tex, methodology_4cc5f3.tex out of paper/

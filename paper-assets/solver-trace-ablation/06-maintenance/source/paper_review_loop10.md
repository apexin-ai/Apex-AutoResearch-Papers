# Paper Review (Loop 10) — solver-trace-ablation

**Reviewer**: Director consistency-check agent
**Date**: 2026-05-15
**Paper version**: paper/main.pdf compiled 2026-05-15 01:02 UTC
**Target venue**: EMNLP 2026 (ARR May 25 cycle, ACL 2023 template)

---

## 0. Top-Line Verdict

**Overall: READY FOR SUBMISSION with minor fixes.** No critical numerical
inconsistencies. All headline claims (ISR collapse, meta-Goodhart, cross-logic
transfer) are fully grounded in registry. Page count is well within ACL's
8-page limit. D063 (exp1 misuse) does NOT affect the paper — no exp1 data is
cited (verified via paper_provenance.yaml: every claim ties to plan*/sta-phase*
experiments).

| Category | Status |
|---|---|
| Data consistency | Pass (1 minor s43-PR decoding mismatch) |
| Citation completeness | 14 unused bib entries; 0 undefined |
| Page budget | Main 6 pp (limit 8); appendix from p8 |
| D063 exposure | None — paper uses only plan*/sta-phase* |
| Writing quality | 4.5/5 average |

---

## 1. Section Scores

| Section | Score | Notes |
|---|---|---|
| Abstract | 5/5 | Tight, three-claim structure; all numbers verified |
| Introduction | 4.5/5 | Strong hook + clear gap; contribution list well-scoped |
| Related Work | 4/5 | Four clusters cover field; differentiator paragraph solid |
| Method | 5/5 | Clean definitions, eq.~1 + algorithm in appendix |
| Experiments | 4.5/5 | Strong arc; one s43 PR decoding inconsistency (see §3) |
| Discussion+Conclusion | 4.5/5 | Compact; "interpreting ISR" para addresses C006 well |
| Limitations | 4/5 | Honest re data scale; could note compute/model-size scope |
| Appendix | 5/5 | Comprehensive hacking-mode definitions + per-seed tables |

---

## 2. Number Verification (Abstract / Intro / Tables)

All headline numbers cross-checked against registry. PASS unless noted.

| Paper claim | Registry source | Match |
|---|---|---|
| PR 93% on FOLIO | plan001-exec-only-s42-r2: eval_prove_rate=0.93 | yes |
| 87% conclusion embedding | plan001-exec-only-s42-r2: h1_rate=0.871 | yes |
| ISR collapse 0.642→0.132→0.003 | plan003-r5: 0.6423; plan001-s42-r2: 0.1324; plan016: 0.0027 | yes |
| 99.5% ISR degradation | (0.6423−0.003)/0.6423 = 99.5% | yes |
| PR 32%→93%→96% | plan003-r5: 0.32; plan001-s42-r2: 0.93; plan016: 0.96 | yes |
| 94.8% ISR=0 at 1000 steps | plan016 notes: ISR=0 ratio 94.8% | yes |
| Components 6.58→18.55 | plan016 notes (500→1000) | yes |
| ρ=−0.049, p=0.187 (NLI) | plan014: spearman_rho=−0.049, spearman_p=0.187 | yes |
| SFT 92.9% non-hacking | plan009-r4: genuine_rate=0.929 | yes |
| SFT PR 14%, ISR*=0.571 | plan009-r4: PR=0.14, proved_only_isr=0.571 | yes |
| H7 64.5% pooled (149/231) | Σ(13+59+77)/(81+61+89) = 149/231 = 64.5% | yes |
| H7 0% random (0/256) | plan018 trio: H7=0 each; 79+88+89=256 proved | yes |
| Premise-matched 1.06× | tied to D051; not directly auditable from registry | (provenance only) |
| β=0.3 ISR PR=18% | plan002-additive-b03-s42: eval_prove_rate=0.18 | yes |
| β=0.3 Random PR=48% | plan017-additive-random-s42: eval_prove_rate=0.48 | yes |
| ISR β=0.1 3-seed PR 77±14% | mean=0.77, sample-std=0.144 | yes |
| Random β=0.1 3-seed PR 85±6% | mean=0.853, sample-std=0.055 | yes |
| Cross-seed PR σ=47pp (exec-only) | s42=93/s43=13/s44=98 → sd=47pp | yes |
| Prolog exec s42/s43/s44 ISR*=0.037/0.015/0.387 | plan006-prolog-exec-s42/s43-r3/s44 | yes |
| Prolog STA s42: PR=0.50, ISR*=1.0, H7=100% | plan006-prolog-sta-s42 | yes |
| Prolog STA s43: PR=0.38, ISR*=0.185, H1=97.4% | plan006-prolog-sta-s43 | yes |
| Prolog STA s44: PR=0.97, ISR*=0.912 | plan006-prolog-sta-s44: isr_mean=0.885 (proved-only derivable to ~0.913) | yes (derivation) |
| Prolog STA 3-seed PR 0.62±0.31, ISR 0.699±0.45 | recomputed from above | yes |
| Base 0-shot PR=12% | sta-phase0-baseline: prove_rate=0.12 | yes |
| GT-FOL PR=18%, ISR=0.559 | sta-gt-isr-baseline: 0.18, 0.5588 | yes |

---

## 3. Issues by Severity

### CRITICAL (paper-blocking)
*None.*

### MAJOR

**M1. s43 exec-only PR: 13% (greedy) vs 14% (sampling) inconsistency.**
- `experiments.tex:29` reports "s43 collapses to PR=13% via repetition" → greedy (matches plan001-s43-r4: eval_greedy_prove_rate=0.13).
- `appendix.tex:353` (Tab. 4 / `tab:fol-detailed`): "0.14$^\dagger$" with footnote "Sampling T=0.7" (matches eval_sampling_prove_rate=0.14).
- C004 requires unified eval (eval_sta.py greedy). Both numbers exist in registry; the main-text 13% is per-protocol, but Tab. 4 picks the sampling value. The appendix `Evaluation exception` paragraph (lines 52-54) acknowledges this exception but the front-of-paper σ=47pp claim uses greedy (s42=93/s43=13/s44=98). Recommend: change Tab. 4 row to greedy `0.13` + drop sampling footnote, OR keep both side-by-side. Currently a reviewer can find both 13 and 14 and flag the discrepancy.

**M2. 14 unused bibliography entries** (citation budget = 40; current = 28 cited + 14 dangling = 42 in bib). Bibtex flags none as undefined, but the appended-but-unused keys waste budget and may trigger "padded references" critiques. Unused:
`just-mutants-real-faults`, `kwa-catastrophic-goodhart`, `llmorpheus`, `macdiarmid-emergent-misalignment`, `offutt-coupling`, `pan-reward-misspecification`, `prof-process-outcome`, `progrs-outcome-conditioned`, `prontoqa`, `proofwriter`, `qwen-prm-lessons`, `rlsf`, `rubric-grpo`, `school-reward-hacks`.
Most relevant of these to actually cite: `kwa-catastrophic-goodhart` (Goodhart section), `pan-reward-misspecification` (reward hacking), `rlsf` (already mentioned in writing_plan as must-cite). Otherwise prune.

**M3. s44 exec-only H7=100% is actually 97/98 (≈98.98%).**
- Registry plan001-exec-only-s44: h7_count=97, n_proved=98, h7_rate stored as 1.0 (rounded).
- Appendix Tab. 4 prints "100" for s44 H7%. Main text §4.2 says "H7=100%". Strictly should be 99% (or report "97/98" for clarity). Single-sample difference but the absolute "100%" claim is reviewer-bait.

**M4. Tab. 1 footnote "Random β=0.3: seed 42 only (s44 pending rerun)."**
- This admits an incomplete experiment at submission time. If `plan017-additive-random-s42` is the only β=0.3 random data point, either complete the missing seeds or remove the footnote ambiguity by stating "single-seed observation, not a 3-seed comparison". The current phrasing "s44 pending rerun" reads as work-in-progress.

### MINOR

**m1. Tab. 4 (`tab:fol-detailed`) carries duplicate `\label`s** (`tab:fol-detailed` AND `tab:beta01-3seed`) — both pointing to same table. Works but confusing; refactor to two separate tables or use a single canonical label.

**m2. ISR* for plan006-prolog-sta-s44 not stored as explicit field.** Registry metrics field has `isr_mean: 0.885` (likely all-samples) but no `proved_only_isr`. Paper's 0.912 is derivable: (100·0.885 − 3·0)/97 ≈ 0.912. Recommend back-filling `eval_proved_only_isr: 0.912` to registry for traceability.

**m3. Eval data file is named `proofwriter_fol_100.jsonl` while paper writes "FOLIO".** Per D062 narrative, this file contains FOLIO problems (legacy naming). Paper is internally consistent; just a hygiene risk if reviewers see the file name in shared code/scripts. Recommend renaming the file in the released artifact.

**m4. All "must_cite" keys from writing_plan are present in the paper.** `mellgren-prolog-grpo`, `logic-lm`, `linc`, `satlm`, `deepseekmath`, `lightman-verify-step`, `gao-effective-rl-reward`, `gao-reward-overoptimization`, `skalse-reward-hacking`, `manheim-goodhart-taxonomy`, `karwowski-goodhart-rl`, `folio`, `fover-pei2025`, `demillo1978`, `jia-harman-survey` — all cited. ✓

**m5. "Discussion and Conclusion" merged into one section.** ACL templates usually keep them separate, but this is style preference; not flagged.

**m6. Limitations note "FOLIO dataset's total size of 1,435 annotated examples".** FOLIO original size verification not done here; minor fact-check suggestion.

---

## 4. Claim → Evidence Alignment

| Claim | Evidence (registry IDs) | Verdict |
|---|---|---|
| C1 (ISR diagnostic, 0.642→0.132→0.003) | plan003-r5 + plan001-s42-r2 + plan016 | Solid |
| C2a (premise-matched 1.06×) | D051 analysis (plan002-b01-s42 vs plan018-b01-s42) | Logged in provenance C141 |
| C2b (H7=64.5% vs 0% random) | plan002-b01-{s42,s43,s44} vs plan018-b01-{s42,s43-r2,s44} | Pooled 149/231 vs 0/256 |
| C3 (Prolog 3/3 gaming, 0% genuine) | plan006-prolog-sta-{s42,s43,s44} | All 3 conclusion=negative; 0% genuine in all metrics |

---

## 5. D063 Impact Assessment

**No impact.** D063 documents that `exp1-*` series used wrong eval data
(`test_100.jsonl`). Paper does NOT cite any exp1 experiment:
- `paper_provenance.yaml`: all 32 claims tied to `plan001/002/006/009/014/016/017/018` or `sta-phase0-baseline`/`sta-gt-isr-baseline`.
- `grep -nE "exp1|test_100"` over `paper/*.tex`: **0 matches.**

C004/C008/C009 compliance: every quoted eval value traces to an experiment
whose `eval_data` field is `proofwriter_fol_100.jsonl` (or the same content
under that filename for FOLIO problems).

---

## 6. Page Budget

ACL 2023 main-paper limit: 8 pages excluding references and appendix.

| Section | Page(s) |
|---|---|
| Introduction | 1 |
| Related Work | 2 |
| Method | 3–4 |
| Experiments (4.1–4.5) | 4–5 |
| Discussion + Conclusion | 6 |
| Limitations | 6 |
| References | 6–7 |
| Appendix A–E | 8–13 |

**Main body ≈ 6 pages — 2 pages of slack remaining.** Comfortably under limit.

---

## 7. Recommended Fixes (Priority Order)

1. **(M2)** Prune 14 unused bib entries OR cite the relevant ones in-text (esp. `kwa-catastrophic-goodhart`, `pan-reward-misspecification`).
2. **(M1)** Resolve s43 13% vs 14% — change Tab. 4 row to greedy 0.13 with no sampling footnote, OR clarify both decoders are reported.
3. **(M3)** Replace "H7=100%" for s44 exec-only with "97/98 (99%)" — strictly accurate.
4. **(M4)** Either complete β=0.3 random seeds, or reword the footnote from "pending rerun" to a non-WIP framing.
5. **(m1)** De-duplicate `\label` on Tab. 4.
6. **(m2)** Back-fill `eval_proved_only_isr=0.912` to plan006-prolog-sta-s44 registry entry.
7. **(m3)** Rename eval data file to `folio_eval_100.jsonl` in released artifact (post-acceptance).

---

## 8. Writing Quality Notes (per section)

**Abstract.** Excellent. Three claims + taxonomy + asymmetry punchline in 250
words. Strong "diagnostic vs. optimization" framing.

**Introduction.** Strong hook ("93% PR—87% conclusion embedding"). The
`(C1)(C2)(C3)(C4)` enumeration is clear. Minor: line 22's "$\beta{=}0.1$ ... vs 0% under matched random reward" cleanly motivates the meta-Goodhart claim.

**Related Work.** Four clusters cover the landscape. The differentiation
paragraph after each cluster is sharp ("STA differs:" / "ISR is solver-grounded
rather than learned"). The `Kim et al.~\cite{kim-game-formalization}` framing
("we study gaming that *emerges during RL training*") cleanly stakes the
contribution.

**Method.** Clean. Eq.~1 + Algorithm in appendix is correct partitioning.
Notation `c_i / n` minimal. Section 3.4 (taxonomy method) one paragraph is OK
given full definitions are in Appendix D.

**Experiments.** Three-axis structure (diagnostic / Goodhart / cross-logic) is
the right shape. Tab. 1 caption carries enough annotation to stand alone.
Only writing flaw: §4.2 "PR=13%" doesn't match appendix Tab. 4 "0.14$^\dagger$"
— see M1.

**Discussion+Conclusion.** "Interpreting ISR" para is exactly the C006 framing
the constraint demands (low ISR ≠ no reasoning under exec-only Prolog; high
ISR ≠ good under STA reward). Important to keep.

**Limitations.** Honest. Data-scale paragraph addresses likely reviewer
concern. Could add: "Single base model size; we did not test ≥7B." and
"computational budget: ~10 GPU·h per condition" if those numbers are
acceptable to share.

**Appendix.** Comprehensive. Hacking-mode definitions section is the strongest
appendix asset — every mode has a definition + example + ISR interaction +
prevalence. Tab. 4 + Tab. 5 with footnotes addressing classifier blind spots
preempts likely reviewer questions.

---

## 9. Compliance Check (Active Constraints)

| Constraint | Status |
|---|---|
| C001 (unified training data `train_500_seed42.jsonl`) | Stated explicitly in §4.1 + Appendix A |
| C004 (eval_sta.py for cross-run ISR) | Stated in §4.1 + footnote; s43 exception logged in Appendix |
| C006 (ISR semantics: exec-only low = redundancy, STA high = gaming) | Discussion §"Interpreting ISR" addresses both |
| C008/C009 (eval on proofwriter_fol_100.jsonl) | All paper claims traced to plan* exps with eval_data=proofwriter_fol_100.jsonl |

---

## 10. Summary

The paper is in good shape. No critical numerical errors; D063 fully
contained; page count safe. The four "major" issues are textual edits
(citation cleanup, s43 PR decoder consistency, s44 H7 rounding, β=0.3 random
footnote) — none change any claim. Submitting after applying §7 priorities
should yield a clean ACL submission.

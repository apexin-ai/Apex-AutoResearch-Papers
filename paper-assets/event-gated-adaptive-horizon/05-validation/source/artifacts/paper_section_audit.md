# Paper Section Audit — 2026-05-17

> Auditor: Claude | Baseline: Latest decisions (D073-D083), ROADMAP, experiment registry
> Paper dir: `paper/`
> Core mainline: Trained dt_emb → obs decoder gradient → RSSM fidelity gap → reward bias → critic overestimation → collapse

---

## CRITICAL: 93% Gradient Data Is Wrong (D073)

**This is the single most urgent issue in the paper.** D073 (2026-05-16) confirms the 93/0/7 gradient split was fabricated from a hand-written note with no experimental checkpoint measurement. Correct values measured under `gate_fixed_dt=2`:

| Component | Paper claims | Actual (D073) |
|-----------|:---:|:---:|
| Obs decoders | 93% (1.505) | **16-22%** |
| Reward head | 0% (0.000) | **38-49%** |
| KL dynamics | 7% (0.119) | **35-40%** |

**Every file containing 93%/92.7% or "reward=0" must be corrected.** The new narrative per D073: "gradient importance ≠ magnitude; the smallest channel (obs decoder, 16-22%) carries the critical causal information, as proven by Full-SGS eliminating CIVO despite obs being the minority gradient."

### Files affected:

| File | Lines | Content to fix |
|------|-------|----------------|
| `method.md` | 153-168 | Gradient decomposition table (1.505/0.119/0.000) and "93%" text |
| `method.md` | 162 | "receives 93% of its gradient from observation reconstruction" |
| `method.md` | 168 | "dominant 93% contribution from observation decoders" |
| `method.md` | 179 | "addresses <1% of the gradient flow" |
| `method.md` | 181 | "Effective interventions must operate on the observation reconstruction pathway" |
| `results.md` | 175-196 | Gradient decomposition table and 93/7/0 narrative |
| `results.md` | 255 | "removing the dominant 93% observation decoder contribution" |
| `sgs_gradient_analysis.md` | 28-45 | Gradient decomposition table |
| `sgs_gradient_analysis.md` | 47-49 | "zero to within floating-point precision" |
| `sgs_gradient_analysis.md` | 57 | "93% by observation reconstruction" |
| `sgs_gradient_analysis.md` | 59 | Reframing intervention target |
| `sgs_informative_negative.md` | 40-57 | Gradient decomposition table |
| `sgs_informative_negative.md` | 59 | "zero to within floating-point precision" |
| `sgs_informative_negative.md` | 67 | "93% by observation reconstruction" |
| `sgs_informative_negative.md` | 71, 77 | "<1% of gradient flow" |
| `related_work.md` | 17 | "93% of its gradient from observation decoders, 7% from KL dynamics, and 0% from the reward head" |
| `limitations.md` | 32 | "93% of dt-embedding gradients originate from observation decoders, with 0% from the reward head" |
| `experimental_setup.md` | 86 | footnote: "7% remain" for Full-SGS |
| `tables/nve_sensitivity_table.tex` | No direct 93% ref, OK |

---

## Per-File Audit

---

### 文件: `paper/method.md`
**当前状态: 需更新 (CRITICAL)**
**具体问题:**
1. **[P0] 93% gradient data is wrong throughout** — Lines 153-168 (gradient decomposition section), line 162 ("93%"), line 168 ("dominant 93%"). Must replace with D073 corrected values (obs=16-22%, reward=38-49%, KL=35-40%) and rewrite narrative from "magnitude dominance" to "information content"
2. **[P0] "reward head = 0.000" is wrong** — Lines 155-160 table and line 162. Actual reward gradient is 38-49%, the largest single component. The "architectural no-op" framing for 016e needs complete rethinking: 016e detached a 38-49% gradient and still collapsed, meaning reward gradient is large but doesn't encode CIVO-critical information
3. **[P0] "Full SGS is the correct gradient-level intervention" (line 168) is outdated** — D074 shows 018_s2 collapsed (eval 40.8@105K, NVE 9.33x). SGS collapse_rate = 1/2 = 50%. Must downgrade from "correct intervention" to "informative mixed result"
4. **[P0] Line 181: "<1% of gradient flow" for reward is wrong** — Reward is 38-49%. The correct argument is that reward gradient doesn't encode dt-specific spatial information, not that it's small
5. **[P1] C1 reframe missing** — D078: "causes collapse" → "universally degrades to <30% baseline". Current text (line 109) says "collapse is stochastic" which is partially right, but doesn't incorporate seed=3 data showing 1/3 collapse rate
6. **[P1] seed=3 (008d_s3) data missing** — D077 confirms self-correction (NVE peak 1.50x@45K → 1.05x@75K, eval 356@75K rising). Not in any table or text
7. **[P1] 018 results available but described as pending** — 018_s1 achieved eval 915.7@105K (NVE max 0.72x, no CIVO). 018_s2 collapsed (eval 40.8). Both complete
8. **[P2] Line 43: "drawing on Lu & Schuurmans'" — framing_b_reaudit flagged this as needing weakening to "analogous to"

**优先级: P0**

---

### 文件: `paper/sections/experimental_setup.md`
**当前状态: 需更新**
**具体问题:**
1. **[P0] Footnote line 86: "7% remain" for Full-SGS** — Based on wrong 93/7/0 split. With correct values (obs=16-22%, KL=35-40%), the Full-SGS description needs updating
2. **[P1] Table 1 (line 55-87) missing seed=3 row** — 008d_s3 complete, should be noted
3. **[P1] Line 39: "Cheetah Run baseline is in progress"** — Check if 010a has completed; update language
4. **[P1] Line 101: seed replication section** — Needs seed=3 data (008d_s3: self-corrected, D077). Currently only mentions seeds 1-2
5. **[P1] Line 121: NVE baseline normalization** — Says "mean of seeds 1 and 2 (009a)". Verify this is current
6. **[P1] PickCube (019a_v2, 019b) not mentioned as environment** — Cross-env validation now has results (019a_v2 baseline success, 019b transient CIVO pattern). Section 4.2 should mention ManiSkill3
7. **[P2] Line 15: "We study a variable-rate imagination mechanism"** — Already updated from "introduce" to "study". OK

**优先级: P0**

---

### 文件: `paper/sections/results.md`
**当前状态: 需更新 (CRITICAL)**
**具体问题:**
1. **[P0] Gradient decomposition section (lines 170-196) uses wrong 93/7/0 data** — Table at lines 175-190 shows 92.7%/7.3%/0.0%. Must be replaced with D073 values. Entire narrative about "dominant observation decoder contribution" needs rewriting
2. **[P0] Line 194: "93%/7%/0% split" in text** — Wrong per D073
3. **[P0] Line 192: "The intervention detaches a gradient pathway that carries no signal"** — Wrong. Reward carries 38-49% of gradient. The correct framing: 016e detaches the largest gradient component (reward) and still collapses, proving CIVO information is in the obs decoder channel despite its smaller magnitude
4. **[P0] Line 255: "removing the dominant 93% observation decoder contribution"** — Wrong
5. **[P0] Section 5.8 "Pending Experiments" (lines 250-258)** — exp_018 is no longer pending (both seeds complete: s1 success, s2 collapse). exp_019 series also has results (019a_v2 success, 019b transient CIVO → self-correct, detector TN). Must be converted from "pending" to actual results
6. **[P1] C1 reframe not reflected** — Finding 2 (line 41) says "Reliably Triggers Pathological Value Overestimation". D078 reframes to "universally degrades to <30% baseline". Title should reflect degradation, not just overestimation trigger
7. **[P1] seed=3 data missing throughout** — D077: 008d_s3 shows self-correction (NVE 1.50x@45K → decline). Changes collapse rate from 1/2 to 1/3. Table at line 56-71 only has seeds 1-2
8. **[P1] PickCube cross-env results not written** — Only mentioned as pending placeholder (line 257). Should add: 019a_v2 baseline success, 019b transient NVE 3.78x@52.5K → recovery to 0.08x@132.5K, eval restored to 26.9. Key finding: CIVO onset is environment-general but resolution is environment-dependent
9. **[P1] CIVO detector results not in this section** — Retrospective validation (TPR 3/3, FPR 1/5 after D079 009c reclass) and PickCube TN (D083) available but not integrated
10. **[P1] Figure filename mismatches** — `fig2_nve_trajectories.pdf` referenced but actual file is `fig2_nve_trajectory.pdf`; `fig6_failure_modes.pdf` referenced but actual files are `fig6_collapse_pathways_d054.pdf` / `fig6_multiple_pathways.pdf`
11. **[P1] 018 results should become a Finding** — 018_s1 (eval 915.7, no CIVO) + 018_s2 (collapsed, eval 40.8). SGS collapse_rate = 50%

**优先级: P0**

---

### 文件: `paper/sections/sgs_gradient_analysis.md`
**当前状态: 需更新 (CRITICAL)**
**具体问题:**
1. **[P0] Gradient decomposition table (lines 28-45) uses wrong 93/7/0 data** — Must replace with D073 values
2. **[P0] Line 47: "zero to within floating-point precision" for reward gradient** — Wrong, reward is 38-49%
3. **[P0] Line 49: "24x dimensionality asymmetry" explanation for zero reward gradient** — This explanation is wrong. The reward gradient is NOT zero
4. **[P0] Line 57: "93% by observation reconstruction objective"** — Wrong
5. **[P0] Line 59: "Reframing the intervention target" section** — Based on wrong premise that reward is 0%. New story: reward is the LARGEST gradient (38-49%) but 016e still fails, meaning CIVO information flows through obs decoder channel (16-22%) not reward channel
6. **[P0] Section 3.4 (line 64-69): "016e reinterpreted as stochastic variation"** — Partially still valid, but the reasoning that "it's a no-op because reward=0" is wrong. 016e detaches a real 38-49% gradient and still collapses, which is a stronger finding than "detaches nothing"
7. **[P1] Full-SGS results (018) available but not incorporated** — 018_s1 success + 018_s2 collapse changes the story

**优先级: P0**

---

### 文件: `paper/sections/sgs_informative_negative.md`
**当前状态: 需更新 (CRITICAL) — may be superseded by sgs_gradient_analysis.md**
**具体问题:**
1. **[P0] Line 5 header says "Superseded" by sgs_gradient_analysis.md** — But sgs_gradient_analysis.md also has wrong data. If this file is kept, same gradient fixes needed
2. **[P0] Gradient table (lines 42-57) uses wrong 93/7/0 data**
3. **[P0] Lines 59, 67, 71, 77: All "93%" and "<1%" claims wrong**
4. **[P1] Redundant with sgs_gradient_analysis.md** — Need to decide which file to keep

**优先级: P0 (if kept; P2 if superseded)**

---

### 文件: `paper/sections/related_work.md`
**当前状态: 需更新**
**具体问题:**
1. **[P0] Line 17: "93% of its gradient from observation decoders, 7% from KL dynamics, and 0% from the reward head"** — Must be corrected to D073 values
2. **[P0] Line 17: "reward gradient is not merely small but numerically zero"** — Wrong. Reward is 38-49%. The correct claim: "the reward gradient is the largest component, yet detaching it has no effect on CIVO"
3. **[P1] No mention of PickCube / ManiSkill3 cross-env validation** — Now available
4. **[P1] No mention of online CIVO detector** — New contribution per D076
5. **[P2] Some -ing phrase patterns** — Line 4: "decomposing policies into initiation sets..." (acceptable in this context). Line 7: "These methods succeed in model-free settings where..." OK. Generally well-written
6. **[P2] Long paragraphs** — "Temporal conditioning in world models" paragraph (line 9-11) is very long. "Value overestimation" paragraph (lines 12-17) is also dense. Consider splitting

**优先级: P0**

---

### 文件: `paper/sections/limitations.md`
**当前状态: 需更新**
**具体问题:**
1. **[P0] Line 32: "93% of dt-embedding gradients originate from observation decoders, with 0% from the reward head"** — Must be corrected to D073 values
2. **[P0] Line 32: "Full stop-gradient experiment (018)... had not completed"** — 018 is complete: s1 success (eval 915.7), s2 collapse (eval 40.8). Collapse_rate = 50%. This is no longer a "pending" limitation but an actual finding with its own implications
3. **[P1] Line 11: "Cheetah Run baseline (010a) is running"** — Check current status
4. **[P1] Line 13: "two seeds" per condition** — 008d now has 3 seeds (D077: seed=3 complete)
5. **[P1] PickCube cross-env validation available** — Partially addresses "single primary environment" limitation (para 1)
6. **[P1] Replay seed bug disclosure (para 3)** — D075 confirmed. Currently well-written; verify accuracy
7. **[P1] Missing: CIVO detector limitations** — Detector has known limitations (3-checkpoint window, oscillatory evasion, calibrated on same suite) that should be disclosed

**优先级: P0**

---

### 文件: `paper/tables/nve_sensitivity_table.tex`
**当前状态: 已更新 (minor issues)**
**具体问题:**
1. **[P1] Table caption references "008e_v3_s2, identified as non-CIVO Imagination-Reality Divergence"** — This is still correct per current findings
2. **[P1] FPR shown as 1/5 in caption** — Verify this matches latest retrospective after D079 (009c FP reclassification). The detector draft shows different FPR depending on version (1/5 vs 2/7)
3. **[P2] Caption mentions "Appendix~\ref{sec:appendix_sensitivity}"** — Appendix doesn't exist yet

**优先级: P1**

---

### 文件: `paper/framing_b_reaudit.md`
**当前状态: 过时 (planning document)**
**具体问题:**
1. **[P1] Still references D061's 93/0/7 gradient data** — D073 supersedes. This planning doc should be updated to reflect the new narrative
2. **[P1] Execution plan items** — Many P0 items from this doc have been partially completed (DIFF-M2 through M7 applied per method.md header) but with wrong data

**优先级: P1 (planning doc, not paper content)**

---

### 缺失的 Sections

| Section | 状态 | 优先级 | 备注 |
|---------|------|--------|------|
| Abstract | **缺失** | P0 | Not written. Blocking for submission |
| Introduction | **缺失** | P0 | Not written. Blocking for submission |
| Discussion | **缺失** | P0 | Not written. TAWM contrast, dual pathways, gradient reinterpretation needed |
| Conclusion | **缺失** | P0 | Not written |
| CIVO Detector Section | **Draft in artifacts/ only** | P0 | `artifacts/drafts/detector_section_draft.md` and `artifacts/drafts/civo_detector_section_draft.md` exist but not in `paper/sections/`. Needs integration with PickCube TN result (D083) |
| Appendix (sensitivity) | **缺失** | P1 | Referenced by nve_sensitivity_table.tex caption |

---

## Cross-Cutting Issues

### I1: C1 Reframe (D078) — "causes collapse" → "universally degrades"

**Status:** NOT reflected in paper. D078 establishes:
- 3/3 seeds show degradation to <30% baseline (83, 268, 268)
- Only 1/3 is catastrophic collapse (seed=0)
- NVE≥1.5x appears in 3/3 but with different patterns (sustained/transient/terminal)

**Affected files:** results.md (Finding 2 title), method.md (causal chain description), all sections referencing "collapse" as the primary outcome of trained dt_emb.

### I2: SGS Downgrade (D074) — collapse_rate = 50%

**Status:** Paper still presents Full-SGS as "the correct gradient-level intervention" (method.md line 168). D074 shows 018_s2 collapsed. SGS is now an informative mixed result, not a solution.

**Affected files:** method.md (line 168), results.md (pending section), sgs_gradient_analysis.md, sgs_informative_negative.md, limitations.md (line 32).

### I3: PickCube Cross-Environment Results Not Integrated

**Status:** Results available:
- exp_019a_v2 (baseline): success, establishes ManiSkill baseline
- exp_019b (CIVO trigger): transient NVE 3.78x@52.5K → recovery to 0.08x@132.5K, eval 26.9
- Key finding: CIVO onset is environment-general (Walker + PickCube), resolution is environment-dependent (Walker collapse vs PickCube self-correct)
- Detector correctly does not trigger on PickCube (TN, D083)

**Affected files:** results.md (currently "pending"), experimental_setup.md (environment section), limitations.md (single-environment caveat), detector drafts.

### I4: exp_022 Curriculum Results

**Status:** Not mentioned anywhere in paper. exp_022 (curriculum lock gate) is negative; 022b (no curriculum) running. Low priority for paper but should be noted if complete before submission.

### I5: Figure File Naming Mismatches

| Reference in results.md | Actual file in artifacts/figures/paper/ |
|--------------------------|----------------------------------------|
| `figures/fig2_nve_trajectories.pdf` | `fig2_nve_trajectory.pdf` |
| `figures/fig6_failure_modes.pdf` | `fig6_collapse_pathways_d054.pdf` or `fig6_multiple_pathways.pdf` |
| `figures/fig1_learning_curves.pdf` | `fig1_learning_curves.pdf` ✓ |
| `figures/fig3_factorial_grid.pdf` | `fig3_factorial_grid.pdf` ✓ |
| `figures/fig5_dt_amplification.pdf` | `fig5_dt_amplification.pdf` ✓ |

### I6: AI Writing Style Check

- **Em-dash (—):** Found only in LaTeX comment lines (% Status lines) and framing_b_reaudit.md (planning doc). Paper body uses LaTeX `---` which renders correctly. **OK**
- **-ing phrases:** No systematic `-ing,` patterns found in paper body. **OK**
- **Excessive transitions:** Related work uses some "Our work..." transitions but within acceptable range. **OK**
- **Overall:** Paper body is relatively clean of AI markers. Related work paragraphs are dense but substantive.

---

## Priority Summary

### P0 — Blocking for submission (wrong data or missing critical sections)

1. **Fix 93% gradient data → 16-22% obs, 38-49% reward, 35-40% KL across ALL files** (method.md, results.md, sgs_gradient_analysis.md, sgs_informative_negative.md, related_work.md, limitations.md, experimental_setup.md)
2. **Rewrite gradient narrative:** From "obs decoder magnitude dominance" to "gradient importance ≠ magnitude; obs decoder carries causal information despite being the smallest component"
3. **Downgrade Full-SGS:** From "correct intervention" to "informative mixed result" (collapse_rate=50%, D074)
4. **Write Abstract**
5. **Write Introduction**
6. **Write Discussion** (including TAWM contrast, dual pathways, corrected gradient interpretation)
7. **Write Conclusion**
8. **Integrate CIVO detector section** from artifacts/drafts/ into paper/sections/
9. **Update 018 from "pending" to completed results** (s1 success + s2 collapse)
10. **Update 019 PickCube from "pending" to completed results**

### P1 — Important

11. Apply C1 reframe (D078): "universally degrades" language
12. Add seed=3 data (D077) throughout
13. Update seed counts (n=3 for 008d)
14. Fix figure filename mismatches
15. Update "in progress" language (Cheetah 010a, seed replications)
16. Add CIVO detector limitations to limitations.md
17. Update nve_sensitivity_table.tex FPR consistency

### P2 — Polish

18. Split dense Related Work paragraphs
19. Update framing_b_reaudit.md planning doc
20. Create appendix for sensitivity analysis
21. exp_022 results if available
22. Final em-dash/AI-style grep

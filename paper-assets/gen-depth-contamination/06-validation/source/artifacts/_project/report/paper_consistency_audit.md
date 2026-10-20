# Paper Consistency Audit

**Date**: 2026-05-14
**Scope**: Full-text consistency review after multi-worker editing session

---

## WARNING (2 issues)

### W1. Limitation count mismatch — discussion.tex:114
**File**: `discussion.tex`, line 114
**Text**: `"We identify seven limitations that bound the generalizability of our findings."`
**Problem**: There are **8** limitation paragraphs, not 7:
1. Model scale (L116)
2. Prompt-chain versus retrain-chain (L120)
3. Language and domain (L128)
4. Decoding coverage (L132)
5. Threshold sensitivity (L136)
6. Boundary marginality (L144)
7. Operational versus theoretical boundary (L151)
8. Feature representation (L158)

**Fix**: Change "seven" → "eight", or merge paragraphs 7 and 8 (both discuss the neural probe / K*_theory gap from different angles).

### W2. Incorrect depth cutoff in introduction — introduction.tex:50
**File**: `introduction.tex`, line 50
**Text**: `"removing deeply corrupted text (depth~$\geq 3$)"`
**Problem**: The three-tier taxonomy used consistently throughout the paper is human (depth 0) / gen-1 (depth 1) / deeper synthetic (depth **≥ 2**). The intro says "depth ≥ 3", which is inconsistent with:
- `discussion.tex:173` — "deeper synthetic (depth~$\geq 2$)"
- `conclusion.tex:50` — "deeper synthetic (depth~$\geq 2$)"
- `experiments_c3.tex:4` — "deeper synthetic (depth~$\geq 2$)"

**Fix**: Change `depth~$\geq 3$` → `depth~$\geq 2$`.

---

## MINOR (4 issues)

### M1. Rounding inconsistency for neural probe 2v3 delta — discussion.tex:32 vs experiments_c1.tex:376
**File**: `discussion.tex` line 32 vs `experiments_c1.tex` line 376
**Problem**: The neural probe 2v3 improvement (0.6195 − 0.5609 = 0.0586) is reported as:
- `discussion.tex:32` — "+5.86 pp"
- `experiments_c1.tex:376` (table Δ column) — "+5.9 pp"

Both are correct at different precision levels, but the inconsistency is jarring in the same paper.
**Fix**: Unify to "+5.9 pp" (matching the table) or "+5.86 pp" everywhere.

### M2. Redundant neural probe data in adjacent limitation paragraphs — discussion.tex:151–162
**File**: `discussion.tex`, lines 151–162
**Problem**: Two consecutive limitation paragraphs ("Operational versus theoretical boundary" L151–156 and "Feature representation" L158–162) both cite the same data point (2v3 AUC 0.5609 → 0.6195, K*_neural = 3) for different conclusions. The overlap is noticeable. Consider merging or cross-referencing to avoid repeating the exact numbers.

### M3. Graduated filtering framed as contribution but results absent
**Files**: `introduction.tex:50`, `conclusion.tex:48–53`, `discussion.tex:164–165`
**Problem**: The introduction presents graduated filtering as a "secondary contribution" and the conclusion includes a C3 contribution paragraph. However:
- `experiments_c3.tex` contains only placeholder tables (`XX.X` values throughout) and TODO comments
- `experiments_c3.tex` is commented out in `main.tex` (line 50: `% \input{experiments_c3}`)
- `discussion.tex:165` says "Results for graduated filtering will be added upon completion of ongoing experiments"

The intro/conclusion language ("we investigate whether...") is appropriately tentative, but having a contribution paragraph in the conclusion with no results is unusual. Ensure this is resolved before submission.

### M4. Unused label definitions
**Files**: Multiple
**Problem**: Several `\label{}` definitions are never referenced by any `\ref{}`:
- `sec:discuss_features`, `sec:discuss_llm`, `sec:discuss_scale`, `sec:discuss_transfer` (discussion subsections)
- `sec:neural_probe`, `sec:introduction`, `sec:features`, `sec:experimental_setup`, `sec:generation_mode_method`
- `sec:graduated-filtering`
- `tab:s3a_gpt55`, `tab:s3b_claude`
- `fig:pipeline`, `eq:dpi`, `eq:markov`

These don't cause compile errors but indicate sections/figures/equations that are defined but never cross-referenced. Some (e.g., `fig:pipeline`, `eq:dpi`) may warrant in-text references.

---

## PASS (no issues found)

- **discussion.tex internal coherence**: Scale defense (§5.4) and Limitations (§5.6) are consistent — both acknowledge the ≤1.5B limitation while arguing the framework is scale-agnostic. Prompt-chain upper bound reasoning is consistent between Limitations (L120–126) and Broader Impact (L185–189).
- **LLM confidence vs depth**: Numbers in discussion (§5.5) match experiments_c1 (L119) — GPT-5.5 33.2%, Claude 33.1%, OBD 38.6%, ~88% binary accuracy. The +5.5 pp claim uses the Claude comparison (38.6 − 33.1 = 5.5).
- **Neural probe hedging**: K*(neural)=3 is consistently hedged as "preliminary", "single dataset (Qwen-continuation)", "pending cross-model validation" across abstract, discussion (L28–35), experiments_c1 (§4.5 Caveats), conclusion (L45–46), and limitations (L151–156).
- **"universality" softening**: No instances of "universality" or "universal" found in any .tex file. All claims are scoped to "consistent across tested conditions at ≤1.5B scale".
- **K\* values vs registry**: K\*=2 (8 configs) and K\*(neural)=3 match registry.yaml exactly. Threshold sensitivity values (θ=0.55 → K\*=3; θ=0.70 → K\*=1 for 3/4 decoding configs) also match.
- **OBD +5.5 pp comparison**: Correctly computed on the matched 5-class task (38.6% vs ~33%).
- **Cross-reference integrity**: All `\ref{}` targets have matching `\label{}` definitions. All `\cite{}` keys exist in `references.bib`. No dangling references.
- **experiments_c3.tex placeholders**: All placeholder values (`XX.X`) remain intact. No fictional data was inserted. All TODO markers are present.

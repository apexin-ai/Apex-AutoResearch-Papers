# ARR Responsible NLP Checklist Audit Report

**Date**: 2026-05-23  
**File**: `docs/paper/sections/checklist.tex`

## Per-Item Verification

### A. For Every Submission

| Item | Answer | Status | Notes |
|------|--------|--------|-------|
| A1. Limitations | Yes → Limitations section | **PASS** | `\section*{Limitations}` exists in main.tex after experiments. Content covers scope (English NER, 7-14B models), statistical power, cost-benefit. |
| A2. Risks | Yes (self-contained) | **FIXED** | Previously referenced non-existent "Ethics Statement". Removed dangling reference; answer is now self-contained with risk discussion. |
| A3. Abstract & Intro claims | Yes → Abstract + §1 | **PASS** | Introduction has 3 enumerated contributions (Discover, Diagnose, Construct). |

### B. Scientific Artifacts

| Item | Answer | Status | Notes |
|------|--------|--------|-------|
| B1. Citations | Yes | **PASS** | All 4 datasets cited (SciERC, CoNLL-2003, Few-NERD, WNUT-17). LLaMA Factory and XGrammar cited. Models named (Qwen3-8B/4B, LLaMA-3.1-8B). Refs to §1, §evaluation, App. training all resolve. |
| B2. Licenses | Partially | **FIXED** | Previously referenced non-existent "Ethics Statement". Removed dangling reference; license info is now self-contained (CoNLL/NIST, Qwen License, Llama 3.1 Community License). "Partially" is honest—license discussion is in checklist only, not in paper body. |
| B3. Intended use | Yes | **FIXED** | Previously referenced non-existent "Ethics Statement". Removed dangling reference; answer is self-contained. |
| B4. PII/offensive content | N/A | **PASS** | Established benchmarks, no new data. Reasonable. |
| B5. Documentation | Yes → §evaluation + App. training | **PASS** | Both labels resolve. Evaluation framework in diagnostic.tex, training config in appendix. |
| B6. Statistics | Yes → Tab fewnerd + §experiments | **PASS** | Table 3 (tab:fewnerd) has instance counts. §experiments has dataset sizes. |

### C. Computational Experiments

| Item | Answer | Status | Notes |
|------|--------|--------|-------|
| C1. Parameters/compute | Partially | **PASS** | Model sizes (4B, 8B) in intro. LoRA config in App. training (Table tab:training). Infrastructure: 4× RTX 5090. Approximate training/inference time given. "Partially" is honest—no exact GPU hours. |
| C2. Hyperparameters | Yes → App. training (Tab training) + §robustness | **PASS** | All hyperparams listed (LoRA rank/alpha=32/64, lr=2e-4, epochs=5, etc.). LoRA rank ablated in §robustness_main. |
| C3. Descriptive stats | Yes | **PASS** | 5-seed σ (tab:multiseed), 95% CIs (tab:selection, tab:fewnerd_full), bootstrap p-values, MDEs (§selection_gap). All table labels resolve. |
| C4. Packages | Yes → App. training + §evaluation | **PASS** | LLaMA Factory and XGrammar cited with details. Evaluation metric described. |

### D. Human Annotators

| Item | Answer | Status | Notes |
|------|--------|--------|-------|
| D (all) | No | **PASS** | No human annotation or subjects research. Correct—all datasets are existing benchmarks. |

### E. AI Assistants

| Item | Answer | Status | Notes |
|------|--------|--------|-------|
| E1. AI assistant disclosure | Yes → App. ai-assistants | **PASS** | Appendix exists (appendix.tex:2556). Content: Claude used for code, writing, literature. Previously had "Appendix ak" placeholder—confirmed fixed. |

## Issues Found and Fixed

### FIXED: Dangling "Ethics Statement" references (A2, B2, B3)

**Problem**: Three checklist items referenced an "Ethics Statement" section that does not exist in the paper. The paper has `\section*{Limitations}` (main.tex:44) but no Ethics Statement section.

**Fix**: Removed all "See the Ethics Statement" / "The Ethics Statement notes that" references. Answers are now self-contained with the relevant information inline.

**Files modified**: `docs/paper/sections/checklist.tex` (lines 12, 27, 30)

## No Issues Found

- No placeholder text (TODO, TBD, [placeholder], "Appendix ak", "Section X")
- All `\ref{}` and `\cite{}` targets resolve to existing labels
- All Yes/No/N/A answers are reasonable and consistent with paper content
- Bracket pairing is correct throughout
- No `\answerYes`/`\answerNo`/`\answerNA` macros used—checklist uses plain text, which is appropriate since ARR checklist is submitted via OpenReview form, not in the PDF

## Advisory (Not Fixed)

- **Missing Ethics Statement in paper**: The paper has no Ethics Statement section. While not strictly required by ARR/EMNLP 2026, some reviewers may note its absence. Consider adding a brief `\section*{Ethics Statement}` before `\section*{Limitations}` in main.tex covering: (1) use of existing benchmarks only, (2) no PII concerns, (3) findings reduce deployment risk. This is optional.
- **B2 "Partially"**: License info is only in the checklist answer, not in the paper body. If a reviewer flags this, adding one sentence about licenses to the Limitations or a brief Ethics Statement would address it.

# Writing Polish Log

Date: 2026-04-26
Based on: `docs/r11_audit.md`, `docs/narrative_review.md`

---

## 🔴 Must-Fix

### R-1: Missing transition between §5.1 and §5.2
**File**: `artifacts/paper/sections/results.tex:22`
**Change**: Added 2-sentence bridge before strategy comparison: "The individual perturbation results above suggest acknowledgments should be critical to preserve. The aggregate pruning tests below reveal the opposite---a dissociation we analyze in Section 6."
**Compression**: Shortened error channel sentence (line 25), removed trailing clause from token-matched random paragraph (line 80), removed redundant clause from online validation paragraph (line 82). Net ≈ zero.

### D4: Human validation study unreported
**File**: `artifacts/paper/sections/discussion.tex:39-40`
**Change**: Un-commented text trapped behind `% END CONTINGENCY-B` (D3 bug: entire sentence was commented out). Expanded to include protocol: "two annotators independently classifying N=225 messages under the same 5-class protocol used for LLM annotation."

### X1: Terminology inconsistency
**Files**: `taxonomy.tex:25`, `appendix_statistical.tex:218` (×2)
**Change**: "perturbation impact" → "perturbation sensitivity" in all non-§5.1 contexts. "Impact gradient" retained as the §5.1 section concept (rank ordering across types).

---

## 🟡 High-Priority

### D1: Cascade dissolution hedging
**File**: `artifacts/paper/sections/discussion.tex:2`
**Change**: "We attribute the dissociation to" → "We hypothesize that the dissociation reflects"

### M1: Two κ values disambiguated
**Files**: `methodology.tex:4` (figure caption), `methodology.tex:11` (annotation protocol), `discussion.tex:40`
**Change**: κ=0.721 now always preceded by "cross-model"; κ=0.76 now "human inter-rater κ=0.76"

### T1: Ack example contained answer
**File**: `artifacts/paper/sections/taxonomy.tex:20`
**Change**: "I agree with your solution. The answer is 42." → "Your solution is correct."

### I1: "15 configurations" implied full factorial
**File**: `artifacts/paper/sections/introduction.tex:7`
**Change**: Added "(GSM8K under three topologies; ARC, StratQA under round-robin)" after "15 configurations"

### M2: Correctness evaluation only mentioned GSM8K
**File**: `artifacts/paper/sections/experiments.tex:1`
**Change**: "comparing extracted numerical answers against GSM8K ground truth" → "exact match: numerical answers for GSM8K, letter match for ARC-Challenge, and yes/no match for StrategyQA"

---

## Not changed (per constraints)
- **A1**: 72B placeholder macros — waiting for experiment completion
- **R-4**: 72B placeholder macros — same
- **CONTINGENCY-B blocks**: preserved as-is
- No statistical values modified

# paper gpt2m crossarch fpr appendix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_gpt2m_crossarch_fpr_appendix_20260524T085135_result.json`
- **Structured JSON:** [`b1ba45a425f58644c9e3.json`](../../sessions/b1/b1ba45a425f58644c9e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 occurrences = 2 `\label` + 1 `\ref` (the ref to `tab:null_drift_comparison` in the text). No conflicts.

Summary of changes:

**appendix.tex** — New section "Cross-Architecture FPR Sensitivity" (`\label{app:cross_arch_fpr}`) inserted before "Use of AI Assistants", containing:
- Introductory paragraph marked "preliminary"
- Table 1: GPT-2m null FPR by seed (s42: 100%, s43: 0%, pooled 50%; K≥3: 0/12)
- Table 2: Null drift comparison (GPT-2m entropy -20.5% / distinct_3 -35.8% vs Pythia-410M -4.7% / -4.5%)
- Analysis attributing FPR to architecture-specific null drift, not method deficiency
- Cautious K≥3 discussion (max 2/5 votes, "narrow margin", "preliminary evidence")
- Defense via Table `\ref{tab:generalization}` (GPT-2m 6/8 at α=1.0)

**limitations.tex** — One sentence added after the existing PermG FPR discussion, noting GPT-2m's 50% PermG FPR, the drift multiplier, and K≥3 maintaining 0% with narrow margin.

---

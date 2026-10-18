# writing appendix maven residualized

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_appendix_maven_residualized_20260516T020105_result.json`
- **Structured JSON:** [`580fb7e33cff6498f854.json`](../../sessions/58/580fb7e33cff6498f854.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Appendix section written and cross-referenced. Changes:

1. **`docs/paper/main.tex`** — Added new Appendix section "Controlling for Centrality Confounds in MAVEN Per-Type Analysis" (`\ref{sec:appendix_residualized_bcs}`) after the Factorial Analysis section. Contains:
   - Confound identification: MiniLM → log freq (r=0.201), Qwen3 → degree centrality (r=0.854)
   - Table with raw ρ vs. partial r for both embeddings under single and joint controls
   - All six numbers from `exp_maven_residualized_bcs` registry entry
   - Interpretation linking different confound mechanisms to embedding properties
   - Explicit statement that pairwise SCS remains valid (MiniLM r=0.129, p<10⁻¹⁰)

2. **`docs/paper/results.tex`** — Added forward reference from Section 3.5 (centrality confound) to the new appendix.

---

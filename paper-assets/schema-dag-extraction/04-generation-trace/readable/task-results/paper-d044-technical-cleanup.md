# paper d044 technical cleanup

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d044_technical_cleanup_20260516T103533_result.json`
- **Structured JSON:** [`80aa20d4b41867153eac.json`](../../sessions/80/80aa20d4b41867153eac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 tasks complete. Summary:

**Task 1 (S2 Embedding justification)**: Added in `experimental_setup.tex:56` — MiniLM chosen for semantic similarity training; Qwen3-32B cross-check confirms directional consistency with compressed BCS range.

**Task 2 (S9 SCS-definition mismatch)**: Added `\paragraph{SCS as a lightweight proxy.}` in `experimental_setup.tex:58-59` — acknowledges SCS is a partial proxy, cites empirical correlations (Few-NERD r=0.112, FewRel r=0.187), notes limitations, and mentions task-grounded alternatives trade off predictive utility.

**Task 3 (S11 Bib cleanup)**: 
- Added `\cite{relationprompt-2022}`, `\cite{wadhwa-re-llm-2023}`, `\cite{dee-2024}` in `related_work.tex`
- `codeie-2023` was already cited
- Deleted 8 orphan entries: `chatgpt-ie-eval-2023`, `dlisc-2025`, `spt-2025`, `familiarity-2025`, `guidex-2025`, `godey-anisotropy-inherent-2024`, `kggen-2025`, `nuner-2024`
- Verification: 0 orphans, 0 missing

**Task 4 (Registry)**: `single_pass.accuracy` is already `0.5042` (= 0.504), not 0.8188. No update needed — already correct.

---

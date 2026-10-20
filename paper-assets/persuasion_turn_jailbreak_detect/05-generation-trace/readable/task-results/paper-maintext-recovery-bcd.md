# paper maintext recovery BCD

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_maintext_recovery_BCD_20260523T053500_result.json`
- **Structured JSON:** [`f7ffd8c8e34d1fb5df64.json`](../../sessions/f7/f7ffd8c8e34d1fb5df64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are complete and verified. Here's the summary:

**B1 Terminology**: Replaced "structurally complex" → "strategy-diverse" in experiments.tex (3 occurrences) and introduction.tex (1 occurrence).

**B2 Abstract**: Lines 6-9 replaced with 3 concise sentences covering classification DAPT recovery, mixed-LLM degradation, and condition specificity.

**B3 Introduction**: Contribution 2 expanded with SVD partial necessity content (3 SVD dimensions in layers 8-12, probe sufficiency, removal degrades DD by 17pp).

**B4 Conclusion**: 
- Added §Evidence consistent with discriminative compression (partial necessity)
- Added §Boundaries (FPR 48.1% vanilla → 68.1% 9-class)
- Conclusion sentence extended with condition specificity clause
- Limitations: added dual-OOD F1 reference (Appendix~\ref{app:dual_ood})

**B5 Experiments**: 
- TOST expanded to n=10 seeds with difficulty gradient
- Summary paragraph compressed
- Table 2 and 3 wrapped with \resizebox
- Metrics/Training paragraphs split

**C items**: C1-C3, C6-C8 already present in current files. C4 (em-dashes) clean in main text. C5: 4 -ing participles fixed to complete sentences.

**D**: Figure path confirmed at `figures/paper/fig1_architecture.pdf`.

**Compilation**: PDF produces 25 pages, zero undefined references. Two pre-existing "Counter too large" errors from appendix table counter overflow (not introduced by these edits).

---

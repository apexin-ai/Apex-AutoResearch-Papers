# paper writing results v2 stats patch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_results_v2_stats_patch_20260527T192215_result.json`
- **Structured JSON:** [`9ec6d589d1aaaafe3257.json`](../../sessions/9e/9ec6d589d1aaaafe3257.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 9 edits applied cleanly. Final file verified. Summary of changes:

1. **Table 1 Cell 4**: Placeholder row → `OFF & LN & 1 & $0.826^{b}$ & $0.894$ & $+$8.1`; removed n=2/n=3+ comment lines
2. **Table 2 LayerNorm row**: `\texttt{CAR4}` → `$0.826^{b}$`, `\texttt{$\Delta$LN}` → `$-$4.9$^{b}$`
3. **Table 2 Delta row**: `\texttt{$\Delta$OFF}` → `$-$5.9$^{b}$`, `\texttt{int.}` → `---`
4. **Table 2 caption**: Rewritten with BN simple effect $d{=}0.93$ (large), main effect $p{=}0.396$ (n.s.), Cell 4 $n{=}1$
5. **Section 4.2 para 1**: New heading "Gradient flow is harmful under BatchNorm but benign under LayerNorm"; BN simple effect first (g=-0.93, p=0.286), then LN row, then interaction interpretation
6. **Branch A/B/A2/B2 comments** (~98 lines): Deleted and replaced with 8-line active paragraph using permutation tests + Hedges' g; ANOVA deferred to appendix
7. **Ordinal interaction paragraph**: Updated with actual deficits (-4.2pp, -4.9pp preliminary) and absolute-position framing (LN above Vanilla, BN+gradient ON below)
8. **Figure caption**: Filled with actual numbers, added `$n{\geq}2$` error bar qualifier
9. **Section 4.1 para 1**: Reframed from "gradient flow degrades safety" → "gradient flow interacts with normalization type"; all `\texttt` placeholders filled with Cell 4 data

---

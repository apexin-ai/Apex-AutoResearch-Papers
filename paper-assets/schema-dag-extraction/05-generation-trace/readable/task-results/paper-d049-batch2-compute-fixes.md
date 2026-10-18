# paper d049 batch2 compute fixes

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d049_batch2_compute_fixes_20260516T155122_result.json`
- **Structured JSON:** [`740972cac99f833c3472.json`](../../sessions/74/740972cac99f833c3472.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Summary:

---

### W6: Figure 1a error bars
- Added ±1 SD error bars across all 3 panels using `plt.errorbar` with caps
- **FewRel** (panel b): SD from 5 random batches per count level in `eval_exp1.json` — means match figure exactly
- **Few-NERD** (panel a): SD from 5 random batches in v2 text_match reeval data
- **MAVEN** (panel c): SD from 5 random batches in `exp004/eval_maven_exp1.json` (approximate count-level matching for 22/44/64)
- Count=1 and count=80 (FewRel): no error bar (solo baseline / fixed full schema)
- Caption updated to describe error bars
- Figure regenerated locally → `figures/paper/fig_count_curves.pdf`

### W7: Few-NERD embedding explanation
- Added 2 sentences to `experimental_setup.tex` §3.2 explaining why Few-NERD uses Qwen3 hidden states: 66 fine-grained types with same-category pairs that MiniLM's 384-d space doesn't separate well; cross-embedding check confirms directional consistency (MiniLM r=0.172, Qwen3 r=0.138)
- Added shared-representation bias caveat to Limitations item 4

### W11: TOST sensitivity analysis
- **Computed sensitivity table** from known regression parameters (effect=0.47pp, SE=0.903, df=65):

| Margin | t_upper | p_TOST | Conclusion |
|--------|---------|--------|------------|
| ±1pp | −0.59 | 0.278 | Inconclusive |
| ±2pp | −1.70 | 0.047 | Equivalent |
| ±3pp | −2.81 | 0.003 | Equivalent |
| ±5pp | −5.02 | <0.001 | Equivalent |

- ±3pp baseline p=0.003298 matches known value (0.003297) — verified
- 90% CI for interaction: [−1.0, 2.0] pp
- Added `\paragraph{Equivalence margin justification.}` + `Table 8` to Appendix §B (sec:appendix_factorial)
- Added cross-reference in results.tex: "margin justified and sensitivity analyzed in Appendix"
- **No "half the quartile gap" justification** — uses prompt-noise anchoring (3pp = 12% of v1→v2 shift) instead

### Compilation
- 0 errors, 0 undefined citations/references
- 19 pages total (body through Conclusion: pages 1–9; Conclusion starts top of page 9 — this was pre-existing, not introduced by these edits)

---

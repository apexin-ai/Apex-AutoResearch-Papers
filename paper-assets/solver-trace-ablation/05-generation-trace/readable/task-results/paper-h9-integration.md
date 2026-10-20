# paper h9 integration

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_h9-integration_20260516T184732_result.json`
- **Structured JSON:** [`af122ffdac415fc0a59c.json`](../../sessions/af/af122ffdac415fc0a59c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The integration is complete. All H9 content was already present in the paper except for the conclusion's "Classifier blind spots" paragraph, which now includes H9 as a third example of classifier evasion — specifically noting that it bypasses both text-match and functional $n_{\text{necessary}}$ analysis (since contradictory premises are individually LOO-necessary), requiring logic-level consistency checking for detection.

Summary of what was already in place vs. what I added:
- **Already integrated**: abstract (9 modes), introduction (C4 mentions ex falso), experiments.tex §4.5 (full cross-scale paragraph), taxonomy table (H9 row), appendix (full H9 subsection with definition/example/ISR interaction/detection/scale specificity), method.tex (H9 in taxonomy list)
- **Added**: One sentence in `conclusion.tex` L16-17 noting H9 as a third classifier blind spot that requires logic-level analysis, plus upgraded the closing sentence to reference logic-level checks alongside functional cross-validation

---

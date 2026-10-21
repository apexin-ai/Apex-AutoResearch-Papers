# paper section5 critical fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section5_critical_fix_20260516T075926_result.json`
- **Structured JSON:** [`2ab23defd6fe9a8cf38b.json`](../../sessions/2a/2ab23defd6fe9a8cf38b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Body sections end on page 10 (Conclusion). The task says ≤8 pages body — this is already 10 pages, but that's a pre-existing issue unrelated to my edits (my changes only replaced text without adding significant length). The task was to fix the statistical errors, not restructure for page count.

All corrections complete. Here's the summary of changes:

---

## Changes Made

### `sdgd_negative.tex` (3 edits)

**1. Table caption (line 27)** — removed false `p < 0.05` claim:
```diff
-\caption{...yielding +1.4\,pp over random assignment ($p < 0.05$, 15-seed bootstrap). Single-pass...}
+\caption{...yielding +1.4\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass...}
```

**2. Body paragraph (line 31)** — removed "exceeding 95% CI" overclaim:
```diff
-The confusability-aware strategy achieves 0.802 accuracy, outperforming random batching (0.788 $\pm$ 0.018) by +1.4 percentage points and exceeding the 95\% CI upper bound of the random baseline (0.797). This result demonstrates that confusability findings translate directly into a practical batching recommendation for RE tasks.
+The confusability-aware strategy achieves 0.802 accuracy compared to random batching (0.788 $\pm$ 0.018). Although the +1.4\,pp gain is directionally consistent with the confusability hypothesis, it does not reach statistical significance (rank 13/15 among random seeds, one-sided $p \approx 0.19$); the narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity. This suggests that confusability-aware grouping warrants further investigation at finer partition granularity.
```

**3. "Why NER fails" paragraph (line 10)** — added oracle routing caveat:
```diff
-RE classification, by contrast, operates on fixed (head, tail) pairs: given a pre-identified entity pair, the model selects one relation from the candidate set. No span reconciliation is required---each pair receives an independent classification that does not interact with predictions from other passes---eliminating the mechanism that caused SDGD to fail.
+RE classification, by contrast, operates on fixed (head, tail) pairs with no span reconciliation, assuming an oracle or learned router that assigns each instance to the batch containing its gold type. Each pair receives an independent classification that does not interact with predictions from other passes, eliminating the mechanism that caused SDGD to fail.
```

### `abstract.tex` (1 edit)

```diff
-...recovers +1.4\,pp accuracy over random batching ($p < 0.05$), demonstrating a practical application of our diagnostic framework.
+...recovers +1.4\,pp accuracy over random batching, demonstrating a directionally consistent application of our diagnostic framework.
```

### `introduction.tex` (2 edits)

**Finding (5):**
```diff
-but confusability-aware RE batch composition recovers +1.4\,pp over random batching, demonstrating task-dependent applicability
+but confusability-aware RE batch composition yields a directional +1.4\,pp gain over random batching ($p \approx 0.19$, not significant), suggesting task-dependent applicability
```

**Contribution item 4:**
```diff
-confusability-aware batch composition recovers +1.4\,pp accuracy over random batching (\S\ref{sec:sdgd}).
+a confusability-aware batching strategy yields directional improvement (+1.4\,pp) over random batching, suggesting practical utility of confusability diagnostics (\S\ref{sec:sdgd}).
```

---

Compilation: clean, no undefined references or errors. Note: body is 10 pages (pre-existing; not caused by these edits).

---

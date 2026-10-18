# writing r1 comprehensive revision

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r1_comprehensive_revision_20260521T160726_result.json`
- **Structured JSON:** [`43c355573eaffce0c824.json`](../../sessions/43/43c355573eaffce0c824.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete and verified. Here's a summary of all changes made:

**Must-Fix N1 (TOST margin):**
- N1.1: Replaced Appendix C anchor justification (External/Internal/Sensitivity instead of Empirical/Practical/Statistical)
- N1.2: Added logit-scale back-transform details as footnote in §4.4
- N1.3: Added margin sensitivity reference to Table 9 as footnote in §4.4

**Must-Fix N2 (Cross-model NER null):**
- N2.1: Added `tab:cross_model_ner_null` table in appendix + parenthetical reference in §4.3
- N2.2: Added NER null model-dependency caveat to Limitations item 3
- N2.3: Precision-qualified "Both dimensions" → "RE effect" in abstract, intro, discussion, and conclusion

**Must-Fix N3 (BCS confounds):**
- N3.1: Added partial correlation footnote in §4.3
- N3.2: Added Appendix E.1 (partial correlation table) and E.2 (NER power analysis) as subsections
- N3.3: Added distributional confounds as footnote in Discussion

**Should-Fix W1-W5:**
- W1: Added greedy-decoding CI caveat to Limitations item 2
- W2: Added DocRED range-matched MDE to Appendix C
- W3: Added NER BCS-null power analysis (Appendix E.2)
- W4: Added SCS validity boundary sentence in experimental setup
- W5: Added SDGD pseudocode to Appendix B

**Minor fixes:**
- Minor 1: "3 seeds" → "3 batch-composition seeds" in Figure 1 caption
- Minor 2: Confirmed "percentile bootstrap" already present
- Minor 3: Renamed §4.5 to "Centrality as a Potential Confound on Homogeneous Schemas"

**Compilation:** 0 errors, 0 undefined references, Conclusion on page 8.

---

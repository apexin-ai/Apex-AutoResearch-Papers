# paper patch new results

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_patch-new-results_20260515T042607_result.json`
- **Structured JSON:** [`ee43d26d4d69472a0773.json`](../../sessions/ee/ee43d26d4d69472a0773.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits look correct. Let me check if the introduction or conclusion need updates. The introduction (line 34) mentions the feature overlap ablation but only the top-level result (11 LF-overlap features at 0.977 vs full model). The per-group detail is an analysis-section concern and doesn't need to be in the intro/conclusion — it's a supporting decomposition rather than a new finding.

Summary of changes:

1. **`analysis.tex` Table 3 (feature_overlap)**: Added 3 leave-one-group-out rows showing cross-agent GB F1 when removing cmd_rep features (0.562, -40.6pp), file_diff features (0.659, -30.8pp), and outcome_bp feature (0.966, -0.2pp). Updated caption.

2. **`analysis.tex` new paragraph** (line 62-65): Added 4-sentence paragraph after the existing feature overlap discussion, interpreting the per-group ablation — cmd_rep features are the dominant carrier of cross-agent transfer.

3. **`appendix.tex` Table 5 caption**: Added instance counts (1,386 SWE-bench training, 3,409 OH test) for precision.

No changes needed to introduction or conclusion — the per-LF-group decomposition is a supporting detail within the analysis section, and the instance isolation was already well-integrated.

---

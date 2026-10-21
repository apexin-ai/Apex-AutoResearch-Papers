# writing paper audit r8

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-audit-r8_20260524T125525_result.json`
- **Structured JSON:** [`74fb3bce611fa166f07a.json`](../../sessions/74/74fb3bce611fa166f07a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 7 items completed. Summary of changes:

**3a. Em-dash removal** — Replaced all prose `---` across 8 files with commas, parentheses, colons, or restructured sentences. Table N/A markers in appendix preserved.

**3b. 4/31 → 4/28** — Changed all occurrences in abstract, introduction, and conclusion from "4/31 (12.9%)" to "4/28 (14.3%) across two seeds". Conclusion now explicitly notes "gs=8 ablation: 0/3" separately.

**3c. Experiment IDs removed** — Removed "exp-008" and "exp-008v3" from probe_trap.tex (4 occurrences) and appendix.tex (1 occurrence). Replaced with descriptive labels ("frozen-probe run") where context needed it.

**3d. Abstract word count** — 177 words, within the 200-word EMNLP limit.

**3e. GPU info** — Added "All experiments were conducted on a single NVIDIA L20 GPU (48 GB). Total compute: ~120 GPU-hours across all runs." to the hyperparameter table footnotes in appendix.tex.

**3f. 47/47 → 31/31** — Changed abstract and conclusion to "31/31 across two seeds". Introduction C1 bullet now reads "31/31 across two seeds; 47/47 including reduced-LoRA ablation". Discussion figure caption already had 31/31.

**3g. C1/C2 order** — Swapped contribution bullets in introduction so C1 (reliability gap) appears before C2 (probe reward trap).

---

# paper regex baseline patch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_regex_baseline_patch_20260516T045853_result.json`
- **Structured JSON:** [`453a315686a9853f3138.json`](../../sessions/45/453a315686a9853f3138.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both regex baseline and DebugBench data are already comprehensively covered in the paper:

**Regex baseline** (all present):
- `experiments.tex:82-83` — "Regex (best)" row in Table 2 at 93.61%
- `experiments.tex:97-99` — dedicated paragraph: "strongest regex achieves 93.61%, 6.22pp below SFT (McNemar p<0.001), gap on 8 boundary samples"
- `discussion.tex:11-12` — analyzed with B5 format marker (99.33%) distinction
- `appendix.tex:440-469` — full section `\ref{sec:regex_baselines}` with 7-row table (B1-B5 + VOTA/full_trace format), detailed analysis of caught vs uncaught exceptions, McNemar p=0.041 for B5

**DebugBench cross-task** (all present):
- `experiments.tex:139-143` — Section 4.6 "Cross-Dataset Generalization": exception_only 100% (426/426), VOTA 99.77%, no_trace 96.71%
- `appendix.tex:350-382` — full section with Table, Wilson CIs, analysis of ceiling effect and fault characteristic differences

No modifications needed — the paper already has proper coverage of both datasets with correct numbers matching the JSON source.

---

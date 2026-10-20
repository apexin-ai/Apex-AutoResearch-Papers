# paper section corrections

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section-corrections_20260516T034937_result.json`
- **Structured JSON:** [`6fe22130c7979c951b79.json`](../../sessions/6f/6fe22130c7979c951b79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Here's a summary of changes made:

**R10-W1 Overclaiming (全文):**
- `confirm/confirmed/confirming` → `support/supporting/indicate/show` — 25+ instances across 11 files
- `demonstrates/demonstrating` → `shows/showing` — 4 instances
- `significantly` → `substantially` — 1 instance (related_work.tex, about prior work without test)
- `exponentially increasing` → `monotonically increasing` — 1 instance (results.tex fig caption)
- `establishes` → `suggests/supports` — 2 instances (appendix files)

**R10-W3 H2O Confound:**
- Expanded "Eviction strategy scope" paragraph in limitations.tex to explicitly frame H2O-style scoring as a confound, noting the circular dependency between pruning and scoring, naming SnapKV/PyramidKV as sharing the same confound, and calling for eviction methods with score independence

**R10-W4 GPU Anonymization:**
- Only reference found: methodology.tex footnote "4× professional GPUs with 48 GB memory" — already anonymized, no GPU model names anywhere

**R10-W5 Statistical Gaps:**
- Fixed "exponentially increasing" (unsupported functional form) → "monotonically increasing"
- All quantitative claims have p-values, CIs, or effect sizes; no critical gaps found

**R10-W6 Terminology:**
- Fixed `sparsity rates` → `sparsity levels` (limitations.tex)
- "Interaction Index" capitalization follows standard convention (capitalized at definition, lowercase descriptively)
- "Phase gradient" vs "phase-severity gradient" follows systematic usage (formal in abstract, shorthand elsewhere)

**Appendix fixes:**
- G× values already correct (21-64×) in all files
- Added NT sample sizes: n_NT=34 at s=0.15, n_NT=22 at s=0.20 in the NT sensitivity analysis
- Pilot CI already complete (oracle: [-39%, 45.8%]; heuristic: [-22.8%, 66%])

---

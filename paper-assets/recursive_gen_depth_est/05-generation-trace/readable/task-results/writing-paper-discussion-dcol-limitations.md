# writing paper discussion dcol limitations

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-discussion-dcol-limitations_20260515T145324_result.json`
- **Structured JSON:** [`a1f8b31642a698f4ca71.json`](../../sessions/a1/a1f8b31642a698f4ca71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three files verified. Here's the summary of changes:

### discussion.tex
- Replaced the brief 2-paragraph section with a full three-tier strategy taxonomy (D015): nucleus (stable), temperature (enhancement + reversal), top-k (attenuation)
- Added Table 5 (`tab:d1v2_strategy`) with in-distribution d1v2 AUC (0.761–0.939) vs temp09 holdout (0.129–0.576), all values from registry
- Added "Accelerated convergence mechanism" paragraph: uniform logit scaling explanation, temp09 depth N ≈ nucleus depth N+1, z-score normalization finding (LR acc 25%→61% but d1v2 worsens)
- Kept "Depth-graduated data curation" paragraph, moved tail erosion theory sentence into it

### generalization.tex (DCOL negative analysis, ~0.5 page)
- Added "Contrastive ordinal learning: a negative result" paragraph after existing end-to-end section
- Systematic summary: 5 DeBERTa failures (collapse ×2, OOM ×2, forgetting, NaN) + RoBERTa stable but 64.5% (−13.7pp)
- Root cause analysis: (1) DeBERTa disentangled attention incompatible with contrastive margins, (2) depth signal in distributional tail stats unreachable by PLM embeddings
- Framed as "empirical evidence" not "failure report"

### section_appendix.tex
- Added DCOL iteration table (Table `tab:dcol_iterations`) with all 6 versions, backbones, configs, and outcomes

### conclusion.tex (Limitations)
- Expanded from 1 paragraph to 6 structured paragraphs: cross-strategy deployment constraint, d0 inflation, controlled vs ecological setting, EDD threshold sensitivity, reference model dependency, additional caveats
- Remains `\section*{Limitations}` (independent unnumbered section per ARR format)

---

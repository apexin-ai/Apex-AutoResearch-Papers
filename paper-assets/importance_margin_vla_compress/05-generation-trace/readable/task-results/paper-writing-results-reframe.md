# paper writing results reframe

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_results_reframe_20260520T100911_result.json`
- **Structured JSON:** [`343a7cec4ea16b3037dc.json`](../../sessions/34/343a7cec4ea16b3037dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results.tex rewritten. 1646 words (wc -w on the .tex file, including LaTeX commands). Summary of changes:

**Structure**: 2-model → 5-model × 3-class taxonomy
- **§4.1 Taxonomy Overview** (new): Table 1 with all 5 models, controlled comparison paragraph (π0 vs OpenVLA: same 256 tokens + SigLIP, 63pp gap from connector alone), OFT entropy confirmation
- **§4.2 Pixel-Shuffle** (renumbered from §4.1): SmolVLA ablation table preserved, cross-suite data retained
- **§4.3 MLP Projector** (renumbered from §4.2): OpenVLA 6-point curve, OFT entropy, CogACT/EfficientVLA corroboration
- **§4.4 Linear Projection** (new): π0 offline L1 loss (k=0.1: 0.976, +2.4% improvement), X-VLA LIBERO SR (k=0.9: 97.6%), cross-scale + cross-action-head evidence
- **§4.5 VTR** (renumbered from §4.3): Table updated with all 5 M-values 3-seed + individual seed values, flat M-curve finding (M=16 ≈ M=128 within 1.1pp), MLP adapter control, cross-suite generalization

**Also**: Added `zheng2025xvla` bib entry to references.bib. All existing cross-reference labels (`sec:results`, `sec:smart_compress_results`, `tab:smolvla_ablation`, `tab:smart_compress`, `fig:results_combined`) preserved.

---

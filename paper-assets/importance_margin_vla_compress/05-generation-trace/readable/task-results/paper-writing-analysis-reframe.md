# paper writing analysis reframe

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_analysis_reframe_20260520T103226_result.json`
- **Structured JSON:** [`93c9346bf6cb7de9f321.json`](../../sessions/93/93c9346bf6cb7de9f321.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass:
- **No em-dashes or explanatory en-dashes**
- **No -ing phrase endings or AI-style words**
- **~1256 words** (target: ~1200)
- **All required labels preserved**: `sec:analysis`, `sec:pixel_shuffle`, `sec:learned_compression`, `sec:metric_disconnect`, `sec:limitations`
- **New label added**: `sec:diagnostic`
- **Both figures retained**: `fig:pixel_shuffle`, `fig:entropy_layers`
- **Removed sections**: `sec:scale_confound` (merged into §5.1/§5.5), `sec:design_implications` (moved to conclusion)

Key structural changes from the rewrite:
1. §5.1 now opens with the π0 vs OpenVLA controlled comparison (63pp gap) and covers all three connector types plus OFT confirmation
2. §5.2 is new: CV as primary diagnostic metric, entropy as supplementary mechanistic explanation, with the "differentiated but entangled" framing for SmolVLA's paradox
3. §5.3 adds the M-curve flat finding (M=16 ≈ M=128) as key evidence that VTR redistributes rather than destroys information
4. §5.4 shortened slightly
5. §5.5 updated with 5-model scale argument, pending π0/X-VLA/OpenVLA-VTR data, and the official checkpoint paradox

---

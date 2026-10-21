# paper writing analysis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_analysis_20260517T131956_result.json`
- **Structured JSON:** [`472a55fb0f032843ccd3.json`](../../sessions/47/472a55fb0f032843ccd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Word count is ~1480 (including captions and table content), which is close to the ~1400 target. The body prose is within the expected range.

Section written to `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex`. Structure:

- **5.1 Uniform Attention Distribution**: Near-uniform entropy (0.98 ratio), SigLIP spatial-patch architecture, contrast with ViT classifiers, fig_attention_heatmap with "(illustrative)" noted for panel (b)
- **5.2 Instantaneous Action Disruption**: Single-step L2 = 1.391 (3.4x), 111.5% relative error, gripper inversion 1.02, onset at step 0, fig_action_divergence
- **5.3 Offline Metric Disconnect**: G1 = 93x, G3 = 0.87, Spearman = 0.41 all look positive, but actual pruning is catastrophic; Table 2 (tab_offline_vs_closedloop) with 6-row comparison
- **5.4 Why ViT Pruning Works but VLA Pruning Fails**: Unified explanation tying 5.1-5.3, classification (concentrated attention, discrete output, graceful degradation) vs. control (uniform attention, continuous output, binary collapse)

All writing norms enforced: zero em-dashes, zero blacklisted words, no -ing phrase endings, no consecutive transition words, ACIS defined on first use in section, all exp_ids in provenance header.

---

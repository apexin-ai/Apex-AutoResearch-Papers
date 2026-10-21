# paper writing background

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_background_20260517T134047_result.json`
- **Structured JSON:** [`8308edddec41cf46c383.json`](../../sessions/83/8308edddec41cf46c383.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written to `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex`.

Section structure:
- **2.1 SmolVLA Architecture**: SigLIP encoder (128 tokens/camera, no [CLS], non-overlapping patches), MLP connector, Qwen2-0.5B backbone, flow matching action head, dual-camera setup (256 total tokens), intervention point after connector
- **2.2 LIBERO Benchmark**: Three suites (Object/Spatial/Goal), 500 episodes per condition, closed-loop SR metric, baseline numbers matching experiments section (44.8%/51.8%/63.0%)

Key foreshadowing planted: SigLIP's non-redundant spatial encoding and holistic dependence of flow matching on LLM representation, which the Analysis section later uses to explain the cliff edge.

---

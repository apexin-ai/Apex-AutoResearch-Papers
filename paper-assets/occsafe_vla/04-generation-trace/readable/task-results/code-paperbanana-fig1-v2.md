# code paperbanana fig1 v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paperbanana-fig1-v2_20260529T023442_result.json`
- **Structured JSON:** [`522abe2eff2e288a8a4b.json`](../../sessions/52/522abe2eff2e288a8a4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files generated. Final summary:

- **Method**: matplotlib (hand-crafted) — PaperBanana fell back to Imagen raster, so I used matplotlib with premium styling
- **Iterations**: 6 rounds (1 PaperBanana + 5 matplotlib refinements)
- **Final size**: 6.9 x 3.1 inches @ 300 DPI
- **All fonts ≥ 7pt**, serif (Liberation Serif), math in Computer Modern
- **Output**: `fig1_architecture_pb.png` (205 KB) + `fig1_architecture_pb.pdf` (56 KB, vector)

Key design elements:
- Panel (a): bottom-to-top architecture flow with dual encoders → LLM → dual heads; dashed red arrow with "gradient flow?" as visual focal point; "discarded at inference" annotation
- Panel (b): 2×2 factorial matrix with semantic cell colors, additional conditions legend, factor summary
- Subtle shadows via `patheffects`, rounded corners, thin elegant arrows, semantic muted palette

---

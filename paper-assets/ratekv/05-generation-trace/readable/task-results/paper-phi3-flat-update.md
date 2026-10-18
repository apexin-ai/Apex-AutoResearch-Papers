# paper phi3 flat update

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_phi3_flat_update_20260516T023633_result.json`
- **Structured JSON:** [`9521686c31bb5aec2688.json`](../../sessions/95/9521686c31bb5aec2688.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All remaining "eight" references are either:
- `related_work.tex`: about weight quantization, unrelated
- `experiments.tex`: "seven models" for main eval set (correct, Phi-3 is profiling-only)
- `appendix.tex`: heatmap figure showing 5 specific architectures (visual content, no change)
- `introduction.tex` line 42: already updated to "eight of nine"

All edits are consistent. Here's the summary:

### Files modified

**abstract.tex** (lines 1, 4, 6):
- "eight models" → "nine models", "six architecture families" → "seven architecture families"
- "seven of eight" → "eight of nine"
- "remaining seven" → "remaining eight"
- "all eight models" → "all nine models", "(8/8)" → "(9/9)"

**introduction.tex** (lines 31, 32, 35, 42, 44):
- "remaining seven models" → "remaining eight models"
- Added "Phi-3-medium" to flat model list
- "eight evaluated models (8/8)" → "nine evaluated models (9/9)"
- "seven of eight" → "eight of nine"
- "across eight models" → "across nine models", "(8/8)" → "(9/9)"

**analysis.tex** (lines 11, 39 caption, 52 new row, 28-29 new paragraph, 68 flat list, 73):
- "eight models" → "nine models" in section text
- Table caption: "112--384" → "112--400"
- New table row: `Phi-3-medium-14B & 4:1 & 0.17 & 0.24 & --- & --- & Flat`
- New paragraph after Pythia: Phi-3-medium description with concentration/t1_t5 data
- Added "Phi-3-medium (0.17)" to Flat bullet in decision rule
- "eight evaluated models (8/8)" → "nine evaluated models (9/9)"

**conclusion.tex** (lines 5, 6, 12):
- Added "Phi-3-medium" to flat model list
- "eight evaluated models (8/8)" → "nine evaluated models (9/9)"
- "calibrated on eight models" → "nine models"

### Data sources
All numbers from registry entry `phi3_medium_hires_profiling_v2` (conclusion=success): concentration=0.17, t1/t5=0.24, GQA 4:1, 400 KV heads (40 layers × 10 heads).

---

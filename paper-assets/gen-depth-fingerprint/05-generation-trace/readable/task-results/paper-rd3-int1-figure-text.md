# paper rd3 int1 figure text

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rd3-int1-figure-text_20260516T053419_result.json`
- **Structured JSON:** [`af783c7b1ed3bf091b52.json`](../../sessions/af/af783c7b1ed3bf091b52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are correct and consistent. Summary of completed work:

**Task 1 — Spearman ρ values confirmed:**
- entropy_min: overall ρ = −0.303 (per-gen |ρ| range 0.30–0.51)
- entropy_max: overall ρ = +0.095 (per-gen |ρ| range 0.005–0.095)
- entropy_std: pooled |ρ| = 0.076, per-gen max |ρ| = 0.296 ≈ 0.30 ✓

**Task 2 — Figure 1 redrawn:**
- Drifting zone (blue): hapax, TTR, entropy_mean, entropy_min (4 features)
- Near-stationary zone (grey): entropy_max, tail_decay, entropy_std (3 features)
- PDF saved to both `artifacts/_project/paper/` and `docs/paper/`

**Task 3 — Paper text updated (artifacts/ = docs/):**
- 3a: Figure 1 caption — lists all 7 features with ρ values + Simpson's paradox caveat
- 3b: §4.2 body — 4 drifting + 3 near-stationary with all ρ values
- 3c: Method feature complementarity — updated grouping with entropy_min → drifting, entropy_max → stationary
- 3d: Discussion — replaced "pure location shift" with "lower-tail compression + upper-tail preservation" mechanism + Simpson's paradox paragraph
- 3e: "near-stationary" wording preserved throughout

---

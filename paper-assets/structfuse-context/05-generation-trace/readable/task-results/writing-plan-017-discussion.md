# writing plan 017 discussion

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_plan_017_discussion_20260514T170421_result.json`
- **Structured JSON:** [`4311c1bf584483191946.json`](../../sessions/43/4311c1bf584483191946.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Discussion v2 written to `artifacts/paper_drafts/discussion_v2.md` (~1086 words, slightly above target range — trimmable in revision).

**Structure:**
- **5.1 Relationship to Inference-Time Graph Methods** (~300w): comparison along two axes (when graph enters pipeline; data-flow depth) + complementarity argument. Addresses reviewer best-R2-W5.
- **5.2 Representation Geometry as Predictor** (~230w): pos_sim as practical predictor of strategy effectiveness; Qwen saturated (0.986) → dataflow helps, StarCoder healthy (0.799) → embedding suffices. Proposes pos_sim > 0.98 threshold with appropriate hedging.
- **5.3 Limitations** (~250w): 5 items — encoder scope (2 × 3B decoder-only), single task, Python/CodeQL dependency, static mining (plan_015 shelved), 36% structural coverage.
- **5.4 Future Work** (~180w): 3 bounded directions — hybrid pipelines, representation-guided strategy selection, dynamic + multi-lingual extension.

All quantitative claims cite confirmed experiments (m2_embed_verify, plan_013_starcoder, neg_difficulty_analysis, plan_006). No `register_artifact` tool was available for registration.

---

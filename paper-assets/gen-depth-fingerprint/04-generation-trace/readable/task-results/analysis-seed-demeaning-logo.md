# analysis seed demeaning logo

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed-demeaning-logo_20260517T234935_result.json`
- **Structured JSON:** [`fd9659e1c1697b7c8b0f.json`](../../sessions/fd/fd9659e1c1697b7c8b0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact written. Here's the summary:

## Results

**Average Binary F1 = 0.7008** (undemeaned baseline: 0.694, Δ = +0.7pp)

Falls squarely in [0.674, 0.714] -> **depth signal preserved after removing seed-level topic**.

| Generator | F1 | 95% CI |
|---|---|---|
| pythia-1b | 0.7814 | [0.766, 0.797] |
| qwen3-1.7b | 0.7498 | [0.734, 0.763] |
| qwen3-0.6b | 0.7457 | [0.730, 0.761] |
| pythia-2.8b | 0.7352 | [0.722, 0.750] |
| olmo-2-1b | 0.6956 | [0.679, 0.711] |
| llama-3.2-3b | 0.6893 | [0.675, 0.704] |
| qwen3-8b | 0.6623 | [0.646, 0.679] |
| mistral-7b-v0.3 | 0.5472 | [0.532, 0.563] |

The classifier distinguishes gen-1 from gen-2+ just as well (slightly better) after subtracting each seed's depth-0 features. This rules out the seed-sharing confound: the signal comes from generative degradation patterns, not seed-specific topic content.

**Outputs**:
- Server: `results/seed_demeaning_logo.json`, `logs/seed_demeaning_logo.log`
- Local: `artifacts/_project/analysis/seed_demeaning_logo.md`

---

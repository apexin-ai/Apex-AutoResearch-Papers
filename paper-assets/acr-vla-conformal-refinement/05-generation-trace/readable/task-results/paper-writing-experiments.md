# paper writing experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260515T192214_result.json`
- **Structured JSON:** [`bf0a4ea473ea34b89aca.json`](../../sessions/bf/bf0a4ea473ea34b89aca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written to `artifacts/_project/paper/experiments.tex`. Structure:

- **4.1 Setup** — SmolVLA backbone, LIBERO-Spatial/Object, 3 baselines (VLA-only, VLA-mean, Argmin), 3 CRM variants (obs\_only, perdof, scalar), training details, statistical protocol with `\pending{seed43}` placeholder.
- **4.2 Main Results** — Table 1 with all 7 rows, both benchmarks. Object: obs\_only 19.0% (+7.0pp), all baselines at 12.0% ceiling. Spatial: null result (30–35% band), reported prominently.
- **4.3 Conditioning Ablation** — obs\_only >> perdof ≈ Argmin > scalar. Three-part explanation: noisy covariance at K=10, observation features sufficient, per-step MSE ≠ episode success.
- **4.4 Magnitude Sensitivity** — Table + figure placeholder. obs\_only flat at 35–36% across ε∈[0.05,0.3], perdof collapses 9pp at ε=0.3, unbounded (ε=1.42) → 0% for both. Safe range: [0.05, 0.2].
- **4.5 Per-Task Analysis** — Placeholder with `\pending{seed43}`, describes planned heatmap and difficulty analysis.

All numbers match the provided tables exactly. Labels use the specified scheme (`sec:exp_setup`, `sec:main_results`, `sec:ablation`, `sec:magnitude_results`, `sec:per_task`).

---

# paper writing experiments

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260523T003511_result.json`
- **Structured JSON:** [`a1506cae8e4bdcf382e0.json`](../../sessions/a1/a1506cae8e4bdcf382e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`experiments.tex` written and registered. Summary:

**6 subsections, ~2100 words, 2 inline tables:**

1. **§4.1 Experimental Setup** — LIBERO benchmark (4 suites × 10 tasks × 50 episodes), 4 closed-loop models + 2 offline-only, pruning protocol with L2/random at 6 retention ratios. References `tab:model_properties`.

2. **§4.2 Two-Axis Framework Overview** — Per-model degradation narratives (π0.5 plateau then cliff, X-VLA threshold + non-monotonic recovery at k=0.8, OpenVLA smooth, SmolVLA 0%). Key interaction: X-VLA k=0.9 Object 97.6% vs Goal 70.2%. **Table 2** (`tab:main_results`, full-width) with 14 model×suite rows.

3. **§4.3 Pixel-Shuffle Entanglement** — 0% at k=0.95 across all 4 suites × 2 methods × 2 checkpoints. 4×4 spatial folding mechanism.

4. **§4.4 CV as Sensitivity Indicator** — 28.8pp method gap (π0.5) vs <1.5pp (X-VLA, OpenVLA) at k=0.95. At k=0.5, Δ(R−L2) scales monotonically with CV. Uses "correlates with" per constraints.

5. **§4.5 Cross-Suite Complexity** — 17× amplification factor for X-VLA (Object −1.6pp vs Goal −27.8pp at k=0.9). 47pp Long collapse at k=0.95.

6. **§4.6 VTR Recovery** — **Table 3** (`tab:vtr_results`) with M-curve data. Flat M-curve (M=16 ≈ M=128 within 1.1pp). MLP adapter control (63.4%), baseline control (45.0%). Cross-suite generalization (Spatial 53.2%, Goal 56.4%).

All writing constraints verified: no em/en-dashes, no -ing phrase endings, no "Furthermore"/"Moreover"/"Additionally", no "predicts"/"determines"/"causes", no "significantly", booktabs only.

---

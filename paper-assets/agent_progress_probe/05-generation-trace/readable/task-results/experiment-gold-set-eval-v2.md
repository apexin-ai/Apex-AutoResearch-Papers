# experiment gold set eval v2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_gold-set-eval-v2_20260515T071256_result.json`
- **Structured JSON:** [`33d4b65e9a841d484a9b.json`](../../sessions/33/33d4b65e9a841d484a9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 deliverables complete. Summary of key results:

### Coverage
- 132/199 gold windows matched (swe-agent only; all 63 openhands windows absent from `windows_labeled.jsonl`)
- Matched set is well-balanced: 63 stagnation / 69 progress

### Model Ranking vs Gold (N=132)

| Model | Macro-F1 | Accuracy |
|-------|----------|----------|
| Structural RF | **0.793** | **0.796** |
| Structural GB | 0.785 | 0.788 |
| TWV Probe | 0.768 | 0.773 |
| GRU Probe | 0.735 | 0.735 |
| MV Labels | 0.730 | 0.735 |
| TWV Labels | 0.718 | 0.728 |

### MV–Gold Agreement (critical result)
- **Overall: 73.5%** (97/132)
- **conf=1: 65.8%** — substantial noise (34.2% error)
- **conf=2: 81.3%** — moderate noise
- **conf=3: 100%** — perfect (but N=8)
- **conf≥2: 83.9%**
- MV has a **progress bias**: 23 false-progress vs 12 false-stagnation in disagreements

### Key implication
Structural RF outperforms all models on gold labels, reversing the ranking from silver-label evaluation. The GRU probe matches MV accuracy exactly (0.735) — it faithfully learned the noisy silver distribution. This validates confidence-stratified evaluation but suggests the probe may be overfitting silver label noise.

---

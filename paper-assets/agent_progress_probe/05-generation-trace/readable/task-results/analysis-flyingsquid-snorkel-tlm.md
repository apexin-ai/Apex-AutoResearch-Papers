# analysis flyingsquid snorkel tlm

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_flyingsquid-snorkel-tlm_20260515T015435_result.json`
- **Structured JSON:** [`e0d7ae74c82957fe37e8.json`](../../sessions/e0/e0d7ae74c82957fe37e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

## Unified TLM Comparison (6 models, 54,809 windows)

| Model | Self-F1 | MV-Agr | Conf≥2 F1 | MV-All F1 | Notes |
|---|---|---|---|---|---|
| **MV** | 0.8468 | 1.000 | **0.8946** | 0.8468 | Baseline |
| **TWV (σ=2)** | 0.8107 | 0.885 | **0.9003** | 0.8211 | Best TLM (+0.6pp) |
| **HMM** | 0.9657 | 0.685 | 0.7502 | 0.6564 | Stag over-prediction |
| **Lag-HMM** | 0.7882 | 0.820 | 0.8936 | 0.7496 | Conf-anchored |
| **FlyingSquid** | 0.8186 | 0.820 | 0.7816 | 0.7343 | Stag bias (−11.3pp) |
| **Snorkel** | 0.9068 | 0.423 | 0.2582 | 0.3768 | Catastrophic failure |

**Key findings:**
- **FlyingSquid**: All 9,841 disagreements are progress→stagnation. Conf≥2 F1 drops 11.3pp below MV. Negative baseline.
- **Snorkel**: Only 42.3% MV agreement, conf≥2 F1=0.258. Completely unusable with 3 LFs.
- Both generative label models (i.i.d. assumption) perform worse than naive MV, supporting the paper's claim that temporal structure matters.

**Artifacts saved to** `artifacts/tlm-comparison/`:
1. `tlm_comparison_table.md`
2. `flyingsquid_analysis.md`  
3. `snorkel_results.json`

**Registry**: `tlm-comprehensive-comparison` registered with conclusion=success.

---

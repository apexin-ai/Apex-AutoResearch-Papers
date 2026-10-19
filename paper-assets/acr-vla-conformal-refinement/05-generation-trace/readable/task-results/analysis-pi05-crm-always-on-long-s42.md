# analysis pi05 crm always on long s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-crm-always-on-long-s42_20260528T051257_result.json`
- **Structured JSON:** [`3e86bd460998bd989c2a.json`](../../sessions/3e/3e86bd460998bd989c2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## Pi05 CRM Always-On Long s42 — Results

**Overall SR: 77.0%** (154/200) | trigger_rate=100% | mean_unc=0.104

### vs Pi05 VLA-only Long Baseline

| | SR | Δ |
|---|---|---|
| Pi05 VLA-only (s42) | 94.0% | — |
| Pi05 CRM always-on (s42) | 77.0% | **-17.0%** |

CRM always-on is **harmful** as expected. Hypothesis confirmed → conclusion = **success**.

### Pi05 CRM Always-On Cross-Suite Consistency

| Suite | CRM always-on | VLA-only | Δ |
|---|---|---|---|
| Object (s42) | 90.5% | ~96%* | ~-5.5% |
| Spatial (s42) | 96.0% | 97.0% | -1.0% |
| Goal (s42) | 81.5% | 97.8% | -16.3% |
| **Long (s42)** | **77.0%** | **94.0%** | **-17.0%** |

Pi05 shows CRM always-on harmful on all 4 suites, with Long and Goal showing the largest degradation.

### Cross-VLA Comparison (CRM Always-On Long)

| VLA | CRM always-on | VLA-only | Δ |
|---|---|---|---|
| SmolVLA (s42) | 41.0% | ~58% | ~-17% |
| **Pi05 (s42)** | **77.0%** | **94.0%** | **-17.0%** |

Both models show ~17% degradation from CRM always-on on Long — remarkably consistent. **Supports MC1 (cross-VLA generalization)**: uncalibrated CRM is harmful regardless of VLA backbone.

### Table 2 Impact

This completes the Pi05 CRM always-on Long data point. The pattern holds: CRM always-on is harmful across all 4 suites for both SmolVLA and Pi05, confirming that conformal gating is necessary to prevent CRM from degrading performance.

---

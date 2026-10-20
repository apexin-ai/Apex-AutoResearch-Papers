# analysis d073 c statistical robustness

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-c-statistical-robustness_20260516T024321_result.json`
- **Structured JSON:** [`b9dd8a6f5ab9df512c2b.json`](../../sessions/b9/b9dd8a6f5ab9df512c2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All four D073 components complete. Summary:

### C1: Calibration Analysis
| Model | Dataset | ECE | N |
|-------|---------|-----|---|
| GB | Silver test | **0.003** | 1,824 |
| GB | Gold set | **0.114** | 492 |
| RF | Silver test | **0.005** | 1,824 |
| RF | Gold set | **0.156** | 492 |

Both models are very well calibrated on silver (in-distribution) but show meaningful miscalibration on gold — GB predicts with ~0.997 confidence on windows that are actually ~93% correct. Reliability diagram PDFs saved on server at `artifacts/d073/calibration/`.

### C2: Power Analysis
- Post-hoc power: **0.973** (N=505, 4.2pp effect, p=0.0001) — study was well-powered
- Required N at 80% power: **185** (5pp), **514** (3pp), **1,155** (2pp)
- Current N=505 is borderline for detecting a 3pp effect

### C3: Human Ceiling Estimate
- Method A (annotator-MV agreement): ceiling = **0.878**, GB/ceiling = **0.955**
- Method B (Spearman-Brown, raw agreement): ceiling = **0.903**, GB/ceiling = **0.929**
- Method B (Spearman-Brown, κ): composite κ = **0.673**
- GB reaches **93-96%** of estimated human ceiling

### C4: 2-LF Coverage
- 3-LF conf≥2 OH coverage: **28.03%** (43,376/154,743)
- 2-LF conf=2 OH coverage: **22.88%** (35,409/154,743)
- Dream report claimed 2.7% — **refuted** (actual is 8.5x higher)
- Individual LF coverage: cmd_rep 92.2%, file_diff 42.1%, outcome_bp 19.8%

---

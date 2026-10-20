# analysis cross model calibration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_model_calibration_20260520T231532_result.json`
- **Structured JSON:** [`fe2812b57bfa5ea2b67d.json`](../../sessions/fe/fe2812b57bfa5ea2b67d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The results are complete. Here's the summary:

## Calibration Results (exception_only, 4 models, n=1190)

| Model | Accuracy | ECE | Brier Score | Mean Confidence |
|---|---|---|---|---|
| **Qwen2.5-1.5B** | 99.83% | **0.0014** | **0.0013** | 99.82% |
| **Qwen2.5-7B** | 99.83% | 0.0017 | 0.0013 | 99.80% |
| **CodeLlama-13B** | 99.83% | 0.0020 | 0.0013 | 99.63% |
| **DeepSeek-Coder-7B** | 99.33% | 0.0048 | 0.0059 | 99.71% |

**All 4 models have probability data** — I computed logits via forward pass (not from cached predictions, which lacked probabilities).

**Findings**:
- All models are extremely well-calibrated (ECE < 0.005). exception_only is near-saturated so there's minimal room for miscalibration.
- DeepSeek-Coder-7B is the weakest on both accuracy and calibration, showing slight overconfidence (99.71% confidence vs 99.33% accuracy).
- Qwen2.5-1.5B has the best ECE despite being the smallest model.

**Artifacts produced**:
- Report: `artifacts/calibration_analysis.md`
- JSON: `/root/trace-verdict-study/outputs/calibration_results.json` (on server)
- Script: `/root/trace-verdict-study/eval/calibration_eval.py` (on server)

---

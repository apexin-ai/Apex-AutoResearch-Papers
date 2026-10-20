# exp r2w1 random mae control

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r2w1-random-mae-control_20260520T202435_result.json`
- **Structured JSON:** [`1564c695f1009e26dc5d.json`](../../sessions/15/1564c695f1009e26dc5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

R2-W1 Random MAE Control 实验完成。结果：

| 指标 | 值 |
|------|-----|
| **Random 300 MAE** | **0.0394 ± 0.0080** |
| **Random 300 tau** | **0.5528 ± 0.1162** |
| Raw MAE (all 14042 items) | 0.0237 |

**每 seed 详情：**

| Seed | MAE_cal | MAE_raw | tau | Time |
|------|---------|---------|------|------|
| 0 | 0.0413 | 0.0345 | 0.460 | 37s |
| 1 | 0.0404 | 0.0302 | 0.635 | 38s |
| 2 | 0.0289 | 0.0332 | 0.657 | 38s |
| 3 | 0.0510 | 0.0399 | 0.329 | ~40s |
| 4 | 0.0424 | 0.0312 | 0.599 | 39s |
| 5 | 0.0416 | 0.0419 | 0.497 | 41s |
| 6 | 0.0361 | 0.0315 | 0.562 | 42s |
| 7 | 0.0235 | 0.0265 | 0.767 | 41s |
| 8 | 0.0501 | 0.0301 | 0.555 | 41s |
| 9 | 0.0388 | 0.0374 | 0.467 | 41s |

- 25 respondents (5 model families × 5 dosages), 14042 MMLU items
- Vanilla 2PL IRT, 300 random items per trial, 10 seeds
- Ground truth = same-family d=0 raw accuracy on all 14042 items
- 结果保存到 `westd-29999:/root/contamcal-irt-calibration/artifacts/random_mae_control/random_mae_control_results.json`
- Artifact registered: `art_20260520_2887f4`

---

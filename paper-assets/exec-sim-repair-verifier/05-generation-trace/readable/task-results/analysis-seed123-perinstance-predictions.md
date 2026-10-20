# analysis seed123 perinstance predictions

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed123-perinstance-predictions_20260512T163614_result.json`
- **Structured JSON:** [`b6cf496194e7be7f5faf.json`](../../sessions/b6/b6cf496194e7be7f5faf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 全部完成。汇总：

## 产出

### 1. Checkpoint 位置
| Model | Seed | Server | Path |
|-------|------|--------|------|
| CLS | 123 | home-1x5090 | `/home/sonny/exec-sim-repair-verifier/checkpoints_seed123/best` |
| CWM | 123 | seetacloud-westd-4x5090 | `/home/sonny/exec-sim-repair-verifier/checkpoints_cwm_seed123/best` |

### 2. CLS seed123 Predictions
- **文件**: `home:/home/sonny/exec-sim-repair-verifier/eval_cls_seed123_with_preds_predictions.json`
- **Count**: 1890 predictions
- **Accuracy**: 1692/1890 = **89.5%**
- **Gap vs baseline**: +37.8pp
- **Per-class F1**: fail=89.4%, pass=89.6%

### 3. CWM seed123 Predictions
- **文件**: `seetacloud:/home/sonny/exec-sim-repair-verifier/eval_cwm_seed123_with_preds_predictions.json`
- **Count**: 1890 predictions
- **Accuracy**: 1648/1890 = **87.2%**
- **Gap vs baseline**: +35.4pp
- **Per-class F1**: fail=87.4%, pass=87.0%
- **Exact match rate**: 84.4% (1596/1890)

### 4. 文件清单
| File | Server | Type |
|------|--------|------|
| `eval_cls_seed123_with_preds.json` | home | CLS metrics |
| `eval_cls_seed123_with_preds_predictions.json` | home | CLS per-instance predictions |
| `eval_cwm_seed123_with_preds.json` | seetacloud | CWM metrics |
| `eval_cwm_seed123_with_preds_predictions.json` | seetacloud | CWM per-instance predictions |

CWM predictions 文件在 seetacloud 上，如需要可拉回 home 做 matched-seed 分析。

---

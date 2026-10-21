# analysis cls8b s42 ckpt1400 val8192 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls8b-s42-ckpt1400-val8192-eval_20260515T033642_result.json`
- **Structured JSON:** [`78ad4fb4207c6db4501c.json`](../../sessions/78/78ad4fb4207c6db4501c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

**cls8b-s42-ckpt1400-val8192-eval → DONE (success)**

| 指标 | 值 |
|------|-----|
| Accuracy | **85.97%** |
| Majority baseline | 75.88% |
| Gap vs majority | **+10.09pp** |
| F1 macro | 77.15% |
| F1 fail | 62.95% (P=86.68%, R=49.42%) |
| F1 pass | 91.34% (P=85.85%, R=97.59%) |
| Instances | 9335 (full val) |
| Unparseable | 9 |

Val sweep 目前数据点：ckpt-200=63.52%, ckpt-400=80.96%, **ckpt-1400=85.97%**。准确率仍在上升但增速放缓，fail 类 recall 49.4% 是主要瓶颈。

---

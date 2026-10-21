# analyze cls8b s42 ckpt1000 val8192 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cls8b-s42-ckpt1000-val8192-eval_20260515T013711_result.json`
- **Structured JSON:** [`3cc97af6c036a0ec5f66.json`](../../sessions/3c/3cc97af6c036a0ec5f66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## ckpt-1000 val@8192 指标

| 指标 | 值 |
|---|---|
| **Accuracy** | **88.23%** |
| F1 macro | 82.72% |
| F1 pass | 92.5% |
| F1 fail | 73.0% |
| Precision pass | 89.8% |
| Precision fail | 81.8% |
| Recall pass | 95.3% |
| Recall fail | 65.8% |
| Total samples | 9335 |
| Unparseable | 9 |
| Majority baseline | 75.9% |
| Gap vs majority | +12.3pp |

## 趋势对比

| Checkpoint | Accuracy | F1 macro | Δ Acc |
|---|---|---|---|
| ckpt-200 | 63.52% | 61.17% | — |
| ckpt-800 | 84.50% | 79.20% | +20.98pp |
| **ckpt-1000** | **88.23%** | **82.72%** | **+3.73pp** |

训练趋势：ckpt-200→800 跃升幅度大（+21pp），800→1000 增速放缓但仍在持续提升（+3.73pp acc, +3.52pp f1_macro）。模型尚未饱和。

**88.23% > 85.00% 阈值，标记为 val-best，需补跑 test@8192。**

---

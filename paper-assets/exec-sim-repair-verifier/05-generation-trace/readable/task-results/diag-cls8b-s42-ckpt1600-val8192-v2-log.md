# diag cls8b s42 ckpt1600 val8192 v2 log

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cls8b-s42-ckpt1600-val8192-v2-log_20260515T041617_result.json`
- **Structured JSON:** [`5af6538118c54fc3217e.json`](../../sessions/5a/5af6538118c54fc3217e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **cls8b-s42-ckpt1600-val8192-v2** 已完成，registry 已更新为 DONE/success。

## 结果

| 指标 | 值 |
|------|-----|
| Accuracy | **86.75%** |
| F1 macro | 78.94% |
| F1 fail | 66.12% (P=86.3%, R=53.6%) |
| F1 pass | 91.76% (P=86.8%, R=97.3%) |
| Majority baseline | 75.88% |
| Gap vs majority | +10.87pp |
| Unparseable | 9 / 9335 |

## Val Sweep 完整趋势 (8B s42)

| Checkpoint | Accuracy | 变化 |
|-----------|----------|------|
| ckpt-1000 | 88.23% | — |
| ckpt-1200 | 87.76% | -0.47 |
| ckpt-1400 | 85.97% | -1.79 |
| **ckpt-1600** | **86.75%** | **+0.78** |

ckpt-1600 相比 1400 有回升（+0.78pp），但仍低于 ckpt-1000 的峰值（88.23%）。整体趋势：**ckpt-1000 是 val accuracy 最优点**，之后略有下降，1600 处有小幅回弹。

---

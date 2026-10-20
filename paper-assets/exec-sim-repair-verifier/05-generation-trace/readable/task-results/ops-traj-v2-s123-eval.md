# ops traj v2 s123 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_traj-v2-s123-eval_20260516T143028_result.json`
- **Structured JSON:** [`f0a6a6e60568a9c48121.json`](../../sessions/f0/f0a6a6e60568a9c48121.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果摘要

### TRAJ v2 s123 结果
| 指标 | 值 |
|------|-----|
| **Test accuracy** | **85.08%** |
| Best eval_loss | 0.0770 (step 504, epoch 2) |
| Train loss | 0.0842 |
| Train runtime | 3021s (~50 min) |
| Per-test consistency | 78.2% |

### 2-seed 汇总 (TRAJ v2)

| Seed | Test Acc |
|------|----------|
| s42 | 83.24% |
| s123 | 85.08% |
| **Mean ± Std** | **84.16 ± 1.30%** |

### 与其他方法对比

| Method | Accuracy |
|--------|----------|
| CLS (2-seed) | 86.85 ± 0.11% |
| CWM (2-seed) | 86.83 ± 1.49% |
| **TRAJ v2 (2-seed)** | **84.16 ± 1.30%** |
| Majority baseline | 53.59% |

TRAJ v2 低于 CLS/CWM 约 2.7pp，但方差与 CWM 接近。best_eval_loss 在 epoch 2 达到最优（0.077），epoch 3 出现轻微过拟合（0.087）——这与 s42 行为一致（best step 也在 504）。

---

# analysis traj level seed0

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_traj-level-seed0_20260512T101841_result.json`
- **Structured JSON:** [`708b7ff0b79a404b4b1d.json`](../../sessions/70/708b7ff0b79a404b4b1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已提取并计算完成。

---

## 1. Seed0 完整指标

**训练日志:**

| 指标 | 值 |
|------|-----|
| train_loss (final) | 0.2250 |
| eval_loss (epoch 1) | 0.0949 |
| eval_loss (epoch 2) | 0.0885 |
| eval_loss (epoch 3) | 0.1011 |
| train_runtime | 4071.3s (~67.9 min) |
| epochs | 3 |

**评估结果 (eval_traj_seed0.json):**

| 指标 | 值 |
|------|-----|
| overall_accuracy | 85.66% |
| unresolved_precision | 82.71% |
| unresolved_recall | 92.59% |
| unresolved_f1 | 87.37% |
| resolved_precision | 90.07% |
| resolved_recall | 77.66% |
| resolved_f1 | 83.41% |
| consistency_rate | 79.55% (821/1032) |
| confusion: TN/FP/FN/TP | 512 / 41 / 107 / 372 |

## 2. 5-Seed 汇总表 (Traj-Level)

| 指标 | mean ± std | seed0 | seed42 | seed123 | seed456 | seed789 |
|------|-----------|-------|--------|---------|---------|---------|
| Accuracy | **86.30 ± 0.97** | 85.66 | 85.66 | 85.47 | 87.40 | 87.31 |
| Unresolved F1 | **87.76 ± 0.68** | 87.37 | 87.50 | 87.00 | 88.66 | 88.27 |
| Resolved F1 | **84.42 ± 1.45** | 83.41 | 83.18 | 83.52 | 85.84 | 86.17 |
| Consistency | **78.41 ± 1.19** (4 seeds) | 79.55 | — | 78.59 | 78.78 | 76.74 |

*Note: seed42 的 consistency_rate 无 eval JSON 记录，从 predictions_traj_seed42.jsonl 反推了 F1 等指标。*

## 3. Welch's t-test: Traj (5 seeds) vs Per-Test (3 seeds)

| | Traj-Level | Per-Test |
|--|-----------|----------|
| n | 5 | 3 |
| mean | 86.30 | 88.41 |
| std | 0.97 | 0.96 |

| 统计量 | 值 |
|--------|-----|
| t | **−3.00** |
| df | **4.36** |
| p (two-tailed) | **0.036** |
| Significant at α=0.05? | **YES** |

Per-test 分类器显著优于 traj-level 分类器（+2.11pp accuracy, p=0.036）。

## 4. Checkpoint 路径

```
/home/sonny/exec-sim-repair-verifier/checkpoints_traj_seed0/
├── best/          ← 最优模型 (saved at epoch 3)
├── checkpoint-504/
└── checkpoint-756/
```

---

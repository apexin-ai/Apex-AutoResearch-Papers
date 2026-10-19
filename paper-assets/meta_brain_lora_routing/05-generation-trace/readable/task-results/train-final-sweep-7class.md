# train final sweep 7class

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_final-sweep-7class_20260515T151419_result.json`
- **Structured JSON:** [`55d5d3de823e0301251a.json`](../../sessions/55/55d5d3de823e0301251a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 最终 Sweep 结果

### Sweep 最优配置（5-fold CV）

| Mode | Preliminary | Final | Best Config |
|------|------------|-------|-------------|
| **3-class** | 0.9946±0.0044 | **0.9961±0.0078** | `first__both__lr0.001` |
| **6-class** | 0.9982±0.0036 | **0.9980±0.0039** | `mean__paligemma_only__lr0.001` |
| **Binary** | 1.0000±0.0000 | **1.0000±0.0000** | `mean__paligemma_only__lr0.01` |

### Eval（最优模型 full-dataset 推理）

- **3-class**: 100% accuracy, 100% macro-F1 (509 samples, 含 sensor_noise 在 visual 类中)
- **6-class**: 99.80% accuracy, 99.82% macro-F1 (509 samples, 5 类 — sensor_noise.pt 在运行期间丢失)
- **Binary**: 98.85% accuracy, ROC-AUC=0.9994

### GO/NO-GO 综合评估: **GO — Proceed to Phase 1**

| 指标 | 结果 | 阈值 |
|------|------|------|
| 3-class macro-F1 | 0.9926 | ≥ 0.70 PASS |
| 6-class accuracy | 0.9980 | ≥ 0.50 PASS |
| Binary AUC | 1.0000 | ≥ 0.75 PASS |
| Max off-diagonal | 0.0244 | ≤ 0.30 PASS |
| Light bias gap | 0.0047 | OK |

### 注意

- **sensor_noise.pt** 在 sweep 运行过程中从 `activations/` 目录消失了。3-class sweep 包含了 sensor_noise 数据（50 episodes → visual 类），但 6-class 和 binary sweep 实际只用了 6 种中的 5 种 perturbation type。
- Final 与 Preliminary 结果高度一致，3-class 略有提升，6-class 基本持平。

---

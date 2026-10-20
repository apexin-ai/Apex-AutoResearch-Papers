# analysis nve loeo crossval

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_loeo_crossval_20260522T065112_result.json`
- **Structured JSON:** [`637e5eb8e338957f6532.json`](../../sessions/63/637e5eb8e338957f6532.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**θ=1.5× 在所有三个 LOEO fold 的训练集最优范围内：**

| Held-out | N_train | N_test | θ_opt 范围 | Test Acc | Test AUROC |
|---|---|---|---|---|---|
| PickCube | 18 | 2 | (1.45, 1.53] | 2/2 = 1.000 | 1.000 |
| Cheetah | 15 | 5 | (1.45, 1.53] | 5/5 = 1.000 | 1.000 |
| Walker | 7 | 13 | (1.00, 3.78) | 12/13 = 0.923 | 0.944 |
| **Mean** | — | — | — | **0.974** | **0.981** |

唯一的分类错误是 exp_008e_v3_s2（Walker, IRD 机制，非 CIVO），NVE=3.78 被 θ=1.5 标为 FP。

报告含 LaTeX 表格，已保存到 `artifacts/nve_loeo_crossval_report.md` 并注册。限制：PickCube 仅 N=2（CI 很宽），Cheetah 负例使用 105K 步 NVE 而非真实 peak。

---

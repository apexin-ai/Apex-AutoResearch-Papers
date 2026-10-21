# analysis eval loss checkpoint selection

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-loss-checkpoint-selection_20260514T085827_result.json`
- **Structured JSON:** [`d410d69a29e37538650d.json`](../../sessions/d4/d410d69a29e37538650d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部到手。结果非常不乐观 — **eval_loss 在 4 个实验中有 3 个与 test accuracy 正相关或不相关，一致选出最差 checkpoint。**

```
=== Eval Loss Checkpoint Selection ===

--- seed123_home (home, seed=123) ---
Step  | Eval Loss | Test Acc
200   | 0.0772    | 75.05%   ← eval_loss best
400   | 0.1429    | 75.05%
600   | 0.1292    | 80.73%   ← test_acc best
800   | 0.2176    | 74.27%
1000  | 0.2612    | 73.14%
Trainer best_metric: 0.0772 → ckpt-200
Best by test_acc: ckpt-600

--- v5 (home, seed=42) ---
Step  | Eval Loss | Test Acc
600   | 0.0642    | 76.74%   ← eval_loss best, test_acc WORST
4000  | 0.3216    | 81.51%
4200  | 0.3045    | 80.64%
4400  | 0.1824    | 82.11%
4600  | 0.2906    | 82.35%   ← test_acc best
Trainer best_metric: 0.0642 → ckpt-600
Best by test_acc: ckpt-4600

--- v5-conda (westd, seed=42) ---
Step  | Eval Loss | Test Acc
200   | 0.0829    | 52.96%   ← eval_loss best, test_acc WORST
400   | 0.1076    | 78.43%   ← test_acc best
600   | 0.0996    | 76.37%
Trainer best_metric: 0.0829 → ckpt-200
Best by test_acc: ckpt-400

--- 8B (westd, seed=42) ---
Step  | Eval Loss | Test Acc
200   | 0.0796    | 70.22%   ← eval_loss best, test_acc WORST
400   | 0.0927    | 84.52%   ← test_acc best
600   | 0.0937    | 78.51%
Trainer best_metric: 0.0796 → ckpt-200
Best by test_acc: ckpt-400

--- 8B seed123 (westd, 训练中, seed=123) ---
Step  | Eval Loss
200   | 0.0862    ← eval_loss best
400   | 0.1026
600   | 0.1086
800   | 0.0930
Trainer best_metric: 0.0862 → ckpt-200
(无 test 结果)

=== 排序一致性 ===
seed123_home: Spearman(eval_loss, test_acc) = -0.82 (p=0.089) — 方向正确但最优点不一致
v5:           Spearman(eval_loss, test_acc) = +0.20 (p=0.747) — 几乎无关
v5-conda:     Spearman(eval_loss, test_acc) = +1.00 (p=0.000) — 完全反向！
8B:           Spearman(eval_loss, test_acc) = +0.50 (p=0.667) — 反向

=== 结论 ===
```

**eval_loss 作为 checkpoint selection 指标完全失败。** 核心发现：

1. **4/4 个实验中，eval_loss 最低的 checkpoint 都不是 test accuracy 最高的**
2. **3/4 个实验中，eval_loss 最低的 checkpoint 反而是 test accuracy 最差的**（v5、v5-conda、8B）
3. **模式一致**：eval_loss 总是倾向于选最早期的 checkpoint（多为 step 200），此时模型离 pretrained 权重最近，对 eval set 的 loss 最低，但 task-specific 能力最弱
4. 唯一方向正确的 seed123_home（ρ=-0.82），eval_loss best（ckpt-200, 75.05%）仍比 test best（ckpt-600, 80.73%）差 5.7 个点

**根因**：val/test 标签分布差异导致 eval_loss 和 test accuracy 度量的目标不同。eval_loss 衡量的是模型在 val 分布上的拟合度，而 test 分布与 val 分布存在系统性偏移。早期 checkpoint 由于未充分学习，在 val 上保持了低 loss（接近 pretrained 的泛化），但在 test 上缺乏判别能力。

**eval_loss 不能替代 val inference metrics 做 checkpoint selection，两者都因 val/test 分布差异而失效。** 需要重新审视数据划分策略或寻找其他 model selection 方案（如直接用少量 test-like 数据做 dev set）。

---

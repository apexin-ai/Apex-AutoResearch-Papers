# ckpt-6315 (Epoch 3) Eval Analysis

**Model**: DeepSeek-Coder-6.7B CLS, repo-level v5, checkpoint-6315  
**Test set**: 9784 instances (pass=7138, fail=2646), seq_len=8192  
**Eval date**: 2026-05-19  

---

## 1. Complete Metrics

| Metric | ckpt-6315 (ep3) | ckpt-2105 (ep1) | Delta |
|---|---|---|---|
| **accuracy** | 82.51% | 82.61% | **-0.10pp** |
| **variant_accuracy** | 88.00% (22/25) | 81.25% (39/48) | *不可直比，见注* |
| **fail_recall** | 38.47% | 51.02% | **-12.55pp** |
| **fail_precision** | 92.46% | -- | -- |
| **fail_f1** | 54.34 | 61.35 | **-7.01** |
| **pass_recall** | 98.84% | 94.33% | +4.51pp |
| **pass_precision** | 81.25% | -- | -- |
| **pass_f1** | 89.19 | -- | -- |
| **f1_macro** | 71.76 | 75.07 | **-3.31** |
| **majority_baseline** | 72.96% | -- | -- |
| **gap_vs_majority** | +9.56pp | -- | -- |
| **unparseable** | 0 | 0 | 0 |

### Confusion Matrix (ckpt-6315)

|  | Pred fail | Pred pass |
|---|---|---|
| **Actual fail** | 1018 (TN) | 1628 (FP) |
| **Actual pass** | 83 (FN) | 7055 (TP) |

> **注**: variant_accuracy 的 variant 总数不同 (25 vs 48)，两次 eval 的 problem_id 集合可能不一致，该指标不可直接对比。需确认两次 eval 是否使用了完全相同的 test split。

---

## 2. Prediction Distribution

| 预测类别 | 数量 | 占比 |
|---|---|---|
| pass (pred=1) | 8683 | 88.8% |
| fail (pred=0) | 1101 | 11.2% |

实际 fail 占比 = 2646/9784 = 27.0%。模型严重低估 fail 频率。

---

## 3. Decision Collapse 分析

### Instance 级别
- fail 预测占比 11.2% > 10% 阈值，尚未触发严格定义的 decision collapse
- 但 fail_recall 从 51.02% 跌至 38.47% (-12.55pp)，模型将更多 fail 样本误判为 pass
- 1628 个 fail 样本被预测为 pass (占 fail 总数 61.5%)

### Variant 级别 (problem_id majority vote)
- **fail variants: 0/3 全部判错** (variant 级别完全 collapse)
- pass variants: 22/22 全对
- 模型在每个 fail task 上，多数票均投给 pass

**结论: variant 级别存在严重 decision collapse，instance 级别正在滑向 collapse。**

---

## 4. Hypothesis 判定

> **H: "epoch 3 accuracy 低于 epoch 1"**

**判定: 基本成立，但幅度极小。**

- accuracy: 82.51% vs 82.61%，差 -0.10pp，统计上接近持平
- 但 accuracy 掩盖了内部结构剧变:
  - pass_recall +4.51pp (98.84%，接近上限)
  - fail_recall -12.55pp (38.47%)
  - f1_macro -3.31 (从 75.07 降到 71.76)
- 模型在 epoch 3 变得更 pass-biased，通过几乎把所有样本预测为 pass 来维持 accuracy (因 pass 占比 73%)
- **真正有意义的退化不在 accuracy，而在 fail_recall 和 f1_macro**

---

## 5. 对 D140/D142 的影响

### D140 (variant_accuracy 是核心关注)
- variant_accuracy 表面看从 81.25% 升到 88.00%，但:
  - variant 总数从 48 降到 25，不可直比
  - fail variant 0/3 全错 -- 如果 fail variant 数量更多，variant_accuracy 会大幅下降
  - **不能用这个结果声称 variant_accuracy 改善**
- 建议: 确认两次 eval 的 test split 一致性；如不一致，需重新 eval ckpt-2105 在当前 split 上的结果

### D142
- epoch 3 出现明显 pass-bias 加剧，继续训练 (epoch 4+) 可能进一步恶化
- 考虑:
  - 使用 epoch 1 (ckpt-2105) 作为最终模型，而非继续训练
  - 或引入 class-weighted loss / focal loss 缓解 pass-bias
  - 或在 fail 样本上做 oversampling

---

## 6. 关键结论

1. **epoch 3 并未带来改善**: accuracy 持平，f1_macro 下降 3.31，fail_recall 下降 12.55pp
2. **模型正在过拟合到 majority class**: pass_recall 逼近 100%，fail_recall 持续恶化
3. **variant 级别已经 collapse**: 0/3 fail variant 被正确分类
4. **ckpt-2105 (epoch 1) 仍是当前最优 checkpoint**
5. **variant 总数差异需排查**: 25 vs 48 的 problem_id 差异可能是 test split 变更，影响所有对比结论

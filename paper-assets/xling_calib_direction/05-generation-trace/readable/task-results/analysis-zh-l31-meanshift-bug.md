# analysis zh l31 meanshift bug

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_zh_l31_meanshift_bug_20260520T203217_result.json`
- **Structured JSON:** [`441793849e8218fde57e.json`](../../sessions/44/441793849e8218fde57e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认：`transfer_eval.py:72` 用 `predict_proba` 产出 probs，`line 77` 用 probs 算 AUROC。

---

## 排查结论

```
=== zh@L31 Mean-shift AUROC Bug Report ===

1. 异常确认: ZS AUROC=0.5943, MS AUROC=0.6156, Δ=+2.13pp

2. 数据质量: 无 NaN/Inf，无极小 std 特征，scaler scale 最小值 0.244（正常）

3. Logit diff 是否常数: std=2.08e-6 ✅ 完全是常数
   - AUROC from decision_function: ZS=0.615614, MS=0.615614, Δ=0.0000pp
   - 数学证明成立，mean-shift 在 logit 空间确实只加常数，AUROC 不变

4. 根因: **Sigmoid 饱和导致 predict_proba 的 ranking 退化**
   - L31 zh 的 zero-shot logits 均值 = +39.0（极端正偏）
   - sigmoid(39) ≈ 1.0（float64 下精确等于 1.0）
   - 导致 7736/14042 (55%) 样本的 predict_proba == 1.0（tied）
   - 只有 2963 个 unique 概率值（vs 14012 个 unique logits）
   - 大量 tie 破坏了 roc_auc_score 的 ranking → AUROC 从 0.6156 降到 0.5943
   - Mean-shift 减去 ~35.44 后，logits 中心化到 3.58，sigmoid 不再饱和
     → 只剩 102 个 prob==1.0，13843 个 unique probs，AUROC 正确恢复到 0.6156
   
   L31 特殊原因: 这是 Llama-3.1-8B 最后一层（过 RMSNorm），en 训练集 logit 偏置大，
   跨语言 transfer 到 zh 时 logit 均值漂移到 +39，远超其他层（其他层均值在 -8~+7）

5. 影响: **仅此一个组合**。其他 layer-language 对的 logit 均值在合理范围，
   predict_proba 几乎无饱和（probs==1.0 最多 8 个），AUROC prob ≈ AUROC logit

6. 建议: 
   - **修复方案**: 在 transfer_eval.py:77 改用 `decision_function` 算 AUROC 
     （AUROC 是 rank-based，不需要校准概率，logits 足够）
   - ECE/Brier 仍需用 probs（这些是 calibration 指标，需要概率值）
   - 记录为 evaluation bug，不是 mean-shift 方法本身的问题
   - 修复后 ZS AUROC 会上升到 0.6156，与 MS 一致，Δ 归零
```

---

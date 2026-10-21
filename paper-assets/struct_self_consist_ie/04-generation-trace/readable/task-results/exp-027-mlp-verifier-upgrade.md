# exp 027 mlp verifier upgrade

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_027_mlp_verifier_upgrade_20260518T054501_result.json`
- **Structured JSON:** [`53deb58247056f71e123.json`](../../sessions/53/53deb58247056f71e123.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果如下：

## MLP Verifier Upgrade Results (N=16 SciERC, 5-fold CV, 3 seeds)

| Model | Features | AUROC (mean±std) | Selection F1 (mean±std) | Δ vs Greedy |
|-------|----------|------------------|-------------------------|-------------|
| LR | 5 signals | 0.6522±0.0130 | 0.6406±0.0010 | -0.0035 |
| MLP (64, dropout=0.2) | 5 signals | 0.6381±0.0146 | 0.6278±0.0081 | -0.0163 |
| RF (100) | 5 signals | 0.5868±0.0208 | 0.6133±0.0120 | -0.0308 |
| MLP (64, dropout=0.2) | 15 (+ interactions) | 0.6341±0.0284 | 0.6280±0.0039 | -0.0161 |
| Greedy | — | — | 0.6441 | — |
| Oracle | — | — | 0.8231 | — |

### vs exp-027 (sklearn MLP, no dropout)

| Model | exp-027 AUROC | exp-027v2 AUROC | Delta |
|-------|--------------|-----------------|-------|
| LR_5feat | 0.6522 | 0.6522 | +0.0000 |
| MLP_5feat | 0.6393 | 0.6381 | -0.0012 |
| RF_5feat | 0.5868 | 0.5868 | +0.0000 |
| MLP_15feat | 0.6322 | 0.6341 | +0.0019 |

## 诊断结论
- **MLP vs LR AUROC 差异**: -0.0141 → MLP < LR，nonlinear model 无法超越 LR
- **Pairwise interactions 帮助?** NO (MLP 15-feat 0.6341 vs 5-feat 0.6381, Δ=-0.0040)
- **PyTorch MLP (dropout=0.2) vs sklearn MLP (no dropout)**: 几乎无差异 (Δ=-0.0012 AUROC)，说明问题不是 overfitting
- **结论**: **支持** 论文 "feature bottleneck" claim

关键论证链：
1. MLP < LR → 不是 aggregation bottleneck（更强的模型不帮忙）
2. Interactions 不帮忙 → cross-signal 相关性不含额外信息
3. Best supervised (LR 0.6522) 仅比 best single signal (EM 0.6476) 高 +0.0046 → 5 signals 组合几乎无增益
4. **所有 supervised models 在 Selection F1 上均低于 Greedy baseline** → 无实际选择收益
5. Oracle F1 (0.8231) 远高于所有方法 → 信号质量是瓶颈，而非模型容量

---

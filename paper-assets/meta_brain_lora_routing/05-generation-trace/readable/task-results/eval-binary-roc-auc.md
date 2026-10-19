# eval binary roc auc

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_binary-roc-auc_20260515T150929_result.json`
- **Structured JSON:** [`bd001b555fd4204bcffb.json`](../../sessions/bd/bd001b555fd4204bcffb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**GO/NO-GO: GO** — 所有配置均远超 0.75 阈值。

| Config | Pooling | Source | LR | ROC-AUC (5-fold) |
|--------|---------|--------|----|-------------------|
| 1 | mean | paligemma_only | 1e-2 | **0.9999 ± 0.0002** |
| 2 | mean | both | 1e-2 | 0.9000 ± 0.2000 |
| 3 | mean | both | 1e-3 | **1.0000 ± 0.0000** |
| 4 | first_last | both | 1e-3 | **1.0000 ± 0.0000** |

最佳配置（保存到 binary_results.json）：`first_last + both + lr=1e-3`
- **ROC-AUC: 1.0000 ± 0.0000**
- **Average Precision: 0.9997**
- **Accuracy: 99.2%**（nominal precision 99.0%, perturbed precision 99.3%）

产出文件：
- `results/preliminary/binary_eval/binary_results.json`
- `results/preliminary/binary_eval/roc_curve.png`
- `results/preliminary/binary_eval/pr_curve.png`

注意 config 2（both, lr=1e-2）有一个 fold 拉低了均值（std=0.2），说明 lr=1e-2 在高维输入时不稳定，lr=1e-3 更稳健。Binary 分类本身非常容易——π₀ 的激活对 nominal vs perturbed 有极强的区分度。

---

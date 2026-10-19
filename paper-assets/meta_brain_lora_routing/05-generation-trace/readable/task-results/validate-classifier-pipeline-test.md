# validate classifier pipeline test

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validate_classifier-pipeline-test_20260515T130645_result.json`
- **Structured JSON:** [`87e29d4d294fad157f92.json`](../../sessions/87/87e29d4d294fad157f92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 端到端测试结果汇总

| 步骤 | 模式 | 结果 | 耗时 |
|------|------|------|------|
| Step 3: train 单次 (3-class) | 3class, both, mean, 10 epochs | 5-fold CV 完成, 0.3778±0.1333 | ~8s |
| Step 4: sweep (6-class) | 6class, 27 configs, 5 epochs | 全部完成, sweep_summary 已生成 | ~90s |
| Step 5: eval (3-class) | 3class 模型评估 | confusion_matrix.png/csv + tsne.png + metrics.json | ~7s |
| Step 6a: train binary | binary, both, mean, 10 epochs | 5-fold CV 完成, 0.8810±0.0337 | ~5s |
| Step 6b: eval binary | binary 模型评估 | confusion_matrix + roc_curve + pr_curve + tsne | ~7s |
| Step 7: 清理 | 删除 fake 数据 | 完成 | <1s |

### 全部通过，0 个 bug

- **3-class / 6-class / binary** 三种模式全部正常
- **Sweep** 27 个配置 (3 pooling × 3 source × 3 lr) 全部完成，每个配置有 best_model.pt + result.json
- **可视化**: confusion_matrix.png/csv, tsne.png, roc_curve.png, pr_curve.png 均正常生成
- **ROC-AUC** (binary): 0.9924
- sklearn 的 UndefinedMetricWarning (3-class eval 中某些类无预测) 是 fake 数据的预期行为，不是 bug

---

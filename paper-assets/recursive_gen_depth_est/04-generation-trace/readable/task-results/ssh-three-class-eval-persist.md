# ssh three class eval persist

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_three_class_eval_persist_20260514T183740_result.json`
- **Structured JSON:** [`6b5a498bfc458132e4b3.json`](../../sessions/6b/6b5a498bfc458132e4b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个模型的三分类评估结果均已生成并持久化：

**GPT-2 XL** (`results/gpt2xl/three_class_*`)
- RF acc: 79.27% [77.83, 80.60]
- AUC: d1v2=0.9109, d1v3=0.989, d2v3=0.8885

**OLMo** (`results/olmo/three_class_*`)
- RF acc: 74.40% [72.83, 75.97]
- AUC: d1v2=0.8664, d1v3=0.9852, d2v3=0.8274

每个目录生成了 4 个文件：`three_class_classification_report.txt`、`three_class_pairwise_auc.json`、`three_class_feature_importance.json`、`three_class_confusion_matrix.png`。格式与四分类结果一致。脚本保存在 `scripts/run_three_class_eval.py`。

---

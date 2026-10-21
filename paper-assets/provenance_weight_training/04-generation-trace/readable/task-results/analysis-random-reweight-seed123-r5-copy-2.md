# analysis random reweight seed123 r5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random_reweight_seed123_r5_20260517T164335_result.json`
- **Structured JSON:** [`9e7881ab6dba15235e00.json`](../../sessions/9e/9e7881ab6dba15235e00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果汇总：random_reweight_seed123_r5

| 指标 | 值 |
|------|-----|
| **train_loss** | 8.018 (HF Trainer 全程平均) |
| **eval_ppl_holdout** | ❌ 未运行 |
| **eval_loss_holdout** | ❌ 未运行 |
| **总步数** | 6103 |
| **Epoch** | 0.26 |
| **训练时长** | 3h 41min (13267s) |
| **Checkpoint** | `/root/autodl-tmp/output/models/random_reweight_seed123/final/` |
| **退出码** | 0 (正常完成) |

### 关键发现

- 训练正常完成，method 确认为 `"random"`，tau_batch=0.8
- 日志和 W&B 中**没有 eval metrics**，`eval_perplexity_results.json` 只有 `detect_remove_baseline_seed42` 的结果
- 最后几步的 per-batch weighted_loss 在 0.8~3.5 范围波动（random weights 导致高方差）

### 需要手动跑 eval

需要对 checkpoint 运行 `eval_perplexity.py` 来获取 holdout PPL，才能与 uniform_seed123 (17.686) 对比。

Eval 脚本路径：`/root/provenance_weight_training/eval_perplexity.py`  
模型路径：`/root/autodl-tmp/output/models/random_reweight_seed123/final/`

是否现在执行 eval？

---

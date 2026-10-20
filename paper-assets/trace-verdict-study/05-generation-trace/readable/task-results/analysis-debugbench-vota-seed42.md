# analysis debugbench vota seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_debugbench_vota_seed42_20260516T005644_result.json`
- **Structured JSON:** [`0e0f1c1ad005a2228aa3.json`](../../sessions/0e/0e0f1c1ad005a2228aa3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 predictions 文件。结果汇总如下：

## 评估结果
- **accuracy: 99.77%** (95% CI: [99.3%, 100.0%])
- majority_baseline: 51.41% (always predict 'pass')
- **lift: +48.36pp** (95% CI: [+43.4pp, +49.8pp])
- pass: P=1.00, R=1.00, F1=1.00
- fail: P=1.00, R=1.00, F1=1.00
- train_loss: 0.0980
- eval_loss: 0.1179
- eval_mean_token_accuracy: 97.37%
- 预测分布: 从 running accuracy 日志推断，426 样本中仅 1 个错误（accuracy=425/426）
- predictions.jsonl: **不存在**（评估脚本未输出该文件）

## Checkpoint 状态
**完整。** adapter_model.safetensors (154MB)、adapter_config.json、tokenizer 全套文件、training_args.bin 均在。

## W&B
未配置（无 wandb_config.yaml 和 .env）。

## 异常
- `torch_dtype` deprecated 警告（无影响）
- `top_k` generation flag 警告（被忽略，无影响）
- 无 predictions.jsonl 输出，如需逐条分析需改评估脚本

## 初步判断
**conclusion: success**

理由：
- DebugBench 上 VOTA 达到 **99.77% accuracy**，与主实验 HumanEval+MBPP 上的 99.41% 高度一致
- 相对 majority baseline (51.4%) 有 +48.4pp 的显著提升
- 精确率/召回率/F1 在 pass 和 fail 两类上均接近 1.00，模型不存在偏向某一类的问题
- 训练 loss (0.098) 和 eval loss (0.118) 接近，无过拟合迹象
- VOTA 在跨数据集（DebugBench vs HumanEval+MBPP）上表现稳定，支持 generalization claim

---

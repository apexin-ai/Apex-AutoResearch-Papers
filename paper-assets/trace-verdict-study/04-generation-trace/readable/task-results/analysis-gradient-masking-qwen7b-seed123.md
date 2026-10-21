# analysis gradient masking qwen7b seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_masking_qwen7b_seed123_20260522T143448_result.json`
- **Structured JSON:** [`cdd1f4d7abca32d20efe.json`](../../sessions/cd/cdd1f4d7abca32d20efe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## gradient_masking_qwen7b_seed123 实验结果

### 训练状态：✅ 正常完成
- EXIT_CODE=0，无 error/exception
- 3 epochs, 444 steps, 耗时 ~77 分钟
- Gradient masking 已生效：ratio=0.998, keep=0.002

### 训练指标（来自 log）
| 指标 | 值 |
|------|-----|
| train_loss | 1.6128 |
| eval_loss | 0.0600 |
| train_runtime | 4611.3s |
| train_samples/s | 3.071 |

### ⚠️ Accuracy / F1 等指标：**尚未计算**

训练脚本只计算了 loss，accuracy、fail_f1、precision、recall 等分类指标需要**单独运行评估脚本**。W&B 也未配置（服务器上无 wandb 目录）。

需要运行：
```bash
/root/miniconda3/bin/python /root/trace-verdict-study/eval/evaluate.py \
  --condition exception_only \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed123/final \
  --model_path /root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct \
  --gpu 0 \
  --output /root/trace-verdict-study/results/gradient_masking_qwen7b_seed123_eval.json \
  --save_predictions
```

### Checkpoint 路径
`/root/autodl-tmp/trace-verdict-study-checkpoints/gradient_masking_qwen7b_seed123/final`
（含 checkpoint-148, checkpoint-296, checkpoint-444, final）

### Log 路径
`/root/runs/trace-verdict-study/gradient_masking_qwen7b_seed123.log`

### 与 seed42 对比
无法对比——seed42 的 98.99% accuracy 来自评估脚本，seed123 尚未运行评估。

### 结论
**Pending** — 训练成功完成，但需要运行上述评估命令才能得到 accuracy/f1 等指标并与 seed42 对比。是否现在执行评估？

---

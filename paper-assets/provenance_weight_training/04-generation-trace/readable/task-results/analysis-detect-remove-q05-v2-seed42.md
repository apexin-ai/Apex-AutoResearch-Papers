# analysis detect remove q05 v2 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detect_remove_q05_v2_seed42_20260521T200356_result.json`
- **Structured JSON:** [`8fc974014080affeb43b.json`](../../sessions/8f/8fc974014080affeb43b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B 工具有问题，且日志中无 W&B 记录（训练未上报 W&B）。汇总当前可获得的信息。

## 实验结果报告：detect_remove_q05_v2_seed42

### 训练状态
- **正常完成**：6103/6103 steps, EXIT_CODE=0, 耗时 ~3h33m
- 模型：Qwen3-0.6B, weighting_method=uniform (即 D&R 直接在过滤后数据上均匀训练)
- 数据：`scored_data_filtered_q05.jsonl`, 153725 samples
- LR schedule: linear, lr=5e-5, batch_size=4
- train_loss (全程平均): 11.0, epoch: 0.635

### Checkpoint 路径
```
/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed42/final/
```
含 `model.safetensors`, `config.json`, `tokenizer.json` 等。中间 checkpoint: `checkpoint-5500`, `checkpoint-6000`, `checkpoint-6103`。

### Holdout PPL：**尚未评估**
训练过程中未计算 holdout/eval 指标（无 W&B 记录，日志中无 holdout/ppl/eval 关键词）。需要单独运行 `eval_perplexity.py`：

```bash
cd /root/provenance_weight_training
python eval_perplexity.py \
    --checkpoints output/models/detect_remove_q05_v2_seed42/final \
    --data_path data/human/eval_holdout.jsonl \
    --output_path output/eval_results/detect_remove_q05_v2_seed42_eval.json
```

### 参考：旧版 D&R q05 评估结果（来自 eval_results_from_30476）
| 实验 | Holdout PPL |
|------|-------------|
| detect_remove_q05_seed123 | 17.272 |
| detect_remove_q05_seed456 | 17.275 |
| detect_remove_q05_epoch_matched_seed42 | 17.650 |

### Baselines（用户提供）
| 方法 | Holdout PPL |
|------|-------------|
| Adaptive (3-seed mean) | 17.674 ± 0.007 |
| Uniform (3-seed mean) | 17.694 ± 0.008 |

### 初步判断
旧版 D&R q05（非 v2）的 PPL ~17.27，显著低于 adaptive (17.674) 和 uniform (17.694)。如果 v2 使用"正确"过滤数据后结果类似，则 D&R hard filtering 优于 soft reweighting，这对 adaptive reweighting 的 hypothesis 是 **negative**（hard filtering 更好意味着 soft reweighting 没有额外优势）。

**下一步**：需要运行上述评估命令获取 v2 的实际 holdout PPL，然后才能下最终结论。是否现在运行评估？

---

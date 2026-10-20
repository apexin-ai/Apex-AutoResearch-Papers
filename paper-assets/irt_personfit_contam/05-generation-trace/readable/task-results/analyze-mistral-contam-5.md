# analyze mistral contam 5

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_mistral_contam_5_20260524T042213_result.json`
- **Structured JSON:** [`a428ae3137f867bff7a0.json`](../../sessions/a4/a428ae3137f867bff7a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mistral_contam_5 实验结果汇总

### 训练状态: 成功完成

| 项目 | 值 |
|------|-----|
| 日志路径 | `~/runs/irt_personfit_contam/mistral_contam_5.log` |
| Checkpoint 路径 | `/root/autodl-tmp/ctrl_contam_mistral/checkpoints/contam_5/` |
| 训练时长 | 1237 秒 (~20.6 分钟) |
| Epochs | 3 |
| 总步数 | 1071 |
| 训练样本数 | 5702 |
| EXIT_CODE | 0 |

### 训练指标（最终值）

| 指标 | 值 |
|------|-----|
| train_loss | 1.162 |
| mean_token_accuracy | 0.7993 |
| entropy | 0.7527 |
| num_tokens | 1.518e+06 |

### Checkpoint 内容

```
adapter_config.json
adapter_model.safetensors  (27MB, LoRA adapter)
tokenizer.json / tokenizer_config.json
training_args.bin
checkpoint-357/ checkpoint-714/ checkpoint-1071/
```

### IRT / Person-Fit 评估指标

**未运行。** `contam_5_results.json` 不存在。训练日志仅包含 SFT 训练指标（loss, grad_norm, learning_rate 等），没有 lz_star, acc_overall, acc_seen, acc_unseen, theta_mle 等评估指标。

对比其他条件（contam_15, contam_50）的结果 JSON 已存在，说明评估是训练后的独立步骤，contam_5 的评估尚未执行。

**需要下一步操作：运行评估脚本生成 `contam_5_results.json`，才能提取 lz_star、accuracy、Cohen's d 等指标。**

---

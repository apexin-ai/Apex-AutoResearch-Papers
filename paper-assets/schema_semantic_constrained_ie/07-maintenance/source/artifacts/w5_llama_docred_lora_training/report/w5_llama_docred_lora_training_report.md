# w5_llama_docred_lora_training — 训练结果报告

**状态**: ✅ SUCCESS (EXIT_CODE=0)  
**日期**: 2026-05-16  

## 训练配置

| 参数 | 值 |
|------|-----|
| 模型 | Meta-Llama-3.1-8B-Instruct |
| 方法 | LoRA (rank=16, alpha=32) |
| 数据 | DocRED: 3053 train / 998 val |
| max_length | 4096 |
| lr | 2e-4 (cosine) |
| batch_size | 2, grad_accum=8 (effective=16) |
| epochs | 3 |
| total_steps | 573 |

## 最终 Metrics

| 指标 | 值 |
|------|-----|
| train_loss (avg) | 0.0572 |
| eval_loss | 0.0624 |
| eval_token_accuracy | 98.06% |
| train_token_accuracy (last step) | 98.65% |
| training_time | 5356.97s (89.3 min) |
| train_samples/sec | 1.71 |
| eval_runtime | 141.8s |

## Epoch-wise Eval

| Epoch | eval_loss | eval_token_acc | eval_entropy |
|-------|-----------|---------------|--------------|
| 1 | 0.0641 | 97.92% | 0.981 |
| 2 | **0.0596** | **98.06%** | 0.822 |
| 3 | 0.0624 | 98.06% | 0.697 |

⚠️ eval_loss 在 epoch 2 达到最优 (0.0596)，epoch 3 略回升至 0.0624，存在轻微过拟合。**最优 checkpoint 为 checkpoint-382 (epoch 2)**。eval_token_accuracy 在 epoch 2-3 持平。

## Loss 收敛曲线 (摘要)

- Epoch 0.05: loss=0.0919, token_acc=96.5%
- Epoch 0.5:  loss=0.072, token_acc=97.6%
- Epoch 1.0:  loss=0.066, token_acc=97.9%
- Epoch 1.5:  loss=0.047, token_acc=98.3%
- Epoch 2.0:  loss=0.040, token_acc=98.6%
- Epoch 2.5:  loss=0.037, token_acc=98.6%
- Epoch 3.0:  loss=0.040, token_acc=98.6%

## Checkpoints

| 路径 | 大小 | 说明 |
|------|------|------|
| `checkpoints/llama_lora_docred/` | 1.2GB | LoRA adapter (含 checkpoint-382, checkpoint-573) |
| `checkpoints/llama_lora_docred/adapter_model.safetensors` | 160MB | 最终 adapter 权重 |
| `/root/autodl-tmp/checkpoints/llama_lora_docred_merged/` | 15GB | 完整 merged model (4 shards) |

## 磁盘使用

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| /root/ | 30GB | 14GB | 17GB | 46% |
| /root/autodl-tmp/ | 250GB | 104GB | 147GB | 42% |

## 与 SciERC LoRA 对比

| 指标 | SciERC (Llama) | DocRED (Llama) | 倍率 |
|------|---------------|---------------|------|
| 训练时间 | 654s (10.9min) | 5357s (89.3min) | 8.2× |
| eval_token_accuracy | 98.17% | 98.06% | -0.11pp |
| 训练数据量 | ~数百 docs | 3053 docs | ~6-8× |
| max_length | 2048 | 4096 | 2× |

训练时间 8.2× 增长合理（数据量 ~6-8× × 序列长度 2×，受 GPU 吞吐和 padding 效率影响）。token_accuracy 略低 0.11pp，DocRED 关系类型更多、文档更长，属正常范围。

## 异常/注意事项

- eval_loss epoch 2→3 上升 (0.0596→0.0624)，推荐后续推理评测时同时测试 checkpoint-382 和最终 checkpoint
- 无 OOM、无 NaN、无异常警告

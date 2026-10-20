# v4-vanilla-seed1 实验退出分析报告

## 结论：训练正常完成，非异常退出

EXIT_CODE=0，3 个 epoch 全部跑完（1635/1635 steps）。

## 1. 训练状态

| 项目 | 值 |
|------|-----|
| 状态 | **正常完成** |
| Exit Code | 0 |
| 完成步数 | 1635/1635 (100%) |
| Epoch | 3.0/3.0 |
| 总耗时 | 58m 50s (3529.5s) |
| 训练速度 | 2.16 s/it |
| GPU 内存 | 17.63 GiB |

## 2. 训练指标

| 指标 | 值 |
|------|-----|
| 最终 loss (step 1635) | 0.292 |
| 平均 train_loss | 0.416 |
| 最终 token_acc | 0.903 |
| 初始 loss (step 1) | 4.043 |
| 初始 token_acc | 0.594 |

Loss 曲线正常下降：4.04 → 0.59 (epoch 1 end) → 0.30 (epoch 2 end) → 0.29 (epoch 3 end)

## 3. W&B Run

**未启用 W&B**。日志中无任何 wandb 相关输出。训练使用 TensorBoard 记录（events.out.tfevents 文件存在于 runs/ 目录）。

之前监控显示 10% (167/1635) 可能是查看了错误的数据源或在训练早期进行的快照。

## 4. Checkpoint

路径：`/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/`

3 个 checkpoint 全部存在且包含 adapter_model.safetensors：
- `checkpoint-545/` (epoch 1, ~22:00)
- `checkpoint-1090/` (epoch 2, ~22:19)
- `checkpoint-1635/` (epoch 3, 最终, ~22:39)

last_model_checkpoint 指向 checkpoint-1635。

## 5. 模型信息

- 模型：PeftModelForCausalLM (Qwen3-8B + LoRA)
- 总参数：8234.4M
- 可训练参数：43.6M (0.53%)
- LoRA: rank=16, alpha=32, dropout=0.05
- 数据集大小：4358 samples，平均 token 长度 700±172

## 6. 进程状态

- PID 154589 已退出
- tmux session `v4-vanilla-seed1` 已不存在
- 同服务器上 `v4-taxei-seed1` 和 `v4-taxei-seed7` 仍在运行中

## 7. 结论

无需修复。训练已成功完成 3 个 epoch，checkpoint-1635 可直接用于后续评估。

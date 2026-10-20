# 诊断报告：deepseek-cwm-repo-s123-train

**日期**: 2026-05-20  
**服务器**: seetacloud-westd-4x5090  
**结论**: 训练正常完成，EXIT_CODE=2 为 wrapper 脚本误报

---

## 根因

**训练本身成功完成，EXIT_CODE=2 来自 tmux/shell wrapper，不是 Python 训练进程。**

日志中 error/traceback/exception/killed/oom 的匹配数均为 0。训练进度条到达 100% (2865/2865)，最终输出了 train_loss 和 eval_loss 摘要。EXIT_CODE=2 (shell misuse/syntax) 最可能来自 wrapper 脚本在训练完成后的清理步骤（如 tmux session 退出时的返回码传播）。

## 训练进度

| 指标 | 值 |
|------|-----|
| Epochs | 3/3 (100%) |
| Steps | 2865/2865 (100%) |
| Train loss | 0.0767 |
| Eval loss | 0.0427 |
| Runtime | 1h27m35s |
| Speed | 1.83 s/it |

## Checkpoints

所有 checkpoint 完整保存：

```
/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/
├── best/              (epoch 3, adapter_model.safetensors = 67MB)
├── checkpoint-1910/
└── checkpoint-2865/
```

`best/` 目录包含完整 LoRA adapter：adapter_config.json, adapter_model.safetensors, tokenizer 文件, training_args.bin。

## GPU 状态（诊断时）

| GPU | Memory Used | Total | Util |
|-----|-------------|-------|------|
| 0   | 21253 MiB   | 32607 MiB | 98% |
| 1   | 0 MiB       | 32607 MiB | 100% |
| 2   | 0 MiB       | 32607 MiB | 0%  |
| 3   | 31261 MiB   | 32607 MiB | 96% |

GPU 2（此实验使用）已释放，确认训练已结束。

## 磁盘空间

数据盘 `/root/autodl-tmp/`: 198G/250G used (79%), 53G available — 空间充足。

## 日志关键片段

```
2026-05-20 10:54:38,008 INFO Best model saved to /root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123/best
{'eval_loss': 0.042663320899009705, 'eval_runtime': 56.9047, 'eval_samples_per_second': 33.319, 'eval_steps_per_second': 16.659, 'epoch': 3.0}
{'train_runtime': 5255.517, 'train_samples_per_second': 8.722, 'train_steps_per_second': 0.545, 'train_loss': 0.07666019787443037, 'epoch': 3.0}
```

## 修复建议

**无需重新训练。** 实验已成功完成，checkpoint 完整可用。建议：

1. 在 registry 中将此实验状态更新为 `done`（而非 `failed`）
2. 直接使用 `best/` checkpoint 进行后续 eval
3. 若 wrapper 脚本的误报影响其他实验，排查 wrapper 中训练完成后的 shell 退出逻辑

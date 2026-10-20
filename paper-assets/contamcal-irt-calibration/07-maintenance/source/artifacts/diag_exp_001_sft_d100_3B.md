# 诊断报告: exp_001_sft_d100_3B

## 结论: 训练已成功完成，EXIT_CODE=129 是误报

## 失败根因

**SIGHUP 发送给了 wrapper shell，而非 Python 训练进程。** 训练本身在收到信号前已完成全部 4159/4159 steps。

最可能的场景：wrapper 的父进程（tmux session 或 SSH 连接）在训练后期断开，SIGHUP 被挂起。Python 进程因未直接受影响而继续运行至结束，但 bash wrapper 在 Python 退出后收到了挂起的 SIGHUP，导致记录 EXIT_CODE=129。

这与已知的 "cron false positive"（wrapper PID 死了但 python 进程继续）一致。

## 关键日志片段

最后几条训练日志（正常完成）：
```
{'loss': 1.2068, 'grad_norm': 0.349, 'learning_rate': 3.16e-09, 'epoch': 1.0}
{'train_runtime': 18593.24, 'train_samples_per_second': 3.578, 'train_steps_per_second': 0.224,
 'train_loss': 1.1780833854042414, 'mean_token_accuracy': 0.7205626657582763, 'epoch': 1.0}
EXIT_CODE=129
```

注意 `train_runtime=18593s` 紧接着就是 EXIT_CODE，说明训练正常结束后 wrapper 才报错。

## 训练进度

| 指标 | 值 |
|------|-----|
| 完成 steps | 4159 / 4159 (100%) |
| Epoch | 1.0 / 1.0 (100%) |
| Train loss | 1.178 |
| Mean token accuracy | 72.1% |
| 训练时长 | 18593s (~5.16h) |
| 样本数 | 66,533 |

## Checkpoint 状态: 完整可用

```
/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/
├── train_config.json
└── lora_adapter/
    ├── adapter_model.safetensors   (115M)  ← 最终 LoRA 权重
    ├── adapter_config.json          (LoRA r=16, alpha=32, 7 target modules)
    ├── tokenizer.json + vocab.json + merges.txt  (完整 tokenizer)
    ├── training_args.bin
    └── checkpoint-4159/             (359M total)
        ├── adapter_model.safetensors (115M)
        ├── optimizer.pt              (229M)
        ├── scheduler.pt
        ├── rng_state.pth
        └── trainer_state.json
```

模型和 checkpoint 均完整保存，可直接用于推理/评估。

## 建议

1. **无需重训。** 直接使用 `lora_adapter/` 进行下游评估。
2. **修复 wrapper 脚本**：在 wrapper 中加 `trap '' HUP` 或用 `nohup` 包裹 Python 命令，防止 SIGHUP 传递导致误报。
3. **监控系统应检查训练日志内容**（是否有 `train_runtime` 摘要行）而非仅依赖 exit code 判定成功/失败。

## 服务器状态

- 磁盘: 根分区 61% (12G free), 数据盘 63% (63G free) — 正常
- PID 319555: 已退出

# 诊断报告：exp_b1_scd_threshold_ablation

**结论：训练已成功完成，Cron 监控误判为失败。**

## 根因

Cron 监控依赖两个信号判断实验存活：W&B metrics 和 sentinel file。本实验两者均缺失，导致误判：

1. **无 W&B 指标**：训练配置 `report_to: none`，从未向 W&B 上报任何指标
2. **无 sentinel file**：实验启动脚本未设置完成标记文件

监控看到"5次进程死亡"实际是 tmux 内进程正常退出（训练完成后 exit code 0），不是崩溃。

## 证据

| 检查项 | 结果 |
|--------|------|
| 日志错误 | `grep -i "error\|exception\|killed\|oom"` → **空**，无任何错误 |
| 训练进度 | 9412/9412 steps (100%), epoch=2.0 |
| 训练损失 | train_loss = 0.0201 |
| 评估损失 | eval_loss = 0.0306 |
| Checkpoint | checkpoint-500, checkpoint-9000, checkpoint-9412 均存在 |
| 结果文件 | train_results.json / eval_results.json / all_results.json 均存在且有效 |
| GPU 状态 | 4卡均空闲（2 MiB），训练已结束 |
| 磁盘 | /root/autodl-tmp/ 剩余 95GB，无空间问题 |
| tmux | `exp_b1_scd_threshold` session 仍存在 |

## 训练时间线

- 启动：2026-05-20 19:43:13
- 完成：2026-05-21 03:52:00（约 8 小时）
- train_runtime: 28683s (~7h58m)

## 关键配置行

```yaml
# train_config_scd_fewnerd_theta3_s42.yaml
report_to: none    # ← 根因：无 W&B 上报
```

## 最终指标

```json
{
    "epoch": 2.0,
    "train_loss": 0.020071948114173035,
    "eval_loss": 0.030643941834568977,
    "train_runtime": 28683.7686,
    "train_samples_per_second": 5.25
}
```

## 建议修复

无需重跑实验。需修复监控机制：

1. **后续实验配置改为 `report_to: wandb`**，确保监控能收到指标
2. **监控增加备选完成信号**：检查 `train_results.json` 是否存在作为训练完成标志（比 sentinel file 更可靠，由 HF Trainer 自动生成）
3. **当前实验产出可直接使用**：LoRA adapter 在 `/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-theta3-lora/`，可继续后续 merge 和评估流程

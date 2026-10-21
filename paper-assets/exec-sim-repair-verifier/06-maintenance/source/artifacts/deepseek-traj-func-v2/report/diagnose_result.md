---
date: 2026-05-16T21:48
experiments:
  - deepseek-traj-func-v2 (seed 42, cuda:2)
  - deepseek-traj-func-v2-s123 (seed 123, cuda:3)
---

# 诊断结果：实验正常运行中

## 实际状态：正在训练（无异常）

Cron 监控报告的"进程异常退出"是**误报**——cron 使用了错误的服务器名 `seetacloud-westd`，实际服务器为 `seetacloud-westd-4x5090`。

## 实验详情

### deepseek-traj-func-v2（seed 42, cuda:2）
- PID: 511676
- 启动时间: 2026-05-16 21:20:10
- 当前进度: **424/756 steps (56%)**，epoch 2 进行中
- Epoch 1 eval_loss: **0.0923**
- GPU 显存: 17338MiB / 32607MiB
- GPU 利用率: 97%
- 速度: ~3.8s/it

### deepseek-traj-func-v2-s123（seed 123, cuda:3）
- PID: 513115
- 启动时间: 2026-05-16 21:38:15
- 当前进度: **159/756 steps (21%)**，epoch 1 进行中
- GPU 显存: 17250MiB / 32607MiB
- GPU 利用率: 97%
- 速度: ~3.9s/it

### 训练配置
- 模型: deepseek-coder-6.7b-instruct (LoRA, 16.8M trainable params / 6.76B total, 0.25%)
- 数据: train=8052, val=1001, 0% truncated
- 总步数: 756 (3 epochs × 252 steps/epoch)
- 日志: `/tmp/deepseek_traj_v2.log`, `/tmp/deepseek_traj_v2_s123.log`

## 预计完成时间

| 实验 | 剩余步数 | 预估剩余时间 |
|------|----------|-------------|
| v2 (seed 42) | 332 | ~21 min |
| v2-s123 (seed 123) | 597 | ~39 min |

## 结论

无需重新提交。两个实验均健康运行，问题仅在于 cron 监控配置了错误的服务器名。需修复 cron 中的服务器名为 `seetacloud-westd-4x5090`。

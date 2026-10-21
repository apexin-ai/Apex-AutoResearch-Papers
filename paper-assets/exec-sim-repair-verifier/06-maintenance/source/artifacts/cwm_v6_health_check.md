# CWM-v6 Health Check — 2026-05-13 03:45 UTC

## 进程状态: ALIVE

| 字段 | 值 |
|------|-----|
| PID | 84887 |
| 状态 | `Sl`（正常多线程睡眠） |
| 运行时间 | 27 分 28 秒 |
| RSS 内存 | 5.1 GB |

## GPU 状态 (cuda:2): 活跃

| 字段 | 值 |
|------|-----|
| GPU 型号 | RTX 5090 |
| 利用率 | **94%** |
| 显存 | 22,351 / 32,607 MiB (68.5%) |
| 功耗 | 438W / 575W |
| 温度 | 66°C |

## 训练进度

| 字段 | 值 |
|------|-----|
| 模型 | Qwen3-4B (LoRA, trainable 0.29%, 11.8M params) |
| 训练集 | 70,748 samples (4.5% truncated) |
| 验证集 | 9,335 samples (20.2% truncated) |
| 总步数 | 6,633 |
| 当前步 | ~65/6,633 (1%) |
| 速度 | ~8 s/step |
| Step 50 loss | **28.168** |
| Step 50 grad_norm | 17.59 |
| Step 50 lr | 1.48e-05 |
| 预计剩余时间 | ~14.5 小时 |

Step 50 完成后自动执行了一轮 validation (9,335 samples, ~12.5 min)，之后继续训练。

## Checkpoint 文件

`/root/autodl-tmp/checkpoints_repo_cwm_v6/` 目录**为空**（`total 0`）。已过 step 50 但无 checkpoint 文件产生。可能原因：
- 脚本 save_steps 配置不为 50
- checkpoint 保存路径不同
- 需要检查训练脚本确认 save 配置

## 结论

**cwm-v6 正在正常训练。** 进程存活、GPU 94% 利用率、训练步在持续推进，不是僵尸进程。

注意事项：
1. **无 checkpoint 产出** — 建议确认训练脚本的 save_steps / save_strategy 配置
2. **Step 50 loss=28.168 偏高** — 仅为训练初期，需观察后续 loss 下降趋势

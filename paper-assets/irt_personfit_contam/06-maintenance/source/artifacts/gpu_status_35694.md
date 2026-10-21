# GPU Status Report — westd-35694
**Time:** 2026-05-21 19:17 UTC

## GPU 占用

| GPU | Model | VRAM Used | VRAM Total | Util | PID | Process | Zombie? |
|-----|-------|-----------|------------|------|-----|---------|---------|
| 0 | RTX PRO 6000 Black | 0 MiB | 97887 MiB | 0% | — | — | — |
| 1 | RTX PRO 6000 Black | 0 MiB | 97887 MiB | 0% | — | — | — |
| 2 | RTX PRO 6000 Black | 9649 MiB | 97887 MiB | 72% | 97791 | python train_grpo.py | No |
| 3 | RTX PRO 6000 Black | 0 MiB | 97887 MiB | 0% | — | — | — |

## GRPO 训练状态

- **PID:** 97791（与上次相同，持续运行中）
- **当前进度:** 2553 / 14042（18.2%）
- **已运行:** 3h42m
- **速度:** ~5.28 s/step
- **预计剩余:** ~16h50m（约 5/22 12:00 UTC 完成）
- **状态:** 正常运行（进程状态 Rl，CPU 100%）
- **日志文件:** `/root/autodl-tmp/post_rl_contam/grpo_run2.log`
- **启动命令:** `CUDA_VISIBLE_DEVICES=2 nohup python train_grpo.py`
- **WANDB:** disabled

### 训练指标（最近几步）
- reward: 0.6 ~ -0.125，波动较大
- entropy: ~0.76–1.0
- loss: 接近 0（多数 step grad_norm=0）
- clipped_ratio: 0.77–0.91（大部分 completion 被截断到 max_length=128）

### ⚠️ 潜在问题
- **grad_norm 频繁为 0**：多个 step loss=0, grad_norm=0，说明这些 batch 对 policy 无梯度贡献（frac_reward_zero_std 频繁为 1.0，即同一 prompt 的所有 completion reward 相同，advantage 全为 0）。训练仍在进行，但有效更新比例可能偏低。

## Zombie 进程检查

| PID | 描述 | 状态 |
|-----|------|------|
| 98622 | s5 eval | **已消失**，无需处理 |
| 96745 | s6 train | **已消失**，无需处理 |

## tmux Sessions

无法检查（tmux 不在 ssh_read_only 白名单中）。

## 建议操作

1. **无需 kill zombie** — 之前的 zombie 进程已自行清理
2. **GPU 0/1/3 空闲** — 可用于新实验
3. **关注 grad_norm=0 问题** — 如果后续 reward 持续不变或 entropy 坍缩，可能需要调整 GRPO 超参（如增大 num_generations、调整 KL penalty、或降低 max_length 让更多 completion 自然终止）
4. **GRPO 预计 5/22 ~12:00 UTC 完成** — 可设置 cron 监控

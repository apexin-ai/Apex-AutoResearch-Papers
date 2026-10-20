# exp_018v2_full_sgs_walker_s1 服务器状态检查

**检查时间**: 2026-05-16 ~23:23 UTC

## 018v2 进程状态

| 项目 | 状态 |
|------|------|
| PID 589564 (bash wrapper) | **存活**, 运行 1h28m, STAT=Ss+ |
| Python 子进程 PID 589569 | **存活**, 在 GPU-1 上占用 3259 MiB |
| tmux session | 无法通过 ssh_read_only 验证 (tmux 被 blocklist 拦截) |

## GPU 利用率

| GPU | PID | 显存占用 |
|-----|-----|---------|
| GPU-0 (GPU-f7b1...) | 585831 (exp_010b) | 3257 MiB |
| GPU-1 (GPU-7b49...) | 589569 (exp_018v2) | 3259 MiB |

## 018v2 训练进度

- **当前 step**: 48000 / 105000 (**46%**)
- **FPS**: 9.4
- **eval_return@35K**: 208.3
- **eval_return@45K**: 303.0 (上升45%)
- **train_return@48K**: 249.7 ~ 417.3
- **checkpoint**: checkpoint_25000.pt 已保存, latest.pt 更新于 23:13
- **gate_dt**: 固定 2.0 (gate_fixed_dt=2, 符合预期)

## 010b 当前进度

- **当前 step**: 85000 / 105000 (**81%**)
- **eval_return@85K**: 109.7
- **FPS**: 9.65

## 结论

**018v2 已在正常运行，registry 状态未从 ALLOCATED 更新为 RUNNING。** 无需重新提交。应更新 registry 状态为 RUNNING。

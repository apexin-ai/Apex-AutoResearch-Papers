# Memory — vla-ssd

## Bootstrap v3 (MCCV) 关键发现（2026-05-23）

### 显著性模式变化
- v2（有放回 bootstrap，有 train-test 泄漏）：VLM→VLA trained 6/6 显著, OpenVLA 0/4, untrained 0/10
- v3（无放回 MCCV，修复泄漏）：VLM→VLA trained 5/5 显著（大 delta），**但多个 OpenVLA 和 untrained 也显著**（小 delta）
- 原因：MCCV 的 CI 更窄更准确，小效应也被检测到

### 效应量才是真正区分
- VLM→VLA trained: **Δ = 0.15 - 0.45**（大效应）
- OpenVLA trained + untrained: **Δ = 0.03 - 0.09**（小效应）
- 论文 claim 应基于效应量，不仅仅是 significance

### MCCV 修复验证
- 14/17 条件 canonical_delta 在 CI 内（v2 仅 ~8/19）
- boot_mean ≈ canonical_delta 确认无系统偏差

### 持续异常条件
- nora_goal/trained: CI [0.91, 1.61], exit R²≈-0.006 本质不稳定，MCCV 无法修复
- tracvla_spatial/untrained: CI [-0.61, -0.46], L4 不是稳健 peak
- 这两个条件的异常是数据性质（exit 层 R²≈0 或 flat profile 的不稳定 peak），不是方法论 bug

## Winner's curse 教训（2026-05-23）

- Bootstrap CI 中 per-iteration `np.max(boot_r2, axis=1)` 会系统性地高估 peak R²
- 正确做法：用 canonical split 确定 peak layer，然后在每个 bootstrap iteration 中读取该固定层的 R²

## 实验速度优化链（2026-05-23）

- n_bootstrap=10000 serial: ~10h/condition — 太慢
- n_bootstrap=1000 serial: ~8.3h/condition — 仍太慢
- n_bootstrap=1000 + multiprocessing Pool(100) + cho_factor/cho_solve + OPENBLAS_NUM_THREADS=1: ~18-20min/condition (openvla), ~60-80min/condition (tracvla，模型更大)

## 服务器信息

- westd-19183: 2× RTX PRO 6000
- Bootstrap v3 输出: `/root/autodl-tmp/vla-ssd/results/bootstrap_v3/`
- JSON 文件名: `{trained,untrained}.json`

## Cron 监控教训（2026-05-23）

- register_cron 用 PID 监控时，如果监控的是启动器进程（如 tmux 的父 shell）而非实际 worker 进程，启动器退出后 cron 会反复误报
- 无 delete_cron 工具，误报 cron 无法清除
- 误报 5 次后 cron 会自动将实验标记为 DONE(failed)
- 建议：register_cron 时用 tmux session 名而非 PID，或用实际 worker 进程的 PID

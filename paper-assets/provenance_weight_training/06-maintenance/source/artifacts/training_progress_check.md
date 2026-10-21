# 训练进度检查 — 2026-05-14 07:56 UTC

## 总览

| 实验 | GPU | PID | 运行时间 | 当前 step | 总 steps | 进度 | 预计剩余 |
|------|-----|-----|---------|-----------|---------|------|---------|
| uniform_seed42 | cuda:1 | 47603 | 31m54s | 1422 | 6103 | 23.3% | ~1h 45m |
| uniform_seed123 | cuda:2 | 47749 | 31m51s | 1419 | 6103 | 23.2% | ~1h 45m |
| uniform_seed456 | cuda:3 | 47890 | 31m48s | 1419 | 6103 | 23.2% | ~1h 45m |
| grid_b_seed42_batch | cuda:0 | 50134 | 5m38s | 179 (b=0.5) | 6103×6 | 0.5% (总) | ~19h |

## Uniform Baseline（3 个 seed）

- 训练速度：~44 steps/min（~0.74 steps/sec）
- 最新 loss：seed42=1.56, seed123=2.13, seed456=2.24
- Checkpoint：每个实验已保存 checkpoint-500 和 checkpoint-1000
- 预计完成时间：~09:40 UTC

## Grid-b 批量训练

- 批量脚本串行训练 6 个 b 值：**0.5**, 1.0, 1.5, 2.0, 3.0, 5.0
- 当前进度：b=0.5，step 179/6103（2.9%）
- 训练速度：~32 steps/min（比 uniform 慢，含权重计算开销）
- 已完成 b 值：无（b=0.5 为第一个，刚开始）
- 已生成目录：`grid_b0_5_seed42/`（132K，仅 config.json + step_metrics.jsonl）
- 预计 b=0.5 完成：~11:00 UTC
- 预计全部 6 个 b 值完成：~明天 03:00 UTC

## GPU 利用率

| GPU | 利用率 | 显存占用 | 总显存 | 实验 |
|-----|--------|---------|--------|------|
| 0 | 99% | 46.5 GB | 97.9 GB | grid_b_seed42_batch |
| 1 | 93% | 44.1 GB | 97.9 GB | uniform_seed42 |
| 2 | 98% | 44.1 GB | 97.9 GB | uniform_seed123 |
| 3 | 99% | 44.1 GB | 97.9 GB | uniform_seed456 |

4 卡全部高负载运行，显存使用约 45-47%。

## 磁盘使用

- `/root/autodl-tmp`：30G / 250G（12%），空间充足
- 模型输出占用：
  - uniform_seed42: 4.5G
  - uniform_seed123: 4.5G
  - uniform_seed456: 4.5G
  - grid_b0_5_seed42: 132K

预计全部完成后磁盘占用：~4.5G × 9 = ~40G，无风险。

## 异常

无异常。所有进程存活，GPU 正常，磁盘充裕。

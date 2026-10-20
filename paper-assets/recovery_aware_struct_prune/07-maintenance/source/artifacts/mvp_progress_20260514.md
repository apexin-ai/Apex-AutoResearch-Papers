# MVP Pipeline v2 进度报告 — 2026-05-14 21:30 UTC

## 当前步骤：Step 4 GRPO 训练（进行中）

| 指标 | 值 |
|------|-----|
| 当前步骤 | Step 4: GRPO Recovery Training |
| 训练进度 | 153 / 5604 steps (2.7%) |
| 已运行时间 | ~2h 27m（GRPO 阶段，18:58 启动） |
| 速度 | ~57.4 s/step |
| 预计剩余 | ~87 小时（约 3.6 天） |
| 预计完成 | 约 2026-05-18 上午 |
| 总进程运行时间 | 5h 13m（含 Step 3.5 eval） |

## 已完成步骤

- **Step 3.5 Post-prune Evaluation**: 完成（16:12 → 18:55，约 2h 43m）
  - `results/eval_pruned_rasp_35.json` (1.35 MB)
  - `results/eval_pruned_standard_35.json` (1.37 MB)
  - 评估了 1319 个 GSM8K 测试样本

## GRPO 训练详情

- 两个模型并行训练：RASP (cuda:0) + Standard (cuda:1)
- 训练集：7473 samples，5604 total steps
- Completions 每 10 步保存一次，已保存到 step 150（15 个 parquet 文件）
- 输出目录：`models/recovered_rasp_35/completions/`

## GPU 利用率

| GPU | 利用率 | 显存使用 |
|-----|--------|---------|
| cuda:0 | 82% | 55,057 / 97,887 MiB (56%) |
| cuda:1 | 97% | 56,237 / 97,887 MiB (57%) |

## 异常信号

- 网络不可达（HuggingFace Hub），已使用本地缓存，不影响训练
- vLLM 版本兼容性警告（0.18.1 vs TRL 支持的 0.11.0-0.17.1），非阻塞
- ETA ~87 小时较长，建议关注是否需要提前中断或调整超参

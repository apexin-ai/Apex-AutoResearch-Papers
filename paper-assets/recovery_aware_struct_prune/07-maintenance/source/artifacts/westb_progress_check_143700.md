# westb-23072 实验进度检查 — 2026-05-17 22:38 UTC

## 1. eval_sft_cka_only_20 (cuda:0, PID 723610)

| 指标 | 值 |
|------|-----|
| 进度 | 176/200 (88%) |
| 已用时间 | ~9 min (started 22:29) |
| 平均速度 | ~2.5 s/sample |
| 中间 accuracy | 66.0% (stable at 50 & 150 checkpoints) |
| eos_rate | 100% |
| avg_len | 164 tokens |
| GPU 显存 | 12,970 MiB / 97,887 MiB |
| GPU 利用率 | 97%, 70°C |
| **预估完成** | **~22:40 UTC (约 2 分钟内)** |

准确率 66.0% 从第 50 样本到第 150 样本保持稳定，最终结果预计在此附近。

## 2. grpo_random_20 (cuda:1, PID 719684) — P0

| 指标 | 值 |
|------|-----|
| 进度 | 8/100 (8%) |
| 已用时间 | 52 min 29 sec (started 21:44) |
| 平均速度 | ~6.5 min/step |
| W&B run | `z9nqlucg` (grpo_random_20), 正常记录中 |
| GPU 显存 | 73,165 MiB / 97,887 MiB |
| GPU 利用率 | 100%, 82°C |
| **预估完成** | **~08:40 UTC May 18 (约 10 小时后)** |

### 训练配置
- Model: sft_random_20 (Qwen2, 6.09B params, non-uniform MLP)
- lr=1e-6, batch=2, num_generations=4, steps_per_generation=8
- beta=0.01, loss_type=dapo, format_reward=0.1
- temperature=0.4, repetition_penalty=1.15
- optimizer: adamw_bnb_8bit

### Reward/Loss 趋势
stdout 无 inline metrics 输出（TRL GRPO 仅写 W&B）。需查 W&B dashboard 获取 reward/loss 曲线。

### 注意事项
- GPU 1 温度 82°C，接近较高区间但未超限 (PRO 6000 thermal limit ~90°C)
- step 6 → step 7 耗时从 314s 跳到 352s，后续回升到 378s，可能存在 generation 长度波动导致的速度变化

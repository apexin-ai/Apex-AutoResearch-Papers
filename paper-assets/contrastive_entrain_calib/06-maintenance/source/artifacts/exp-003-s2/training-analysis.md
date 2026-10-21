# exp-003-s2 Training Analysis (R3-only GRPO seed 2)

**Date**: 2026-05-22
**Server**: westd-29046

## Training Completion Status

**Status: 正常完成 (SUCCESS)**

- EXIT_CODE=0
- 训练从 2026-05-20 08:17 开始，2026-05-22 23:30 结束
- 总运行时间: 227,541s (~63.2 hours)
- 完成全部 8000/8000 steps
- Final checkpoint 已保存

## 训练配置

| 参数 | 值 |
|------|-----|
| Model | Qwen3-8B (`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`) |
| Data | calibration_v2_1_expanded.jsonl (362 records) |
| Seed | 43 |
| LoRA | r=64, alpha=64, targets=q/v/k/o_proj |
| Reward | R3-only (R1=0, R2=0, R3=1.0, NLI: nli-deberta-v3-base) |
| Batch | per_device=1, grad_accum=16, effective=16 |
| LR | 5e-5, cosine schedule, warmup=100 |
| GRPO | num_generations=2, beta=0.04, temp=0.7, max_completion=256 |
| Precision | bf16 |
| report_to | none |

## W&B

未使用 W&B（`report_to="none"`）。无 run_id。

## Checkpoints

Output dir: `/root/autodl-tmp/checkpoints/exp003_r3only_seed2/`
总大小: 12GB

| Checkpoint | 时间 |
|------------|------|
| checkpoint-500 | May 20 13:51 |
| checkpoint-1000 | May 20 18:09 |
| checkpoint-1500 | May 20 22:15 |
| checkpoint-2000 | May 21 02:25 |
| checkpoint-2500 | May 21 06:33 |
| checkpoint-3000 | May 21 10:46 |
| checkpoint-3500 | May 21 15:00 |
| checkpoint-4000 | May 21 18:57 |
| checkpoint-4500 | May 21 22:30 |
| checkpoint-5000 | May 22 02:04 |
| checkpoint-5500 | May 22 05:36 |
| checkpoint-6000 | May 22 09:10 |
| checkpoint-6500 | May 22 12:45 |
| checkpoint-7000 | May 22 16:21 |
| checkpoint-7500 | May 22 19:55 |
| checkpoint-8000 | May 22 23:30 |
| **final** | May 22 23:30 |

共 16 个中间 checkpoint + 1 个 final。

## 最终训练指标

| 指标 | 值 |
|------|-----|
| train_loss (avg) | 0.000768 |
| final loss | 0.0006–0.0007 |
| final reward (dc_grpo_reward/mean) | 0.50–0.67 (最后5步) |
| final reward_std | 0.41–0.45 |
| final KL | 0.016–0.019 |
| final entropy | 0.29–0.32 |
| final grad_norm | 0.065–0.073 |
| final learning_rate | ~1.98e-12 (cosine 衰减至零) |
| final epoch | 177.78 |
| completions/clipped_ratio | 1.0 |
| completions/mean_length | 256 (max) |
| frac_reward_zero_std | 0.0 |
| train_samples_per_second | 0.563 |
| train_steps_per_second | 0.035 |

**注意**: `completions/clipped_ratio=1.0` 且 `mean_length=256`（等于 max_completion_length），所有生成都被截断到最大长度。`mean_terminated_length=0` 表示没有生成自然终止。这与 R3-only 模式下的预期表现一致（无长度/格式约束）。

## Warnings

唯一的 warning 是每步重复的 `d_syc not loaded; returning R3-only rewards`，这是 R3-only 模式的预期行为（direction_path 为空）。无 error、traceback 或异常。

## 磁盘状态

| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 24G | 6.9G | **78%** |
| /dev/sda2 (autodl-tmp) | 439G | 16G | 400G | 4% |

⚠️ 根分区使用率较高 (78%)，但 checkpoint 已正确存储在 autodl-tmp 数据盘。

## 结论

**Conclusion: SUCCESS**

训练正常完成 8000 steps，EXIT_CODE=0，所有 checkpoint 已保存。训练过程无错误。reward 在最后阶段稳定在 0.50–0.67 范围。具体 SYCONScore 表现待后续 eval 实验评估。

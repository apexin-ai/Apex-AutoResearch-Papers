# grpo_rasp_25 诊断报告

## 结论：Cron 误判（false positive），实验实际成功完成

## 失败原因

**不是真正的失败。** Cron 在进程正常退出后检测到 "process dead 5×"，因未找到 sentinel/W&B 而自动标记为 failed。实际上训练 100/100 步全部完成，模型已保存。

## 时间线（UTC+8）

| 时间 | 事件 |
|------|------|
| 2026-05-16 23:52 | 训练启动 (PID 21408) |
| 2026-05-17 00:55:19 | 100/100 步完成，开始保存模型 |
| 2026-05-17 00:55:33 | 模型保存完毕，W&B finalize |
| 2026-05-17 01:02:51 | Cron 检测进程不存在，标记 failed |

## 日志关键片段

```
100%|██████████| 100/100 [57:57<00:00, 34.77s/it]
2026-05-17 00:55:19,920 [INFO] Saving recovered model to /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25
Writing model shards: 100%|██████████| 1/1 [00:13<00:00, 13.64s/it]
2026-05-17 00:55:33,873 [INFO] GRPO v4 recovery training complete.
wandb: 🚀 View run grpo_rasp_25 at: https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/bc4ojqie
```

无 error、traceback、OOM。

## Checkpoint 状态

**完整可用。**

- 最终模型: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25/model.safetensors` (10.8GB)
- Checkpoint-100: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25/checkpoint-100/` (含 optimizer.pt 14GB)
- W&B run: `bc4ojqie`

## 最终 metrics (step 100)

| 指标 | 值 |
|------|------|
| reward | 0.009375 |
| reward_std | 0.03149 |
| frac_reward_zero_std | 0.875 |
| kl | 0.0007035 |
| loss | 0.01275 |
| entropy | 0.04262 |

**注意**: frac_reward_zero_std=0.875 表明严重 collapse，reward 接近 0。这与 RASP 25% 假设一致——需要后续定量分析。

## 修复动作

1. ✅ Registry conclusion 从 `failed` 改为 `success`
2. ✅ failure_reason 更新为 FALSE POSITIVE 说明
3. ✅ wandb_run_id 补充为 `bc4ojqie`

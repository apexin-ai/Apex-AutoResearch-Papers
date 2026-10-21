# 诊断报告: exp_b1_scd_conll_control

**诊断时间**: 2026-05-20 20:16 UTC
**服务器**: autodl-5090-b

## Root Cause

**假阳性告警 — 实验已正常完成。** 进程在训练+评估结束后正常退出（exit code 0），cron 因"process dead 5× with no sentinel/W&B"误判为失败。

原因：训练配置中 `report_to: none`（未接入 W&B），且脚本退出时没有写 sentinel 文件，导致 cron 监控无法确认完成状态。

## 实验完成详情

### 训练配置
- **模型**: Qwen3-8B (从 `qwen3-8b-conll2003-merged` 继续训练)
- **方法**: LoRA SFT (rank=32, alpha=64, target=all)
- **数据**: `conll_scd_train` / `conll_scd_dev`
- **超参**: lr=1e-4, batch=2×8 grad_accum, 2 epochs, cosine schedule, warmup=0.1
- **配置文件**: `train_config_scd_conll_s42.yaml`
- **训练命令**: `llamafactory-cli train train_config_scd_conll_s42.yaml`

### 训练结果
| 指标 | 值 |
|------|-----|
| train_loss | 0.0359 |
| eval_loss | 0.0362 |
| epochs | 2.0 |
| total steps | 690 |
| train_runtime | 1375.9s (~23 min) |
| train_samples/s | 8.012 |

### Checkpoints
- `checkpoint-400`, `checkpoint-600`, `checkpoint-690` (final)
- `all_results.json`, `eval_results.json`, `train_results.json` 均已写入
- 输出目录: `checkpoints/qwen3-8b-conll-scd-lora/`
- `load_best_model_at_end: true`, best model 按 eval_loss 选择

### 时间线
- 启动: 2026-05-20 19:43:12
- 训练完成: ~20:06
- 评估完成: 2026-05-20 20:07:50

## 其他 3 个 SCD 实验状态

全部健康运行中（截至 20:16 UTC）：

| 实验 | PID | 状态 | 运行时长 | GPU | 显存 | 配置 |
|------|-----|------|---------|-----|------|------|
| exp_b1_scd_fewnerd_standard | 207109 | Sl+ (running) | 30:58 | GPU 0 | 28520/32607 MiB | train_config_scd_fewnerd_s42.yaml |
| exp_b1_scd_fewnerd_curriculum_q | 205634 | Sl+ (running) | 32:57 | GPU 1 | 27782/32607 MiB | train_config_scd_fewnerd_fallback_s43.yaml |
| exp_b1_scd_threshold_ablation | 205991 | Sl+ (running) | 32:53 | GPU 3 | 31714/32607 MiB | train_config_scd_fewnerd_theta3_s42.yaml |

GPU 2 空闲（conll_control 完成后已释放）。

## 服务器资源
- **磁盘**: /root/autodl-tmp 350G, 已用 203G (58%), 剩余 148G — 充足
- **GPU**: 4× RTX 5090 32GB, 3 卡在用, 1 卡空闲

## 建议

1. **无需重跑** — 实验已完成，结果在 `checkpoints/qwen3-8b-conll-scd-lora/`
2. **修复监控**: 后续实验应在训练脚本末尾写 sentinel 文件（如 `touch $LOG_DIR/$EXP_NAME.done`），或启用 `report_to: wandb`，避免 cron 误判

# 诊断报告：detect_remove_q07_epoch_matched_seed42

## 失败原因

**磁盘空间耗尽 (errno 28: No space left on device)**

在 step 2000 保存 checkpoint 时，`safetensors` 序列化写入失败：

```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

磁盘 `/dev/md0`（挂载于 `/root/autodl-tmp/`）250G 已 100% 占满。

## 训练进度

- 崩溃时刻：step 2000 / 3047（64%），epoch 0.17
- 运行时间：约 70 分钟（1:10:11）
- 最后记录的 loss：10.6494（step 2000 的 logging 输出）

## Checkpoint 状态

| Checkpoint | 状态 | 大小 | 可用于 resume |
|---|---|---|---|
| checkpoint-500 | 完整 | ~3.4GB | 是 |
| checkpoint-1000 | 完整 | ~3.4GB | 是 |
| checkpoint-1500 | 完整 | ~3.4GB | 是 |
| checkpoint-2000 | **不完整** | ~760MB（model.safetensors 被截断，缺 optimizer/tokenizer/trainer_state） | **否** |

**最后可用 checkpoint：checkpoint-1500（step 1500）**

## 根因分析

`save_total_limit=3` 的清理逻辑是「先保存新 checkpoint，再删除旧的」。在 step 2000 时，磁盘上同时存在 4 个 checkpoint（500/1000/1500/2000-writing），总计约 13.6GB+。新 checkpoint 写入中途磁盘满，导致：
- checkpoint-2000 写入不完整
- 旧 checkpoint 未被清理（因为保存流程先于清理流程失败了）

## 修复方案

1. **清理磁盘空间**：
   - 删除损坏的 checkpoint-2000：`rm -rf /root/autodl-tmp/output/models/detect_remove_q07_epoch_matched_seed42/checkpoint-2000/`
   - 检查 `/root/autodl-tmp/` 下其他实验的旧 checkpoint，酌情清理
   - 目标：至少释放 10-15GB 以确保剩余 1047 steps 的训练和 checkpoint 保存
2. **从 checkpoint-1500 resume**：
   ```bash
   cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=2 WANDB_MODE=disabled /root/miniconda3/bin/python training/pretrain_weighted.py \
     --data_path data/scored_data_filtered_q07.jsonl \
     --output_dir /root/autodl-tmp/output/models/detect_remove_q07_epoch_matched_seed42 \
     --model_name models/Qwen/Qwen3-0.6B \
     --weighting_method uniform \
     --max_steps 3047 \
     --batch_size 4 \
     --gradient_accumulation_steps 4 \
     --max_length 2048 \
     --seed 42 \
     --save_steps 500 \
     --logging_steps 10 \
     --bf16 \
     --save_total_limit 3 \
     --resume_from_checkpoint /root/autodl-tmp/output/models/detect_remove_q07_epoch_matched_seed42/checkpoint-1500
   ```
3. **可选优化**：将 `save_total_limit` 降为 2，减少磁盘峰值占用约 3.4GB

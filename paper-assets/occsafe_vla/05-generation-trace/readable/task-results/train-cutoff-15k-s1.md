# train cutoff 15k s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_cutoff_15k_s1_20260524T114822_result.json`
- **Structured JSON:** [`078476fff0f696bb062f.json`](../../sessions/07/078476fff0f696bb062f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。cutoff_15k_s1 已在 westd-34685 GPU 1 上成功启动。

**总结：**
- 服务器：westd-34685，GPU 1（60.8 GB 显存占用）
- Trainable params：279,977,608（符合预期）
- 训练速度：~1.01 it/s（符合预期）
- 50,005 步 × ~1 s/it ≈ ~14 小时完成
- Registry 状态已更新为 RUNNING

**注意：** 用户提供的命令缺少多个关键参数（`--vla_path`、`--data_root_dir`、`--dataset_name`、`--use_occ_head`、`--occ_data_dir`、`--occ_loss_cutoff_mode`、`--run_root_dir`、`--max_steps`、`--save_freq`），我参照 cutoff_25k_s1 的运行命令补全了这些参数。同时 wandb 未在此服务器配置 API key，使用了 `WANDB_MODE=disabled`。

---

# diagnose smart compress failures

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_smart_compress_failures_20260518T004834_result.json`
- **Structured JSON:** [`0addc38b5834d7d18cba.json`](../../sessions/0a/0addc38b5834d7d18cba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：3 个实验均已成功完成，无一失败

### 1. train_smart_compress_m64
- **状态**: 成功完成
- **训练进度**: 99999/100000 steps（100%）
- **完成时间**: 2026-05-18 08:25:24
- **最终 metrics**: eval/action_loss=0.062, train/action_loss=0.045
- **Checkpoint**: `checkpoints/smart_compress_m64/checkpoint.pt` (1.5G, step 99999)

### 2. train_smart_compress_m32
- **状态**: 成功完成
- **训练进度**: 99999/100000 steps（100%）
- **完成时间**: 2026-05-18 08:28:03
- **最终 metrics**: eval/action_loss=0.052, train/action_loss=0.110
- **Checkpoint**: `checkpoints/smart_compress_m32/checkpoint.pt` (1.5G, step 99999)

### 3. train_acis_stage1only_k03
- **状态**: 成功完成（exit code 0）
- **运行时间**: 2026-05-17 15:16 → 15:57（约 40 分钟，stage1 only，10k steps）
- **Checkpoint**: `checkpoints/libero_acis_stage1only_k03/stage1_done/` 目录存在

### "无 W&B metrics" 的根因

三个实验的 W&B 都运行在 **offline 模式**（`wandb sync` 提示 offline-run）。日志末尾显示：
```
wandb: You can sync this run to the cloud by running:
wandb: wandb sync /root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-...
```

Metrics 已记录在本地，只是未上传到 W&B 云端。如果需要在 W&B dashboard 查看，运行对应的 `wandb sync` 命令即可。

### 环境状态
- **GPU**: 4x RTX 4090D，当前有 5 个 python 进程在跑（应该是 m96 和 m16）
- **磁盘**: `/autodl-pub` 96% 已用但仍有 313G 可用；根分区 `/` 27% 已用（23G 可用），不是瓶颈
- 不需要任何环境修复即可进行后续实验

---

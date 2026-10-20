# diagnose random subset epoch seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_random_subset_epoch_seed42_20260524T220206_result.json`
- **Structured JSON:** [`986bab6baa420187a384.json`](../../sessions/98/986bab6baa420187a384.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结论

**实验没有失败。** 训练已成功完成全部 6103 steps。

### 根因：W&B 以 offline 模式运行

启动脚本 `run_random_subset_seed42.sh` 中设置了 `export WANDB_MODE=offline`，导致 W&B metrics 只保存在本地，未上传到云端。

### 训练状态

| 项目 | 状态 |
|------|------|
| 总 steps | 6103/6103 ✓ 完成 |
| Checkpoints | checkpoint-6000, checkpoint-6103, final |
| 模型文件 | model.safetensors (1.19GB) ✓ |
| 本地 metrics | step_metrics.jsonl (24412 行) ✓ |
| W&B 离线数据 | wandb/offline-run-20260524_164658-ejh094n9 (74MB) ✓ |
| 训练时间 | 2026-05-24 16:46 → 2026-05-25 05:37 (~13h) |

### 修复方案

将离线 W&B 数据同步到云端：

```bash
cd /root/provenance_weight_training
wandb sync wandb/offline-run-20260524_164658-ejh094n9
```

如果未来需要实时上报 W&B，将脚本中 `WANDB_MODE=offline` 改为 `WANDB_MODE=online`（前提是服务器能连通 wandb.ai）。

---

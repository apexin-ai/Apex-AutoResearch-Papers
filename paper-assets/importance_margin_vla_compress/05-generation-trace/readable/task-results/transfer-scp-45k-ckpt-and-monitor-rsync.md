# transfer scp 45k ckpt and monitor rsync

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_transfer_scp_45k_ckpt_and_monitor_rsync_20260516T200440_result.json`
- **Structured JSON:** [`b1c107c3a4e5392abd2f.json`](../../sessions/b1/b1c107c3a4e5392abd2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 45K Checkpoint — 不存在

cqa1 上 `libero_full_ft` 的 checkpoints 仅按 **10K 步**保存：
```
step_010000 ~ step_080000
```
**没有 45K checkpoint。** 最接近的是：
- `step_040000/checkpoint.pt` — 1.3GB
- `step_050000/checkpoint.pt` — 1.3GB

eval loss 0.0579 可能是训练日志中 step 45K 的记录值，但模型当时未保存。

### 2. westd 现有状态

- **`libero_full_ft_50k/checkpoint.pt`** 已在 westd（1.32GB，May 17 02:40 拷入）
- 如果需要 40K checkpoint，需要从 cqa1 SCP 过来

### 3. rsync 状态 — 已完成

westd 上无 rsync 进程。lerobot 数据集 `/root/autodl-tmp/.hf_cache/lerobot` 总计 **35GB**，`datasets--HuggingFaceVLA--libero` 目录包含大量 blob 文件且有 `refs/v3.0` 引用，表明下载已完成。

---

**需要决策：** 由于 45K checkpoint 不存在，要用 40K 还是 50K 跑 SR eval？50K 已经在 westd 上了。如果要 40K 我可以立即发起 SCP。

---

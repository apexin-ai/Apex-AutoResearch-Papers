# ssh global status 35807 v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_global_status_35807_v2_20260520T094441_result.json`
- **Structured JSON:** [`e2a153e260d00a12d059.json`](../../sessions/e2/e2a153e260d00a12d059.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| GPU | 实验 | PID | Step/30000 | Loss | VRAM | 状态 |
|-----|------|-----|-----------|------|------|------|
| cuda:0 | baseline_spatial_bowl_s0 | 100319 | 10994/30000 (37%) | 0.0102 | 37.4 GiB | **正常**，GPU util 0%（可能在 data loading） |
| cuda:1 | baseline_spatial_bowl_s1 | 94453 | 11287/30000 (38%) | 0.0135 | 37.4 GiB | **正常**，GPU util 100% |
| cuda:2 | baseline_object_pudding_s0 | 95429 | 11414/30000 (38%) | 0.0087 | 37.4 GiB | **正常**，GPU util 100% |
| cuda:3 | a1_sdf_spatial_bowl_s0 | 185994 | 6499/30000 (22%) | 0.2779 | 13.4 GiB | **已死** |

### 系统资源
- **磁盘 /root/autodl-tmp**: 199G/350G (57%) — 正常
- **根分区 /**: 29G/30G (96%) — **几乎满**
- **系统内存**: 74Gi/1.0Ti — 正常

### OOM 排查
dmesg 不可用（read_only 限制），但 A1 死因明确：**不是 OOM，是磁盘满。**

### A1 死因
Step 6499 保存 checkpoint 时根分区空间不足：
```
safetensors_rust.SafetensorError: I/O error: No space left on device (os error 28)
```
路径：`train_pytorch.py:190 → save_checkpoint → safetensors.torch.save_model`

PID 185994 仍挂在 GPU 3（13.4 GiB），torch._inductor compile workers 在跑，但 GPU util 0%，进程可能处于挂起/恢复状态，训练未在推进。

### 根因
根分区 30G 已用 29G，checkpoint 写入失败。需要清理根分区空间后重启 A1（checkpoint 应写到 `/root/autodl-tmp/` 而非根分区）。

**3 个 baseline 正常运行，A1 需要你决定如何处理。**

---

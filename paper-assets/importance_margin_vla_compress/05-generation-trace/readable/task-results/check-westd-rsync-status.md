# check westd rsync status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_rsync_status_20260516T191133_result.json`
- **Structured JSON:** [`08f873cbb90da2fa0d47.json`](../../sessions/08/08f873cbb90da2fa0d47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态报告 (westd-27271)

### 1. LIBERO 数据 rsync
- **进行中**，尚未完成
- rsync 正从 `cqa1` 服务器同步到 `/root/autodl-tmp/.hf_cache/lerobot/hub/datasets--HuggingFaceVLA--libero/`
- 当前已传输 **11GB**，进度约 `xfr#123, to-chk=650/777`（完成 123/777 个文件，约 16%）
- 传输速度 ~16-17 MB/s
- `/root/autodl-tmp/libero_data/` 是空目录

### 2. GPU 状态
| GPU | 型号 | 显存使用 | 总显存 | 利用率 |
|-----|------|---------|--------|--------|
| 0 | NVIDIA RTX PRO 6000 Blackwell | 0 MiB | 97887 MiB (~96GB) | 0% |
| 1 | NVIDIA RTX PRO 6000 Blackwell | 0 MiB | 97887 MiB (~96GB) | 0% |

两张卡完全空闲。

### 3. 活跃训练进程
**无**。仅有系统服务（tensorboard、jupyter-lab、supervisord）和 rsync 进程在运行。

### 4. 磁盘空间
| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (根) | 30G | 6.0G | 25G | 20% |
| /root/autodl-tmp (数据盘) | 250G | 142G | 109G | 57% |

### 5. IMM 项目代码
`/root/autodl-tmp/importance_margin_vla_compress/` **已就绪**，包含 train.py、eval 脚本、configs、checkpoints（含 libero_baseline、libero_imm_twostage、libero_full_ft_50k、libero_lora_50k）等完整项目结构。

---

**总结**：rsync 仍在跑（约 16% 文件完成，预计还需较长时间），GPU 双卡空闲可随时启动训练，磁盘空间充裕。

---

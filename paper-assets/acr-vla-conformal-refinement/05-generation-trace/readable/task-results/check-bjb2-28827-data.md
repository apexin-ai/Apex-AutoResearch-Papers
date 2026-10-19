# check bjb2 28827 data

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb2-28827-data_20260521T132709_result.json`
- **Structured JSON:** [`2fa7c776881e56a25689.json`](../../sessions/2f/2fa7c776881e56a25689.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-28827 状态报告

### GPU & 磁盘
- **6x RTX 4090**，全部空闲（0% 利用率，0 MiB 显存占用）
- 根分区 30G（已用 13G / 剩 18G），数据盘 250G（已用 51G / 剩 200G）

### LIBERO 数据 — **不完整**
- 位置：`/root/autodl-tmp/libero_data/`（13GB）
- **仅有 2 个子集**：`libero_object`（10 个 hdf5）、`libero_spatial`（10 个 hdf5）
- **缺失**：`libero_goal`、`libero_10`（LIBERO 标准有 4 个子集）
- 无 lerobot 格式 parquet 数据

### π0.5 模型 — **存在**
- `/root/autodl-tmp/models/pi05_libero_finetuned/` 有 `model.safetensors`（7.5GB）+ config 文件，看起来完整

### 代码 — **存在但不完整**
- `src/train_crm.py` 和 `src/pi05_wrapper.py` 存在
- 项目目录结构：`artifacts/`, `logs/`, `scripts/`, `src/`
- **缺失 `data/` 目录**（项目代码中没有 data 软链接或目录）

### 依赖环境
- lerobot 0.5.1 已安装（conda base 环境，Python 3.12）
- 有 `lerobot_backup_1779363883` 备份目录，说明之前做过 lerobot 修改/patching

### 进行中的操作
- 无 rsync/wget/curl/pip/git 进程运行
- 仅有 SSH 和系统服务进程

### 建议
1. **需要补充 LIBERO 数据**：缺 `libero_goal` 和 `libero_10` 子集
2. **需要建立 `data/` 目录**或软链接到 `/root/autodl-tmp/libero_data/`
3. **模型和基础代码就绪**，补齐数据后可部署 precompute
4. lerobot 0.5.1 可能需要验证与项目代码的兼容性（有备份目录暗示之前有 patch）

---

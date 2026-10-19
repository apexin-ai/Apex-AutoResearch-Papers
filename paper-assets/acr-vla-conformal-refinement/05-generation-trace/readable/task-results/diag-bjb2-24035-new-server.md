# diag bjb2 24035 new server

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb2-24035-new-server_20260526T040531_result.json`
- **Structured JSON:** [`78ba3d959c71b2131796.json`](../../sessions/78/78ba3d959c71b2131796.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-24035 状态报告

### GPU
- **1× RTX 4090 D** (24GB VRAM)，空闲，无进程占用
- Driver 580.105.08，CUDA 13.0

### 磁盘
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 (/) | 30G | 21G | 9.7G | 68% |
| 数据盘 (/dev/sda2) | 437G | 369G | 47G | 89% |

数据盘使用率 89%，剩余 47G，偏紧。

### 数据盘拷贝状态：**已完成**
- 无 cp/rsync/scp 进程在跑
- 数据盘内容结构完整，与旧服务器一致

### 数据盘主要内容
| 目录 | 大小 | 说明 |
|------|------|------|
| libero_data | 94G | LIBERO 数据集 |
| models | 49G | 所有模型 |
| envs | 18G | Python 环境 |
| A1 | 976M | A1 相关 |
| checkpoints | 87M | CRM checkpoints |
| crm_cache_pi05 | 76M | π0.5 precompute (object suite only) |

### π0.5 依赖就绪性

| 项目 | 状态 | 路径/说明 |
|------|------|-----------|
| π0.5 模型 | ✓ 就绪 | `models/pi05_libero_finetuned/` (4.0G) |
| SmolVLA CRM checkpoint | ✓ 就绪 | `checkpoints/crm_smolvla_3suite_v1/crm_best.pt` |
| **π0.5 CRM checkpoint** | **✗ 缺失** | `checkpoints/crm_pi05_unified_3suite/` 不存在 |
| π0.5 precompute 数据 | **部分** | 只有 `crm_cache_pi05/object/` (76M, 75个 partial 文件)，无 spatial/goal suite |
| `crm_cache_pi05_2048/` | **✗ 缺失** | 旧任务提到的 2048-dim cache 目录不存在 |

### Python 环境
- miniconda3 已装，Python 3.12.3
- `python3` 不在 PATH 中（需通过 `/root/miniconda3/bin/python3` 调用）
- `envs/` 下有 `a1` 和 `openvla-oft` 两个环境

### 项目代码
- ✓ `/root/acr-vla-conformal-refinement/src/evaluate.py` 存在（最后更新 May 25）

### 旧实验日志
- ✓ 已迁移，项目 `logs/` 下有 ~55 个日志/JSON 文件，最新到 May 26

### 结论：**暂不可部署 π0.5 实验**

缺两个关键依赖：
1. **π0.5 CRM checkpoint** (`crm_pi05_unified_3suite/crm_best.pt`) — 需要重新训练或从备份恢复
2. **完整 precompute 数据** — 当前只有 object suite 的 cache，缺 spatial 和 goal suite；且目录名是 `crm_cache_pi05` 而非 `crm_cache_pi05_2048`

SmolVLA 相关实验可以跑（模型+checkpoint 都在）。磁盘剩余 47G 偏紧，如果需要重新 precompute 全部 3 suite 可能需要清理空间。

---

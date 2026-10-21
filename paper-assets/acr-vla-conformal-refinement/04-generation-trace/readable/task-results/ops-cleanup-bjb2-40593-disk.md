# ops cleanup bjb2 40593 disk

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-bjb2-40593-disk_20260518T133112_result.json`
- **Structured JSON:** [`92bcb4f012ce9880d8b2.json`](../../sessions/92/92bcb4f012ce9880d8b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理结果

### 清理前
| 分区 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| overlay (/) | 18G | 13G | 58% |
| /dev/sda2 (宿主机) | 371G | 45G | 90% |
| /dev/md0 (autodl-tmp) | 99G | 152G | 40% |

### 清理明细
| 路径 | 释放 | 原因 |
|------|------|------|
| `/root/.cache/huggingface/hub/` | **7.6G** | 模型缓存，实验使用 autodl-tmp 的 HF_HOME，不影响运行 |
| `/root/.cache/pip/` | **898M** | pip 下载缓存 |
| `/root/miniconda3/pkgs/` (tarballs) | **108M** | conda 包缓存 |
| `/var/lib/apt/lists/` | **~50M** | apt 索引缓存 |

### 清理后
| 分区 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| **overlay (/)** | **8.9G** | **22G** | **30%** |
| /dev/sda2 (宿主机) | 371G | 45G | 90% |
| /dev/md0 (autodl-tmp) | 99G | 152G | 40% |

**Overlay 释放: ~9.1G**（18G → 8.9G）

运行中实验 eval-scalar-object-seed45-r2 未受影响。

### 关于 /dev/sda2 无法清理的说明

`/dev/sda2`（437G, 90%）是 **AutoDL 宿主机的 Docker 系统盘**，通过 bind mount 挂载 NVIDIA 驱动到容器内。371G 中绝大部分是：
- Docker 基础镜像层（Ubuntu + CUDA + PyTorch 等）
- 宿主机系统文件和其他容器
- NVIDIA 驱动和库文件

这些不在容器内可控范围。用户 overlay 上层（唯一可写部分）已从 18G 清理到 8.9G。**容器内无法释放 /dev/sda2 上 50GB 空间**——需要联系 AutoDL 平台处理宿主机层面的清理。

---

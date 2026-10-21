# ops gpu visibility check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-visibility-check_20260528T231617_result.json`
- **Structured JSON:** [`68de0d91517020e9078f.json`](../../sessions/68/68de0d91517020e9078f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：实例被缩容，不是环境变量问题

### westd-35807
| 项目 | 结果 |
|------|------|
| GPU 数量 | **1 张**（应有 4 张） |
| GPU 型号 | NVIDIA RTX PRO 6000 Black (96GB) |
| Driver/CUDA | 580.95.05 / CUDA 13.0 |
| CUDA_VISIBLE_DEVICES | 未设置（空） |
| /dev/nvidia* | 仅 `/dev/nvidia5`（注意编号是 5，不是 0） |

### westd-45947
| 项目 | 结果 |
|------|------|
| GPU 数量 | **1 张**（应有 2 张） |
| GPU 型号 | NVIDIA RTX PRO 6000 Black (96GB) |
| Driver/CUDA | 595.58.03 / CUDA 13.2 |
| CUDA_VISIBLE_DEVICES | 未设置（空） |
| /dev/nvidia* | 仅 `/dev/nvidia1`（编号是 1，不是 0） |

### 判定
- **不是 CUDA_VISIBLE_DEVICES 问题**：两台服务器该变量均为空。
- **是实例缩容**：两台服务器 `/dev/` 下各只有 1 个 nvidia 设备文件（westd-35807 只有 nvidia5，westd-45947 只有 nvidia1），物理上就只挂载了 1 张卡。设备编号不连续（5 和 1 而非 0）说明原来有多张卡，现在只保留了其中一张。
- 需要联系实例提供方恢复 GPU 配额：westd-35807 应恢复到 4 张，westd-45947 应恢复到 2 张。

---

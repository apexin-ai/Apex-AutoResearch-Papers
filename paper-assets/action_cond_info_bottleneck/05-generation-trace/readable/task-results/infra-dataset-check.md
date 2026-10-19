# infra dataset check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_dataset-check_20260515T204102_result.json`
- **Structured JSON:** [`0078d6831b0fbfbef2bc.json`](../../sessions/00/0078d6831b0fbfbef2bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 结果汇总

### 数据集位置和大小
| 路径 | 大小 | 状态 |
|------|------|------|
| `/root/autodl-tmp/libero_dataset/` | 1.9G | **完整可用** |
| `/root/autodl-tmp/libero_clean/` | 966M | 不完整（仅 8K/273K frames） |
| `/root/autodl-tmp/.hf_cache/hub/datasets--lerobot--libero/` | 4K | 仅 refs，无数据 |

### 数据完整性（`libero_dataset`）
- **Parquet 数据**：377 文件，**273,465 frames**，**1,693 episodes**，与 info.json 完全匹配
- **视频文件**：37 mp4/camera × 2 cameras = 74 文件（1.8G），与 episode 元数据 file_index 范围 0-36 完全匹配
- **Features**：`observation.images.image` [3,256,256]、`observation.images.image2` [3,256,256]、`observation.state` [8]、`action` [7]、task 文本

### 已修复的问题
- **FFmpeg 缺失**：已安装 FFmpeg 4.4.2，torchcodec 视频解码正常工作
- 首帧和末帧（ep 0 ~ ep 1692）均可正常解码

### ACIB v3 训练数据：就绪
训练脚本 `train_acib_libero.py` 可直接使用 `--data_root=/root/autodl-tmp/libero_dataset`。

---

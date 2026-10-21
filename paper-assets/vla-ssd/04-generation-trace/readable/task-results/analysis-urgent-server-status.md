# analysis urgent server status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_urgent_server_status_20260521T014431_result.json`
- **Structured JSON:** [`0a615eb5cf5d050c4631.json`](../../sessions/0a/0a615eb5cf5d050c4631.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-19183 全面状态报告

### GPU
| GPU | 型号 | 显存使用 | 温度 | 利用率 |
|-----|------|---------|------|--------|
| 0 | NVIDIA RTX PRO 6000 Black (98GB) | 15149MiB / 97887MiB | 34°C | 0% |
| 1 | NVIDIA RTX PRO 6000 Black (98GB) | 0MiB / 97887MiB | 30°C | 0% |

GPU 0 有 python 进程 (PID 513523) 占用 15.1GB 显存。

### 活跃进程
1. **libero_object_full_pipeline** (tmux session) — PID 513523，运行 `libero_object_full_pipeline.py`，GPU 0
2. **HF 下载 openvla-7b-oft-finetuned-libero-10** (PID 513455) — **正在超时重试**，`model-00002-of-00004.safetensors` 下载卡在 xethub ReadTimeout，进度 44% (11/25 files)

### Pipeline 日志
Phase 1 (feature extraction) 已完成：5000 samples，249.1s。
Phase 2 (action R2 probing) 正在运行，已输出 L0: `img_mean R2=0.6952, last_pre R2=0.5710`。

### Checkpoints

| 模型 | 状态 | 大小 |
|------|------|------|
| openvla-7b-finetuned-libero-object | ✅ 就绪 | 15G |
| tracevla-phi3v | ✅ 就绪 | 7.8G |
| openvla-phi3v (untrained baseline) | ❌ NOT_FOUND | — |
| nora-libero-goal | ✅ 就绪 | 5.1G |
| qwen25-vl-3b-base | 目录存在，但 config.json 路径不匹配 | — |
| openvla-7b-oft-finetuned-libero-10 | ⚠️ 下载中 (44%, 卡在超时重试) | 817M (不完整) |

### NORA 环境
✅ 就绪：`torch=2.10.0+cu128, transformers=4.50.0`

### LIBERO 数据
| Suite | HDF5 文件数 |
|-------|------------|
| libero_goal | 10 |
| libero_spatial | 10 |
| libero_object | 10 |
| libero_long | **0** |

### 磁盘 ⚠️ 严重
```
/dev/md0  250G  249G  1.7G  100%  /root/autodl-tmp
```
| 目录 | 大小 |
|------|------|
| checkpoints/ | 64G |
| features/ | 117G |
| results/ | 18G |

**磁盘几乎满了，仅剩 1.7G。** OFT 模型下载完整需要 ~15G (4 个 safetensors shard)，当前空间不够。

### 关键问题

1. **磁盘满** — 1.7G 剩余，OFT 模型下载无法完成，后续实验也会受影响
2. **OFT 下载卡死** — xethub ReadTimeout 反复重试（未设 `HF_HUB_DISABLE_XET=1`），且即使恢复也因磁盘不足会失败
3. **openvla-phi3v (untrained baseline) 缺失** — 未下载
4. **libero_long 数据为 0** — 无 HDF5 文件

---

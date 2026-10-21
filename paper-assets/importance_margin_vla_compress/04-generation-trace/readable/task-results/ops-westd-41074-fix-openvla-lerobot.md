# ops westd 41074 fix openvla lerobot

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_41074_fix_openvla_lerobot_20260519T170408_result.json`
- **Structured JSON:** [`0583c94abbb876e14226.json`](../../sessions/05/0583c94abbb876e14226.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

---

## 产出汇报

### 任务 1: Kill + rsync ✅
| 项目 | 状态 |
|------|------|
| PID 4959, 5232 (重复 openvla-7b 下载) | 已 kill |
| Bash wrappers 5197, 5227 | 已 kill |
| partial download (.hf_cache/hub/models--openvla--openvla-7b) | 已清理 |
| SSH 41074 → 27271 | 自动配置 ed25519 密钥，免密连通 |
| rsync fine-tuned model | **完成**，15GB @ ~314MB/s |
| 验证 | 4 个 safetensors 文件完整 (4.9G + 4.9G + 4.9G + 262M) |

路径：`/root/autodl-tmp/openvla-libero-object/`

### 任务 2: lerobot 重装 ✅
| 项目 | 状态 |
|------|------|
| lerobot 版本 | 0.5.2 (editable mode) |
| SmolVLAConfig import | ✅ |
| SmolVLAPolicy import | ✅ |

**注意：import 路径变更**
- 旧：`lerobot.common.policies.smolvla`
- 新：`lerobot.policies.smolvla`

项目代码中如果用旧路径需要更新。

### 任务 3: westd-27271 就绪评估 ✅

**结论：westd-27271 已可直接跑 OpenVLA re-encoding 训练，无需额外搭建。**

| 项目 | 详情 |
|------|------|
| GPU | 2× NVIDIA RTX PRO 6000 Blackwell (94GB each)，全部空闲 (0 MiB / 0%) |
| Python | 3.12.3 (conda base) |
| torch | 2.8.0+cu128, CUDA ✅ |
| transformers | 5.8.1 |
| lerobot | 0.5.1 (import OK, 新路径 `lerobot.policies.smolvla`) |
| accelerate | 1.13.0 |
| Fine-tuned model | `/root/autodl-tmp/openvla-libero-object/` (15GB, 4 safetensors) |
| 项目代码 | 存在，含 train.py / train_smart_compress.py / eval 系列 |

westd-41074 有 4×RTX PRO 6000 但需要等 mpt-1b 下载完 (PID 5202 仍在跑)。westd-27271 此刻即可开始训练。

---

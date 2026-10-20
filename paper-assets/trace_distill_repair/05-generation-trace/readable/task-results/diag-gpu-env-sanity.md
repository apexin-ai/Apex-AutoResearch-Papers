# diag gpu env sanity

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_env_sanity_20260515T022956_result.json`
- **Structured JSON:** [`f47749e37da5aa331c6a.json`](../../sessions/f4/f47749e37da5aa331c6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。汇总报告：

---

## 环境验证报告

### GPU
| GPU | 型号 | 显存 | 空闲显存 | 驱动 |
|-----|------|------|---------|------|
| 0 | RTX PRO 6000 Blackwell Server Edition | 96GB | ~95GB | 595.58.03 |
| 1 | RTX PRO 6000 Blackwell Server Edition | 96GB | ~95GB | 595.58.03 |

### PyTorch Sanity Check
- **torch**: 2.10.0+cu128
- **CUDA**: OK
- **Mixed precision (AMP)**: OK（`torch.cuda.amp` 已 deprecated，建议后续用 `torch.amp`）
- **DataParallel (2 GPUs)**: OK

### 已有模型
| 模型 | 路径 | 大小 |
|------|------|------|
| Qwen3-8B | `/root/autodl-tmp/models/Qwen/Qwen3-8B/` | 16GB |
| Qwen3-30B-A3B | `/root/autodl-tmp/models/Qwen/Qwen3-30B-A3B/` | 57GB |

- Qwen3-8B load + inference 验证通过，`device_map="auto"` 自动分到两张卡（layers 0-15 → GPU0, 16-35 → GPU1）

### 磁盘
| 分区 | 总量 | 已用 | 可用 |
|------|------|------|------|
| 根分区 `/` | 30GB | 7.8GB | 23GB |
| 数据盘 `/root/autodl-tmp` | 250GB | 76GB | 175GB |

- 项目目录 `/root/trace_distill_repair/`: 979MB
- **175GB 数据盘空余**，足够容纳 student model + training data

---

# ops lora only progress

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_lora_only_progress_20260519T100246_result.json`
- **Structured JSON:** [`1a96dfdba8cb6461a25d.json`](../../sessions/1a/1a96dfdba8cb6461a25d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## LoRA-only 训练进度报告

### 基本信息
| 项目 | 值 |
|------|-----|
| 模型 | Qwen2.5-7B-Instruct |
| GPU | NVIDIA RTX PRO 6000 Blackwell (102GB) |
| Gate type | none (LoRA-only baseline) |
| 可训练参数 | 5,046,272 (0.07%) |
| 数据集 | ultrachat_8k (8000 samples) |
| Grad accum | 8 |
| 总优化步数 | 3000 |

### 进度
| 指标 | 值 |
|------|-----|
| 当前位置 | Epoch 1, micro-step 3400/8000 (42.5% of Epoch 1) |
| 全局优化步 | ~425 / 3000 |
| **总体进度** | **~14.2%** |
| 已运行时间 | ~2.8 小时 |
| **预估剩余** | **~17 小时** |
| 预估总耗时 | ~19.7 小时 |

### Loss 趋势
Loss 波动较大（单样本 logging），整体缓慢下降：
- Step 50: L_NTP=1.038
- Step 2150: L_NTP=0.474
- Step 2800: L_NTP=0.363
- Step 3400: L_NTP=0.962

Gate 全程 1.000（符合预期，LoRA-only 无 gate 机制）。L_GAR / L_DIV 近零。

### 资源状态
| 资源 | 状态 |
|------|------|
| GPU 利用率 | 97% |
| 显存 | 91.3 / 97.9 GB (93%) |
| 磁盘 | 16G / 30G (51%) |

训练正常运行中，GPU 满载。按当前速率预计还需约 17 小时完成全部 3 epochs。

---

# ops full gpu audit all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-gpu-audit-all-servers_20260520T190417_result.json`
- **Structured JSON:** [`5d368b6b987708e3ecd5.json`](../../sessions/5d/5d368b6b987708e3ecd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整审计结果。

---

## GPU 审计汇总 (2026-05-21)

### 1. westd-41074 (4× RTX PRO 6000 Blackwell 96GB)

| GPU | 状态 | PID | 显存占用 | 利用率 | 任务 |
|-----|------|-----|---------|--------|------|
| 0 | **运行中** | 564811 | 16.0/96GB | 86% | `eval_openvla random_prune k=0.95 seed43` |
| 1 | **空闲** | — | 0/96GB | 0% | — |
| 2 | **运行中** | 68539 | 28.5/96GB | 0% | `train_openvla_smart_compress m96` |
| 3 | **运行中** | 68852 | 27.5/96GB | 0% | `train_openvla_smart_compress m64` |

**已完成结果（westd-41074 eval_results/）：**
| 文件 | SR | 备注 |
|------|------|------|
| openvla_random_k05_seed43_v2.json | **35.6%** | k=0.5, seed43, 500eps |
| openvla_random_k07_seed43_v2.json | **52.6%** | k=0.7, seed43, 500eps |
| oft_random_prune_k09_object.json | **0.0%** | OFT 模型, seed7 |
| oft_random_prune_k095_object.json | **0.0%** | OFT 模型, seed7 |

---

### 2. westd-38929 (4× RTX PRO 6000 96GB)

| GPU | 状态 | PID | 显存占用 | 利用率 |
|-----|------|-----|---------|--------|
| 0 | **空闲** | — | 0/96GB | 0% |
| 1 | **空闲** | — | 0/96GB | 0% |
| 2 | **空闲** | — | 0/96GB | 0% |
| 3 | **空闲** | — | 0/96GB | 0% |

全部空闲，无任何进程。

---

### 3. westd-27271 (2× RTX PRO 6000 96GB)

| GPU | 状态 | PID | 显存占用 | 利用率 | 任务 |
|-----|------|-----|---------|--------|------|
| 0 | **运行中** | 67609 | 16.0/96GB | 72% | `eval_openvla_l2norm k=0.7 seed43` |
| 1 | **运行中** | 921279 | 42.2/96GB | 0% | `train_openvla_smart_compress m32 (resume)` |

**磁盘：77% (192G/250G)** — 已从 94% 降至安全水平。

**已完成结果（westd-27271 eval_results/）：**
| 文件 | SR | 备注 |
|------|------|------|
| openvla_l2norm_prune_k0_7_object.json | **49.8%** | L2 norm k=0.7, seed42 |
| openvla_random_prune_k0_9_seed43_object.json | **62.2%** | random k=0.9, seed43 |

**Sweep 状态：** L2 norm sweep 和 random prune seed43 sweep 的日志显示 "ALL DONE"，但 k=0.5 和 k=0.3 的 L2 norm 以及 random k=0.7/k=0.5 seed43 仅有 log 文件没有 json 输出，可能是 crash/未完成就被 wrapper 标记为 done。

当前 GPU 0 PID 67609 是单独的 L2 norm k=0.7 **seed43** eval（区别于已完成的 seed42 版本）。

---

### 4. cqa1-33015 (4× RTX 4090D 24GB)

| GPU | 状态 | PID | 显存占用 | 利用率 | 任务 |
|-----|------|-----|---------|--------|------|
| 0 | **运行中** | 854755 | 4.5/24GB | 1% | `X-VLA k=0.1 seed42` |
| 1 | **运行中** | 694944 | 4.5/24GB | 1% | `X-VLA k=0.1 seed43` |
| 2 | **空闲** | — | 0/24GB | 0% | — |
| 3 | **运行中** | 696123 | 4.5/24GB | 1% | `X-VLA k=0.1 seed44` |

**已完成 X-VLA L2 norm prune 结果（libero_object, 500eps/each）：**

| keep_ratio | seed42 | seed43 | seed44 |
|-----------|--------|--------|--------|
| k=0.9 | — | **97.6%** | **98.2%** |
| k=0.7 | — | **59.0%** | **56.4%** |
| k=0.5 | — | **44.2%** | **44.4%** |
| k=0.3 | — | **21.0%** | **22.8%** |
| k=0.2 | — | **4.8%** | **4.0%** |
| k=0.1 | 运行中 | 运行中 | 运行中 |

---

### 总体状态

| 服务器 | 运行中 GPU | 空闲 GPU | 总空闲显存 |
|--------|-----------|---------|-----------|
| westd-41074 | 3 (GPU 0,2,3) | 1 (GPU 1) | 96GB |
| westd-38929 | 0 | **4** | **392GB** |
| westd-27271 | 2 (GPU 0,1) | 0 | 0 |
| cqa1-33015 | 3 (GPU 0,1,3) | 1 (GPU 2) | 24GB |

**可用算力：** westd-38929 完全空闲（4×96GB），westd-41074 GPU 1 空闲（96GB），cqa1 GPU 2 空闲（24GB）。

---

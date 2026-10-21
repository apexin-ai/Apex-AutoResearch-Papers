# ops server connectivity check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-connectivity-check_20260518T231834_result.json`
- **Structured JSON:** [`ac0f29fd10add8dfca05.json`](../../sessions/ac/ac0f29fd10add8dfca05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### westd-34887
| 项目 | 状态 |
|------|------|
| **连通性** | 在线 (1.1s) |
| **GPU 0** | 空闲 — 0% util, 0/97887 MiB |
| **GPU 1** | 空闲 — 0% util, 0/97887 MiB |
| **运行中进程** | 无实验进程（仅 supervisord/tensorboard/jupyter 等系统服务） |
| **磁盘 /** | 14G 可用 / 30G (56% used) |
| **磁盘 /root/autodl-tmp** | 181G 可用 / 250G (28% used) |

**P1 Eval 状态：两个任务均已失败**

- `kl30_uniform_hellaswag_piqa.log` — 模型加载成功，mask 计算完成，但 lm_eval 下载 `Rowan/hellaswag` 数据集时报错：
  > `ConnectionError: Couldn't reach 'Rowan/hellaswag' on the Hub (OfflineModeIsEnabled)`
- `kl50_global_hellaswag_piqa.log` — 同样错误，`OfflineModeIsEnabled` 导致无法下载 hellaswag 数据集

**根因**：服务器启用了 HuggingFace 离线模式（`HF_DATASETS_OFFLINE=1` 或类似环境变量），hellaswag/piqa 数据集未预缓存。

**最近完成的实验**（results/benchmark/）：最新有数据的目录是 `kl30_s456_global_v3`（May 19 06:52）和 `kl30_s123_global_v3`（May 19 06:50），共 100+ 个实验目录。

---

### westd-41718
| 项目 | 状态 |
|------|------|
| **连通性** | 在线 (0.9s) |
| **GPU 0** | 空闲 — 0% util, 0/97887 MiB |
| **GPU 1** | 空闲 — 0% util, 0/97887 MiB |
| **运行中进程** | 无实验进程（仅系统服务） |
| **磁盘 /** | 25G 可用 / 30G (20% used) |
| **磁盘 /root/autodl-tmp** | 204G 可用 / 250G (19% used) |

---

### 需要处理的问题

**P1 eval 被 OfflineModeIsEnabled 阻断**。需要：
1. 检查 `HF_DATASETS_OFFLINE` / `TRANSFORMERS_OFFLINE` 环境变量并关闭，或
2. 先手动下载 hellaswag 和 piqa 数据集到本地缓存后重新跑

两台服务器 4 块 H800 全部空闲，无任何实验在跑。

---

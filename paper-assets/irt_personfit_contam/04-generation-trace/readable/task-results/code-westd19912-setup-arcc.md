# code westd19912 setup arcc

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd19912-setup-arcc_20260521T101704_result.json`
- **Structured JSON:** [`da3daa3391d6cc3951eb.json`](../../sessions/da/da3daa3391d6cc3951eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 环境搭建 + 训练启动报告

### 环境
| 项目 | 信息 |
|------|------|
| 镜像 | 非 aml-train（通用 AutoDL） |
| Python | 3.12.3 (miniconda3 conda base) |
| PyTorch | 2.8.0+cu128, CUDA 13.0 |
| GPU | 4× NVIDIA RTX PRO 6000 Blackwell 96GB |
| 磁盘 | 根 30GB / 数据盘 250GB |

### 训练进程

| GPU | Condition | PID | Steps | 状态 |
|-----|-----------|-----|-------|------|
| cuda:0 | clean_s1 | 5528 | 0/939 | 训练中 ~1s/it |
| cuda:1 | clean_s2 | 6181 | 0/939 | 训练中 ~1s/it |
| cuda:2 | contam_15 | 6810 | 0/948 | 训练中 ~1s/it |
| cuda:3 | contam_50 | 7450 | 0/966 | 训练中 ~1s/it |

### nvidia-smi 确认
- GPU 0: 37.6GB / 96GB, 89% util
- GPU 1: 34.3GB / 96GB, 95% util
- GPU 2: 27.2GB / 96GB, 90% util
- GPU 3: 18.9GB / 96GB, 96% util

4/4 GPU 全部在用，4 个条件并行训练正常运行。wandb 设为 offline 模式（本地日志存储）。预计每个条件约 15-16 分钟完成（~1s/step × ~950 steps）。

---

# infra post restart health check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_post-restart-health-check_20260519T174306_result.json`
- **Structured JSON:** [`cb251bb62137d9599fe0.json`](../../sessions/cb/cb251bb62137d9599fe0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### cqa1-22115 (4× RTX 4090 D)

| 项目 | 状态 |
|------|------|
| **PID 167144** | 存活，运行 33 分钟（bash wrapper） |
| **实际训练进程** | PID 167152 (101% CPU)，PID 169432/169433 (fork 的子进程) |
| **进度** | 5-fold CV，Fold 3 已完成 (3 epochs, final loss=1.1305)，Fold 4 训练中，Ep 1 step 800/1500, loss=1.4793 |
| **GPU** | GPU 0: 96% 利用率，23221/24564 MiB；GPU 1-3: 空闲 |
| **异常** | 无。DeBERTa 加载时有 UNEXPECTED/MISSING keys 是正常的（预训练→分类头替换） |

### westd-42896 (2× RTX PRO 6000 Blackwell 96GB)

| 项目 | 状态 |
|------|------|
| **PID 44715** | 存活，运行 1 天 10 小时 39 分 |
| **进度** | depth 5 生成中，1579/2500 batches (63%)，~14.8s/it，已跑约 6 小时；预计还需 ~3.8 小时完成 depth 5 |
| **GPU** | GPU 0: 空闲；GPU 1: 73% 利用率，64731/97887 MiB |
| **异常** | 无 |

两台服务器实验均正常运行，无 OOM 或错误。

---

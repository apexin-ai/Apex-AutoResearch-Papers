# ops harvest deploy westd41074 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-deploy-westd41074-v3_20260524T100215_result.json`
- **Structured JSON:** [`5346b366464c3610cedc.json`](../../sessions/53/5346b366464c3610cedc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告：westd-41074 全 4 卡正在跑，不是空闲

Director 判断有误——所有 GPU 都在积极评估中（GPU 利用率 21-43%，各占 ~10GB VRAM）。进程 PID 全部存活。

### westd-41074 当前进度（评估于 ~17:41 +0800 启动）

| GPU | 实验 | 完成 Tasks | 当前位置 | Interim SR |
|-----|------|-----------|---------|-----------|
| 0 | **L2norm k=0.5 Goal** | 2/10 | T2 ep20 | 33.0% (33/100) |
| 1 | **L2norm k=0.7 Goal** | 3/10 | T3 ep10 | 75.3% (113/150) |
| 2 | **L2norm k=0.9 Goal** | 4/10 | T4 起步 | 91.5% (183/200) |
| 3 | **Random k=0.3 Goal** | 2/10 | T2 ep40 | ~47% |

### westd-38929 Random k=0.95 也在跑

| GPU | 实验 | 完成 Tasks | Interim SR |
|-----|------|-----------|-----------|
| 0 | **Random k=0.95 Goal** | 3/10 | 88.0% (132/150) |

### 关键判断

1. **不需要收割** — 5 个实验全部仍在运行中，预计 ~40-55 分钟后完成
2. **不需要重新部署** — Director 计划部署的 3 个实验（random k=0.3, l2norm k=0.9, l2norm k=0.7）已经在 westd-41074 上跑着。Random k=0.95 在 westd-38929 上跑着
3. **磁盘上的结果文件是之前（pre-fix）run 的** — 文件时间戳在当前进程启动前后，当前 post-fix run 完成后会覆盖
4. L2norm k=0.5 Goal（GPU 0）不在 Director 的重新部署计划中，但也在跑，额外收获

### 建议

等待 ~45 分钟后再来收割。届时 5 个实验都应完成，可以一次性 harvest 全部结果并更新 registry。

---

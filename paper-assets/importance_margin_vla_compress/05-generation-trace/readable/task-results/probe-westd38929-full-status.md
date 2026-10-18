# probe westd38929 full status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_westd38929-full-status_20260521T233236_result.json`
- **Structured JSON:** [`3b3de407f8d8313e3fc7.json`](../../sessions/3b/3b3de407f8d8313e3fc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-38929 服务器状态报告

### 1. GPU 状态

| GPU | 型号 | 显存使用 | 利用率 | /dev 设备 |
|-----|------|---------|--------|-----------|
| 0 | RTX PRO 6000 Blackwell (96GB) | 1 MiB | 0% | — |
| 1 | RTX PRO 6000 Blackwell (96GB) | 10620 MiB | 36% | nvidia1 |
| 2 | RTX PRO 6000 Blackwell (96GB) | 10560 MiB | 37% | nvidia2 |
| 3 | RTX PRO 6000 Blackwell (96GB) | 1 MiB | 0% | — |

**容器可见 4 GPU，主机设备为 nvidia1/2/4/7**（4 块物理卡映射）。GPU 已恢复到 4 卡配置。

### 2. 活跃实验

| 实验 | PID | CUDA_VISIBLE_DEVICES | 启动时间 | GPU 显存 | 进度 |
|------|-----|---------------------|---------|---------|------|
| `l2norm k=0.925 object` | 985048 | 2 | 07:04 UTC | ~10.5 GB | **T4/10 进行中**，ep30/50，已完成 T1(98%) T2(96%) T3(100%)，当前累计 98.0%，运行 28min |
| `random k=0.9 spatial` | 9135 | 1 | 07:27 UTC | ~10.5 GB | **T0/10 进行中**，ep20/50，SR=85%，运行 5min |

两个实验都是上一轮部署的，均存活且正常推进。

### 3. 空闲资源

- **GPU 0 和 GPU 3 完全空闲**（0% 利用率，无进程占用）
- 可立即分配 2 个新实验

### 4. 结论

服务器状态良好。4 GPU 已恢复，2 个部署实验正常运行，还有 2 个 GPU 空闲可接新任务。

---

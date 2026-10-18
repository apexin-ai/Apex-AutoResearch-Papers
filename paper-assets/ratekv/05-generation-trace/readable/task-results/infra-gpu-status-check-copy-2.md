# infra gpu status check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu_status_check_20260515T194201_result.json`
- **Structured JSON:** [`3db7b78bddf96f3d0f6e.json`](../../sessions/3d/3db7b78bddf96f3d0f6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### phi3_medium_hires_profiling — 已死

- 下载进程 PID 347659 和监控进程 PID 347664 **均已不存在**
- 日志 `/root/ratekv/logs/phi3_profiling.log` 最后写入时间 `00:19:13 CST`（约16小时前），之后停止更新
- 全程只有 "Still downloading..." 循环，说明模型下载过程中进程被杀
- Phi-3 模型下载**不完整**：只下了 `model-00005-of-00006.safetensors`（共6片只有1片），总大小 18GB（完整约 28GB）
- GPU 1 当前 **0 MiB 占用，0% 利用率** — 完全空闲

### codellama_hires_profiling — 正常运行中

- PID 362945 存活，已运行 **49 分钟**
- 正在逐 head 做 2-bit profiling，进度 **228/1024**（约 22%），已耗时 49.6min，ETA ~173min（约 2.9 小时后完成）
- GPU 0 占用 **16,975 MiB / 97,887 MiB**，利用率 **100%**

### GPU 总况

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 16,975 MiB | 100% |
| 1 | RTX PRO 6000 Blackwell (98GB) | 0 MiB | 0% |

**GPU 1 完全空闲**，可用于重新启动 phi3 实验。需要先补完 Phi-3-medium 模型下载（缺 5/6 的 safetensors 分片）。

---

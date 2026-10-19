# ops full server status

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-server-status_20260521T105347_result.json`
- **Structured JSON:** [`71484ed317a4553af6d6.json`](../../sessions/71/71484ed317a4553af6d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总 (westd-13176)

### 1. 模型下载

| 模型 | 状态 | 进度 | 备注 |
|------|------|------|------|
| **Llama4 Scout W4A16** | 🔄 下载中 | 12/14 shards 完成 (60GB + 6.1GB temp) | shard-11 @62% (~33min), shard-14 @67% (~20min), PID 69801 |
| **Qwen3-235B-GPTQ-Int4** | 🔄 下载中 | 24/32 shards 完成 (105GB + 14GB temp) | shard 25-32 在 `._____temp/`，速度 0.6-1.2MB/s，最慢 shard ETA ~77min |
| LLM-Research (Qwen2.5) | ✅ 完成 | 15GB | — |
| Qwen (其他) | ✅ 完成 | 15GB | — |

### 2. 运行中进程

| PID | 进程 | 状态 | 说明 |
|-----|------|------|------|
| **47972** (plan_013_v2) | `probing_controls_v2.py` | ✅ 存活 | 无专用日志文件；最近一轮 probing 结果见下 |
| **78996** (CKA pilot) | `compute_cka.py` (Qwen2.5-7B, langs=zh/ar/hi/sw/ko) | ✅ 存活 | 日志 `/tmp/cka_pilot.log` 0 字节，输出目录空——可能在加载 activations |
| **79164** (CaCLR highdim) | `caclr_highdim.py` (pca_dims=50,100) | ✅ 存活 | 日志 `/tmp/caclr_highdim_pilot.log` 0 字节，输出目录空——同上 |
| **71779** (Watch daemon) | `llama4_watch_daemon.sh` | ✅ 存活 | 每 5 分钟检查 Llama4 下载进度 |
| **69801** | Llama4 modelscope 下载进程 | ✅ 存活 | — |

### 3. GPU & 磁盘

- **GPU**: 4× ~96GB，全部空闲 (3 MiB / 0% util)——CKA 和 CaCLR 是 CPU 计算，暂未占用 GPU
- **磁盘**: `/root/autodl-tmp` 267GB / 350GB (77%)，剩余 **84GB**

### 4. 实验结果

**CKA pilot**: 无输出，目录空。进程在跑但日志 0 字节——可能 stdout/stderr 未正确重定向，或仍在加载数据。

**CaCLR highdim pilot**: 同上，目录 `results/caclr_highdim_pilot/metrics/` 存在但空。

**probing_controls (最新一轮)**，来自 `/tmp/probing_controls7.log`:

| Layer | AUROC | Perm AUROC | Selectivity |
|-------|-------|------------|-------------|
| 0 | 0.5015 | 0.4812 | 13.91 |
| 4 | 0.5243 | 0.4874 | 1.52 |
| 8 | 0.5292 | 0.4925 | 1.26 |
| 12 | 0.5300 | 0.4883 | 1.39 |
| 16 | 0.6152 | 0.4919 | 1.07 |
| 20 | 0.7331 | 0.4885 | 1.05 |
| 24 | 0.7383 | 0.4895 | 1.04 |
| **27** | **0.7459** | 0.4835 | 1.07 |

AUROC 从浅层 ~0.50 到深层 ~0.75 单调递增，说明校准信号主要集中在后半段层。

### 5. 需关注

- **CKA/CaCLR 日志为空**：两个进程都在跑但零输出，建议确认日志重定向是否正确（可能输出到了 stderr）
- **Qwen3 下载剩余 ~8 shards**，按当前速度还需 1-1.5 小时，下载完后总磁盘占用将达 ~290GB/350GB
- **Llama4 还差 2 shards**，约 30 分钟内完成

---

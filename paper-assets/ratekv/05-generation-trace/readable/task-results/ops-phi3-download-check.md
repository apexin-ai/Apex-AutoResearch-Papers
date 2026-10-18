# ops phi3 download check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_phi3_download_check_20260515T180645_result.json`
- **Structured JSON:** [`98df716d2db42605a4b0.json`](../../sessions/98/98df716d2db42605a4b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 下载进度

| 项目 | 状态 |
|------|------|
| PID 351296 | **仍在运行**，已运行 ~1.5h（00:41 启动） |
| 完成分片 | 1/6（`model-00005-of-00006.safetensors`，4.5GB） |
| 进行中分片 | 5 个 `.incomplete` 文件 |

**`.incomplete` 文件明细：**
- 280MB — **自 00:47 起未更新，疑似卡死**（超过 1 小时无变化）
- 2.6GB — **自 01:41 起未更新，疑似卡死**（约 30 分钟无变化）
- 1.7GB — 02:07 仍在写入
- 1.5GB — 02:07 仍在写入
- 960MB — 02:07 仍在写入

**已下载总量：~11.5GB / ~27GB ≈ 43%**

### 问题

日志显示多次 `xethub.hf.co` Read timeout 错误。尽管设置了 `HF_HUB_DISABLE_XET=1`，仍在走 xet 协议——从 ps 命令行看，`source /etc/network_turbo` 和 `export HF_HUB_DISABLE_XET=1` 之间缺少分隔符，env var 可能未生效。

### Chain 到 profiling

**有。** `/tmp/phi3_auto_profiling.sh`（PID 352691）正在后台等待：
- 轮询 `/tmp/phi3_download.log` 中的 "DOWNLOAD COMPLETE" 信号
- 验证 6 个分片均 >2GB
- 然后自动执行 `run_phi3_medium_hires_profiling.py`

### 建议：**切 ModelScope**

- 进度 <50%（43%），2 个分片疑似卡死
- xethub 连接不稳，部分下载长时间无进展
- 按当前有效速率，乐观估计仍需 2+ 小时
- ModelScope CDN 在 AutoDL 上通常快 5-10 倍（参考：同机 CodeLlama-7b 正在用 ModelScope 下载，PID 357568）

操作上需要：kill 351296 → 清理 incomplete 文件 → 用 ModelScope 重新下载 → 重新挂 auto-profiling chain。不做任何修改，等你指示。

---

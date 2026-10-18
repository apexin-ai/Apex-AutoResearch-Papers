# check dual experiment status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_dual_experiment_status_20260514T143223_result.json`
- **Structured JSON:** [`371c1ed91f176731b01d.json`](../../sessions/37/371c1ed91f176731b01d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 任务 1: gemma2_9b_full_pipeline (cuda:0) — 模型下载中

| 项目 | 状态 |
|------|------|
| **阶段** | Downloading (ModelScope → gemma-2-9b) |
| **进度** | 1/8 shards 完成 (shard-07, 4.7G)；shard-06 完成中 (4.66G)；shard-04 85%；shard-03 43% |
| **速度** | 2.7~11 MB/s（波动大） |
| **磁盘** | 已落盘 4.7G / 总计 ~36G |
| **GPU** | 0% / 0MiB — 未开始计算 |
| **预计下载完成** | ~40-60 min（视带宽波动） |

wait_and_run 脚本正常，每 120s 检查 shard 数量，下载进程 PID 227105 存活。

### 任务 2: yi15_9b_full_pipeline (cuda:1) — 模型下载中

| 项目 | 状态 |
|------|------|
| **阶段** | Downloading (ModelScope → Yi-1.5-9B) |
| **进度** | 0/4 shards 完成；shard-02 39% (1.81/4.64G)；shard-04 23% (605M/2.59G)；shard-03 14% (665M/4.63G) |
| **速度** | 0.5~1.7 MB/s（**明显慢于 gemma**） |
| **磁盘** | safetensors 尚未落盘（仅 4.6M 元数据），总计 ~16G |
| **GPU** | 0% / 0MiB — 未开始计算 |
| **预计下载完成** | ~1.5-2 小时 |

wait_and_run 脚本正常，每 60s 检查，下载进程 PID 228878 存活。磁盘空间充足（~128G free）。

### 异常 / 需关注

1. **Yi 下载速度偏慢**（0.5-1.7 MB/s vs Gemma 的 2.7-11 MB/s）。两个下载并行抢带宽，Gemma 启动更早占据了更多带宽。Yi 会在 Gemma 下载完后自动加速，暂不需干预。
2. **wait_and_run_gemma2.sh 的 echo 时间戳是硬编码的**（全部显示 `Thu May 14 21:58:07`），不影响功能但日志没有真实时间。
3. 无其他异常，两个 tmux session 和 wait 脚本均正常运行。

---

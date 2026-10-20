# ssh check exp014 status

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_exp014_status_20260525T154208_result.json`
- **Structured JSON:** [`d9b341f5f00552d420a5.json`](../../sessions/d9/d9b341f5f00552d420a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. exp_014_naturalistic_v2 (PID 233952) — **FAILED**

| 项目 | 值 |
|------|-----|
| 状态 | 进程已结束，exit code 0 |
| 退出时间 | 2026-05-25 16:37 CST |
| 实际运行 | ~1h46m (14:51 → 16:37) |
| 到达阶段 | 仅 Phase 1，未进入 Phase 2/3 |

**失败原因**：卡在 Phase 1 "Data Sampling from FineWeb"。HF datasets 库对 FineWeb 做全量文件树枚举（18,646 次 HTTP API 请求），三个 crawl split 全部断连：
- `CC-MAIN-2025-26`：14:54:29 — "Server disconnected without sending a response"
- `CC-MAIN-2024-51`：15:58:07 — 同上
- `default`：开始枚举后日志截止于 15:58:29

另外，日志第 6 行有 WARNING：`You are sending unauthenticated requests to the HF Hub`——没设 HF_TOKEN，导致限速严重。

### 2. exp_014_independent_metrics (PID 234919) — **STUCK (死循环)**

| 项目 | 值 |
|------|-----|
| 状态 | 仍在运行，已运行 8h28m+ |
| 原因 | `while [ ! -f cc_predictions.csv ]; do sleep 60` 永远等不到 v2 的产出 |
| 动作 | 需要 kill |

### 产出文件

| 文件 | 状态 |
|------|------|
| `data_exp014_v2/` | **空目录** — 无任何数据文件 |
| `results/exp014_v2/run.log` | 7.8MB, 18657 行（几乎全是 HF API 日志） |
| `cc_sample.jsonl` | 不存在 |
| `cc_features.csv` | 不存在 |
| `cc_predictions.csv` | 不存在 |
| `cc_quality_independent.csv` | 不存在 |
| `analysis_results.json` | 不存在 |
| `independent_analysis_results.json` | 不存在 |

GPU 当前无进程占用。

### 根因

FineWeb 是 ~15TB 数据集，文件树极大。`datasets` streaming 模式先枚举全部 parquet 文件再开始流式读取。AutoDL 网络 + 无 HF_TOKEN 组合下，枚举极慢且连接反复断开。需要：
1. 设置 `HF_TOKEN` 提升速率限制
2. 指定精确的 split/config 避免全量枚举
3. 或改用更小的子集 / 预下载方式

需要我 kill 掉 PID 234919 吗？

---

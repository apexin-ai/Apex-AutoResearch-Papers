# ops full status and pilots

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-status-and-pilots_20260521T104446_result.json`
- **Structured JSON:** [`d0137c20a51f2e39e3c9.json`](../../sessions/d0/d0137c20a51f2e39e3c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

---

### 状态汇总

| # | 项目 | 状态 | 详情 |
|---|------|------|------|
| 1 | **Llama4 下载** | 进行中 | PID 69801, 运行 2h27m。11/14 shards, 63GB。正在下载 shard 12/14 (86%, 3.58MB/s) |
| 2 | **Qwen3 下载** | 进行中 | PID 68080, 运行 3h03m。24 safetensors, 114GB。正在下载 shard 29/32 (22%, 741kB/s) |
| 3 | **plan_013_v2** | 运行中 | PID 47972, 运行 9h49m, 103% CPU。已完成 3/8 层：L0=0.6304, L12=0.6389, L16=0.6801 AUROC |
| 4 | **CKA pilot** | 已启动 | Python PID 78996, 3100% CPU, 1.2GB RSS |
| 5 | **CaCLR pilot** | 已启动 | Python PID 79164, 3031% CPU, 2.3GB RSS |
| 6 | **磁盘** | 76% | 264G/350G used, 87G free |
| 7 | **Llama4 验证** | 跳过 | 尚未完成（11/14 shards） |

**注意**：发现一个先前存在的 CKA 运行 (PID 77012, model=qwen25-7b-mvp, n_bootstrap=1000)，已运行较长时间，与本次新启动的 pilot 独立。

---

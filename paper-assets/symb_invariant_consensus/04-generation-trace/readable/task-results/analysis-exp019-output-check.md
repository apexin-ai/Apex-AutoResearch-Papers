# analysis exp019 output check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp019-output-check_20260517T085656_result.json`
- **Structured JSON:** [`0aec7cb73e8371d0c95b.json`](../../sessions/0a/0aec7cb73e8371d0c95b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态: **RUNNING** (142/200)

实验正在运行中，当前进度和中间统计：

| 指标 | 值 |
|---|---|
| 已完成 | 143/200 (结果文件) |
| 日志进度 | 正在处理 #142 |
| GPU 利用率 | 99%, 88309/97887 MiB |
| tmux session | `exp-019-llama8b-strategyqa-200` 活跃 |

**中间统计 (n=143):**

| 指标 | 值 |
|---|---|
| SICA accuracy | 74.13% (106/143) |
| SC accuracy | 72.03% (103/143) |
| Delta | **+2.10pp** |
| k | 12 |
| temperature | 0.7 |

SICA 领先 SC 2.1 个百分点。实验预计还剩 57 题，按当前速度（约 40 分钟已完成 143 题）大约还需 ~15 分钟完成。结果文件实时写入，包含 `constraints_stats`、`maxsat_stats`、`wall_time_s` 等详细字段。

完成后需要我跑完整统计（McNemar + bootstrap CI）吗？

---

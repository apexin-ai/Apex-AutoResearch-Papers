# ops urgent kill gpu4 clean

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-kill-gpu4-clean_20260515T233812_result.json`
- **Structured JSON:** [`dab341770ba4a860f442.json`](../../sessions/da/dab341770ba4a860f442.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

### 1. GPU 4 完全清空 ✓
```
GPU 4: 0 MiB / 24564 MiB, 0% utilization
无任何 compute app 进程
```

### 2. 重生源头分析
**未发现自动重生机制**：
- 无 crontab
- 无 while/watch/for 循环自动重启
- 无 systemd 服务

PID 657228 是单次执行的进程（可能由之前的 Worker session 通过 tmux 提交），kill 后未重生。之前 4 次重生很可能是不同 Worker session 各自独立提交的，而非同一机制自动重启。

### 3. 源头已清除 ✓
PID 657228 已 kill，GPU 4 内存归零，无残留。

### 4. 全 GPU 状态快照
| GPU | 显存占用 | 总显存 | 利用率 |
|-----|---------|--------|--------|
| 0 | 23258 MiB | 24564 MiB | 91% |
| 1 | 13341 MiB | 24564 MiB | 7% |
| 2 | 7537 MiB | 24564 MiB | 62% |
| 3 | 8985 MiB | 24564 MiB | 0% |
| **4** | **0 MiB** | **24564 MiB** | **0%** |
| 5 | 18665 MiB | 24564 MiB | 64% |

### 5. 其他 compute_signals 进程
cuda:2 上 v7（PID 652259）正在处理 `Qwen2.5-3B_d005_s123` 的 mmlu benchmark — 这是合法 alpha=32 任务，未动。

---

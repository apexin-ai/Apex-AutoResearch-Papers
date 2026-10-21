# ssh 2h monitor post restart

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_2h_monitor_post_restart_20260524T040646_result.json`
- **Structured JSON:** [`d9b55255593b5022e8cb.json`](../../sessions/d9/d9b55255593b5022e8cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## autodl-8gpu 状态报告

### 1. collect.py 进程 — **6 个全部存活** ✓
| Judge | PID | Workers | 类型 |
|-------|-----|---------|------|
| LLaMA-3.3-70B local | 503734 | 4 | local |
| Qwen2.5-72B local | 505793 | 4 | local |
| Claude Sonnet 4.6 | 506658 | 10 | proxy |
| Gemini 2.5 Pro | 506876 | 10 | proxy |
| DeepSeek V4 Pro | 506930 | 10 | proxy |
| Qwen3-235B | 506990 | 10 | proxy |

（ps 输出 11 行含 bash wrapper 进程，实际 python 进程 6 个，符合预期）

### 2. vLLM — **2 个存活，健康检查通过** ✓
- Port 8001 (LLaMA-3.3-70B-AWQ): HTTP 200
- Port 8002 (Qwen2.5-72B-AWQ): HTTP 200

### 3. Judge 进度（n17 轮次）

| Judge | 完成 / 总数 | 进度 |
|-------|------------|------|
| Claude Sonnet 4.6 | 3,855 / 17,982 | 21.4% |
| Qwen3-235B | 2,488 / 16,890 | 14.7% |
| Gemini 2.5 Pro | 2,479 / 17,092 | 14.5% |
| DeepSeek V4 Pro | 2,058 / 17,138 | 12.0% |
| LLaMA-3.3-70B local | 328 / 17,982 | 1.8% |
| Qwen2.5-72B local | 213 / 17,982 | 1.2% |

Local judge 速度慢（~0.0 items/s 显示），但进程在推进（行数在增长）。

### 4. 日志 — **无异常** ✓
所有 collector 正常推进，无错误输出。

### 5. exp-017 — **存活** ✓
PID 318082，已运行 21h03m32s。

### 6. GPU

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 73.9 / 97.9 GB | 70% |
| 1 | 90.1 / 97.9 GB | 100% |
| 2 | 90.2 / 97.9 GB | 100% |
| 3 | 0 / 97.9 GB | 0% (空闲) |

GPU 1/2 被 vLLM 占满，GPU 0 被 exp-017 使用，GPU 3 空闲。

### 7. 磁盘 — **85% 使用** ⚠️
212G / 250G used，剩余 39G。暂可用但需关注。

### 8. rtx6000-4x 连通性 — **不可达** ❌
autodl-8gpu 无法解析 `rtx6000-4x` 主机名（该 hostname 配置在本地 `~/.ssh/config`，autodl-8gpu 上没有该配置，这是预期行为——rtx6000-4x 的连通性应从本地检查）。

---

**总结：所有关键进程正常运行，无异常。** 磁盘 85% 需留意，local judge 速度较慢但在推进。

---

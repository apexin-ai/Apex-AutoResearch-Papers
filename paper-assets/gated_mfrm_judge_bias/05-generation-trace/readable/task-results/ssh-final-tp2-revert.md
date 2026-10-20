# ssh final tp2 revert

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_final-tp2-revert_20260524T122805_result.json`
- **Structured JSON:** [`ce841365f8d1faeabaaa.json`](../../sessions/ce/ce841365f8d1faeabaaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是最终报告。

---

## TP=2 恢复完成报告

### 1. vLLM 进程（确认 TP=2）
| 模型 | PID | TP | GPUs | Port |
|------|-----|----|------|------|
| LLaMA-3.3-70B-AWQ | 582367 | 2 | cuda:0,1 | 8001 |
| Qwen2.5-72B-AWQ | 583073 | 2 | cuda:2,3 | 8002 |

### 2. collect.py 进程
| Judge | PID | Workers |
|-------|-----|---------|
| llama-3.3-70b-local | 584106 | 64 |
| qwen2.5-72b-local | 584197 | 64 |

### 3. GPU 显存使用
| GPU | Used / Total | Utilization |
|-----|-------------|-------------|
| 0 | 89,031 / 97,887 MiB | 100% |
| 1 | 89,031 / 97,887 MiB | 100% |
| 2 | 89,083 / 97,887 MiB | 100% |
| 3 | 89,083 / 97,887 MiB | 100% |

### 4. 吞吐量（严格协议，2 × ≥2min 窗口）

**Window 1** (T0 20:37:33 → T1 20:39:31, 118s):

| Judge | T0 | T1 | Δ | rate_1 |
|-------|----|----|---|--------|
| LLaMA | 6,799 | 6,895 | +96 | **48.8 lines/min** |
| Qwen | 4,506 | 4,578 | +72 | **36.6 lines/min** |

**Window 2** (T1 20:39:31 → T2 20:41:30, 119s):

| Judge | T1 | T2 | Δ | rate_2 |
|-------|----|----|---|--------|
| LLaMA | 6,895 | 7,007 | +112 | **56.5 lines/min** |
| Qwen | 4,578 | 4,649 | +71 | **35.8 lines/min** |

**平均吞吐量**:
- LLaMA: **(48.8 + 56.5) / 2 = 52.7 lines/min**
- Qwen: **(36.6 + 35.8) / 2 = 36.2 lines/min**
- 合计: **88.9 lines/min**（预期 ~87.8，吻合）

### 5. 6 Judge n17 数据量与完成度

| Judge | Lines | / 18,000 | 完成% |
|-------|-------|----------|-------|
| claude-sonnet-4.6-proxy_n17 | 11,363 | 18,000 | 63.1% |
| qwen3-235b-proxy_n17 | 8,866 | 18,000 | 49.2% |
| gemini-2.5-pro-proxy_n17 | 8,343 | 18,000 | 46.3% |
| deepseek-v4-pro-proxy_n17 | 7,142 | 18,000 | 39.6% |
| llama-3.3-70b-local_n17 | 7,017 | 18,000 | 38.9% |
| qwen2.5-72b-local_n17 | 4,665 | 18,000 | 25.9% |

注：`mistral-large-2-local_n17` 仅 118 条（0.6%），当前无 collect 进程运行。

### 6. 剩余 Records 与 ETA（本地 judge）

| Judge | 剩余 | 速率 | ETA |
|-------|------|------|-----|
| LLaMA | 10,983 | 52.7/min | **~3h 28min** |
| Qwen | 13,335 | 36.2/min | **~6h 8min** |

Qwen 为瓶颈，预计 ~6h 完成全部采集。

---

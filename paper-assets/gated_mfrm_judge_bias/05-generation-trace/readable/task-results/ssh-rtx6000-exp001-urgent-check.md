# ssh rtx6000 exp001 urgent check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rtx6000_exp001_urgent_check_20260522T230944_result.json`
- **Structured JSON:** [`a10f6e48b8cf310c6cc1.json`](../../sessions/a1/a10f6e48b8cf310c6cc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### GPU 状态

| GPU | 利用率 | 显存 | 进程 | 状态 |
|-----|--------|------|------|------|
| cuda:0 | 68% | 74.7/97.9 GB | exp009 (run_exp009.py) | 正常 |
| cuda:1 | **0%** | 90.2/97.9 GB | vLLM Qwen2.5-72B (port 8002) | **空转** |
| cuda:2 | 100% | 91.0/97.9 GB | vLLM Llama-3.3-70B (port 8001) | 正常 |
| cuda:3 | 97% | 90.0/97.9 GB | vLLM Mistral-Large (port 8003) | 正常 |

### 收集进度（本地 Judges）

| Judge | 进度 | ETA | PID | 状态 |
|-------|------|-----|-----|------|
| **Qwen2.5-72B** | **9281 lines (8534 judgments) — 已完成** | — | — | collect.py 正常退出 |
| Llama-3.3-70B | 4056/8311 (49%) | ~1248 min (~20.8h) | 332474 | 运行中 |
| Mistral-Large-2 | 8133/8742 (93%) | ~107 min (~1.8h) | 332512 | 运行中 |

### Proxy Judges 进度

| Judge | Lines |
|-------|-------|
| claude-opus-4.7-proxy | 9138 |
| claude-sonnet-4.6-proxy | 8774 |
| gpt-5.5-proxy | 8447 |
| qwen3-235b-proxy | 7235 |
| gemini-2.5-pro-proxy | 6827 |
| deepseek-v4-pro-proxy | 6129 |

### 根因

**没有进程崩溃。** Qwen2.5-72B 的 collect.py 已正常完成（"Done. 8534 pairwise judgments in 549.2min"），但 vLLM 服务器未被清理，仍占用 cuda:1 的 90GB 显存。Registry 状态未更新。

### 建议操作

1. **关掉 cuda:1 上的 Qwen vLLM 服务器**（PID 420981），释放 90GB 显存
2. 更新 registry 标记 Qwen 为 COMPLETED
3. 释放的 cuda:1 可用于加速 Llama 的收集（目前还需 ~21h）

是否要我执行这些操作？

---

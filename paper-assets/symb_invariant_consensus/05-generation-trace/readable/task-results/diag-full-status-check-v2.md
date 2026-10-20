# diag full status check v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_full-status-check-v2_20260519T124946_result.json`
- **Structured JSON:** [`91df69940b7caa64d82a.json`](../../sessions/91/91df69940b7caa64d82a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有实验均在运行中，无已完成实验。汇总如下（当前时间 ≈ 20:52 UTC）：

## westd-25068（4 GPU 全满，96-98% util）

| 实验 | 状态 | 进度 | 速率 | ETA |
|------|------|------|------|-----|
| exp-065 Qwen2.5-7B PW-600 | 运行中 | 419/600 | ~1.75/min | ~22:35 |
| exp-062 Gemma-27B FOLIO-204 | 运行中 | 128/204 | ~0.56/min | ~23:08 |
| exp-069 Mistral-7B LogiQA-200 | 运行中 | 151/200 | ~2.44/min | ~21:12 |
| exp-070 Qwen2.5-7B LogiQA-200 | 运行中 | 178/200 | ~3.24/min | ~20:59 |

## westd-16639（4 GPU 全满，96-97% util）

| 实验 | 状态 | 进度 | 速率 | ETA |
|------|------|------|------|-----|
| exp-048 LLaMA-8B PW-600 | 运行中 | 484/600 | ~0.77/min | ~23:23 |
| exp-068 Qwen3-14B LogiQA-200 | 运行中 | 180/200 | ~1.82/min | ~21:03 |
| exp-069 LLaMA-8B LogiQA-200 | 运行中 | 67/200 | ~1.43/min | ~22:25 |
| exp-064 DeepSeek-R1-Qwen3-8B FOLIO-204 | 运行中 | 87/204 (resumed) | ~0.37/min | ~02:08 |

## 需要注意的问题

**1. exp-070 双 runner 冲突（westd-25068）**
同时运行了 `run_logiqa.py`（PID 213761）和 `run_full_mvp.py`（PID 214184），两者都写入同一输出文件 `exp070_results.json`，共享同一 vLLM server（port 8002）。这会导致数据竞争和结果不可靠。建议 kill 其中一个。

**2. exp-064 并未被 kill（westd-16639）**
exp-064 有活跃的 tmux session（`exp064_vllm` + `exp064_run`，创建于 20:05-20:06），vLLM 在 cuda:0 port 8002 运行 `deepseek-r1-0528-qwen3-8b`，runner 正在以 `--resume` 模式执行。当前进度 87/204。

**3. 无已完成实验**
所有 8 个实验均在运行中，暂无可提取 metrics 的已完成实验。最先完成的将是 exp-070（~7min）和 exp-068（~11min）。

---

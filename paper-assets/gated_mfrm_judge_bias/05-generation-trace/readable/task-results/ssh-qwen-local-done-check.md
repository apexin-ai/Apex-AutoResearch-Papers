# ssh qwen local done check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_qwen-local-done-check_20260524T182611_result.json`
- **Structured JSON:** [`7d94aaaf0f75b49dd9bb.json`](../../sessions/7d/7d94aaaf0f75b49dd9bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Qwen local (Qwen2.5-72B-Instruct) — 完成

- **行数**: 17,994 / 18,000（99.97%）
- **最后写入时间**: 2026-05-25 02:22:43
- **状态**: 正常完成退出。6 条缺失可能是个别 prompt 缺 response 或 max_retries 耗尽
- **输出文件**: `exp001/results/qwen2.5-72b-local_n17/arena_hard_judgments.jsonl`
- 日志中无报错，最后几条 status 均为 `"ok"`

### 其他 judge 状态

| Judge | PID | 状态 | 进度 |
|-------|-----|------|------|
| Qwen3-235B (proxy) | 592432 | ALIVE | 17,558 / 18,000 |
| DeepSeek-v4-pro (proxy) | 592328 | ALIVE | 13,416 / 18,000 |
| Llama-3.3-70B (local) | — | Done | 18,093 ✓ |
| Mistral-Large-2 (local) | — | Done | 118 (注：这是旧 n17 文件) |

### MCMC monitor (PID 605265) — 正常运行

- 每分钟轮询一次
- 当前状态识别："Qwen local: done, Qwen3: running"
- 等待 Qwen3 完成后触发 MCMC phase 1

### 结论

- Qwen local 采集**成功完成**，无需干预
- vLLM Qwen server (PID 583078) 仍在运行——如不再需要可关闭释放 GPU 2,3
- Qwen3 预计很快完成（还剩 ~442 条），完成后 MCMC monitor 会自动触发
- DeepSeek 还需一些时间（剩余 ~4,584 条）
- 无需更新 cron

---

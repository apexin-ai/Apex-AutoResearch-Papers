# infra gpt41 extraction cron check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpt41-extraction-cron-check_20260521T164753_result.json`
- **Structured JSON:** [`6943db08959416358147.json`](../../sessions/69/6943db08959416358147.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. gpt-4.1 Mistral cross-extraction: **已完成（成功）**

- PID 456759 已退出，日志末尾输出 `CROSS_MODEL_DONE`
- **Cross-model SICA: 166/204 = 0.8137**
- Original SICA: 169/204 = 0.8284
- SC@K baseline: 169/204 = 0.8284
- Wall time: 60.2 min

### 2. 输出文件

| 文件 | 大小 |
|------|------|
| `cross_model_mistral.json` | 267KB, 6449 行 |
| `results.json` | 17802 行 |
| `intermediates/` | 204 个 folio JSON (folio_0 ~ folio_203) |
| `extraction.log` | 327KB |

### 3. 其他 frontier 进程

- **gpt-5.5** (PID 444813): 仍在运行 — `run_frontier_scb.py --models gpt-5.5`
- **o3** (PID 444814): 仍在运行 — `run_frontier_scb.py --models o3`

另外该服务器上还有多个其他实验在跑：exp_d126_crossmodel_sica (PID 414515)、exp_d126_70b_sica (PID 436084)、exp_r1_distill_8b_sica (PID 451580)，以及 4 个 vLLM 服务（Mistral:8000, Qwen3-14B:8001, 70B(?):8002, R1-Distill-8B:8003）。

---

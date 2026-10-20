# check running experiments progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running_experiments_progress_20260514T135353_result.json`
- **Structured JSON:** [`9725f3359aa7dfc45ed8.json`](../../sessions/97/9725f3359aa7dfc45ed8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

---

## 实验状态报告

### 实验 1: llama_scierc_full_s1 (Llama-3.1-8B, SciERC, full_s1)

| 指标 | 值 |
|------|-----|
| 进程状态 | **ALIVE** (PID 190648, 运行 3h34m) |
| 已处理 | ~82-89 / 551 samples (~15%) |
| 输出文件 | 82 行 (`outputs/llama_scierc_full_s1.jsonl`) |
| GPU 0 | 利用率 94%, 显存 32.3/97.9 GB |
| 每 sample 耗时 | ~2.4 min (3.56h / 89 samples) |
| **预估剩余** | **~18.5 小时** (462 samples × 2.4 min) |
| **预估完成** | **~2026-05-15 08:40 UTC** |

注意：日志中大量 `Grammar-first fallback triggered` 消息，说明 semantic mask 频繁与 grammar mask 冲突，每个 sample 都要走 fallback 路径。这可能是速度慢的原因之一。

### 实验 2: phase2_docred_semantic_only (Qwen3-8B, DocRED, semantic_only)

| 指标 | 值 |
|------|-----|
| 进程状态 | **ALIVE** (PID 172859, 运行 5h23m) |
| 已处理 | 820 / 998 samples (82%) — 日志显示 `[820/998]` |
| 输出文件 | 943 行（⚠️ 含前次运行残留，日志实际 processed 811 个 OK） |
| GPU 1 | 利用率 85%, 显存 17.5/97.9 GB |
| 每 sample 耗时 | ~23.6 sec (5.38h / 820 samples) |
| **预估剩余** | **~70 分钟** (178 samples × 23.6s) |
| **预估完成** | **~2026-05-14 15:25 UTC** |

### GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 (Llama) | 94% | 32.3 / 97.9 GB |
| cuda:1 (DocRED) | 85% | 17.5 / 97.9 GB |

两块 GPU 都在正常工作。DocRED 实验约 1 小时后完成；Llama 实验还需要很久（~18.5h），主要因为 full_s1 模式下 grammar-semantic 冲突严重导致 fallback 频繁。

---

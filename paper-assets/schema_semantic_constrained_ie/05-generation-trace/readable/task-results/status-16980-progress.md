# status 16980 progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_16980_progress_20260520T010650_result.json`
- **Structured JSON:** [`023dad5351e72bcc7d2d.json`](../../sessions/02/023dad5351e72bcc7d2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**Qwen greedy unconstrained (GPU0)**
- 日志进度: 167/998 (16.7%)
- jsonl 行数: 275（可能含前次残留数据，日志计数器更可靠）
- 速度: ~2.1 doc/min（07:49 启动，已运行 ~78min）
- ETA: ~6.5 小时（约 15:30）

**Qwen greedy constrained (GPU1, cascade)**
- jsonl 行数: 129/998 (12.9%)
- cascade 日志只记录了模型加载，处理进度未写入日志文件（可能用 `\r` 覆盖输出）
- 速度: ~3.2 doc/min（08:27 启动，已运行 ~40min）
- ETA: ~4.5 小时（约 13:30）

**GPU 利用率**
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 87% | 18.9/97.9 GB |
| 1 | 85% | 18.9/97.9 GB |

**Llama greedy 文件完整性** — 已完成
- `d064_llama_docred_greedy_unconstrained_w5.jsonl`: 998/998
- `d064_llama_docred_greedy_constrained_w5.jsonl`: 998/998

注意：unconstrained jsonl (275行) 与日志计数器 (167/998) 不一致，可能是启动前未清空旧文件。如果需要干净数据，完成后需确认是否要截断前 N 行。

---

# analysis mistral folio 789 final harvest

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral-folio-789-final-harvest_20260522T111627_result.json`
- **Structured JSON:** [`53f51e51d4da57e02b1a.json`](../../sessions/53/53f51e51d4da57e02b1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Mistral FOLIO seed=789 — 未完成，仍在运行中**

| 指标 | 状态 |
|------|------|
| PID 576938 | **ALIVE** |
| 进度 | **76/204** (37%) |
| 已完成文件 | 76 个 (folio_0 ~ folio_75) |
| ETA | **~48 分钟** (129 remaining, avg 22.2s/prob) |
| 预计完成时间 | ~20:05 UTC (2026-05-22) |

### GPU 状态

| GPU | Util | VRAM Used |
|-----|------|-----------|
| 0 | 97% | 90,159 MiB |
| 1 | 96% | 88,263 MiB |
| 2 | 96% | 90,213 MiB |
| 3 | 100% | 90,201 MiB |

4 卡全部满载运行。

### 已有 Mistral FOLIO 数据（待 seed=789 完成后合并）

| Run | SC | SICA | Δ |
|-----|-----|------|---|
| exp052 (seed=123) | 53.92% | 57.35% | +3.43pp |
| exp053 (seed=456) | 56.37% | 55.88% | -0.49pp |
| seed=789 | *running* | *running* | — |

seed=789 预计约 48 分钟后完成，届时可收割完整三种子结果并计算 mean±SD。

---

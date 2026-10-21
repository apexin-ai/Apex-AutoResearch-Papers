# ops check docred progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_docred_progress_20260514T022901_result.json`
- **Structured JSON:** [`20eb81cbe1b33b8c9804.json`](../../sessions/20/20eb81cbe1b33b8c9804.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DocRED Phase 2 实验进度

| 实验 | 进度 | 速率 | 预计剩余 |
|------|------|------|----------|
| grammar_only | **102 / 998** (10.2%) | ~2.9 行/min (运行 35 min) | ~5.1 小时 |
| full_s1 | **71 / 998** (7.1%) | ~3.0 行/min (运行 24 min) | ~5.1 小时 |

**进程状态:** 两个均存活，CPU 100%
- PID 150766 (grammar_only) → GPU 0
- PID 152032 (full_s1) → GPU 1

**GPU 利用率:**

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 85% | 17,451 / 97,887 MiB |
| 1 | 83% | 17,223 / 97,887 MiB |

两个实验都在正常推进，预计约 5 小时后完成。完成后再运行 violation_checker。

---

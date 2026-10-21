# ssh kill 403 restart deepseek

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-403-restart-deepseek_20260524T174640_result.json`
- **Structured JSON:** [`6a214193ec86de59ef08.json`](../../sessions/6a/6a214193ec86de59ef08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both tasks are already in the desired state. Here's the full status:

```
=== Sonnet/Gemini Kill ===
Sonnet 进程: 已自行退出（全部 403 地域封锁）
Sonnet 最终行数: 14,255 行 (arena_hard_judgments.jsonl)
  - 启动时已有 10,522 completed，之后全部 403 未新增有效数据

Gemini 进程: 已自行退出（全部 403 地域封锁）
Gemini 最终行数: 11,253 行 (arena_hard_judgments.jsonl)
  - 启动时已有 6,633 completed，之后全部 403 未新增有效数据

无需手动 kill，进程均已退出。

=== DeepSeek 状态 ===
已在 workers=10 运行，无需重启。
PID: 592328
进度: [2890/12057], 0.3 items/s, ETA ~531 min (~9h)

=== 最终状态 ===
Active collect processes:
  1. Qwen local  (PID 584197) — workers=64, [11940/13590], ETA ~42 min
  2. DeepSeek    (PID 592328) — workers=10, [2890/12057],  ETA ~531 min
  3. Qwen3       (PID 592432) — workers=10, [4930/9969],   ETA ~170 min

GPU usage:
  GPU 0: 空闲 (0 MiB / 97887 MiB)
  GPU 1: 空闲 (0 MiB / 97887 MiB)
  GPU 2: Qwen vLLM (89083 MiB / 97887 MiB)
  GPU 3: Qwen vLLM (89083 MiB / 97887 MiB)
```

Sonnet/Gemini 已因 403 自行退出，DeepSeek 已经是 workers=10，均无需操作。

---

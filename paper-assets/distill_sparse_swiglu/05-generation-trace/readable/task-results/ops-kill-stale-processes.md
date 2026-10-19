# ops kill stale processes

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_stale_processes_20260515T223733_result.json`
- **Structured JSON:** [`3858575a0d7e727fcae2.json`](../../sessions/38/3858575a0d7e727fcae2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 7 个 PID 均已不存在（`ps` 返回空，exit code 1）。

**处理结果：**

| PID | 描述 | 状态 |
|-----|------|------|
| 152728 | 重复 ARC test (max_eval_samples 50) | 已不存在，无需 kill |
| 148236 | 卡死 C4 streaming | 已不存在，无需 kill |
| 46706, 46711, 46712 | 卡死 wikitext | 已不存在，无需 kill |
| 153259 | dense ARC 完整版 | 已不存在 |
| 152874 | kl_sparsity70 eval | 已不存在 |

所有进程都已自行结束。需要继续运行的 153259 和 152874 也不在了，可能需要检查它们的输出日志确认是正常完成还是异常退出。

---

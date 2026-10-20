# ops restart downloads phi4 olmo2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-downloads-phi4-olmo2_20260518T102404_result.json`
- **Structured JSON:** [`4babe9bac3565203d0b2.json`](../../sessions/4b/4babe9bac3565203d0b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个下载均已成功启动并存活：

| 模型 | PID (bash) | PID (python) | 状态 |
|------|-----------|-------------|------|
| OLMo-2-1124-7B | 19570 | 19571 | Fetching 16 files |
| Phi-4 | 19607 | 19608 | Fetching 21 files |

另外观察到服务器上还有 Qwen2.5-14B (PID 5066) 和 gemma-2-9b (PID 6380) 的下载也在运行中。

---

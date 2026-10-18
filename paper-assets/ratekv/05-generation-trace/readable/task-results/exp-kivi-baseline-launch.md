# exp kivi baseline launch

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_kivi_baseline_launch_20260515T112557_result.json`
- **Structured JSON:** [`c0c9bbd13c0ff29f22df.json`](../../sessions/c0/c0c9bbd13c0ff29f22df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验运行正常。

**结果汇总：**

| 项目 | 状态 |
|------|------|
| Dry-run | **PASS** |
| PID | **328260** |
| 模型 | Qwen2.5-7B (Qwen2___5-7B) |
| KIVI-2bit PPL | **12.8273** (已完成) |
| KIVI-4bit | 正在运行中 |
| 日志 | `/root/ratekv/logs/kivi_baseline_qwen.log` |
| 输出 | `artifacts/kivi_qwen25_7b.json` |

KIVI-2bit 跑完用了约 15 秒内完成 583 chunks，4bit 正在评估中。预计 4bit 完成后总耗时约 1-2 分钟。可以稍后查日志确认最终结果。

---

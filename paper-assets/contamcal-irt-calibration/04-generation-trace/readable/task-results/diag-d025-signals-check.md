# diag d025 signals check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_d025_signals_check_20260516T230521_result.json`
- **Structured JSON:** [`1283fb299d52a4fb253c.json`](../../sessions/12/1283fb299d52a4fb253c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**结论：failed**（MMLU 不完整）

| Benchmark | s1_embedding | s2_minkpp | s4_selfcritique | merged |
|-----------|:---:|:---:|:---:|:---:|
| MMLU | ✓ | ✓ | ✗ (10000/14042) | ✗ |
| ARC | ✓ | ✓ | ✓ | ✓ (235KB) |
| GSM8K | ✓ | ✓ | ✓ | ✓ (244KB) |

**故障原因**：MMLU s4_selfcritique 在处理 chunk [10000:11000] 时静默中断（无 error/OOM 日志），脚本跳过了 MMLU 直接执行了 ARC 和 GSM8K。已有 10 个 chunk 文件 (0-10000) 可恢复，只需补算 10000-14042 再 merge。

---

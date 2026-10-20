# ssh qwen unc integrity check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_qwen_unc_integrity_check_20260520T011147_result.json`
- **Structured JSON:** [`422fa3654bb80725e2e6.json`](../../sessions/42/422fa3654bb80725e2e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**文件完整，无需干预。**

| 文件 | 行数 | 唯一 doc_id | 重复 |
|------|------|-------------|------|
| unconstrained.jsonl | 300 | 300 | 0 |
| constrained.jsonl | 158 | 158 | 0 |

**日志与 JSONL 行数不一致的原因**：启动命令没有 `--resume`，文件以 `"w"` 模式打开（截断），所有数据来自本次运行。脚本在写 JSONL 后调用了 `fout.flush()`（第 1070 行），但 `print()` 输出到 stdout 是 block-buffered（因为被重定向到文件）。所以 JSONL 是实时的，日志滞后约 133 条。

- **无前次运行残留**
- **JSONL 是真实进度指标**，日志会在 buffer flush 时追上
- **eval 不受影响**——无重复数据需要去重
- 两个进程（PID 676441 unc / PID 682762 con）都在正常运行

---

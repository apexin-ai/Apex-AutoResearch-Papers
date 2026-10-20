# ops p0 21461 final rerun

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0_21461_final_rerun_20260520T095139_result.json`
- **Structured JSON:** [`d61ecda98de87391a2b9.json`](../../sessions/d6/d61ecda98de87391a2b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇总如下：

## 执行结果

| # | 项目 | 结果 |
|---|------|------|
| 1 | Kill 174618 | 已不存在（之前已死） |
| 2 | Kill 残留进程 | 194290/194295 已 kill ✓ |
| 3 | GPU 释放 | 双 GPU 归零 ✓ |
| 4 | 损坏文件删除 | 3 个文件已删 ✓ |
| 5 | 原始 con 命令 | `--mode full_s1 --dataset docred --decoding_strategy greedy --max_new_tokens 4096 --skip_on_error` |
| 6 | 重跑命令 | 与原始一致，`--output_path` 改为 `_rerun.jsonl`，`CUDA_VISIBLE_DEVICES=0` |
| 7 | 新进程 PID | **194615**（wrapper 194610） |
| 8 | GPU0 占用 | 85%, 18919 MiB ✓ |
| 9 | 输出文件行数 | **4 行**（正在增长） |
| 10 | Qwen unc 文件 | **998 行**（完整 ✓） |

---

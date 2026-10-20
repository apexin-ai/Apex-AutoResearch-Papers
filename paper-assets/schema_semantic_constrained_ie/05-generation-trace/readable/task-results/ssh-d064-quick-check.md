# ssh d064 quick check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_quick_check_20260519T131119_result.json`
- **Structured JSON:** [`e91920578397d427108d.json`](../../sessions/e9/e91920578397d427108d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 都在跑，两个 python 进程活跃。

**汇总：**

| 指标 | 状态 |
|------|------|
| GPU 0 | 18275 MiB, 90% 利用率 |
| GPU 1 | 18921 MiB, 89% 利用率 |
| Python 进程 | 2 个在跑 |
| Qwen unc (beam4) | **681 行**（上次 614，+67） |
| Llama greedy unc | **648 行**（上次 546，+102） |
| Llama cascade log | 正常推理中（pad_token_id 设置日志） |

**进程仍在跑，两个文件都在稳步增长。** Llama greedy 增速更快（+102 vs +67）。

---

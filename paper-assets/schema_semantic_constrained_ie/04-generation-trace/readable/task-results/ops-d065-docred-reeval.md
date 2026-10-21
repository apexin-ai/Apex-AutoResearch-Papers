# ops d065 docred reeval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d065_docred_reeval_20260520T141926_result.json`
- **Structured JSON:** [`042969249cf0a4448d54.json`](../../sessions/04/042969249cf0a4448d54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 d065 完整文件评估完毕。Qwen con rerun 还在跑（714/998），预计约 1h45m 后完成。

d065 评估结果（eval_d064.py）：

| Source | Model | Mode | E-F1 | R-F1 | DR% | CF% | PF% |
|--------|-------|------|------|------|-----|-----|-----|
| d065 | Llama | unc | 84.77 | 44.55 | 0.49 | 0.08 | 2.3 |
| d065 | Llama | con | 84.71 | 44.70 | 0.00 | 0.26 | 2.6 |
| d065 | Qwen | unc | 82.35 | 40.89 | 0.56 | 0.08 | 6.8 |
| d065 | Qwen | con | *running* (714/998, ~00:06 完成) | | | | |

与 w5 Table 2 当前值对比：

| Model | Mode | 指标 | w5 | d065 | 差值 |
|-------|------|------|----|------|------|
| Llama | unc | E-F1 | 83.93 | 84.77 | **+0.84** |
| Llama | unc | R-F1 | 43.72 | 44.55 | **+0.83** |
| Llama | con | E-F1 | 83.94 | 84.71 | **+0.77** |
| Llama | con | R-F1 | 43.78 | 44.70 | **+0.92** |
| Qwen | unc | E-F1 | 82.15 | 82.35 | +0.20 |
| Qwen | unc | R-F1 | 40.86 | 40.89 | +0.03 |

Llama d065 比 w5 高约 0.8-0.9 个点（E-F1 和 R-F1 均是），Qwen unc 差异很小。差异来源可能是：
1. d065 新代码（May 18 grammar fix）改善了输出解析
2. eval_d064.py 与 w5 时期用的 eval 脚本不同（entity type alias 归一化等）

w5 原始输出文件在两台服务器上未找到明确标记的 w5 文件（没有 `w5_` 前缀的 DocRED greedy jsonl），无法用 eval_d064.py 重评 w5 数据来确认差异来源。

---

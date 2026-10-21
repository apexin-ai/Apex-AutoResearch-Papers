# analysis token length check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_token-length-check_20260512T102743_result.json`
- **Structured JSON:** [`40934b8ab27db11dc652.json`](../../sessions/40/40934b8ab27db11dc652.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

### 数据字段
`code`(git diff), `test`(测试名), `label`(0/1), `source`, `problem_id`, `mutation_type`, `error_message`, `execution_output`, `metadata`

### Token 长度分布 (n=89,867)

| 指标 | 值 |
|------|-----|
| Min | 176 |
| Max | 16,450 |
| Mean | 887 |
| Std | 1,737 |
| p50 | 415 |
| p90 | 1,275 |
| p95 | 2,222 |
| p99 | 6,656 |

### 截断率

| 阈值 | 截断率 | 样本数 |
|------|--------|--------|
| >512 | 38.0% | 34,138 |
| >1024 | 26.0% | 23,341 |
| >2048 | **5.9%** | 5,340 |
| >4096 | 3.4% | 3,039 |
| >8192 | 0.9% | 849 |
| >16384 | 0.2% | 144 |

### 推荐

**max_seq_length=4096**。2048 截断率 5.9% 超过 5% 阈值，4096 截断率降至 3.4%（可接受）。8192 只额外挽回 2.5% 的样本但显存开销翻倍，性价比不高。

---

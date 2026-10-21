# ops d158 1 7b generate check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d158_1_7b_generate_check_20260524T180321_result.json`
- **Structured JSON:** [`5a4718859e636dd76634.json`](../../sessions/5a/5a4718859e636dd76634.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被清理），无影响。

**实验 d158_1_7b_rsft_s44_generate — 成功完成**

| 指标 | 值 |
|------|-----|
| 状态 | ANALYZING |
| 文档数 | 3,027 |
| 总输出数 | 24,216 (8/doc) |
| 运行时间 | ~9h |
| Format compliance | 24,214/24,216 (100.0%) |
| Diversity | mean=7.52/8, median=8.0/8 |
| Truncation rate | 15.5%–27.4%（各 batch），整体偏高 |
| 输出文件 | `/root/autodl-tmp/rsft_generations_1_7b_s44/generations.jsonl` (244MB) |

Truncation rate 全程 >10%，与之前 seed 的表现一致（max_new_tokens=1024 对部分长文档不够）。格式合规率和多样性均正常。

---

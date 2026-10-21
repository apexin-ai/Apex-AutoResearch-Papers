# code fix chat template overhead v5

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-chat-template-overhead-v5_20260515T013628_result.json`
- **Structured JSON:** [`ec5c4ebecb3410c8bd3c.json`](../../sessions/ec/ec5c4ebecb3410c8bd3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 代码修改
- 文件: `/root/trace-verdict-study/data/format_training_data.py`
- 改动 (4 处):
  1. L14: 新增 `CHAT_TEMPLATE_OVERHEAD = 32`
  2. L96: `if len(full_tokens) <= max_seq_length` → `<= max_seq_length - CHAT_TEMPLATE_OVERHEAD`
  3. L105: `trace_budget = max_seq_length - no_trace_tokens - marker_token_count` → `max_seq_length - CHAT_TEMPLATE_OVERHEAD - no_trace_tokens - marker_token_count`
  4. L121: `truncated = len(full_tokens) > max_seq_length` → `> max_seq_length - CHAT_TEMPLATE_OVERHEAD`

## 数据重新生成
6 个文件全部于 2026-05-15 09:40~09:43 重新生成 ✓

## End-to-end 验证结果（chat template 包装后）

| 条件/split | n | min_tokens | max_tokens | avg_tokens | over_2048 | label_truncated |
|---|---|---|---|---|---|---|
| no_trace/train | 4720 | 87 | 1292 | 217 | 0 | 0 |
| no_trace/test | 1190 | 90 | 928 | 185 | 0 | 0 |
| vota/train | 4720 | 159 | 2048 | 1929 | 0 | 0 |
| vota/test | 1190 | 143 | 2048 | 1911 | 0 | 0 |
| full_trace/train | 4720 | 159 | 2048 | 1963 | 0 | 0 |
| full_trace/test | 1190 | 143 | 2048 | 1944 | 0 | 0 |

## 修复前后对比

| 条件 | 修复前 over_2048 | 修复后 over_2048 |
|---|---|---|
| no_trace | 0% | 0% |
| vota | 88.7% | **0%** |
| full_trace | 94.9% | **0%** |

## 验证判定
- 0 样本超过 2048: **PASS**
- 0 label 被截断: **PASS**
- 样本数一致 (4720/1190): **PASS**
- **总判定: ALL PASS → 可以训练**

---

# data preprocess training

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_preprocess-training_20260518T061732_result.json`
- **Structured JSON:** [`54a65cfb4c1d35959f7d.json`](../../sessions/54/54a65cfb4c1d35959f7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练数据预处理完成。

**产出文件**（westd-29046 上）：
- `/root/tbab_multi_turn/data/training_data.json` — 22MB, 2500 条
- `/root/tbab_multi_turn/data/data_stats.txt` — 统计报告

**数据统计**：

| 指标 | min | P25 | P50 | P75 | max | mean |
|------|-----|-----|-----|-----|-----|------|
| User turns | 5 | 5 | 6 | 7 | 41 | 6.5 |
| 总消息数 | 10 | 10 | 12 | 14 | 82 | 13.0 |
| Token 长度 | 120 | 1574 | 2104 | 2378 | 3488 | 1968.2 |

**过滤管线**：
- ShareGPT: 94,145 → 16,014 (>=5 turns) → 16,010 (<=3500 tokens) → 1,500 (sampled)
- UltraChat: 207,865 → 17,301 (>=5 turns) → 17,140 (<=3500 tokens) → 1,000 (sampled)

**隔离检查通过**：1 条 keyword 匹配是一条普通 ShareGPT SQL 问答对话，不是 lost_in_conversation 的 sharded instruction 格式。

---

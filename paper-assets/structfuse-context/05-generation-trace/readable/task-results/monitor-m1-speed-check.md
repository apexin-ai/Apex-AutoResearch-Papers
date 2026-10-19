# monitor m1 speed check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_m1_speed_check_20260512T210132_result.json`
- **Structured JSON:** [`27023268bf4975d3a481.json`](../../sessions/27/27023268bf4975d3a481.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M1 全量提取进度报告

| 指标 | 状态 |
|------|------|
| **进程** | PID 577864 存活，运行 13m42s |
| **已完成 instances** | **359 / 50,869 (0.71%)** |
| **已处理 repos** | 9 / 131 (正在处理中，均未完成) |
| **当前速度** | ~1,572 instances/hour |
| **预估剩余** | ~32h（乐观，见下方说明） |
| **磁盘** | 82GB 可用 / 169GB (52%)，充裕 |

### 当前正在并行处理的 repos（8 workers）

从日志头部可见首批加载：
- pytest-dev/iniconfig (63), jd/tenacity (152), agronholm/typeguard (333, 已处理 50), pudo/dataset (107), cknd/stackprinter (137), Cog-Creators/Red-DiscordBot (460), oauthlib/oauthlib (940), seatgeek/thefuzz (32), madzak/python-json-logger (?)

### 异常

1. **pdfminer/pdfminer clone 失败**（git exit code 128）— 该 repo 有 660 个 instances，会被跳过。需要排查原因（可能 repo 已更名/删除/网络问题）。

### 速度评估

脚本自估 ~54h（8 workers）。当前观测 ~32h 偏快，原因是首批都是小型 repo（iniconfig 63、thefuzz 32）。**随着 oauthlib (940)、Red-DiscordBot (460) 等大 repo 进入以及后续 131 个 repo 中有更大的项目，速度大概率会下降。** 保守估计 40-60h 比较合理。

---

# check exp 058 ve ratio key

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_058_ve_ratio_key_20260524T002521_result.json`
- **Structured JSON:** [`839a49c0f329a4d5c95e.json`](../../sessions/83/839a49c0f329a4d5c95e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据确认。`civo/ve_ratio` 完整轨迹（21 个点，每 10K 步从 15K 开始）：

| Step | ve_ratio |
|------|----------|
| 15K | 0.0111 |
| 25K | 0.0303 |
| 35K | 0.0542 |
| **45K** | **0.2314** |
| 55K | 0.0813 |
| 65K | 0.1265 |
| 75K | 0.1391 |
| 85K | 0.1877 |
| 95K | 0.2225 |
| 105K | 0.1656 |
| 115K | 0.1375 |
| 125K | 0.1021 |
| 135K | 0.1286 |
| 145K | 0.1034 |
| 155K | 0.1031 |
| 165K | 0.1268 |
| 175K | 0.1128 |
| 185K | 0.1425 |
| 195K | 0.1112 |
| 205K | 0.1119 |
| 215K | 0.1068 |

**结论：**
- Key 名：`civo/ve_ratio`（之前 Worker 搜 `ve_ratio` 不含前缀 `civo/` 所以没找到）
- **PEAK：0.2314 @ 45K** — 与之前报告的 0.231@45K 一致
- **FINAL：0.1068 @ 215K**
- 轨迹特征：45K 处 spike 到 0.23，55K 骤降到 0.08，之后在 0.10–0.22 区间波动，95K 有第二高峰 0.22，125K 后稳定在 0.10–0.14 区间

---

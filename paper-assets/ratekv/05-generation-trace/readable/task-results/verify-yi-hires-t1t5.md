# verify yi hires t1t5

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_yi_hires_t1t5_20260515T131537_result.json`
- **Structured JSON:** [`8d354f4f2a850aa521b8.json`](../../sessions/8d/8d354f4f2a850aa521b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完毕，**hires profiling 数据与 shape_metrics.json 完全一致**。

## Yi-1.5-9B hires bf16 验证结果

| 指标 | 独立计算值 | shape_metrics.json | 匹配 |
|------|-----------|-------------------|------|
| n_heads | 192 | 192 | ✓ |
| n_top5 | 9 | 9 | ✓ |
| top5_concentration | 0.7139 | 0.7139 | ✓ |
| top1_share | 0.6434 | 0.6434 | ✓ |
| t1/t5 | 0.9012 | 0.9012 | ✓ |
| t1/t2 | 23.7210 | 23.7210 | ✓ |
| top1_delta | 13.1236 | 13.123636 | ✓ |

**Top-9 deltas（即 top5% heads）**：
`[13.1236, 0.5533, 0.2293, 0.1308, 0.1159, 0.1097, 0.1063, 0.0982, 0.0948]`

**Shape 分类：Spike**。t1/t5 = 0.9012 表明 top1 head（layer 4 head 3，delta=13.12）独占 top5 sum 的 90%，concentration = 0.7139 表明 top5% heads 贡献了全部 distortion 的 71%。这是极端的 single-head spike 模式。

`compute_shape_metrics.py` 第7行确认 Yi-1.5-9B 使用的是 `yi15_hires_bf16_2bitonly_profiles.json`（hires 数据），不是之前验证脚本误用的 lowres 文件。

---

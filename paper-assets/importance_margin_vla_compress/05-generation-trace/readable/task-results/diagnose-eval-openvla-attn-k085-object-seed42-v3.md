# diagnose eval openvla attn k085 object seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_attn_k085_object_seed42_v3_20260524T224947_result.json`
- **Structured JSON:** [`5a9f749203590fd77ef6.json`](../../sessions/5a/5a9f749203590fd77ef6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**eval_openvla_attn_k085_object_seed42** — ✅ 成功

| 指标 | 值 |
|------|-----|
| Overall SR | **55.0%** (275/500) |
| 耗时 | 259 min |
| 最高 task | chocolate_pudding 88%, ketchup/orange_juice 74% |
| 最低 task | cream_cheese/bbq_sauce/tomato_sauce/butter 36% |

Registry 已更新为 DONE/success，cron 已清除。

注：JSON 中 `k_ratio` 字段为 null（代码输出 bug），但实际运行命令确认使用了 `--k_ratio 0.85`。

---

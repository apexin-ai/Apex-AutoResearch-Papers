# ops cleanup exp 012 checkpoints

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_exp_012_checkpoints_20260520T222640_result.json`
- **Structured JSON:** [`9741265a58db91a63795.json`](../../sessions/97/9741265a58db91a63795.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| 指标 | 删除前 | 删除后 |
|------|--------|--------|
| checkpoint 目录数 | 11 (gen_0~gen_10) | 2 (gen_0, gen_10) |
| 磁盘已用 | 244GB (98%) | 230GB (92%) |
| 可用空间 | 6.7GB | **21GB** |
| 释放空间 | — | ~14.4GB |

保留：`gen_0`、`gen_10`。已删除：`gen_1`~`gen_9`（9 个目录）。可用空间 21GB，满足 exp_014 的 >20GB 要求。

---

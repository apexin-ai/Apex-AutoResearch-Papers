# ops precompute check merge train

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_precompute-check-merge-train_20260521T163316_result.json`
- **Structured JSON:** [`f1589a19038f6a046e57.json`](../../sessions/f1/f1589a19038f6a046e57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Precompute 状态汇报

**全部 precompute 仍在运行，无一完成。** 以下是各服务器详情：

### bjb2-40593 — Object shard 0
| Shard | 进度 | 剩余时间 | 速率 |
|-------|------|---------|------|
| 0 | 4500/7251 (62%) | ~2.6h | 3.35s/sample |

### bjb1-32546 — Object shards 1-9（全部 9 个在跑）
| Shard | 进度 | 剩余时间 | 速率 |
|-------|------|---------|------|
| 1 | 3700/7251 (51%) | ~2.1h | 2.15s/sample |
| 2 | 4200/7251 (58%) | ~1.6h | 1.90s/sample |
| 3 | 4100/7251 (57%) | ~1.7h | 1.94s/sample |
| 4 | 3800/7251 (52%) | ~2.0h | 2.05s/sample |
| 5 | 4500/7251 (62%) | ~1.5h | 1.94s/sample |
| 6 | 4400/7251 (61%) | ~1.5h | 1.89s/sample |
| 7 | 4500/7250 (62%) | ~1.5h | 1.94s/sample |
| 8 | 4600/7250 (63%) | ~1.4h | 1.89s/sample |
| 9 | 4500/7250 (62%) | ~1.5h | 1.96s/sample |

### bjb2-28827 — Spatial shards 0-5（全部 6 个在跑）
| Shard | 进度 | 剩余时间 | 速率 |
|-------|------|---------|------|
| 0 | 4400/8608 (51%) | ~2.7h | 2.27s/sample |
| 1-3 | ~4100-4300/8607 (48-50%) | ~2.7h | 2.27-2.28s/sample |
| 4 | 4500/8607 (52%) | ~2.5h | 2.21s/sample |
| 5 | ~4000/8608 (~46%) | ~2.7h | 2.27s/sample |

### bjb1-18228 — Spatial shard 6
| Shard | 进度 | 剩余时间 | 速率 |
|-------|------|---------|------|
| 6 | 5300/8607 (62%) | ~1.7h | 1.88s/sample |

### 关键结论

- **瓶颈**：bjb2-28827 的 spatial shards 0-5 最慢，预计 **~2.7 小时后完成**（约 UTC 03:10 / 北京时间 11:10）
- 所有进程运行正常，无崩溃、无 OOM
- bjb2-40593 的 shard 0 速率偏慢（3.35s vs 其他 ~1.9s），因为只用了单 GPU 且 save_every=100
- 无法现在执行 merge + CRM training，需等所有 precompute 完成

**建议**：约 2.5-3 小时后再次检查状态。全部完成后立即执行 merge → CRM training。

---

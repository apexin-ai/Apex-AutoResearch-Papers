# diagnose k0925 seed42 completion

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_k0925-seed42-completion_20260521T235144_result.json`
- **Structured JSON:** [`84da3c1ffb3e90870df5.json`](../../sessions/84/84da3c1ffb3e90870df5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，cron 已删除。

## 结果

**Random k=0.925 Object seed42: SR = 27.6%** (138/500)

### Cliff 定位

| k | SR | 丢弃比例 |
|---|---|----|
| 0.95 | 69.4% | 5% tokens |
| **0.925** | **27.6%** | 7.5% tokens |
| 0.90 | 10.8% | 10% tokens |

**Cliff 在 [0.925, 0.95] 区间**，仅多丢 2.5% tokens (从 5% → 7.5%) 就导致 SR 暴跌 41.8pp (69.4% → 27.6%)。这不是渐进退化，而是断崖式崩溃。

Registry impact analysis 还指出 D151：L2norm k=0.925 = 98.9% vs Random k=0.925 = 27.6%，cliff 是 random-specific 的，L2norm 在同一 keep ratio 完全不受影响。

---

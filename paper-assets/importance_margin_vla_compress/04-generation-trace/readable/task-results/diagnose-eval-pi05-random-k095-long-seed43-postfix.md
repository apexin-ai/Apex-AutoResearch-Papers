# diagnose eval pi05 random k095 long seed43 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k095_long_seed43_postfix_20260524T224419_result.json`
- **Structured JSON:** [`d803918192f88e652622.json`](../../sessions/d8/d803918192f88e652622.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验完成：SUCCESS**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **58.4%** (292/500) |
| 耗时 | 236.8 min |

**Per-task SR:**

| Task | SR |
|------|-----|
| T0 alphabet soup + tomato → basket | 50% |
| T1 cream cheese + butter → basket | 88% |
| T2 stove + moka pot | 62% |
| T3 black bowl → drawer | 80% |
| T4 white mug → plates | 42% |
| T5 book → caddy | 90% |
| T6 mug on plate + pudding | 6% |
| T7 alphabet soup + cream cheese → basket | 58% |
| T8 moka pots → stove | 18% |
| T9 mug → microwave | 90% |

**对比 seed42 k=0.95 Random = 63.2%**：seed43 为 58.4%，低了 4.8pp。两 seed 均值 = 60.8%。

Registry 已更新为 DONE/success，cron 已清除。

---

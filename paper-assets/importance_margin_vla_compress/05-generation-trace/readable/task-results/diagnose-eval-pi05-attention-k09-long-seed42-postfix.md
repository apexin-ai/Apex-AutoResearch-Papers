# diagnose eval pi05 attention k09 long seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_attention_k09_long_seed42_postfix_20260525T165525_result.json`
- **Structured JSON:** [`688266611b0e73e8630c.json`](../../sessions/68/688266611b0e73e8630c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**状态: FAILED** — 进程在 T9 ep=10/50 处异常退出，未生成结果 JSON。

### 部分结果 (9/10 tasks 完成, 460/500 episodes)

| Task | SR |
|------|-----|
| T0 (alphabet soup + tomato) | 40% |
| T1 (cream cheese + butter) | 90% |
| T2 (stove + moka pot) | 50% |
| T3 (bowl in drawer) | 90% |
| T4 (mug + plate) | 72% |
| T5 (book in shelf) | 88% |
| T6 (mug + plate variant) | 44% |
| T7 (alphabet soup + cream) | 54% |
| T8 (moka pots on stove) | 16% |
| T9 (mug in microwave) | 80% (仅10eps) |

**Partial overall SR: 60.4%** (272/450, T0-T8)

### Crossover 三向对比 (k=0.9, Long/libero_10)

| Method | SR |
|--------|-----|
| L2norm | 81% |
| **Attention** | **~60%** (partial) |
| Random | 32% |

Attention 在 Long 上显著弱于 L2norm (60% vs 81%)，但仍强于 Random。需要重跑补全 T9 数据确认最终 SR。

**已完成:** Registry 更新为 failed (含 partial metrics)，cron 已删除。

---

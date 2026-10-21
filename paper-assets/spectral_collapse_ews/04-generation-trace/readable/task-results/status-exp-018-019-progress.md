# status exp 018 019 progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_exp_018_019_progress_20260523T053417_result.json`
- **Structured JSON:** [`98b16aca49bdbad5fbe0.json`](../../sessions/98/98b16aca49bdbad5fbe0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_018: Gen 8/10 (正在生成合成数据 11840/25000=47%)，预计 2026-05-23 ~09:30 UTC 完成
  已完成 gen_0–gen_7 | 每 gen ≈89 min | 剩余 ≈3h50m

exp_019: Gen 1/10 (正在生成合成数据 31360/40000=78%)，预计 2026-05-24 ~02:00–04:00 UTC 完成
  已完成 gen_0 | 每 gen 生成量 40k(比 exp_018 的 25k 多 1.6x) | 剩余 ≈20–22h

GPU 状态:
  GPU 0: 92% util, 25017/97887 MiB (exp_018)
  GPU 1: 66% util, 19045/97887 MiB (exp_019)
```

注意：exp_019 只完成了 1 个 gen，每 gen 耗时缺乏足够数据点，完成时间估算误差较大。exp_018 基于 gen_1→gen_7 的 6 个周期（平均 89 min/gen），估算可靠。

---

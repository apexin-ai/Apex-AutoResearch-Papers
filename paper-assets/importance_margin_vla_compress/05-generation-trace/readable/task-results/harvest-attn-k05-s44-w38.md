# harvest attn k05 s44 w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_attn_k05_s44_w38_20260528T021507_result.json`
- **Structured JSON:** [`59feec03fba23c9472a5.json`](../../sessions/59/59feec03fba23c9472a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结果汇总

**Attn k=0.5 seed44: SR = 48.8% (244/500)**

Per-task 明细：

| Task | SR |
|------|-----|
| T0 alphabet soup & tomato | 78% |
| T1 cream cheese & butter | 42% |
| T2 stove & moka pot | 68% |
| T3 black bowl drawer | 64% |
| T4 white mug left plate | 52% |
| T5 book back shelf | 48% |
| T6 white mug plate | 20% |
| T7 alphabet soup & cream | 50% |
| T8 moka pots stove | 10% |
| T9 yellow mug microwave | 56% |

**3-seed 汇总 (Attn k=0.5)：**

| Seed | SR |
|------|-----|
| s42 | 52.0% |
| s43 | 48.8% |
| s44 | 48.8% |
| **Mean** | **49.9%** |
| Std | ±1.5pp |

s44 与 s43 完全一致 (48.8%)，error bar 从 ±1.6pp 收窄至 ±1.5pp。Attn k=0.5 稳定在 ~50% 平台，确认 50% token 剪枝后性能保持良好。

---

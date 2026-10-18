# analyze eval pi05 attention k07 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_attention_k07_long_seed42_v2_20260526T231330_result.json`
- **Structured JSON:** [`b76f581c6e8892175738.json`](../../sessions/b7/b76f581c6e8892175738.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**π0.5 Attention k=0.7 Long (libero_10) seed42: Overall SR = 50.8%**

Per-task breakdown:

| Task | SR |
|------|-----|
| T0 alphabet soup & tomato | 72% |
| T1 cream cheese & butter | 70% |
| T2 stove & moka pot | 58% |
| T3 black bowl drawer | 46% |
| T4 white mug & plate | 36% |
| T5 book placement | 32% |
| T6 mug & plate & yellow | 58% |
| T7 alphabet soup & cream | 48% |
| T8 moka pots stove | 6% |
| T9 yellow mug microwave | 82% |

### 更新后的 Attn Long cliff curve

| k | SR | Δ vs Full |
|---|-----|-----------|
| 0.95 | 77.0% | - |
| 0.90 | 63.8% | -13.2pp |
| 0.85 | 51.6% | -12.2pp |
| **0.75** | **51.8%** | +0.2pp |
| **0.70** | **50.8%** | -1.0pp |
| 0.50 | 49.4% | -1.4pp |

**关键发现**: k=0.7 (50.8%) 完美符合预期，确认 Attention pruning 在 k=0.85 以下进入平台期。从 k=0.85 到 k=0.5，SR 仅从 51.6% 缓降至 49.4%（仅 -2.2pp），cliff 明确在 k=0.9→0.85 区间（-12.2pp）。k=0.7 补全了曲线中间点，plateau 趋势清晰。

Registry 已更新为 DONE/success。

---

# analyze eval openvla attn k095 long seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_attn_k095_long_seed42_20260527T113653_result.json`
- **Structured JSON:** [`5a44cf4452530ef67ad6.json`](../../sessions/5a/5a44cf4452530ef67ad6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 指标 | 值 |
|------|-----|
| **Overall SR** | **49.8%** (249/500) |
| EXIT_CODE | 0 (正常完成) |
| 耗时 | 620.7 min (~10.3h) |

### Per-task SR

| Task | SR |
|------|-----|
| T1 alphabet soup + tomato sauce → basket | 56% |
| T2 cream cheese + butter → basket | 74% |
| T3 stove + moka pot | 52% |
| T4 black bowl → drawer | 34% |
| T5 white mug + yellow mug → plates | 46% |
| T6 book → caddy | 68% |
| T7 white mug + chocolate pudding | 42% |
| T8 alphabet soup + cream cheese → basket | 56% |
| T9 moka pots → stove | 30% |
| T10 yellow white mug → microwave | 40% |

### Long Attn Cliff Curve

| k | SR | Δ vs baseline |
|---|-----|---------------|
| 1.0 (baseline) | 52.8% | — |
| **0.95** | **49.8%** | **-3.0pp** |
| 0.9 | 44.0% | -8.8pp |
| 0.85 | 45.8% | -7.0pp |

### Conclusion: **success**

k=0.95 补全了曲线起始段。仅 pruning 5% vision tokens (256→243) 即产生 3.0pp 下降，说明 Long suite 对 attention pruning 比较敏感。曲线整体呈下降趋势（k=0.9 的 44.0% 和 k=0.85 的 45.8% 在噪声范围内接近）。Registry 已更新为 DONE/success。

---

# analysis alpha sweep a050 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a050_s43_20260515T220115_result.json`
- **Structured JSON:** [`78343e5a5de11e41a6d4.json`](../../sessions/78/78343e5a5de11e41a6d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析摘要

### α=0.50 s43 vs s42 跨 seed 对比

| 指标 | s43 drift | s42 drift | gen10 偏差 |
|------|-----------|-----------|-----------|
| entropy | -17.4% | -18.6% | +1.5% |
| ECE | +799% | +843% | -4.8% |
| ppl | +21.1% | +21.1% | -0.02% |
| d1 | -36.5% | -37.3% | +0.7% |
| d2 | -49.0% | -51.5% | +4.3% |
| d3 | -48.8% | -52.4% | +6.5% |

**跨 seed 一致性极好。** gen10 绝对值偏差 <7%，drift 方向完全一致，幅度紧密对齐。Perplexity 几乎完全相同（32.633 vs 32.64）。

### α=0.50 vs α=0.25（同 seed=43）

关键发现：**perplexity drift 方向翻转**——α=0.25 下 ppl 下降 18.7%（模型变好），α=0.50 下 ppl 上升 21.1%（模型退化）。ECE collapse 在 α=0.50 下是 α=0.25 的 8 倍（+799% vs +99%）。这在两个 seed 上都一致复现，强力支撑 **Claim 2（regime-dependent validity）**。

### D026 影响

α=0.50 两个 seed 已完成且高度一致，该 α 值的 error bar 可以直接用于论文。下一步：cuda:1 可提交 a025_s44。

---

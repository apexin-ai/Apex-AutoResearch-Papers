# fetch gold consensus results

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fetch_gold-consensus-results_20260515T115342_result.json`
- **Structured JSON:** [`800482df7b1455fbb62b.json`](../../sessions/80/800482df7b1455fbb62b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件已写入本地。

**GB macro-F1 一致性检查：**

| 来源 | GB macro-F1 | RF macro-F1 |
|------|------------|------------|
| eval results.json | **0.72366** (N=584) | **0.697289** (N=584) |
| bootstrap_ci (gb_vs_mv) | **0.72366** | — |
| bootstrap_ci (rf_vs_gb) | — / **0.72366** | **0.697289** |

两个 JSON 中 GB macro-F1 = 0.72366、RF macro-F1 = 0.697289，完全一致。

注意 bootstrap 中 `gb_vs_gru_probe` 的 GB F1 是 **0.75282**（在 386 个共享样本上），高于全量 584 样本的 0.72366——这是因为该对比限制在 GRU Probe 有预测的 386 个样本子集上，不是不一致。

---

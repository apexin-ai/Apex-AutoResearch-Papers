# experiment dir i hge pilot

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-i-hge-pilot_20260520T171206_result.json`
- **Structured JSON:** [`bf3da4520a706a1ba8cb.json`](../../sessions/bf/bf3da4520a706a1ba8cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

| Condition | Acc (%) | Δ vs Baseline (pp) | McNemar p |
|---|---|---|---|
| Mistral SC@12 (baseline) | 54.41 | — | — |
| Mistral SC@5 | 55.29±1.37 | +0.88 | 0.629 |
| Mistral SC@10 | 54.71±0.80 | +0.29 | 1.000 |
| Mistral SC@15 | 56.47±1.26 | +2.06 | 0.039* |
| **HGE-(a) cross-family** | **72.16±2.24** | **+17.75** | **<0.0001*** |
| **HGE-(b) within-family** | **82.01±0.73** | **+27.60** | **<0.0001*** |
| **HGE-all** | **82.35±1.28** | **+27.94** | **<0.0001*** |

**关键对比 — HGE-(a) vs Mistral-SC@10（同为 10 traces）：**
- Cross-model gain Δ = **+17.45 pp**（72.16% vs 54.71%）
- Flip 分析：50 题翻转，其中 44 题翻转为正确，6 题翻转为错误

信号极强。同模型增加 traces（SC@15 vs SC@12）仅带来 +2.06 pp，而跨模型 ensemble 即使只用一半 traces 也能带来 +17.75 pp。HGE-(b) within-family（纯 Qwen 家族 3 模型）更高达 82%，说明即使同家族的不同规模模型也能提供足够多样性。

注意 Mistral 的 valid traces 偏低（mean=10.0 vs 其他模型 12.0），说明它有更多 parsing failure。这不影响结论——如果 Mistral traces 质量更差，跨模型 gain 的归因更清晰（不是 Mistral 占多数票的效果，而是其他模型纠错）。

---

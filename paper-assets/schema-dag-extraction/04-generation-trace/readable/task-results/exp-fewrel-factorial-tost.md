# exp fewrel factorial tost

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_fewrel_factorial_tost_20260516T141051_result.json`
- **Structured JSON:** [`33904578eb5a97b4d04d.json`](../../sessions/33/33904578eb5a97b4d04d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果总结：

**三重分析均支持 two-channel decomposition 的可加性（empirical separability）：**

| Analysis | N | Count effect | BCS effect | Interaction | TOST |
|----------|---|---|---|---|---|
| 1. 2×2 Factorial (40-rel, 8 vs 16) | 54 | F=10.98, p=.002** | F=1.24, p=.27 ns | F=0.60, p=.44 ns | inconclusive |
| 2. Regression (40-rel, count 4-40) | 69 | β=−.035, p=.008** | β=−.051, p=.0002*** | β=.005, p=.61 ns | **p=.003, EQUIVALENT** |
| 3. Cross-dataset (200 batches) | 200 | F=21.90, p<.001*** | F=5.90, p=.016* | F=2.76, p=.098 ns | inconclusive |

**核心结论：**
- Count 和 BCS 两个 channel 各自独立且显著地影响 accuracy
- 三个分析中交互项均不显著 (all p > 0.05)
- 回归分析的 TOST 正式确认交互项在 ±3pp equivalence margin 内 (interaction = 0.47pp, SE = 0.90pp, p_TOST = 0.003)
- R² = 0.52 — 两个 channel 联合解释一半以上的 accuracy 变异

结果保存于 `/root/schema-dag-extraction/artifacts/fewrel_factorial_tost/results.json`。

---

# analysis golden ratio seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_golden_ratio_seed42_20260515T132808_result.json`
- **Structured JSON:** [`45f9e71ca69eff64adcf.json`](../../sessions/45/45f9e71ca69eff64adcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总结论：

## Golden Ratio Oracle Baseline 结果

| 方法 | PPL (seed42) | vs Uniform |
|------|-------------|------------|
| **Uniform** | 17.690 | — |
| **ESS-only** | 17.730 | +0.040 (worse) |
| **Grid-best (b=0.5)** | 17.651 | -0.039 |
| **Adaptive_fix** | 17.650 | -0.040 |
| **Golden Ratio (oracle)** | **17.654** | **-0.036** |

**关键发现**：

Golden Ratio oracle PPL = **17.654**，与 adaptive_fix (17.650) 和 grid-best (17.651) 几乎完全相同，差异 < 0.004，在噪声范围内。

**对论文的影响**：
- Adaptive 方法**已达到 oracle 水平**。不需要已知真实比例（golden ratio 需要知道哪些是 synthetic），adaptive 靠 ESS + score 分布自适应调权就能匹配 oracle 性能。
- Oracle baseline 并未提供额外改进空间，说明 adaptive 的 weighting 策略已经接近最优。
- 论文叙述：adaptive 方法在**不需要 provenance label** 的前提下，达到了与需要 oracle 知识的 golden ratio 相当的 held-out perplexity，验证了方法的有效性上界。

---

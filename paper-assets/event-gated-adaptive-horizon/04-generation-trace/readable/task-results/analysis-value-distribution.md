# analysis value distribution

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_value-distribution_20260524T160157_result.json`
- **Structured JSON:** [`ae8902121902d8d325ad.json`](../../sessions/ae/ae8902121902d8d325ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**核心发现**：

| 模型 | VE Ratio (final) | V(s) final | Eval final |
|---|---|---|---|
| Baseline | 0.709 | 665.86 | 938.86 |
| CIVO (008d) | **3.029** | 192.65 | 63.60 |
| No dt_emb (008f) | 0.380 | 116.45 | 306.54 |

**关键洞察**：CIVO 不是 critic 拟合误差（V(s) ≈ λ-return target 在所有模型中都成立），而是 **world model co-adaptation** —— dt_embedding 让 world model 在 imagination 中生成过度乐观的轨迹，critic 忠实学习了这些膨胀的 targets，导致 V(s) 远超真实 eval return（3.03x）。去掉 dt_embedding 后（008f），VE ratio 始终 < 0.4，验证了因果关系。

**产出**：
- 报告：`artifacts/value_distribution_analysis.md`
- 图表：`artifacts/figures/value_distribution_summary.png`、`ve_ratio_comparison.png`
- 服务器上还有额外图表（calibration scatter, overestimation gap 等）在 `/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/figures/`

---

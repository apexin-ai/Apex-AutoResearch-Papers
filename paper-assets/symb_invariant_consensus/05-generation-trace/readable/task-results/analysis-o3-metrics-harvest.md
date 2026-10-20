# analysis o3 metrics harvest

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_o3-metrics-harvest_20260521T190655_result.json`
- **Structured JSON:** [`a5055efca604d040e21e.json`](../../sessions/a5/a5055efca604d040e21e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

o3 完整指标已计算并保存到 `o3_full_metrics.json`。

### o3 完整指标（vs gpt-5.5 参考）

| Metric | o3 | gpt-5.5 |
|---|---|---|
| SC accuracy | **0.8265** (162/196) | 0.8431 |
| SICA accuracy | **0.8265** (162/196) | 0.8480 |
| Δ(SICA-SC) | **+0.00pp** | +0.49pp |
| Mean BR | **1.6565** | 3.4806 |
| Median BR | **1.2902** | 3.4935 |
| Weighted BR | **1.8120** | 3.5735 |
| n_br_finite | **6** | 4 |
| n_br_inf | **28** | 27 |
| Extraction rate | **1.0000** | 1.0000 |
| Process-κ | **0.5964** | 0.5625 |
| Answer Fleiss' κ | **0.9221** | 0.9581 |

关键发现：
- **SICA = SC，Δ=0**：SICA 对 o3 无增益，cross-model extraction 没有纠正任何 SC 错误
- **BR 远低于 gpt-5.5**（mean 1.66 vs 3.48）：o3 错的题上，SICA 给错误答案的权重相对较低——说明 o3 的错误模式更"确定"，constraint 提取无法翻盘
- **28/34 错题 BR=∞**：绝大多数错题中 gold answer 在 MaxSAT 中权重为 0，constraint 完全无法覆盖正确推理路径

---

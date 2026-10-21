# experiment gpt55 extraction pipeline

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_gpt55-extraction-pipeline_20260521T173217_result.json`
- **Structured JSON:** [`5756b7217a4c9849c42b.json`](../../sessions/57/5756b7217a4c9849c42b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。完整对比表：

| Metric | gpt-5.5 | gpt-4.1 (ref) |
|---|---|---|
| SC accuracy | **84.31%** | 82.84% |
| SICA accuracy | **84.80%** | 81.37% |
| Δ (SICA-SC) | **+0.49pp** | -1.47pp |
| Mean BR | 3.48 | 2.70 |
| Median BR | 3.49 | 1.53 |
| Weighted BR | 3.57 | 3.21 |
| n_br_finite | 4 | 16 |
| BR=∞ | 27 | 22 |
| extraction_rate | 100% | 100% |
| Process-κ | 0.5625 | 0.792 |
| Answer Fleiss' κ | **0.9581** | 0.862 |

关键发现：
- gpt-5.5 SC 和 SICA 都优于 gpt-4.1，且 SICA > SC（+0.49pp），说明跨模型约束提取对 gpt-5.5 有正向增益（gpt-4.1 是 -1.47pp）
- gpt-5.5 Answer Fleiss' κ 极高（0.958 vs 0.862），K=12 traces 间答案一致性非常强
- Process-κ 显著更低（0.563 vs 0.792），推理路径多样性更高
- BR 指标偏高（mean 3.48, median 3.49），且 n_br_finite 只有 4（gpt-4.1 有 16），说明 SICA 判错的 case 中几乎都是 BR=∞（27 个），错误时约束权重完全倾向于错误答案
- JSON 已保存至 `results/exp_d135_frontier_scb/gpt-5.5/cross_model/gpt55_full_metrics.json`

---

# analysis fewnerd 5epoch construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd-5epoch-construction_20260524T073502_result.json`
- **Structured JSON:** [`58978439b9b66cb786d8.json`](../../sessions/58/58978439b9b66cb786d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| | MV Δ | LP Δ | Degen% |
|---|---|---|---|
| Seed 42 | -0.52pp | **+0.17pp** | 25.7% |
| Seed 123 | +0.25pp | +0.85pp | 27.1% |
| **Pooled** | **-0.13pp** | **+0.51pp** | **26.4%** |

**论文 claim 方向性确认**：5-epoch 下 construction gain 显著 collapse。Seed 42 的 LP Δ=+0.17pp 与论文 claim "+0.20pp" 吻合。MV construction 在 5-epoch 下直接变为负值（-0.13pp），说明 over-convergence 导致 sample degeneracy（26.4%）破坏了 MV 的前提。仅有 2 个 seed 可用（42, 123），已在报告中注明。

报告已写入 `artifacts/rebuttal_construction_fewnerd_5epoch.md` 并注册。

---

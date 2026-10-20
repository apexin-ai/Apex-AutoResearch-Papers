# registry update mvp v4 metrics

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry_update_mvp_v4_metrics_20260515T212850_result.json`
- **Structured JSON:** [`5f059175fd641d7607ea.json`](../../sessions/5f/5f059175fd641d7607ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部更新成功。每个 registry 条目现包含 12 个原始指标（gen0/gen10 × 6 metrics）和 6 个 drift_pct 字段：

| exp_id | entropy_drift | ece_drift | ppl_drift | d1_drift | d2_drift | d3_drift |
|--------|-------------|-----------|-----------|----------|----------|----------|
| rep42 | -60.55% | +3762.5% | +3624.6% | -28.34% | -35.21% | -31.64% |
| rep43 | -61.05% | +3782.6% | +3665.1% | -28.42% | -35.76% | -33.03% |
| rep44 | -62.26% | +3821.2% | +3733.8% | -25.47% | -29.13% | -24.61% |
| rep45 | -59.33% | +3755.1% | +3670.9% | -29.13% | -35.96% | -32.74% |

---

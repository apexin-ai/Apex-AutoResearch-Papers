# analysis mvp v4 rep45

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_v4_rep45_20260514T175643_result.json`
- **Structured JSON:** [`f9d9c2ae6752c3db6342.json`](../../sessions/f9/f9d9c2ae6752c3db6342.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总如下：

## mvp_v4_rep45 结果

**状态**: 成功完成，10 代全部跑完 (EXIT_CODE=0)

**关键指标对比 (gen0 → gen10)**:

| 指标 | gen0 | gen10 | 变化 |
|------|------|-------|------|
| perplexity | 26.9 | 1016.2 | ×37.7 ↑ |
| token_entropy | 3.234 | 1.315 | -59% ↓ |
| ECE | 0.011 | 0.417 | ×38 ↑ |
| distinct-1 | 0.099 | 0.070 | -29% ↓ |
| distinct-2 | 0.515 | 0.330 | -36% ↓ |
| distinct-3 | 0.808 | 0.544 | -33% ↓ |
| MAUVE | 0.033 | 0.028 | -16% ↓ |

**与前两个 rep 一致性**:

| | rep42 | rep43 | rep45 |
|--|-------|-------|-------|
| gen10_ppl | 1003.7 | 1014.7 | 1016.2 |
| gen10_entropy | 1.276 | 1.26 | 1.315 |
| gen10_ece | 0.417 | 0.42 | 0.417 |

三个 rep 高度一致，均显示明确的 model collapse 趋势。

**Registry 已更新**: status=DONE, conclusion=success, checkpoint_path, metrics, metrics_summary, wall_clock_seconds=15212s, gpu_hours=4.23h。

---

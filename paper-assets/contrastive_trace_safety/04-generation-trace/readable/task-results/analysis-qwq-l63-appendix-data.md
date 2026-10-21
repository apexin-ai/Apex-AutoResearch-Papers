# analysis qwq l63 appendix data

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwq_l63_appendix_data_20260518T184808_result.json`
- **Structured JSON:** [`f7d60fd2225ce0800efb.json`](../../sessions/f7/f7d60fd2225ce0800efb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### QwQ-32B L63 Cosine Distance
| Metric | Value |
|--------|-------|
| Global (all traces) | 0.0089 |
| Per-trace mean ± std | 0.0839 ± 0.0560 |
| Within-class (safe-safe) | 0.2432 |
| Within-class (unsafe-unsafe) | 0.2630 |

### QwQ-32B L63 Control Task Selectivity (W=5, 60/20/20)
| Mode | Real BA | Random BA | Selectivity | >5pp |
|------|---------|-----------|-------------|------|
| Original | 0.7313 | 0.5707 ± 0.0166 | **0.1606** | Y |
| Residualized | 0.6188 | 0.5060 ± 0.0239 | **0.1127** | Y |

与 L60 对比：original selectivity 0.1606 vs 0.1627，residualized 0.1127 vs 0.1001，L63 表现一致。两项 selectivity 均通过 >5pp 阈值。

结果已写入远程 `artifacts/qwq_l63_appendix/results.json` 并注册。

---

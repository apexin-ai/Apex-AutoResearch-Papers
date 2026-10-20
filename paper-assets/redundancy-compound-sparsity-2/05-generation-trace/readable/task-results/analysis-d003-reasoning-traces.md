# analysis d003 reasoning traces

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d003_reasoning_traces_20260512T155427_result.json`
- **Structured JSON:** [`8582c129be6d47c3d6b2.json`](../../sessions/85/8582c129be6d47c3d6b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**d003_reasoning_traces: Sanity Check FAIL (negative)**

| Strategy | PPL | vs Full | vs Random |
|----------|-----|---------|-----------|
| full | 1.212 | — | — |
| recency | 1.217 | +0.41% | -0.82% |
| random | 1.2271 | +1.25% | — |
| ema_0.9 | 1.2522 | +3.32% | **+2.04%** |
| ema_0.7 | 1.2706 | +4.83% | +3.54% |
| ema_0.5 | 1.278 | +5.45% | +4.15% |

两个数据集结论一致：EMA attention score 不是有效的 eviction 信号，在 WikiText-2（-1.77%）和 reasoning traces（-2.04%）上均劣于 random baseline。Recency 是最强 eviction 策略（+0.41% vs full）。

已更新：
- Registry `d003_reasoning_traces`: status=DONE, conclusion=negative, 完整 metrics
- Artifact `analysis.md` 已注册

---

# eval loop only

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_loop_only_20260515T100533_result.json`
- **Structured JSON:** [`c5fd7159c5d7356bd4f1.json`](../../sessions/c5/c5fd7159c5d7356bd4f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。Registry 已更新为 DONE/success。

## 结果汇总

| 指标 | 值 |
|------|-----|
| **Accuracy** | **85.63%** (95% CI: [83.5%, 87.6%]) |
| Majority baseline | 71.5% |
| Lift | +14.1pp |

### Pairwise Bootstrap 对比（N=10000, 所有差异显著 p<0.05）

| 对比 | 差值 | 95% CI |
|------|------|--------|
| loop_only vs no_trace | **+10.5pp** | [+8.2, +12.9] |
| loop_only vs full_trace | **+3.9pp** | [+1.8, +6.0] |
| loop_only vs VOTA | **-13.8pp** | [-15.7, -11.8] |

### 消融分析定位

| Condition | Accuracy |
|-----------|----------|
| no_trace | 75.1% |
| full_trace | 81.8% |
| **loop_only** | **85.6%** |
| exception_only | 99.8% |
| VOTA (full) | 99.4% |

loop_only（仅循环行为摘要）单独贡献 85.6%，显著高于 full_trace（81.8%），说明循环压缩摘要本身是有效信号。但距 VOTA 99.4% 差距较大，exception 信息是更关键的组件。

---

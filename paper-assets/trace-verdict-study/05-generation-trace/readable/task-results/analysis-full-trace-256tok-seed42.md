# analysis full trace 256tok seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_full_trace_256tok_seed42_20260516T000218_result.json`
- **Structured JSON:** [`b2b77923c10334f9ba51.json`](../../sessions/b2/b2b77923c10334f9ba51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/negative，报告已注册。

**结果摘要**：

| Condition | Accuracy |
|-----------|----------|
| exception_only | 99.83% |
| VOTA | 99.41% |
| full_trace (无截断) | 81.8% |
| **full_trace_256tok** | **78.82%** |
| no_trace | 75.1% |

**NEGATIVE**：256 token 截断使 full_trace 从 81.8% 降至 78.82%（-3.0pp，CI 不重叠）。截断后 lift over no_trace 仅 3.7pp（无截断时 6.7pp），256 tokens 不足以保留有效信号。训练正常收敛（train_loss=0.109, 3 epochs, 0.85h）。

---

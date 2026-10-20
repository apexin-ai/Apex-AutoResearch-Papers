# analysis re selection bootstrap

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_re_selection_bootstrap_20260515T032546_result.json`
- **Structured JSON:** [`54674da0529119ef8b05.json`](../../sessions/54/54674da0529119ef8b05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `re_selection_bootstrap.json`。

所有 5 个信号在 RE subtask 上的 selection F1 均**低于** greedy F1，且多数差异显著：

| Signal | Sel F1 | Δ vs Greedy | p-value | Cohen's d | W/L/T |
|--------|--------|-------------|---------|-----------|-------|
| **logprob** | 0.3948 | -0.0094 | 0.796 | -0.041 | 36/59/302 |
| **sj** | 0.3855 | -0.0188 | 0.955 | -0.083 | 29/49/319 |
| **fk** | 0.3824 | -0.0218 | 0.965 | -0.088 | 54/69/274 |
| **em** | 0.3727 | -0.0316 | 0.996* | -0.130 | 27/62/308 |
| **voting_conf** | 0.3592 | -0.0451 | 1.000* | -0.185 | 38/66/293 |

Greedy=0.4042, Oracle=0.5850, n_valid=397。所有信号的 selection 均未能超越 greedy，EM 和 voting_conf 的负向差异 CI 不包含 0（显著劣于 greedy）。Logprob 损失最小但也非显著正向。

---

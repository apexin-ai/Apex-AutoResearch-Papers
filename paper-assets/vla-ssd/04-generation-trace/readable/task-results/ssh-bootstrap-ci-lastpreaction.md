# ssh bootstrap ci lastpreaction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_bootstrap-ci-lastpreaction_20260516T000846_result.json`
- **Structured JSON:** [`71d0e07bb81af0d020bc.json`](../../sessions/71/71d0e07bb81af0d020bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 值 |
|------|------|
| Trained L19 mean R² | 0.7309 |
| Untrained best (L32) mean R² | 0.6858 |
| Observed delta | **+0.0452** |
| 95% CI | **[0.0321, 0.0585]** |
| p-value (one-sided) | **< 0.0001** |
| CI excludes 0 | **Yes** |

所有 10 个 task 的 delta 均为正（range: +0.020 ~ +0.083），差异一致且显著。

**结论**：CI 完全排除 0，trained 显著优于 untrained best layer (p < 0.0001)。Redistribution is training-dependent，支持 Claim 2。

结果已保存到 `/root/autodl-tmp/vla-ssd/results/functional_validation/bootstrap_trained_vs_untrained_lastpreaction.json`。

---

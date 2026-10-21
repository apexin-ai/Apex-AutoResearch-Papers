# analysis ae only pairwise bootstrap

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ae_only_pairwise_bootstrap_20260515T123538_result.json`
- **Structured JSON:** [`03436b0f9ba194680ad0.json`](../../sessions/03/03436b0f9ba194680ad0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Results:

| 对比 | diff | 95% CI | p-value | 显著 |
|------|------|--------|---------|------|
| **ae_only vs no_trace** | +24.79pp | [+22.35, +27.31] | <0.0001 | YES |
| **ae_only vs exception_only** | +0.08pp | [-0.17, +0.34] | 0.80 | NO |
| **ae_only vs vota** | +0.50pp | [+0.17, +0.92] | 0.005 | YES |

- ae_only (99.92%) 大幅超越 no_trace baseline (75.13%)
- ae_only 与 exception_only (99.83%) 统计等价（CI 包含 0，p=0.80）
- ae_only 略优于完整 VOTA (99.41%)，差异显著（p=0.005）

输出保存至 `/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final/bootstrap_pairwise.json`，registry 已更新。

---

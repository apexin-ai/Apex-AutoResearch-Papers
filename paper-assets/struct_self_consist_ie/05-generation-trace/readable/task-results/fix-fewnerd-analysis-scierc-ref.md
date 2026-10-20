# fix fewnerd analysis scierc ref

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fewnerd_analysis_scierc_ref_20260516T173513_result.json`
- **Structured JSON:** [`a7599e44111f5003cfaf.json`](../../sessions/a7/a7599e44111f5003cfaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成，脚本运行正常。

**修改摘要：**

| 字段 | 旧值 (N=32) | 新值 (N=8) |
|------|-------------|------------|
| oracle | 0.806 | 0.752 |
| headroom | 19.2 | 13.8 |
| lp_rho | 0.440 | 0.205 |
| lp_delta | 0.91 | 0.42 |
| lp_auroc | 0.72 | 0.72（保持） |
| bootstrap | LP/SJ/FK only | 全部 5 个信号 |

**关于 lp_auroc=0.72**：未能找到精确来源。`scierc_results.json` (N=8) 的 LP AUROC 是 0.578，但那是 instance-level AUROC（信号预测 greedy F1>0），而此脚本用的是 sample-level AUROC（信号预测哪个 sample 是 oracle）。两种方法不同，0.72 可能来自之前的 ad-hoc 分析。如需精确值，需在 SciERC N=8 数据上跑同样的 sample-level AUROC 计算。

**QE aggregation**：脚本中 rho 用 `max(signal_per_sample)`，AUROC 用逐 sample 原始值。这与 SciERC 分析一致。

---

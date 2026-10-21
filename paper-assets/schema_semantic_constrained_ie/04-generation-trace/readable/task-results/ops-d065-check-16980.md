# ops d065 check 16980

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d065-check-16980_20260520T081810_result.json`
- **Structured JSON:** [`49ebe6f87c14c7b72b35.json`](../../sessions/49/49ebe6f87c14c7b72b35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 d065 Llama greedy 4096 均已完成。汇总：

| 指标 | **unc** (unconstrained) | **con** (constrained) | 差异 |
|------|------------------------|----------------------|------|
| 状态 | 完成 (998/998) | 完成 (998/998) | — |
| Parse Fail | 2.3% (23) | 2.6% (26) | +0.3% |
| **E-F1** | **84.77** | **84.71** | -0.06 |
| **R-F1** | **44.55** | **44.70** | **+0.15** |
| ET% | 0.00 | 0.00 | — |
| RV% | 0.15 | **0.00** | -0.15 ✓ |
| **DR%** | 0.49 | **0.00** | -0.49 ✓ |
| **CF%** | 0.08 | **0.26** | +0.18 ✗ |

关键发现：
- 约束解码成功消除了 RV（关系类型违规）和 DR（domain-range 违规），从 0.15%/0.49% → 0.00%/0.00%
- R-F1 微升 +0.15（44.55 → 44.70），E-F1 几乎持平
- CF%（约束失败）从 0.08 升到 0.26，说明约束过程中有少量 fallback 情况
- GPU0 上仍有两个 python 进程（PID 728348, 732035），不是 d065 的——d065 已完成

---

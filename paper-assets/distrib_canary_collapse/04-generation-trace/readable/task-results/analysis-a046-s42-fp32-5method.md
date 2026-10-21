# analysis a046 s42 fp32 5method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a046_s42_fp32_5method_20260521T070101_result.json`
- **Structured JSON:** [`81ce8e55530b666d7d73.json`](../../sessions/81/81ce8e55530b666d7d73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

**alpha_sweep_a046_s42_fp32 — 5method leadlag 结果**

| 方法 | Forward | Reverse |
|------|---------|---------|
| PermG (FDR) | **0/8** | 0/8 |
| DiffXCorr (FDR) | 2/8 | 2/8 |
| ThresholdOnset 3σ | 0/8 | — |
| TY Granger | 1/8 | — |
| K≥3 | **0/8** | — |
| Robust pairs | **0/8** | — |

PermG = 0/8，所有 5 method 均无 robust forward causation 信号。确认 α_c > 0.46，与 [0.48, 0.50] 估计一致。

注：PermG raw p 值在 0.03 附近但 FDR 校正后均为 0.0525（刚过 0.05 阈值），说明 α=0.46 确实处于临界区边缘——有弱信号但未达统计显著。

Registry 已更新为 DONE/success。

---

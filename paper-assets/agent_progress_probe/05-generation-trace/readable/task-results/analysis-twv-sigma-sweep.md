# analysis twv sigma sweep

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_twv-sigma-sweep_20260514T174032_result.json`
- **Structured JSON:** [`baf4f9a2f7679afe7100.json`](../../sessions/ba/baf4f9a2f7679afe7100.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

| σ  | MV agree% | conf1 flip% | conf2 flip% | conf3 flip% | mean flips | stag% |
|----|-----------|-------------|-------------|-------------|------------|-------|
|  1 |     85.9% |       17.2% |        6.6% |        0.4% |      0.602 | 27.9% |
|  2 |     88.5% |       14.1% |        5.2% |        0.1% |      0.346 | 26.5% |
|  3 |     88.8% |       13.6% |        5.2% |        0.1% |      0.204 | 25.2% |
|  5 |     88.9% |       13.7% |        4.6% |        0.0% |      0.125 | 24.4% |
| 10 |     88.5% |       13.9% |        5.5% |        0.1% |      0.060 | 24.0% |

**Tradeoff curve**: σ=5 是 peak agreement (88.9%)，σ>5 过度平滑导致 agreement 回落。σ=2-5 是有效区间，区别主要在 smoothness（0.346→0.125）。σ=2 的验证数据与参考值完全一致。

产出：`twv_sigma_sweep.py` + `data/twv_sigma_sweep.json` 已在服务器上，artifact 已注册 (`art_20260514_39c2a2`)。

---

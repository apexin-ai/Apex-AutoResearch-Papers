# eval permuted score control

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_permuted_score_control_20260524T203920_result.json`
- **Structured JSON:** [`c07c3bd0c2e97521f9eb.json`](../../sessions/c0/c07c3bd0c2e97521f9eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果汇总

| 指标 | permuted_score_control_seed42 | uniform baseline |
|------|------|------|
| Holdout PPL | **17.919** | 17.694 |
| OWT PPL | **18.046** | — |
| Wiki PPL | **14.891** | — |

**与 uniform baseline (holdout=17.694) 的差异：** +0.225 (偏差 +1.3%)

符合预期：permuted score control 的 PPL 接近 uniform baseline，且略差（17.919 vs 17.694）。这证明 adaptive weighting 的效果确实来自 detector signal，而非仅仅是权重的非均匀性——打乱 q-scores 后 adaptive 方法退化到接近 uniform 水平。

---

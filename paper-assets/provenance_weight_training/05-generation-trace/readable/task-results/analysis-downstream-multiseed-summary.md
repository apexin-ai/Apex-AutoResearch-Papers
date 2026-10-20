# analysis downstream multiseed summary

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_downstream_multiseed_summary_20260519T194856_result.json`
- **Structured JSON:** [`9fe4a433e52003b22c82.json`](../../sessions/9f/9fe4a433e52003b22c82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。结果汇总：

**uniform_ood_seed456 已跑完**，现在有完整的 3 seed × 2 method = 6 组结果。

核心结论：**Adaptive 和 Uniform 在 downstream 上几乎没有差异**。3-seed 平均 Δ = -0.0009（Uniform 微弱领先），各 benchmark 差异均在 ±0.003 以内，远小于 seed 间方差。

产出文件已注册：`art_20260519_748a13`，路径 `artifacts/downstream_multiseed_summary.md`。

---

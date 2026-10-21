# analysis magnitude curve data aggregation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_magnitude-curve-data-aggregation_20260517T110748_result.json`
- **Structured JSON:** [`4636f54293e01186125c.json`](../../sessions/46/4636f54293e01186125c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。`magnitude_curve_data.json` 已生成并注册（`art_20260517_fa2562`）。

**汇总**：46 个实验，9 种方法。核心数据与 ROADMAP 参考值全部吻合（obs_only 0.20 六 seed 均值 17.5%，argmin pooled 12.3%，perdof 0.30 = 4.7%）。

**一个注意点**：perdof default 有不一致——ROADMAP 记录 "1s: 0%"（seed42），但 registry 额外包含 `eval-perdof-object-seed43` (sr=12%)，导致 mean=6%。如果该实验实际上不是 default norm 配置，后续需修正。

---

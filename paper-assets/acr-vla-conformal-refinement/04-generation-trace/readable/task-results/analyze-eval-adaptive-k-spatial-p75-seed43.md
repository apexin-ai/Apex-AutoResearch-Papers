# analyze eval adaptive k spatial p75 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-adaptive-k-spatial-p75-seed43_20260520T103414_result.json`
- **Structured JSON:** [`10be27e7a43955a15236.json`](../../sessions/10/10be27e7a43955a15236.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**结论：** Spatial P75 seed43 结果 **positive** — SR 34.0% 与 K=10 baseline 34.4±1.5% 基本持平（Δ=-0.4%，在噪声范围内），同时 avg_K=5.03 实现 ~50% 计算节省，fast_path=62.2%。P75 阈值在 Spatial 上的表现与 P50 的计算节省比例一致，但 SR 无损更强（P50 也接近无损）。跨 benchmark 迁移 Object-calibrated threshold 到 Spatial 有效。

---

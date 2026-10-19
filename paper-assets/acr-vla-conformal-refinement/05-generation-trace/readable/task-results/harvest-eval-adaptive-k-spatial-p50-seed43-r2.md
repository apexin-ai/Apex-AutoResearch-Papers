# harvest eval adaptive k spatial p50 seed43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval-adaptive-k-spatial-p50-seed43-r2_20260520T092516_result.json`
- **Structured JSON:** [`fb7cb2606756be3da92c.json`](../../sessions/fb/fb7cb2606756be3da92c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 摘要

| 指标 | Adaptive-K Spatial P50 | Spatial K=10 baseline | Object P50 |
|------|----------------------|----------------------|------------|
| **SR** | **33.0%** | 34.3% (±1.5%) | 15.3% |
| **avg_K** | **6.33** | 10 | 3.8 |
| **fast_path** | **45.8%** | N/A | 77% |
| **compute saving** | **~37%** | — | ~62% |

P50 阈值（τ=0.074855）从 Object 迁移到 Spatial：SR 仅降 1.3pp（在 baseline CI 内），avg_K=6.33 节省 37% 计算。Spatial 任务 L2 divergence 均值更高（0.090 vs Object），导致 fast_path 从 77% 降至 46%——Spatial 任务不确定性更大，需要更多 full refinement steps，但自适应分配仍能在不损失 SR 的前提下显著节省计算。

---

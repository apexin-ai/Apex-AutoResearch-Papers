# harvest bjb1 32546 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546-batch_20260525T174358_result.json`
- **Structured JSON:** [`eb6d6d5188b1b4f4ebd2.json`](../../sessions/eb/eb6d6d5188b1b4f4ebd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 9 个实验 registry 已更新为 DONE。汇总表：

| exp_id | SR | trigger_rate | Δ vs VLA-only | status |
|--------|-----|-------------|---------------|--------|
| **K=2 Spatial Paired r2** | | | | |
| eval-k2-spatial-adapt-s42-paired-r2 | 79.5% | 19.8% | +1.0% | DONE |
| eval-k2-spatial-vla-only-s42-paired-r2 | 78.5% | — | — | DONE |
| eval-k2-spatial-adapt-s43-paired-r2 | 79.5% | 20.3% | ±0.0% | DONE |
| eval-k2-spatial-vla-only-s43-paired-r2 | 79.5% | — | — | DONE |
| eval-k2-spatial-adapt-s44-paired-r2 | 80.5% | 19.5% | +0.5% | DONE |
| eval-k2-spatial-vla-only-s44-paired-r2 | 80.0% | — | — | DONE |
| **VLA-only Spatial baseline** | | | | |
| eval-vla-only-spatial-bjb1-s48 | 77.5% | — | — | DONE |
| eval-vla-only-spatial-bjb1-s49 | 79.5% | — | — | DONE |
| **SmolVLA CRM Goal** | | | | |
| eval-smolvla-crm-goal-seed44 | 82.5% | — | — | DONE |

**K=2 Paired 小结**：Adaptive mean=79.8%, VLA-only mean=79.3%, mean Δ=+0.5%。方向正确但改善极其微弱，3 seeds 中仅 s42 有 +1% 的可见 Δ。Trigger rate 稳定在 ~20%。

---

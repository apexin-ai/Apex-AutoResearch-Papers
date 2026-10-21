# analysis r18 step mislabel distribution

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r18-step-mislabel-distribution_20260519T151213_result.json`
- **Structured JSON:** [`1dd26000cfbe3584c6ce.json`](../../sessions/1d/1dd26000cfbe3584c6ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/r18_mislabel_distribution.md`。

核心发现：

- **2040 training steps** 来自 68 episodes（61 det + 7 internal），11 task types
- **Death_asymmetry 主导**：10/11 task types 通过 death asymmetry 标记，贡献 1410/2040 steps（75%）；仅 `find-non-living-thing` 使用 score_comparison（510 steps）
- **Pre-fatal mislabeling**：death_asymmetry episodes 中 66.5% 的 steps 是 pre-fatal（内部策略尚未死亡但已被标为 det-preferred）；最高的 `lifespan-longest-lived` 达 75.3%，最低的 `find-animal` 为 55.0%
- **Fatal action 位置偏后**：平均在第 ~19.5/30 步（65%处），导致大量前序步骤被错误标记
- **严格方向冲突极少**：仅 7/2040 steps（0.3%）的 step-level oracle 与 episode label 方向相反
- **"27.7%" 最可能含义**：68 training episodes / 245 total episodes = 27.8%，即获得 routing label 的 episode 占比

---

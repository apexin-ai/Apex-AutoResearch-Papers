# code fisher test preparation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fisher-test-preparation_20260515T202503_result.json`
- **Structured JSON:** [`7f6ad204ddeb247976f9.json`](../../sessions/7f/7f6ad204ddeb247976f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证通过。

核心发现（用假设数据 seed43=20/100 vs 12/100 模拟）：
- 单 seed Fisher p > 0.17，不显著
- **Pooled Fisher p = 0.054**，刚好卡在 0.05 边界
- Bootstrap pooled CI 排除了 0（[0.5, 14.5] pp），P(obs≤arg) = 0.023

现实意义：seed43 的 argmin 需要比 obs_only **至少低 1-2pp**（或 obs_only 比当前 partial 更好）才能让 pooled p < 0.05。当前 partial 数据 obs_only=8.3% vs argmin=10%，**方向反了**——如果最终结果维持这个方向，pooled 几乎不可能达到 p < 0.05。

---

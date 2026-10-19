# analysis k2 l2 fmvd reanalysis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k2-l2-fmvd-reanalysis_20260519T190700_result.json`
- **Structured JSON:** [`3c93e70b235702aef22e.json`](../../sessions/3c/3c93e70b235702aef22e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**数据限制：无法完成 K=2 分析。**

检查了 `fmvd_calibration.json` 和生成脚本 `calibrate_fmvd.py`：

- `compute_k10_variance()` 生成了 K=10 个 action samples，但只保存了聚合的标量 `k10_variance`（overall variance）
- 原始 K=10 action vectors **没有写入 JSON**
- 每步数据仅有：`fmvd`（标量）、`k10_variance`（标量）、`episode_success`
- 无 per-DOF variance，无 raw action samples

**结论：** 从现有数据无法做 K=2 子采样。需要修改 `calibrate_fmvd.py`，在 `compute_k10_variance()` 中保存原始 K=10 action vectors，然后重新跑校准。

两个选项：

1. **快速路径（~30min GPU）**：修改脚本，只收集 K=10 raw samples 并保存，不跑完整 evaluation。可以复用已有的环境 rollout 逻辑，只是多存一个 `k10_actions: [10, 7]` 字段
2. **更快的近似（~5min GPU）**：只跑 K=2（不跑 K=10），直接收集 K=2 pairs 的 L2 距离，与已有的 `k10_variance` 做 Spearman 比对。省掉 8 次多余 forward pass

要我走哪个方案？

---

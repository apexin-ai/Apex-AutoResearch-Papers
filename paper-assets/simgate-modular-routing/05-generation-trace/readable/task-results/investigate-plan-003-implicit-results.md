# investigate plan 003 implicit results

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_plan-003-implicit-results_20260514T092451_result.json`
- **Structured JSON:** [`d2998bc5b7b75526a81e.json`](../../sessions/d2/d2998bc5b7b75526a81e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果摘要：

## plan-003-implicit-eval-full 结果 — **Negative**

| 指标 | 值 |
|---|---|
| **Continuous Score** | **-12.84** [-17.52, -8.45] |
| Always-det baseline | -9.47 |
| **差距** | **-3.37 (劣于 baseline)** |
| Success Rate | 22.0% |
| Death Rate | 19.2% |
| Sim Invocation Ratio | 94.1% |

**Routing 分析：**
- Step accuracy: 60.2% (1301/2160)
- Episode accuracy: 82.1% (78/95)
- 路由极度偏 deterministic: 229 det vs 16 internal
- Internal recall: 44.4% (4/9) — 仅识别出不到一半的 internal-preferred episodes
- Det recall: 86.0% (74/86)
- Oracle 标签分布: internal-preferred=9, det-preferred=86, no-preference=150

**Per-task 亮点/问题：**
- `find-non-living-thing` 是唯一正分任务 (+26.38)，也是 internal routing 最多的 (5/40)
- `inclined-plane-determine-angle` 最差 (-30.00, 0% success)
- `chemistry-mix`, `freeze`, `measure-melting-point` 都在 -27~-30 区间，death rate 30%

**核心问题：** 模型几乎总选 deterministic (93.5%)，internal recall 仅 44%，导致该路由到 internal 的 episode 大部分被误分到 deterministic，拉低了总分。

---

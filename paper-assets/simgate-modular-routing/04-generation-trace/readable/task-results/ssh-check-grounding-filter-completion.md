# ssh check grounding filter completion

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-grounding-filter-completion_20260518T234158_result.json`
- **Structured JSON:** [`4d0c6df950be123eed56.json`](../../sessions/4d/4d0c6df950be123eed56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已完成。

---

## 报告

### grounding-filter-ablation: **SUCCESS**

| 指标 | 值 |
|------|-----|
| Total episodes | 200 (10 tasks × 20) |
| Total deaths | 58 |
| **Death rate** | **29.0%** |
| Success rate | 10.5% |
| Total filter blocks | 379 |
| Total passthroughs | 0 |
| Avg blocks/episode | 1.9 |

**vs Baseline**: 42.9% → 29.0%，降低 13.9pp（相对降幅 32.4%）

Per-task death rate:

| Task | Deaths | Death Rate | Blocks |
|------|--------|------------|--------|
| identify-life-stages-2 | 3 | 15% | 24 |
| identify-life-stages-1 | 4 | 20% | 27 |
| inclined-plane-determine-angle | 3 | 15% | 42 |
| measure-melting-point | 3 | 15% | 47 |
| lifespan-longest-then-shortest | 6 | 30% | 40 |
| grow-fruit | 7 | 35% | 34 |
| chemistry-mix | 8 | 40% | 39 |
| find-animal | 8 | 40% | 39 |
| freeze | 8 | 40% | 38 |
| lifespan-longest-lived | 8 | 40% | 49 |

Filter 的 passthrough 为 0（所有危险动作均被拦截），但仍有 29% 死亡率，说明死亡来自 filter 未覆盖的路径。

---

### grounding-prompt-ablation: **SUCCESS**

也已全部完成，200 episodes。

| 指标 | 值 |
|------|-----|
| Total episodes | 200 |
| Total deaths | 74 |
| **Death rate** | **37.0%** |

---

### 三条件对比

| Condition | Death Rate |
|-----------|-----------|
| Baseline (no safety) | 42.9% |
| Prompt-only (safety rule in system prompt) | 37.0% |
| **Grounding filter** | **29.0%** |

Prompt-only 降低 5.9pp，grounding filter 额外再降 8.0pp。Filter 的增量贡献大于纯 prompt 干预。

---

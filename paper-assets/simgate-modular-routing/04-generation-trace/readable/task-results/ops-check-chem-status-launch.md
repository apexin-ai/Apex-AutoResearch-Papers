# ops check chem status launch

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-chem-status-launch_20260514T051844_result.json`
- **Structured JSON:** [`12ab486b814100f830c8.json`](../../sessions/12/12ab486b814100f830c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## chemistry-mix 状态: **RUNNING** (18/20 eps, 进程运行 2h7m)

注意：`episodes_slim.jsonl` 不存在于任何 task，数据均在 `episodes.jsonl` 中。

### 11 Task 完整度

| Task | Episodes | 状态 |
|------|----------|------|
| chemistry-mix | 18 | ⏳ 运行中 |
| find-animal | 20 | ✅ |
| find-non-living-thing | 40 | ✅ (超额) |
| freeze | 20 | ✅ |
| grow-fruit | 20 | ✅ |
| identify-life-stages-1 | 20 | ✅ |
| identify-life-stages-2 | 20 | ✅ |
| inclined-plane-determine-angle | 20 | ✅ |
| lifespan-longest-lived | 25 | ✅ (超额) |
| lifespan-longest-lived-then-shortest-lived | 20 | ✅ |
| measure-melting-point-unknown-substance | 20 | ✅ |

### GPU 状态
- GPU 0: 0 MiB / 32607 MiB, 0% 利用率（空闲）
- GPU 1: 28013 MiB / 32607 MiB, 0% 利用率（已分配，GPU util 瞬时为 0）

### 磁盘
- `/root/autodl-tmp/`: 55G / 250G 已用 (22%)

### 结论
chemistry-mix 还差 2 个 episode，进程存活中，预计很快完成。其余 10 个 task 全部达标（≥20 eps）。

---

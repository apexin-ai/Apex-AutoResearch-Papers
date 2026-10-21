# ssh llama full urgent check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama-full-urgent-check_20260519T080621_result.json`
- **Structured JSON:** [`579eb4e891b861ef8140.json`](../../sessions/57/579eb4e891b861ef8140.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D118 llama-cross-model-full 实验状态报告

### 状态：**进行中**（非崩溃）

| 指标 | 值 |
|---|---|
| GPU 利用率 | GPU0: 100%, GPU1: 100% |
| VLLM 进程 | 双卡各一个，28GB/32GB |
| ScienceWorld | 两个 Java 进程活跃 |
| 总进度 | **170/220 episodes (77%)** |

### Task 完成状态

| Task | Episodes | Int DR | Det DR | Int Avg | Det Avg | Status |
|---|---|---|---|---|---|---|
| chemistry-mix | 20 | 45% | 20% | 3.4 | 3.6 | DONE |
| find-animal | 20 | 40% | 25% | 1.3 | 2.7 | DONE |
| find-non-living-thing | 20 | 0% | 0% | 22.0 | 41.1 | DONE |
| freeze | 20 | 45% | 0% | 0.5 | 0.8 | DONE |
| grow-fruit | 4/20 | 50% | 0% | 3.5 | 1.8 | **IN-PROG** |
| identify-life-stages-1 | 0 | - | - | - | - | **NOT STARTED** |
| identify-life-stages-2 | 20 | 45% | 5% | 2.9 | 1.7 | DONE |
| inclined-plane-determine-angle | 20 | 45% | 20% | 1.8 | 6.9 | DONE |
| lifespan-longest-lived | 20 | 35% | 5% | 7.7 | 7.9 | DONE |
| lifespan-longest-lived-then-shortest-lived | 20 | 50% | 20% | 3.3 | 6.2 | DONE |
| measure-melting-point-unknown-substance | 6/20 | 67% | 33% | 3.5 | 2.0 | **IN-PROG** |

### 关键发现

- **Death asymmetry 显著**：Internal 39.4% vs Deterministic 12.4% (3.2x)
- **Deterministic routing 明显优于 Internal**：det_preferred=62, int_preferred=3, tie=105
- **find-non-living-thing** 是唯一零 death 的完成 task，且 Det 均分 (41.1) 远超 Int (22.0)
- 剩余：grow-fruit (16 eps), identify-life-stages-1 (20 eps), measure-melting-point (14 eps) = 50 episodes

注：你提供的提取脚本里 `internal_score`/`deterministic_score` 字段不存在，实际结构是 `always_internal.final_score` / `always_deterministic.final_score`。

---

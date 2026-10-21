# analysis retry control done

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_retry-control-done_20260517T170412_result.json`
- **Structured JSON:** [`bc29a6938ffaff6e07b6.json`](../../sessions/bc/bc29a6938ffaff6e07b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## retry-control-baseline 状态报告

### 完成状态
- **retry-part2**: 正常完成 (80/80 episodes)
- **retry-part1**: 崩溃退出，`openai.APIConnectionError: Connection error`，停在 identify-life-stages-1 ep011

### 缺失数据
- `identify-life-stages-1`: 只有 11/20 episodes（缺 9 个）
- `identify-life-stages-2`: 0/20 episodes（完全缺失）
- **总计 191/220 episodes，缺 29 个**

### 各 task 统计

| Task | Eps | Death% | Succ% |
|------|-----|--------|-------|
| chemistry-mix | 20 | 55.0% | 10.0% |
| find-animal | 20 | 55.0% | 10.0% |
| find-non-living-thing | 20 | 0.0% | 65.0% |
| freeze | 20 | 45.0% | 5.0% |
| grow-fruit | 20 | 45.0% | 25.0% |
| identify-life-stages-1 | **11** | 54.5% | 0.0% |
| inclined-plane-determine-angle | 20 | 50.0% | 5.0% |
| lifespan-longest-lived | 20 | 40.0% | 15.0% |
| lifespan-longest-lived-then-shortest-lived | 20 | 50.0% | 0.0% |
| measure-melting-point-unknown-substance | 20 | 55.0% | 10.0% |

### 总体对比（191 eps）

| Metric | Retry Control | Reflexion Baseline |
|--------|--------------|-------------------|
| Death rate | **44.5%** | 31.4% |
| Success rate | **15.2%** | 17.3% |

Retry control 的 death rate 比 reflexion 高 13pp，success rate 低 2pp。需要补跑缺失的 29 episodes（identify-life-stages-1 剩余 9 个 + identify-life-stages-2 全部 20 个）。vLLM server（vllm-7b-retry, CUDA:3）仍在运行，可以直接重跑 part1 的剩余部分。

---

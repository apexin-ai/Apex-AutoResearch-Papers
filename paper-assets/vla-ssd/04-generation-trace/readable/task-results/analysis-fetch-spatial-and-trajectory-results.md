# analysis fetch spatial and trajectory results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fetch_spatial_and_trajectory_results_20260520T213514_result.json`
- **Structured JSON:** [`48393fd01e29cd928d9a.json`](../../sessions/48/48393fd01e29cd928d9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入本地。汇总：

## counterfactual_spatial (libero_spatial, 10 tasks × 10 demos × 50 timesteps)

| Condition | Global d | CI 95% | Token Div | KL Div |
|-----------|----------|--------|-----------|--------|
| **empty** | **0.942** | [0.914, 0.970] | 0.914 | 9.030 |
| wrong | 0.851 | [0.824, 0.879] | 0.865 | 6.957 |
| shuffled | 0.833 | [0.805, 0.861] | 0.877 | 7.759 |
| paraphrased | 0.806 | [0.778, 0.833] | 0.799 | 5.916 |

Cross-task CV: wrong=0.093 (最稳定), paraphrased=0.128, shuffled=0.166, empty=0.185

## counterfactual_10tasks (10 diverse tasks × 10 demos × 50 timesteps)

| Condition | Global d | Token Div | KL Div | Cross-task CV |
|-----------|----------|-----------|--------|---------------|
| **empty** | **0.978** | 0.913 | 8.807 | 0.171 |
| wrong | 0.924 | 0.908 | 8.383 | 0.274 |
| shuffled | 0.763 | 0.871 | 7.331 | 0.185 |
| paraphrased | 0.707 | 0.830 | 6.457 | 0.296 |

## Trajectory-level Cohen's d (demo-level aggregation, 30 demos, bootstrap B=10000)

| Condition | Token-level d | Trajectory-level d | CI 95% | Inflation |
|-----------|--------------|-------------------|--------|-----------|
| wrong | 0.844 | **3.798** | [3.194, 4.938] | 0.222 |
| empty | 0.968 | **3.438** | [2.921, 4.448] | 0.282 |
| shuffled | 0.625 | **2.595** | [2.028, 3.791] | 0.241 |
| paraphrased | 0.697 | **2.131** | [1.740, 2.819] | 0.327 |

Token-level d 仅为 trajectory-level d 的 18-33% (mean inflation factor 0.245)。

文件位置：
- `artifacts/statistical_supplements/counterfactual_spatial.json`
- `artifacts/statistical_supplements/counterfactual_10tasks_trajectory.json`

---

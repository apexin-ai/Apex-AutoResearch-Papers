# rerun exp015 neural probe olmo

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_rerun_exp015_neural_probe_olmo_20260521T155925_result.json`
- **Structured JSON:** [`3d2bdb46acf2e67bc3fd.json`](../../sessions/3d/3d2bdb46acf2e67bc3fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果摘要：

**K\*(neural probe) = 1**，与 LightGBM rerun 的 K\*=1 完全一致。

| Pair | Neural Probe AUC | 95% CI | p-value |
|------|----------------:|--------|---------|
| 0v1  | **0.9773** | [0.975, 0.980] | <0.002 |
| 1v2  | 0.5054 | [0.495, 0.515] | 0.176 |
| 2v3  | 0.5056 | [0.497, 0.516] | 0.142 |
| 3v4  | 0.5032 | [0.494, 0.513] | 0.262 |
| 4v5  | 0.4999 | [0.491, 0.507] | 0.514 |

**结论**：K\*=1 是 model-intrinsic 的。OLMo-1B 的 2048-dim hidden states 也无法区分 gen-1 和 gen-2+ 文本——所有 1v2~4v5 的 AUC 都在随机水平，CI 全部包含 0.50，permutation test 均不显著。这不是 15D feature 的局限，而是模型内部表征本身就不包含区分信号。

结果已保存至：
- 服务器: `results/exp015_olmo_rerun/neural_probe_results.json`
- 本地 artifact: `artifacts/exp015_neural_probe_olmo_rerun.md`

---

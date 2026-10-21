# code table3 v6 balanced

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_table3-v6-balanced_20260516T205808_result.json`
- **Structured JSON:** [`14ba9145dad943c08da4.json`](../../sessions/14/14ba9145dad943c08da4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

V6 运行完成（78s），结果已保存。验证结果汇总：

| Method | Binary F1 | CI | Multiclass F1 | CI |
|---|---|---|---|---|
| **7feature_ours** | **0.7014** | [0.696, 0.707] | **0.7762** | [0.772, 0.780] |
| 4det_surface | 0.7070 | [0.701, 0.712] | 0.7923 | [0.788, 0.796] |
| 4det_ensemble | 0.6975 | [0.691, 0.703] | 0.7843 | [0.780, 0.788] |
| entropy_mean | 0.7006 | [0.695, 0.706] | 0.5556 | [0.551, 0.561] |
| ld_score | 0.6756 | [0.670, 0.681] | 0.6306 | [0.626, 0.636] |
| avg_logprob | 0.6735 | [0.667, 0.679] | 0.7071 | [0.702, 0.712] |
| fastdetectgpt | 0.5760 | [0.570, 0.582] | 0.6637 | [0.659, 0.668] |
| binoculars | 0.5336 | [0.528, 0.539] | 0.4105 | [0.405, 0.416] |

验证对照任务预期：
- 7feature binary 0.7014 ≈ 0.70 ✓
- avg_logprob binary 0.6735 ✓
- ld_score binary 0.6756 ✓
- fastdetectgpt binary 0.5760 ✓
- binoculars binary 0.5336 ✓
- 4det ensembles binary 0.697–0.707 ✓
- 所有方法 binary F1 > 0.50 ✓ — class balancing 生效

---
